import schemdraw
from schemdraw import dsp, logic
from schemdraw import elements as elem

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    pfet = elem.PFet().reverse()
    nfet = elem.NFet().reverse()

    p = (
        logic.Line()
        .left(d.unit * 2)
        .at(pfet.gate)
        .label("OFF", "top", ofst=(-0.2, -0.1), fontsize=d.unit * 14, color="green")
    )
    n = (
        logic.Line()
        .left(d.unit * 2)
        .at(nfet.gate)
        .label("ON", "bottom", ofst=(-0.2, 0.1), fontsize=d.unit * 14, color="green")
    )

    mid_point = (p.end[0], pfet.drain[1])
    logic.Line().left(d.unit * 1.5).at(mid_point)
    dsp.Square().scale(d.unit * 2.0).label(
        "Output\ncontrol", halign="center", valign="center", fontsize=d.unit * 14
    )
    logic.Line().left(d.unit * 1.5)
    dsp.Square().scale(d.unit * 0.5).fill("yellow").label(
        "DATA FROM\nCORE", "top", ofst=(0, -d.unit * 0.5), fontsize=d.unit * 14
    ).label(
        "'0'", "bottom", ofst=(0, d.unit * 0.5), fontsize=d.unit * 14, color="green"
    )
    logic.Line().right(d.unit * 1.5).at(nfet.drain)
    dsp.Square().scale(d.unit * 0.5).fill("gray").label(
        "EXTERNAL\nPAD", "top", ofst=(0, d.unit * 0.5), fontsize=d.unit * 14
    )
    logic.Line().right(d.unit * 1.5)
    down_line = logic.Line().down(d.unit * 0.5)
    down_line2 = logic.Line().down(d.unit * 2.5)
    cm = elem.CurrentMirror().down().at(down_line.end)

    logic.Wire("|-").at(mid_point).to(p.end)
    logic.Wire("|-").at(mid_point).to(n.end)

    vdd_y = pfet.source[1] + d.unit * 0.5
    gnd_y = nfet.source[1] - d.unit * 0.5

    logic.Wire("|-").at(pfet.source).to((pfet.source[0], vdd_y))
    logic.Wire("|-").at(nfet.source).to((nfet.source[0], gnd_y))
    logic.Wire("|-").at(cm.end).to((cm.end[0], gnd_y))
    elem.GroundChassis().reverse().at((nfet.source[0], gnd_y))

    # [start] Current
    current_offset = d.unit * 0.3

    start_pt = (cm.end[0] - current_offset, gnd_y + 0.1)
    corner1 = (cm.end[0] - current_offset, nfet.drain[1] - current_offset)
    corner2 = (nfet.source[0] + current_offset, nfet.drain[1] - current_offset)
    end_pt = (nfet.source[0] + current_offset, gnd_y + 0.1)

    logic.Wire("|-").at(start_pt).to(corner2).color("green").linewidth(2)
    logic.Wire("-|", arrow="->").at(corner1).to(end_pt).color("green").linewidth(2)

    # I_OH 라벨 추가
    logic.Line().at((nfet.source[0] + current_offset, gnd_y + d.unit)).length(0).color(
        "green"
    ).label(
        r"$\text{I}_\text{OH}$",
        loc="right",
        color="green",
        ofst=(0, d.unit * 0.5),
        fontsize=d.unit * 20,
    )
    # [end] Current

    vdd_line = (
        logic.Line()
        .at((p.end[0] - d.unit * 4, vdd_y))
        .right(d.unit * 16)
        .label("VDD", loc="start", halign="left", fontsize=d.unit * 20)
        .color("blue")
        .linewidth(4)
    )

    gnd_line = (
        logic.Line()
        .at((p.end[0] - d.unit * 4, gnd_y))
        .right(d.unit * 16)
        .label("GND", loc="start", halign="left", fontsize=d.unit * 20)
        .color("red")
        .linewidth(4)
    )

    image_bytes = d.get_imagedata("svg")

with open("io-sink-current.svg", "wb") as f:
    f.write(image_bytes)
