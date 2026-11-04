+++
date = '2026-11-04T15:12:57+09:00'
draft = true
title = '05 GPIO Pin Specification'
+++

## Absolute Maximum Ratings

Production Specification에는 AMR(Absolute Maximum Ratings)에 대한 내용이 있는데, 여기에는 MCU 칩에 대한 허용가능한 전압, 전류, 온도 특성이 적혀있다.

![Product Specification 11. Voltage Characteristics](product-specification-11-voltage-characteristics.webp)

위 표는 전압 특성에 대한 내용으로, $\text{V}_\text{DD}$는 MCU로 공급되는 외부에서 공급되는 main power supply를 의미하며, 이는 MCU가 $\text{V}_\text{DD}$ 파워 핀을 통해 외부에서 공급된다는 것을 말한다.

MCU가 정상적으로 동작하기 위한 $\text{V}_\text{DD}$는 $1.8 \text{V} \le \text{V}_\text{DD} \le 3.6 \text{V}$ 이다. 만약 $1.8 \text{V}$보다 낮은 전압이 인가되면 MCU는 정상적으로 동작하지 못한다.

위 표에 따르면, MCU가 수용할 수 있는 $\text{V}_\text{DD}$의 최대 전압은 $4 \text{V}$이다. 이는 Symbol 칼럼의 $\text{V}_\text{DD}-\text{V}_\text{SS}$ 항목의 MAX 컬럼에서 확인할 수 있다. 만약 이를 초과하면 MCU는 고장날 수 있다. 때문에 어떤 MCU를 사용하던, AMR을 확인해서 적절한 전압을 확인해야만 한다.

$\text{V}_\text{SS}$는 MCU의 ground reference를 의미하며 이는 $0 \text{V}$로 유지되어야 하나, 위 표에 따르면 $\text{V}_\text{SS}$는 최소 $-0.3 \text{V}$까지 허용된다. 이는 Symbol 칼럼의 $\text{V}_\text{DD}-\text{V}_\text{SS}$ 항목의 MIN 컬럼에서 확인할 수 있다.

### General Operating Conditions

![Product Specification 14. General Operating Conditions](product-specification-14-general-operating-conditions-0.webp) ![Product Specification 14. General Operating Conditions](product-specification-14-general-operating-conditions-1.webp)

General operating condition은 MCU가 정상 동작을 보장하는 조건에 대해 설명한다. 그렇기 때문에, MCU의 $\text{V}_\text{DD}$ 핀에 전압을 공급하기 전에 이 조건을 반드시 확인해야 한다. MCU의 정상 동작을 위해서는 전압뿐만 아니라 동작 주파수 및 온도 조건도 함께 고려해야 한다.

$\text{V}_\text{DD}$ 항목을 확인해보면, 해당 칩은 $1.7 \text{V} \sim 3.6 \text{V}$ 범위에서 동작이 보장된다. $\text{V}_\text{DDA}$는 MCU의 아날로그 블록에 사용되는 전압으로, ADC, DAC과 같은 아날로그 주변장치에 공급되는 전압을 의미한다.

#### $\text{V}_\text{IN}$

![Product Specification 17. Input Voltage Measurement](product-specification-17-input-voltage-measurement.webp)

$\text{V}_\text{IN}$은 MCU I/O 핀에 인가되는 입력 전압을 말한다.

STM32 Microcontroller는 주로 2가지 종류의 GPIO 핀을 구조를 가진다. 하나는 $\text{TT}$(Three volt tolerant), 다른 하나는 $\text{FT}$(Five-volt tolerant)이다.
$\text{TT}$는 $3.3 \text{V}$ 전압을 수용할 수 있는 GPIO 핀이고, $\text{FT}$는 $5 \text{V}$ 전압을 수용할 수 있는 GPIO 핀을 의미이다.
$\text{TT}$, $\text{FT}$ 외에 $\text{TTa}$ 핀도 존재하는데, 이는 $\text{TT}$이면서 ADC 등 아날로그 주변장치와 연결되는 핀을 의미하며, $\text{TT}$와 동일하게 생각해도 된다.

![Product Specification 8. STM32F401xB:STM32F401xC Pin Definitions](product-specification-8-STM32F401xB:STM32F401xC-pin-definitions.webp)

