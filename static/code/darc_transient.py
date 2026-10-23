"""DARC step: dose loss and gas-ratio error caused by MFC transients.

Assumptions: each MFC loop is a first-order plant (tau = 33 ms) with pure integral control.
Gas A settles to 98 % in 0.7 s, gas B in 1.4 s. The plasma is on from the flow command,
the step lasts 8 s, and the deposition rate follows the flow of gas A.
Requirements: numpy, scipy, matplotlib.
"""
import numpy as np
from scipy import signal, optimize
tau=0.033
def resp(ki,t): _,y=signal.step(signal.lti([ki],[tau,1,ki]),T=t); return y
def ki_for(t98):
    return optimize.brentq(lambda k: resp(k,np.array([0,t98]))[-1]-0.98, 0.5, 50)
t=np.arange(0,8,0.0005)
k_fast=ki_for(0.7); k_slow=ki_for(1.4)
print("Ki fast",k_fast,"slow",k_slow, "1/Ki",1/k_fast,1/k_slow)
y1=resp(k_fast,t); y2=resp(k_slow,t)
T=8.0
loss1=np.trapezoid(1-y1,t)/T; loss2=np.trapezoid(1-y2,t)/T
print("dose loss over 8 s step: SiH4 %.2f %%, N2O %.2f %%"%(loss1*100,loss2*100))
# ratio deviation
r=np.where(y2>1e-6,y1/np.maximum(y2,1e-9),np.nan)
dev=np.abs(r-1)
# time until ratio within 2% and 5%
for th in (0.05,0.02):
    idx=np.where(dev>th)[0]; print("ratio within %d%% after %.2f s"%(th*100,t[idx[-1]] if len(idx) else 0))
# fraction of SiH4-limited deposit made while ratio off by >2%
dep=y1  # deposition rate ~ SiH4 flow (assumption)
mask=dev>0.02
print("share of film deposited with ratio off >2%%: %.1f %%"%(100*np.trapezoid(dep*mask,t)/np.trapezoid(dep,t)))
mask5=dev>0.05
print("share with ratio off >5%%: %.1f %%"%(100*np.trapezoid(dep*mask5,t)/np.trapezoid(dep,t)))
print("max ratio",np.nanmax(r[t>0.02]))
# same unit +-10% missing area variation -> dose variation
print("dose variation from +-10%% missing area: +-%.2f %%"%(0.1*loss1*100))
# thickness 300 A
print("thickness equivalent of SiH4 loss: %.1f A"%(loss1*300))
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"sans-serif","font.sans-serif":["IBM Plex Sans","IBM Plex Sans KR","DejaVu Sans"],"font.size":11,"axes.unicode_minus":False,"axes.spines.top":False,"axes.spines.right":False})
ink,grey,light="#262624","#8c8c85","#cbcbc3"
fig,ax=plt.subplots(2,1,figsize=(7.2,5.2),sharex=True,gridspec_kw={"height_ratios":[3,2]})
ax[0].plot(t,y1,color=ink,lw=1.8,label="Gas A: settles in 0.7 s")
ax[0].plot(t,y2,color=grey,lw=1.8,ls="--",label="Gas B: settles in 1.4 s")
ax[0].set_ylabel("Flow (fraction of setpoint)"); ax[0].legend(frameon=False,loc="lower right"); ax[0].set_ylim(0,1.08)
ax[1].plot(t[t>0.03],r[t>0.03],color=ink,lw=1.6)
ax[1].axhspan(0.98,1.02,color=light,lw=0)
ax[1].set_ylabel("Ratio A/B\n(1 = target)"); ax[1].set_xlabel("Time after the flow command (s)")
ax[1].set_ylim(0.9,2.2); ax[0].set_xlim(0,3)
fig.tight_layout(); fig.savefig("darc-ratio.png", dpi=160)
