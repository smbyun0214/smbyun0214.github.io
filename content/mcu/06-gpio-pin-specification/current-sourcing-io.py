import schemdraw
from schemdraw import dsp, logic

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    # ==========================================
    # [1] 첫 번째 그림 (왼쪽: 5 I/Os)
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
    logic.Line().down()

    IO0 = (
        dsp.Square()
        .scalex(d.unit)
        .scaley(d.unit * 2)
        .label("1", "center", fontsize=d.unit * 20)
        .label("I/Os", "right", ofst=(-d.unit * 0.5, d.unit), fontsize=d.unit * 25)
    )
    logic.Line().down()
    IO1 = (
        dsp.Square()
        .scalex(d.unit)
        .scaley(d.unit * 2)
        .label("2", "center", fontsize=d.unit * 20)
    )
    logic.Line().down()
    IO2 = (
        dsp.Square()
        .scalex(d.unit)
        .scaley(d.unit * 2)
        .label("3", "center", fontsize=d.unit * 20)
    )
    logic.Line().down()
    IO3 = (
        dsp.Square()
        .scalex(d.unit)
        .scaley(d.unit * 2)
        .label("4", "center", fontsize=d.unit * 20)
    )
    logic.Line().down()
    IO4 = (
        dsp.Square()
        .scalex(d.unit)
        .scaley(d.unit * 2)
        .label("5", "center", fontsize=d.unit * 20)
    )
    logic.Line().down()

    logic.Line().down()
    logic.Line().left(d.unit * 3)
    logic.Line().left(d.unit)
    logic.Line().left(d.unit * 3)

    logic.Wire("|-").to(VDD.W)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO0.S).label(
        "125mA", ofst=(d.unit * 0.2, d.unit * 0.5), fontsize=d.unit * 15
    )
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO1.S)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO2.S)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO3.S)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO4.S)

    logic.Line(arrow="->").right(d.unit).at(IO0.N).label(
        "25mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO1.N).label(
        "25mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO2.N).label(
        "25mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO3.N).label(
        "25mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO4.N).label(
        "25mA", "right", fontsize=d.unit * 20
    )

    # ==========================================
    # [2] 두 번째 그림 (오른쪽: 20 I/Os)
    # ==========================================

    VDD = (
        dsp.Square()
        .scalex(d.unit)
        .scaley(d.unit * 2)
        .at((d.unit * 15, 0))
        .label(
            r"$+\text{V}_\text{DD}$",
            "top",
            ofst=(0, d.unit * 0.2),
            fontsize=d.unit * 25,
        )
    )

    logic.Line().right(d.unit * 3).at(VDD.E)
    logic.Line().down()

    IO0 = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("1", "center", fontsize=d.unit * 15)
        .label("I/Os", "right", ofst=(-d.unit, d.unit), fontsize=d.unit * 25)
    )
    logic.Line().down(d.unit * 0.5)
    IO1 = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("2", "center", fontsize=d.unit * 15)
    )
    logic.Line().down(d.unit * 0.5)
    IO2 = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("3", "center", fontsize=d.unit * 15)
    )
    logic.Line().down(d.unit * 0.5)
    IO3 = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("4", "center", fontsize=d.unit * 15)
    )
    logic.Line().down(d.unit * 0.5)
    IO4 = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("5", "center", fontsize=d.unit * 15)
    )
    logic.Line().down(d.unit * 0.5)

    logic.Line().down(d.unit * 5)

    IO5 = (
        dsp.Square()
        .scalex(d.unit * 0.5)
        .scaley(d.unit * 2)
        .label("20", "center", fontsize=d.unit * 15)
    )
    logic.Line().down(d.unit * 0.5)

    logic.Line().left(d.unit * 3)
    logic.Line().left(d.unit)
    logic.Line().left(d.unit * 3)

    logic.Wire("|-").to(VDD.W)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO0.S).label(
        "240mA", ofst=(d.unit * 0.2, d.unit * 0.5), fontsize=d.unit * 15
    )
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO1.S)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO2.S)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO3.S)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO4.S)
    logic.Wire("|-", arrow="->").at(VDD.S).to(IO5.S)

    logic.Line(arrow="->").right(d.unit).at(IO0.N).label(
        "12mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO1.N).label(
        "12mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO2.N).label(
        "12mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO3.N).label(
        "12mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO4.N).label(
        "12mA", "right", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").right(d.unit).at(IO5.N).label(
        "12mA", "right", fontsize=d.unit * 20
    )

    image_bytes = d.get_imagedata("svg")

with open("current-sourcing-io.svg", "wb") as f:
    f.write(image_bytes)
