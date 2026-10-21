import schemdraw
from schemdraw import dsp, logic

with schemdraw.Drawing() as d:
    d.config(unit=0.5)
    output_buffer = (
        logic.Tristate(outputnot=False, controlnot=True).right().length(d.unit * 2.5)
    )
    logic.Line().left(d.unit * 6).at(output_buffer.in1).label("Output buffer", "top")
    logic.Line().up().at(output_buffer.c)
    logic.Line().left(d.unit * 6.5).label("Enable line", "top")
    branch = logic.Line().right().at(output_buffer.out).dot()
    logic.Line().right()
    dsp.Square().scale(d.unit * 0.5).label("Pin", "right", ofst=(1, 0))
    d.move_from(output_buffer.out, dy=-d.unit * 3)
    input_buffer = logic.Buf().left().length(d.unit * 2.5)
    logic.Line().left(d.unit * 5.9).at(input_buffer.out).label("Input buffer", "top")
    logic.Wire("-|").at(input_buffer.in1).to(branch.end)

    image_bytes = d.get_imagedata("svg")

with open("mcu-diagram.svg", "wb") as f:
    f.write(image_bytes)
