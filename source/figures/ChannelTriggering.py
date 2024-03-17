import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.patches import Rectangle
import numpy as np
from sys import argv
from dataclasses import dataclass


@dataclass
class Config:
    """
    Configuration class for plots

    Parameters
    ----------
    samples : int
        How many samples are in one clock cycle?
        (8, 16, 32 for Ndigo6G-12)

    clock_cycle_duration: str
        How long is one clock cycle?
        (5000 ps for Ndigo6G-12)

    precursor: int
        In units of *clock_cycles_duration_ps*

    length: int
        In units of *clock_cycles_duration_ps*

    filenames : list[str]
        Including filetype. All files will be created in ./source/figures/
    """
    samples: int
    clock_cycle_duration: str
    precursor: int
    length: int
    filenames: list[str]

    def __len__(self):
        return 5

    def __getitem__(self, index):
        return [self.samples,
                self.clock_cycle_duration,
                self.precursor,
                self.length,
                self.filenames][index]

    def __setitem__(self, index, value):
        if index == 0:
            self.samples = value
        if index == 1:
            self.clock_cycle_duration = value
        if index == 2:
            self.precursor = value
        if index == 3:
            self.length = value
        if index == 4:
            self.filenames = value


def plot(config: Config):
    """
    Plot a sketch for triggering for the different channel modes.

    Parameters
    ----------
    config : Config
        If script is called with len(config) system parameters (argv), use
        these instead
    """
    orange = "#ED7807"
    lightorange = "#F6BB82"
    blue = "#376EB5"
    lightblue = "#569fd6"
    plt.rcParams["lines.linewidth"] = plt.rcParams["axes.linewidth"]
    plt.rcParams["lines.linestyle"] = "--"
    plt.rcParams["axes.spines.bottom"] = False
    plt.rcParams["axes.spines.left"] = False
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["figure.figsize"] = 6.4, 6.4/2
    plt.rcParams["figure.edgecolor"] = lightblue
    plt.rcParams["figure.constrained_layout.use"] = True
    plt.rcParams["axes.spines.right"] = False
    plt.rcParams["xtick.color"] = blue
    plt.rcParams["xtick.major.size"] = 8.0
    plt.rcParams["xtick.major.width"] = plt.rcParams["axes.linewidth"]
    plt.rcParams["ytick.left"] = False
    plt.rcParams["ytick.labelleft"] = False

    if len(argv) > 1:
        if len(argv) < 6:
            msg = (
                f"\nCall {__file__} like this:\n"
                f"{__file__} samples clock_cycle_duration_str precursor "
                "length filename1 filename2 ..."
            )
            raise ValueError(msg)
        config.samples = int(argv[1])
        config.clock_cycle_duration = str(argv[2])
        config.precursor = int(argv[3])
        config.length = int(argv[4])
        config.filenames = [str(x) for x in argv[5:]]

    n_cycles = config.precursor + config.length + 3  # cycles that are shown

    x = np.linspace(0, 1, n_cycles*config.samples,
                    endpoint=False)
    dx = x[1]-x[0]
    y = 1.0 * np.exp(-(x - 1.2)**2 / 2.0 / 1.0**2)

    fig, ax = plt.subplots(1, 1)
    ax: Axes
    ax.set_prop_cycle(color=[blue])

    kwargs = {"align": "edge", "fc": "none", "lw": 0.5}
    # grey
    edgel = config.samples
    ax.bar(x[:edgel], y[:edgel], dx, ec="grey", **kwargs)
    edger = (n_cycles-1) * config.samples
    ax.bar(x[edger:], y[edger:], dx, ec="grey", **kwargs)
    # orange
    ax.bar(x[edgel:edger], y[edgel:edger], dx, ec=orange, zorder=2, **kwargs)

    xmin = -0.05
    ax.set_xlim(xmin-0.015, 1.015)
    ax.set_ylim(0.0, ax.get_ylim()[1]*1.2)

    ax.set_xticks(
        np.linspace(0.0, 1.0, n_cycles+1),
        [""] * (n_cycles+1),
    )
    # the clock cycle where trigger threshold is surpassed
    threshold_cycle = config.precursor + 1
    # the bin which is at threshold height
    threshold_idx = (threshold_cycle * config.samples
                     + config.samples//2) - 1

    ax.add_patch(Rectangle(
        (x[threshold_idx], 0), dx, y[threshold_idx],
        fc=lightorange, ec="none", zorder=1))

    ax.plot([xmin, 1.0], [y[threshold_idx]]*2, ls="-")
    ax.plot([xmin, 0], [0, 0], clip_on=False)

    # threshold
    arrowprops = dict(arrowstyle="<->", color=blue, clip_on=False)
    ax.annotate("", xy=(xmin/2, 0), xytext=(xmin/2, y[threshold_idx]),
                clip_on=False, arrowprops=arrowprops)
    ax.text(xmin/2-0.005, y[threshold_idx]/2.0, "threshold",
            rotation=90, va="center", ha="right", color=blue)

    # clock cycle duration
    ax.text(x=x[config.samples//2],
            y=-0.025,
            s=config.clock_cycle_duration,
            ha="center", va="top", color=blue, clip_on=False)

    # precursor
    yhigh = ax.get_ylim()[1]*0.98
    yofs = 0.01
    idx_l = config.samples
    idx_r = config.samples * (1 + config.precursor)
    ax.plot([x[idx_l]]*2, [yhigh, y[idx_l]])
    ax.plot([x[idx_r]]*2, [y[-1], y[idx_r]])

    ax.annotate("",
                xytext=(x[idx_r], y[-1]-yofs),
                xy=(x[idx_l], y[-1]-yofs),
                arrowprops=dict(arrowstyle="->", color=blue))
    ax.text(
        x[idx_l], y[-1]+3*yofs,
        f" precursor = {config.precursor}", color=blue)

    # length
    idx_r = config.samples*(n_cycles-1)
    idx_l = config.samples*(2 + config.precursor)
    ax.plot([x[idx_r]]*2,
            [yhigh, y[idx_r]])
    ax.plot([x[idx_l]]*2,
            [y[-1], y[idx_l]])

    ax.annotate("",
                xytext=(x[idx_r], y[-1]-yofs),
                xy=(x[idx_l], y[-1]-yofs),
                arrowprops=dict(arrowstyle="<-", color=blue))
    ax.text(
        x[idx_l], y[-1]+3*yofs,
        f" length = {config.length}", color=blue)

    # total length
    idx_l, idx_r = config.samples, config.samples*(n_cycles-1)
    ax.annotate("",
                xytext=(x[idx_r], yhigh-yofs),
                xy=(x[idx_l], yhigh-yofs),
                arrowprops=dict(arrowstyle="<->", color=blue))
    ax.text(
        0.5*(x[idx_l] + x[idx_r]),
        yhigh-5*yofs,
        f"total length = {config.precursor + config.length + 1}",
        color=blue, va="top", ha="center")

    fig.patch.set_linewidth(2)
    for filename in config.filenames:
        print(f"Creating .source/figures/{filename}")
        fig.savefig(f"./source/figures/{filename}",
                    edgecolor=fig.get_edgecolor())


if __name__ == "__main__":
    plot(
        Config(
            samples=8,
            clock_cycle_duration="5000 ps",
            precursor=1,
            length=2,
            filenames=["4ChannelTriggering.pdf",
                       "4ChannelTriggering.svg"]
        )
    )