위 테이블을 보면 각 GPIO 핀의 I/O 구조를 알 수 있는데, 현재 사용하는 STM32F401CCU6의 모든 GPIO 핀은 $\text{FT}$이다. 하지만, 다른 칩의 경우 특정 GPIO 핀이 $\text{TT}$ 일수도 있으니 확인이 필요하다. GPIO 핀의 I/O 구조가 $\text{TT}$일때, $3.3 \text{V}$ 이상의 전압이 들어오면 다이오드에 손상될 수 있기 때문이다.

#### Three-volt tolerant pin ($\text{TT}$ or $\text{TTa}$)

최대 $\text{V}_\text{IN}$ 전압은 $\text{V}_\text{DD} + 0.3 \text{V}$ 이다. 이를 초과하면 $\text{TT(a)}$ 핀이 손상을 입거나 칩 자체에 장애가 생길 수 있다.

$\text{TT(a)}$ 핀에 대한 general operating condition은 $\text{V}_\text{SS} -0.3  \text{V} \le \text{V}_\text{IN} \le \text{V}_\text{DD} + 0.3 \text{V}$ 이다.

STM32 Microcontroller가 전원이 꺼져있어서 $\text{V}_\text{DD} = 0$인 경우, GPIO의 $\text{TT}$ 핀의 $\text{V}_\text{IN} \gt 0.3 \text{V}$가 되어서는 안된다.

#### Five-volt tolerant pin ($\text{FT}$)

GPIO 핀이 $\text{FT}$ I/O 구조를 갖는다는 의미는 $-0.3 \text{V} \le \text{V}_\text{IN} \le 5.5 \text{V}$ 범위의 전압이 들어올 때 Voltage protection이 보장된다는 의미이다. 회로로 들어오는 전압이 특정 기준치(상한선이나 하한선)를 넘어가지 못하도록 강제로 제한하는 보호 다이오드를 통해 Voltage protection가 보장된다.

GPIO는 오직 Input mode에서만 $\text{FT}$를 사용할 수 있으며, Output mode나 analog 모드에서는 사용할 수 없다. GPIO $\text{FT}$ 핀의 최대 $\text{V}_\text{IN}$은 $\text{V}_\text{DD} + 4\text{V}$ 이다.

$\text{FT}$ 핀에 대한 general operating condition은 $\text{V}_\text{SS} -0.3  \text{V} \le \text{V}_\text{IN} \le 5.5 \text{V}$이다. 즉, $\text{FT}$ 핀은 어떠한 경우에서도 $\text{V}_\text{IN} \gt 5.5 \text{V}$이 되어서는 안된다.

STM32 Microcontroller가 전원이 꺼져있어서 $\text{V}_\text{DD} = 0$인 경우, GPIO의 $\text{FT}$ 핀의 $\text{V}_\text{IN} \gt 4 \text{V}$가 되어서는 안된다.

### Current characteristics

![Product Specification 12. Current Characteristics](product-specification-12-current-characteristics.webp)

$\text{I}_\text{VDD}$는 $\text{V}_\text{DD}$ power line으로 흘러 들어가는 전체 전류를 의미한다. $\text{I}_\text{VSS}$는 $\text{V}_\text{SS}$ ground line에서 흘러 나가는에서 전체 전류를 의미한다.

$\text{I}_\text{IO}$에는 2가지 종류의 전류가 있는데, 하나는 MCU에서 외부로 흘러 나가는 source current이고, 다른 하나는 MCU로 흘러 들어오는 sink current이다.

#### I/O Source Current

![I/O Source Current](io-source-current.svg)

핀 출력이 HIGH('1')일 때, 내부 PMOS가 켜지면서 칩 내부($\text{V}_\text{DD}$)에서 외부 회로로 전류가 흘러 나간다. 참고로 핀 하나당 안전하게 흘려보낼 수 있는 최대 전류는 보통 $25 \text{mA}$로 제한된다.

#### I/O Sink Current

![I/O Sink Current](io-sink-current.svg)

핀 출력이 LOW('0')일 때, 내부 NMOS가 켜지면서 외부 회로의 전류가 핀을 타고 들어와 접지($\text{V}_\text{SS}$)로 빠져나간다. 참고로 핀 하나당 최대 $25 \text{mA}$를 넘으면 칩이 손상될 수 있다.
