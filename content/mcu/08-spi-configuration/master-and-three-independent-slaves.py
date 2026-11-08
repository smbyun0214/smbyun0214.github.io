import schemdraw
import schemdraw.elements as elem
from schemdraw import dsp, logic

with schemdraw.Drawing() as d:
    d.config(unit=0.5)

    # 1. Master 및 Slaves IC 생성
    # Master IC (좌측) - 핀 이름을 안전한 식별자로 수정
    master = elem.Ic(
        pins=[
            elem.IcPin(anchorname="IO3", pin="IO3", side="right"),
            elem.IcPin(anchorname="IO2", pin="IO2", side="right"),
            elem.IcPin(anchorname="IO1", pin="IO1", side="right"),
            elem.IcPin(anchorname="SCK", pin="SCK", side="right"),
            elem.IcPin(anchorname="MOSI", pin="MOSI", side="right"),
            elem.IcPin(anchorname="MISO", pin="MISO", side="right"),
            elem.IcPin(anchorname="NSS1", pin="NSS1", side="right"),
        ],
        pinspacing=d.unit * 2,
    ).label("Master", "top", ofst=(-d.unit * 0.4, d.unit * 0.2), fontsize=d.unit * 30)

    # Slave 1 IC (우상단)
    slave1 = (
        elem.Ic(
            pins=[
                elem.IcPin(anchorname="NSS", pin="NSS", side="left"),
                elem.IcPin(anchorname="SCK", pin="SCK", side="left"),
                elem.IcPin(anchorname="MOSI", pin="MOSI", side="left"),
                elem.IcPin(anchorname="MISO", pin="MISO", side="left"),
            ],
            pinspacing=d.unit * 2,
        )
        .label(
            "Slave 1",
            loc="top",
            ofst=(d.unit * 0.5, d.unit * 0.2),
            fontsize=d.unit * 30,
        )
        .at((10, 2))
    )

    # Slave 2 IC (우중단)
    slave2 = (
        elem.Ic(
            pins=[
                elem.IcPin(anchorname="NSS", pin="NSS", side="left"),
                elem.IcPin(anchorname="SCK", pin="SCK", side="left"),
                elem.IcPin(anchorname="MOSI", pin="MOSI", side="left"),
                elem.IcPin(anchorname="MISO", pin="MISO", side="left"),
            ],
            pinspacing=d.unit * 2,
        )
        .label(
            "Slave 2",
            loc="top",
            ofst=(d.unit * 0.5, d.unit * 0.2),
            fontsize=d.unit * 30,
        )
        .at((10, -4))
    )

    # Slave 3 IC (우하단)
    slave3 = (
        elem.Ic(
            pins=[
                elem.IcPin(anchorname="NSS", pin="NSS", side="left"),
                elem.IcPin(anchorname="SCK", pin="SCK", side="left"),
                elem.IcPin(anchorname="MOSI", pin="MOSI", side="left"),
                elem.IcPin(anchorname="MISO", pin="MISO", side="left"),
            ],
            pinspacing=d.unit * 2,
        )
        .label(
            "Slave 3",
            loc="top",
            ofst=(d.unit * 0.5, d.unit * 0.2),
            fontsize=d.unit * 30,
        )
        .at((10, -10))
    )

    # 2. Master NSS1 풀업 (+VDD) 연결 및 'X' 표시
    logic.Line().at(master.NSS1).length(d.unit * 2)
    logic.Line().up()
    elem.Vdd().label(r"$+\text{V}_\text{DD}$")

    # 3. 공유 데이터/클럭 버스 연결 (MISO, MOSI, SCK)
    elem.Wire("-|").at(master.MISO).to(slave1.MISO)
    elem.Wire("-|").at(master.MOSI).to(slave1.MOSI)
    elem.Wire("-|").at(master.SCK).to(slave1.SCK)
    elem.Wire("-|").at(master.IO1).to(slave1.NSS)

    m_miso = logic.Line().right(d.unit * 9).at(master.MISO).dot()
    m_mosi = logic.Line().right(d.unit * 7).at(master.MOSI).dot()
    m_sck = logic.Line().right(d.unit * 5).at(master.SCK).dot()
    m_io2 = logic.Line().right(d.unit * 3).at(master.IO2)
    m_io3 = logic.Line().right(d.unit).at(master.IO3)

    s2_miso = logic.Line().left(d.unit * 4).at(slave2.MISO).dot()
    s2_mosi = logic.Line().left(d.unit * 6).at(slave2.MOSI).dot()
    s2_sck = logic.Line().left(d.unit * 8).at(slave2.SCK).dot()

    elem.Wire().at(m_miso.end).to(s2_miso.end)
    elem.Wire().at(m_mosi.end).to(s2_mosi.end)
    elem.Wire().at(m_sck.end).to(s2_sck.end)
    elem.Wire("|-").at(m_io2.end).to(slave2.NSS)

    s3_miso = logic.Line().left(d.unit * 4).at(slave3.MISO).dot()
    s3_mosi = logic.Line().left(d.unit * 6).at(slave3.MOSI).dot()
    s3_sck = logic.Line().left(d.unit * 8).at(slave3.SCK).dot()

    elem.Wire().at(m_miso.end).to(s3_miso.end)
    elem.Wire().at(m_mosi.end).to(s3_mosi.end)
    elem.Wire().at(m_sck.end).to(s3_sck.end)
    elem.Wire("|-").at(m_io3.end).to(slave3.NSS)

    image_bytes = d.get_imagedata("svg")

with open("master-and-three-independent-slaves.svg", "wb") as f:
    f.write(image_bytes)
