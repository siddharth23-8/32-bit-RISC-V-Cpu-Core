# RISC V

## Table of contents:
- [Aim](#aim)
- [About the project](#about)
- [Theory](#Theory)
- [Flowchart](#Flowchart)
- [Tech stack](#software)
- [Getting Started](#Geting-started)
- [Usage](#Usage)
- [Screen shot and demo](#ss)
- [Future work](#future-work)
- [Troubleshooting](#Troubleshoot)
- [Contributors](#contributors)
- [Mentors](#mentors)
- [Acknowlegdements and Resources](#resources)

<a name="aim"></a>
## Aim:
![Main](https://user-images.githubusercontent.com/84727176/138549829-0a1ef365-6fe0-4a3b-8472-10c10c33a75e.png)

To build a 32-bit RISC V processor core in logisim.


<a name="about"></a>
## About the project:
RISC-V(Reduced Instruction Set Architecture) is an open standard instruction set architecture (ISA) based on established reduced instruction set computer (RISC) principles. Unlike most other ISA designs, the RISC-V ISA is provided under open source licenses that do not require fees to use.
This project focuses on making a RISC-V CPU Core using logisim software.

RISC-V is significant because it will allow smaller device manufacturers to build hardware without paying royalties and allow developers and researchers to design and experiment with a proven and freely available instruction set architecture. RISC-V is ideal for a variety of applications from IOTs to Embedded systems such as disks, CPUs, Calculators, SOCs, etc.

<a name="Theory"></a>
## Theory:
In a RISC V processor, first the **PC** (program counter) gives the byte adderess to **IMem** . IMem (Instruction Memory) is the place where program instructions are stored. IMem gives out the instruction located on address given by PC. This instruction is coded in RISC V ISA. It needs to be decoded in various fields and identified. This job is done by **Decode Logic** . After the instruction is identified and relevent data is extracted, we access the registers from **Register File**. Data from respective registers and/or IMM (Imediate value) is sent to **ALU** to perform computational and logical operations. Result of these operations can modify register values/ can be stored in **DMem** (Data Memory)/ can be desplayed on **7 segment output display**. **Control Logic** is the chip which monitors all this flow and controls which chip needs to be enabled.

*Note: This is the general flow for most of the commands. There are few exceptions like jump instruction where data needs to flow in different manner*

For more detailed information follow [Project Report](https://github.com/siddharth23-8/RISC-V/blob/Main/RISCV%20PROJECT.pdf)

<a name="Flowchart"></a>
## Flowchart:
![Flowchart](https://user-images.githubusercontent.com/84727176/138566664-0be35c0d-dea9-4b08-9c56-e8ab2842f929.jpeg)

<a name="software"></a>
## Tech stack:
- [Logisim](http://www.cburch.com/logisim/)
- [JVM](https://www.java.com/en/download/windows_manual.jsp) (To run logisim software)
- [Makerchip online IDE](https://makerchip.com/)
- [Github](https://github.com/)
- [Python 3](https://www.python.org/)

<a name="Geting-started"></a>
## Getting Started
- Download Logisim software from the link given above.
- Download logisim circuit [files](https://github.com/siddharth23-8/RISC-V/blob/Main/Main/Final.circ).
- Download text file of [program](https://github.com/siddharth23-8/RISC-V/blob/Main/IMem/Fibo.txt) and initial data.

<a name="Usage"></a>
## Usage
### To run Fibonacci series:
1. Open [final.circ](https://github.com/siddharth23-8/RISC-V/blob/Main/Main/Final.circ) in logisim
2. In main circuit, right click on IMEM chip and select 'View IMEM' from drop down
3. In IMEM circuit, right click on RAM module and load '[Fibo.txt](https://github.com/siddharth23-8/RISC-V/blob/Main/IMem/Fibo.txt)' from IMem folder
4. Back to main circuit, in the top right corner, click on load pin to activate processor
5. Turn on the clock from either the Simulate menu or using ctrl+k
6. To halt the program press ctrl+k
7. To reset the processor, press reset button
8. After reset, the processor is ready to load nest pogram

<a name="ss"></a>
## Screen shot and demo:
![Fibonacci_2971215073](https://user-images.githubusercontent.com/84727176/138549836-16440568-0fe9-4e85-acb3-da9d5ab02195.jpg)

### 32 bit processor running fibonacci series code:
![fibonacci](https://user-images.githubusercontent.com/84727176/138549853-234674b6-7d01-40c1-9a1c-c79e18afa5b9.gif)


<a name="future-work"></a>
## Future work:
- [ ] Add more instrcutions and functionality
- [ ] Create verilog model

<a name="Troubleshoot"></a>
## Troubleshooting
- Problem in Logisim installation
  - Check if your system has java installed
- Circuit showing-
  - Red wires: Reset the simulation from Simulate menu/ Check if all connections are correct (You can refer to images of circuits from indevidual folder)
  - Blue wire: Reset the simulation from Simulate menu/ make sure simulation is enabled
  - Gray wire: Check if all connections are correct (You can refer to images of circuits from indevidual folder)

<a name="contributors"></a>
## Contributors:
-   [Premraj Jadhav](https://github.com/Premraj02)
-   [Siddhesh Patil](https://github.com/Sidshx)
-   [Siddharth Sankhe](https://github.com/siddharth23-8)

<a name="mentors"></a>
## Mentors:
-   [Ninad Jangle](https://github.com/ninja3011)
-   [Gautam Agrawal](https://github.com/gautam-dev-maker)

<a name="resources"></a>
## Acknowlegdements and Resources:
-   [SRA VJTI Eklavya 2020](http://sra.vjti.info/)
