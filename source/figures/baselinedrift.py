import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
from typing import Any

# requires atompy v 4.20.0
# get it via github
# pip git+https://github.com/frekm/atompy.git@v4.20.0
import atompy as ap


def exp(x, x0, y0, scale, tau):
    return scale * np.exp((x - x0) / tau) + y0


def plot():

    ap._set_theme_atompy("lb", use_latex=True, use_serif=False)
    plt.rcParams["figure.figsize"] = 4.0, 3.0

    axs: tuple[Axes, Axes]
    fig, axs = plt.subplots(2, 1)

    pulse_kwargs: dict[Any, Any] = dict(lw=3.0, c=ap.PALETTE_OKABE_ITO[0], ls="-")
    record_kwargs: dict[Any, Any] = dict(lw=3.0, c=ap.PALETTE_OKABE_ITO[1], ls="-")

    pulse_x = np.linspace(0, 100, 100)
    pulse_y = np.full(100, 0).astype(float)

    edges = (10, 40, 60, 90)

    pulse_y[edges[0] : edges[1]] = 100
    pulse_y[edges[2] : edges[3]] = 100

    axs[0].plot(pulse_x, pulse_y, **pulse_kwargs)
    axs[0].set_ylabel("Signal height", color=plt.rcParams["axes.edgecolor"])

    signal_x = pulse_x.copy()
    signal_y = pulse_y.copy()

    x_single_pulse = np.linspace(0, 30, 30)

    exp_fall = exp(x_single_pulse, 0, 0, 100, -40)
    delta_exp = 100 - exp_fall

    signal_y[edges[0] : edges[1]] -= delta_exp

    signal_y[edges[1] : edges[2]] += signal_y[edges[1] - 1] - 100
    signal_y[edges[1] : edges[2]] += delta_exp[:20]

    signal_y[edges[2] : edges[3]] = signal_y[edges[2] - 1] + 100
    signal_y[edges[2] : edges[3]] -= delta_exp

    signal_y[edges[3] :] += signal_y[edges[3] - 1] - 100
    signal_y[edges[3] :] += delta_exp[:10]

    axs[1].plot(signal_x, signal_y, **record_kwargs)
    axs[1].set_ylabel("ADC sample", color=plt.rcParams["axes.edgecolor"])

    axs[1].axhline(
        signal_y[edges[2] - 1], ls=":", c=plt.rcParams["axes.edgecolor"], lw=0.8
    )

    for ax in axs:
        ax.spines[["left", "bottom"]].set_position(("data", 0))
        ax.set_axisbelow(True)
        ax.plot(
            1,
            0,
            ">",
            transform=ax.get_yaxis_transform(),
            clip_on=False,
            c=plt.rcParams["axes.edgecolor"],
        )
        ax.plot(
            0,
            1,
            "^",
            transform=ax.get_xaxis_transform(),
            clip_on=False,
            c=plt.rcParams["axes.edgecolor"],
        )
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_box_aspect(0.3)
        ax.set_ylim(-110, 110)
        ax.set_xlim(-0, 105)

    ap.make_me_nice()
    ap.savefig("*", ftype=("pdf", "png"), dpi=300, transparent=True)


if __name__ == "__main__":
    plot()
