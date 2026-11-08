import schemdraw
from schemdraw import logic

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    logic.TimingDiagram(
        {
            "signal": [
                {"name": "CPOL=0", "wave": "0p........"},
                {"name": "CPOL=1", "wave": "1n........"},
            ]
        }
    )

    image_bytes = d.get_imagedata("svg")

with open("cpol-comparsion.svg", "wb") as f:
    f.write(image_bytes)
