"""Frequency content of a step response: theory compared with FFT.

Model: first-order plant G(s) = K / (tau*s + 1), tau = 33 ms, K = 1.
Controller: I-PD (integral on the error; P and D on the measured value).
Reference design: pure integral control, tuned so that y(0.7 s) = 0.98.

The script prints the numbers used in the post and saves two figures.
Requirements: numpy, scipy, matplotlib.
"""
import numpy as np
from scipy import signal, optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TAU, K = 0.033, 1.0
FS, T_REC, NFFT = 1000.0, 4.0, 2**16          # sample rate, record length, FFT length
TS = 1 / FS


def den(kp, ki, kd):
    """Closed-loop denominator for the setpoint: (tau + K*Kd) s^2 + (1 + K*Kp) s + K*Ki."""
    return [TAU + K * kd, 1 + K * kp, K * ki]


def y_at(ki, t_end=0.7):
    _, y = signal.step(signal.lti([K * ki], den(0, ki, 0)), T=[0, t_end])
    return y[-1]


# 1. Pure integral control: find Ki so that y(0.7 s) = 0.98.
ki = optimize.brentq(lambda k: y_at(k) - 0.98, 3, 7)
d = den(0, ki, 0)
poles = np.roots(d)
zeta = d[1] / (2 * np.sqrt(d[0] * d[2]))
print(f"Ki = {ki:.4f}, damping ratio = {zeta:.3f}")
print(f"poles = {np.sort(poles.real)} rad/s = {np.sort(np.abs(poles)) / (2 * np.pi)} Hz")

# 2. Step response, sampled at 1 kHz for 4 s.
t = np.arange(0, T_REC, TS)
sys = signal.lti([K * ki], d)
_, y = signal.step(sys, T=t)
_, h = signal.impulse(sys, T=t)               # dy/dt of the step response
e = 1 - y                                     # error for a unit step
print(f"y(0.7 s) = {np.interp(0.7, t, y):.4f}, max(y) = {y.max():.5f}, e(end) = {e[-1]:.1e}")

# 3. FFT scaled to match the continuous Fourier transform: Ts * DFT,
#    with a trapezoid correction for the jump at t = 0.
f = np.fft.rfftfreq(NFFT, TS)
w = 2 * np.pi * f
H_fft = TS * np.fft.rfft(h, NFFT) - TS / 2 * h[0]
E_fft = TS * np.fft.rfft(e, NFFT) - TS / 2 * e[0]

# 4. Theory.
jw = 1j * w
T_th = K * ki / np.polyval(d, jw)             # closed-loop frequency response T(jw)
with np.errstate(divide="ignore", invalid="ignore"):
    E_th = (1 - T_th) / jw                    # Fourier transform of e(t)
    Y_th = T_th / jw                          # Fourier transform of y(t) = T(jw) * 1/(jw)
E_th[0] = d[1] / d[2]                         # limit at w = 0: the area under e(t)

band = (f > 0) & (f <= 5)
rel = lambda a, b: np.max(np.abs(np.abs(a[band]) - np.abs(b[band])) / np.abs(b[band]))
print(f"area under e(t): numeric {np.sum(e) * TS:.4f} s, theory 1/Ki = {1 / ki:.4f} s")
print(f"max relative error, 0-5 Hz: dy/dt {rel(H_fft, T_th):.1e}, e(t) {rel(E_fft, E_th):.1e}")
print(f"frequency resolution 1/T_rec = {1 / T_REC:.2f} Hz, FFT bin spacing = {FS / NFFT:.4f} Hz")

# 5. Bandwidth and loop margins.
mag = np.abs(T_th)
f3db = f[np.argmax(mag < 1 / np.sqrt(2))]
with np.errstate(divide="ignore", invalid="ignore"):
    L = K * ki / (jw * (TAU * jw + 1))        # loop transfer function
