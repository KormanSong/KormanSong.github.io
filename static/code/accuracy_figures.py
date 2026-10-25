"""Figures for the post on accuracy and repeatability.

1. targets.png: four targets (true or biased, precise or imprecise).
2. drift-targets.png: one unit over months, and several units on one day.
3. spec-error.png: error limit in % of reading against setpoint, for a spec of
   ±1 % of reading at 25 % F.S. and above, and ±0.25 % F.S. below 25 % F.S.
Requirements: numpy, matplotlib.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["IBM Plex Sans", "IBM Plex Sans KR", "DejaVu Sans"],
                     "font.size": 11, "axes.unicode_minus": False, "axes.spines.top": False, "axes.spines.right": False})
ink, grey, light = "#262624", "#8c8c85", "#cbcbc3"
rng = np.random.default_rng(7)


def target(ax, pts, title, color=ink, extra=None):
    for r, lw in ((1.0, 1.0), (0.6, 1.0), (0.2, 2.0)):
        ax.add_patch(plt.Circle((0, 0), r, fill=False, color=grey if r > 0.2 else ink, lw=lw))
    if extra:
        for p, c, lab in extra:
            ax.scatter(p[:, 0], p[:, 1], s=36, color=c, zorder=3)
            ax.text(p[:, 0].max() + 0.08, p[:, 1].mean(), lab, ha="left", va="center", fontsize=9.5, color=c,
                    bbox=dict(facecolor="white", edgecolor="none", pad=1))
    else:
        ax.scatter(pts[:, 0], pts[:, 1], s=36, color=color, zorder=3)
    ax.set_xlim(-1.08, 1.08); ax.set_ylim(-1.08, 1.08); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(title, fontsize=11.5, pad=6)


def cloud(cx, cy, s, n=7):
    return np.column_stack([rng.normal(cx, s, n), rng.normal(cy, s, n)])


# 1. Four targets
fig, axs = plt.subplots(1, 4, figsize=(10, 3.0))
target(axs[0], cloud(0, 0, 0.05), "True + precise\n= accurate")
target(axs[1], cloud(-0.38, -0.42, 0.05), "Biased + precise")
target(axs[2], cloud(0, 0, 0.33), "True on average\n+ imprecise")
target(axs[3], cloud(0.3, 0.35, 0.33), "Biased + imprecise")
fig.tight_layout(); fig.savefig("targets.png", dpi=160)

# 2. Time and unit axes
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.4))
months = [(cloud(0.0, 0.0, 0.03, 5), ink, "Month 1"), (cloud(-0.28, -0.32, 0.03, 5), grey, "Month 6"),
          (cloud(-0.56, -0.64, 0.03, 5), ink, "Month 12")]
target(axs[0], None, "One unit over a year\n(drift)", extra=months)
units = [(cloud(-0.35, 0.30, 0.04, 5), ink, "Unit A"), (cloud(0.32, 0.18, 0.04, 5), grey, "Unit B"),
         (cloud(0.0, -0.45, 0.04, 5), ink, "Unit C")]
target(axs[1], None, "Three units on one day\n(unit to unit)", extra=units)
fig.tight_layout(); fig.savefig("drift-targets.png", dpi=160)

# 3. Spec error curve
sp = np.logspace(0, 2, 400)                       # setpoint, % F.S.
rd = np.full_like(sp, 1.0)                        # ±1 % of reading
fs = 0.25 / sp * 100                              # ±0.25 % F.S., as % of reading
spec = np.where(sp >= 25, rd, fs)
fig, ax = plt.subplots(figsize=(7.2, 4.0))
ax.plot(sp, fs, color=grey, ls="--", lw=1.2, label="±0.25 % F.S. alone")
ax.plot(sp, rd, color=grey, ls=":", lw=1.4, label="±1 % of reading alone")
ax.plot(sp, spec, color=ink, lw=2.2, label="Spec: ±1 % Rd at ≥ 25 % F.S., ±0.25 % F.S. below")
for x in (2, 5, 10):
    y = 0.25 / x * 100
    ax.plot([x], [y], "o", color=ink, ms=4)
    ax.annotate(f"{y:g} % at {x} % F.S.", (x, y), xytext=(8, 4), textcoords="offset points", fontsize=9.5)
ax.set_xscale("log"); ax.set_xticks([1, 2, 5, 10, 25, 50, 100]); ax.set_xticklabels(["1", "2", "5", "10", "25", "50", "100"])
ax.set_ylim(0, 27)
ax.set_xlabel("Setpoint (% of full scale)"); ax.set_ylabel("Error limit (± % of reading)")
ax.legend(frameon=False, loc="upper right")
fig.tight_layout(); fig.savefig("spec-error.png", dpi=160)
