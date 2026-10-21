import schemdraw
from schemdraw import dsp, logic
from schemdraw import elements as elem

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    nmos = elem.NMos().label("NMOS")

    N = (
        logic.Line()
        .left(d.unit * 2)
        .at(nmos.gate)
        .label("gate", "top", ofst=(-0.2, -0.1), fontsize=10)
    )
    A = logic.Not().left().at(N.end).reverse()
    logic.Line().left(d.unit * 1.5).at(A.in1)
    elem.CurrentLabelInline(direction="in").reverse().scale(0.5)

    logic.Line().right(d.unit * 5).at(nmos.drain).label(
        "drain", ofst=(-0.8, 0.15), fontsize=10
    )
    dsp.Square().scale(d.unit * 0.5).label("Pin", "top", ofst=(0, 0.2))
    logic.Line().right(d.unit * 2).dot()

    logic.Line().up(d.unit * 2).at(nmos.drain)
    elem.Resistor().scale(0.5)
    logic.Line().up().dot().label("+VCC", "right")

    logic.Line().down().at(nmos.source)
    elem.Ground().label("GND", "bottom")

    image_bytes = d.get_imagedata("svg")

with open("open-drain-pull-up.svg", "wb") as f:
    f.write(image_bytes)