i_c = np.argmax(np.abs(L[1:]) < 1) + 1
pm = 180 + np.degrees(np.angle(L[i_c]))
print(f"-3 dB bandwidth = {f3db:.2f} Hz; crossover = {f[i_c]:.2f} Hz, phase margin = {pm:.0f} deg")

# 6. Where is the energy of dy/dt?
energy = np.cumsum(np.abs(T_th) ** 2)
energy /= energy[-1]
for p in (0.90, 0.99, 0.999):
    print(f"{p * 100:g} % of the dy/dt energy is below {f[np.argmax(energy >= p)]:.1f} Hz")

# 7. Two critically damped designs that reach 98 % at 0.7 s.
wn = optimize.brentq(lambda x: (1 + x * 0.7) * np.exp(-x * 0.7) - 0.02, 1, 20)
kp_a, ki_a = 2 * TAU * wn - 1, TAU * wn ** 2          # design A: D = 0
ki_b, kd_b = wn / 2, 1 / (2 * wn) - TAU               # design B: P = 0
na, nb = np.array(den(kp_a, ki_a, 0)), np.array(den(0, ki_b, kd_b))
print(f"design A (D = 0): Kp = {kp_a:.3f}, Ki = {ki_a:.3f}")
print(f"design B (P = 0): Ki = {ki_b:.3f}, Kd = {kd_b:.3f}")
print(f"normalized denominators: A {na / na[0]}, B {nb / nb[0]}")
print(f"normalized numerators:   A {K * ki_a / na[0]:.3f}, B {K * ki_b / nb[0]:.3f}")

# 8. An aggressive tuning for comparison: Ki = 60.
d60 = den(0, 60, 0)
T60 = K * 60 / np.polyval(d60, jw)
with np.errstate(divide="ignore", invalid="ignore"):
    L60 = K * 60 / (jw * (TAU * jw + 1))
i60 = np.argmax(np.abs(L60[1:]) < 1) + 1
print(f"Ki = 60: phase margin = {180 + np.degrees(np.angle(L60[i60])):.0f} deg, "
      f"peak |T| = {20 * np.log10(np.abs(T60).max()):.1f} dB at {f[np.argmax(np.abs(T60))]:.1f} Hz")

# Figures
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["IBM Plex Sans", "IBM Plex Sans KR", "DejaVu Sans"],
                     "font.size": 11, "axes.unicode_minus": False, "mathtext.fontset": "dejavusans", "axes.spines.top": False, "axes.spines.right": False})
ink, grey, light = "#262624", "#8c8c85", "#cbcbc3"
m = (f >= 0.05) & (f <= 100)

fig, ax = plt.subplots(figsize=(7.2, 4.0))
db = lambda x: 20 * np.log10(np.abs(x))
ax.semilogx(f[m], db(1 / w[m]), color=grey, ls="--", lw=1.2, label=r"Step command alone: $1/\omega$")
ax.semilogx(f[m], db(Y_th[m]), color=ink, lw=1.8, label=r"Step response: $|T(j\omega)|/\omega$")
for pf in np.sort(np.abs(poles)) / (2 * np.pi):
    ax.axvline(pf, color=light, lw=1)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.legend(frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig("step-spectrum.png", dpi=160)

fig, ax = plt.subplots(figsize=(7.2, 4.0))
ax.semilogx(f[m], 20 * np.log10(np.abs(T_th[m])), color=light, lw=5, label=r"Theory: $|T(j\omega)|$")
ax.semilogx(f[m], 20 * np.log10(np.abs(H_fft[m])), color=ink, lw=1.2, ls="--", label="FFT of dy/dt")
ax.axvline(f3db, color=grey, lw=1, ls=":")
ax.annotate(f"-3 dB: {f3db:.2f} Hz", (f3db / 1.15, -14), color=grey, ha="right")
ax.set_ylim(-80, 5)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.legend(frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig("dydt-spectrum.png", dpi=160)
