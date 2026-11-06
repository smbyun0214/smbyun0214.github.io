import schemdraw
from schemdraw import dsp, logic
from schemdraw import elements as elem

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    # ==========================================
    # [1] 첫 번째 그림 (Current Sourcing)
    # ==========================================

    VDD = (
        dsp.Square()
        .scalex(d.unit)
        .scaley(d.unit * 2)
        .label(
            r"$+\text{V}_\text{DD}$",
            "top",
            ofst=(0, d.unit * 0.2),
            fontsize=d.unit * 25,
        )
    )

    logic.Line().right(d.unit * 3).at(VDD.E)
    logic.Line().down(d.unit * 2)

    IO = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("I/O Pin", "top", ofst=(0, -d.unit * 0.5), fontsize=d.unit * 25)
    )

    logic.Line().down(d.unit * 10)
    logic.Line().left(d.unit * 3)
    logic.Line().left(d.unit)
    logic.Line().left(d.unit * 3)

    logic.Wire("|-").to(VDD.W)

    logic.Line().right(d.unit * 2).at(IO.N)
    logic.Line().down()
    elem.Resistor().scale(d.unit).label(
        "R1", "bottom", ofst=(0, d.unit * 0.5), fontsize=d.unit * 25
    )
    logic.Line().down(d.unit * 2)
    elem.LED()
    logic.Line().down(d.unit * 3)
    elem.Ground()

    # ==========================================
    # [2] 두 번째 그림 (Current Sinking)
    # ==========================================

    VDD = (
        dsp.Square()
        .scalex(d.unit * 2)
        .scaley(d.unit)
        .at((d.unit * 15, d.unit))
        .label(
            r"$+\text{V}_\text{DD}$",
            "right",
            ofst=(-d.unit * 0.2, 0),
            fontsize=d.unit * 25,
        )
    )

    logic.Line().right(d.unit * 3).at(VDD.N)
    logic.Line().down(d.unit * 10)

    IO = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("I/O Pin", "top", ofst=(0, -d.unit * 0.5), fontsize=d.unit * 25)
    )

    logic.Line().down(d.unit * 2)
    logic.Line().left(d.unit * 3)

    VSS = (
        dsp.Square()
        .scaley(d.unit * 2)
        .scalex(d.unit)
        .label(
            r"$+\text{V}_\text{SS}$",
            "right",
            ofst=(-d.unit * 0.2, d.unit * 0.7),
            fontsize=d.unit * 25,
        )
    )

    logic.Line().left(d.unit * 3)

    logic.Wire("|-").to(VDD.S)

    logic.Line().right(d.unit * 2).at(IO.N)
    logic.Line().up()
    elem.LED().reverse().flip()
    logic.Line().up(d.unit * 2)
    elem.Resistor().scale(d.unit).label(
        "R1", "bottom", ofst=(0, -d.unit * 0.5), fontsize=d.unit * 25
    )
    logic.Line().up(d.unit * 3)
    elem.Vdd().label("5V", fontsize=d.unit * 25)

    image_bytes = d.get_imagedata("svg")

with open("current-sourcing-sinking.svg", "wb") as f:
    f.write(image_bytes)
