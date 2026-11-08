import schemdraw
import schemdraw.elements as elem
from schemdraw import flow, logic

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    # 1. Multiplexer 및 입력 신호 (HSI, HSE, PLL) 설정
    mux = elem.Multiplexer(
        pins=[
            elem.IcPin(anchorname="PLL", side="L"),
            elem.IcPin(anchorname="HSE", side="L"),
            elem.IcPin(anchorname="HSI", side="L"),
            elem.IcPin(anchorname="OUT", side="R"),
        ],
        leadlen=0,
        edgepadH=-d.unit,
        edgepadW=-d.unit * 2,
    )

    logic.Line(arrow="->").left(d.unit * 4).reverse().at(mux.HSI).label(
        "HSI", "left", fontsize=d.unit * 25
    )
    logic.Line().left(d.unit * 4).reverse().at(mux.HSE).linestyle(":").label(
        "HSE", "left", fontsize=d.unit * 25
    )
    logic.Line().left(d.unit * 4).reverse().at(mux.PLL).linestyle(":").label(
        "PLL", "left", fontsize=d.unit * 25
    )

    # 2. 16MHz 클럭 라인 및 APB2 버스 분주기 (Prescaler)
    logic.Line().right(d.unit * 5).at(mux.OUT).label(
        "16Mz", "top", fontsize=d.unit * 20
    )
    logic.Line(arrow="->").down(d.unit * 3)
    flow.RoundBox(w=d.unit * 2, h=d.unit * 2).label("/", "center").label(
        "APB2 bus prescalar", "right", ofst=(d.unit * 0.5, 0), fontsize=d.unit * 20
    )

    # 3. APB 2 버스 라인 (84 MHz Max)
    logic.Line(arrow="->").down(d.unit * 2)
    flow.Box(w=d.unit * 20, h=d.unit * 2).label(
        "APB 2 bus ( 84 Mhz Max)", "center", fontsize=d.unit * 25
    )

    # 4. SPI1 컨트롤러 및 SCLK (8MHz) 클럭 출력
    logic.Line(arrow="->").down(d.unit * 2).label(
        r"$f_{\text{pclk}} = 16\text{MHz}$", "bottom", fontsize=d.unit * 20
    )
    spi = flow.Box(w=d.unit * 4, h=d.unit * 2).label("SPI1", "center")

    logic.Line(arrow="->").left(d.unit * 2).at(spi.W)
    flow.RoundBox(w=d.unit * 2, h=d.unit * 2).label("/", "center").label(
        "Min Prescalr = 2", "top", ofst=(0, d.unit * 0.5), fontsize=d.unit * 20
    )
    logic.Line(arrow="->").left(d.unit * 4).label("SCLK", fontsize=d.unit * 20).label(
        "8MHz", "left", fontsize=d.unit * 25
    )

    # 5. 이미지 추출 및 파일 저장
    image_bytes = d.get_imagedata("svg")

with open("spi-serial-clock-frequency-1.svg", "wb") as f:
    f.write(image_bytes)
