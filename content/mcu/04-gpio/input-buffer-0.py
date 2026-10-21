import schemdraw
from schemdraw import dsp, logic
from schemdraw import elements as elem


def wrapper(elem):
    return elem.linestyle("--").color("gray").linewidth(1)


with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    pmos = elem.PMos().reverse().label("PMOS", "left")
    pmos = wrapper(pmos)
    nmos = elem.NMos().reverse().label("NMOS", "left")

    P = (
        logic.Line()
        .right(d.unit * 2)
        .at(pmos.gate)
        .label("gate", "top", ofst=(-0.2, 0.1), fontsize=10)
    )
    P = wrapper(P)
    N = (
        logic.Line()
        .right(d.unit * 2)
        .at(nmos.gate)
        .label("gate", "bottom", ofst=(-0.2, -0.1), fontsize=10)
    )

    mid_point = (P.end[0], pmos.drain[1])
    logic.Line().right(d.unit * 1.5).at(mid_point).idot(open=True).label(
        "1", "bottom", fontsize=10, color="red", ofst=(0.1, 0)
    )
    A = logic.Not().reverse()
    logic.Line().right(d.unit * 1.5).at(A.in1).label(
        "0", "bottom", fontsize=10, color="red", ofst=(0, -0.1)
    )
    dsp.Square().scale(d.unit * 0.5).label("Pin", "top", ofst=(0, 0.2))
    logic.Line().right(d.unit * 2)
    logic.Line().down(d.unit * 2)
    elem.Ground().label("GND", "bottom")

    wrapper(logic.Wire("|-").at(mid_point).to(P.end))
    logic.Wire("|-").at(mid_point).to(N.end)

    logic.Line().left(d.unit * 5).at(pmos.drain).label(
        "drain", ofst=(-0.8, -0.1), fontsize=10
    ).label("0", "bottom", fontsize=10, color="red", ofst=(1.0, 0.1))

    wrapper(logic.Line().up().at(pmos.source).dot().label("+VCC\nSource", "right"))
    logic.Line().down().at(nmos.source)
    elem.Ground().label("GND", "bottom")

    image_bytes = d.get_imagedata("svg")

with open("input-buffer-0.svg", "wb") as f:
    f.write(image_bytes)
