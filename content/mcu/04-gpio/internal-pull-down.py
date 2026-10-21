import schemdraw
from schemdraw import dsp, logic
from schemdraw import elements as elem

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    A = logic.Buf().left()
    logic.Line().at(A.out)
    L = logic.Line().right(d.unit * 3).at(A.in1)
    B = dsp.Square().scale(d.unit * 0.5).label("Pin", "top", ofst=(1.5, 0.2))
    logic.Line().right(d.unit * 2).dot()
    elem.CurrentLabelInline(direction="in").reverse().scale(0.6)
    logic.Line().down(d.unit * 2).at(B.S)
    logic.Line().up(d.unit * 2).at(B.N)
    logic.Line().down().at(L.center)
    elem.Resistor().scale(0.5).label(
        "Internal Pull-Down", "top", ofst=(0, -0.2), fontsize=10
    )
    elem.Ground()

    image_bytes = d.get_imagedata("svg")

with open("internal-pull-down.svg", "wb") as f:
    f.write(image_bytes)
