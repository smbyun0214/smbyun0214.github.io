import schemdraw
from schemdraw import dsp, logic
from schemdraw import elements as elem


def wrapper(elem):
    return elem.linestyle("--").color("gray").linewidth(1)


with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    pmos = elem.PMos().label("PMOS")
    nmos = elem.NMos().label("NMOS")
    nmos = wrapper(nmos)

    P = (
        logic.Line()
        .left(d.unit * 2)
        .at(pmos.gate)
        .label("gate", "top", ofst=(-0.2, -0.1), fontsize=10)
    )
    N = (
        logic.Line()
        .left(d.unit * 2)
        .at(nmos.gate)
        .label("gate", "bottom", ofst=(-0.2, 0.1), fontsize=10)
    )
    N = wrapper(N)

    mid_point = (P.end[0], pmos.drain[1])
    logic.Line().left(d.unit * 1.5).at(mid_point).idot(open=True).label(
        "0", "bottom", fontsize=10, color="red", ofst=(0.1, 0)
    )
    A = logic.Not().left().reverse()
    logic.Line().left(d.unit * 1.5).at(A.in1).label(
        "1", "bottom", fontsize=10, color="red"
    )

    logic.Wire("|-").at(mid_point).to(P.end)
    wrapper(logic.Wire("|-").at(mid_point).to(N.end))

    logic.Line().right(d.unit * 5).at(pmos.drain).label(
        "drain", ofst=(-0.8, 0.15), fontsize=10
    )
    dsp.Square().scale(d.unit * 0.5).label("Pin", "top", ofst=(0, 0.2))
    logic.Line().right(d.unit * 2).dot().label(
        "1", "bottom", fontsize=10, color="red", ofst=(0, -0.03)
    )

    logic.Line().up().at(pmos.source).dot().label("+VCC\nSource", "right")
    wrapper(logic.Line().down().at(nmos.source))
    wrapper(elem.Ground().label("GND", "bottom"))

    image_bytes = d.get_imagedata("svg")

with open("output-buffer-1.svg", "wb") as f:
    f.write(image_bytes)
