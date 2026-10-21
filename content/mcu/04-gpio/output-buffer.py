import schemdraw
from schemdraw import dsp, logic
from schemdraw import elements as elem

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    pmos = elem.PMos().label("PMOS")
    nmos = elem.NMos().label("NMOS")

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

    mid_point = (P.end[0], pmos.drain[1])
    logic.Line().left(d.unit * 1.5).at(mid_point).idot(open=True)
    A = logic.Not().left().reverse()
    logic.Line().left(d.unit * 1.5).at(A.in1)

    logic.Wire("|-").at(mid_point).to(P.end)
    logic.Wire("|-").at(mid_point).to(N.end)

    logic.Line().right(d.unit * 5).at(pmos.drain).label(
        "drain", ofst=(-0.8, 0.1), fontsize=10
    )
    dsp.Square().scale(d.unit * 0.5).label("Pin", "top", ofst=(0, 0.2))
    logic.Line().right(d.unit * 2).dot()

    logic.Line().up().at(pmos.source).dot().label("+VCC\nSource", "right")
    logic.Line().down().at(nmos.source)
    elem.Ground().label("GND", "bottom")

    image_bytes = d.get_imagedata("svg")

with open("output-buffer.svg", "wb") as f:
    f.write(image_bytes)
