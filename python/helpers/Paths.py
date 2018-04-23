from os import path

base_d = path.join(path.abspath(path.dirname(__file__)), "../..")

# Path declarations
Accu_v = path.join(base_d, "samples/Accumulator.v")
Accu_o = path.join(base_d, "bin/Accumulator.o")
ALU_v = path.join(base_d, "verilog/ALU.v")
ALU_cosim_v = path.join(base_d, "verilog/ALU.v")
ALU_control_v = path.join(base_d, "verilog/ALU_control.v")
bj_calc = path.join(base_d, "verilog/branch_jump_calc.v")
Control_v = path.join(base_d, "verilog/Control.v")
CPU_Cosim_o = path.join(base_d, "bin/CPU_Cosim.o")
CPU_Cosim_v = path.join(base_d, "verilog/CPU_cosim.v")
DM_v = path.join(base_d, "verilog/Data_Memory.v")
EX_MEM_v = path.join(base_d, "verilog/EX_MEM.v")
FU_v = path.join(base_d, "verilog/Forwarding_Unit.v")
HD_v = path.join(base_d, "verilog/Hazard_Detection_Unit.v")
ID_EX_v = path.join(base_d, "verilog/ID_EX.v")
IF_ID_v = path.join(base_d, "verilog/IF_ID.v")
IM_v = path.join(base_d, "verilog/Instruction_Memory.v")
INDEX_256 = path.join(base_d, "samples/Index_Memory_256.hex")
MEM_WB_v = path.join(base_d, "verilog/MEM_WB.v")
MUX_v = path.join(base_d, "verilog/Multiplexers.v")
PC_v = path.join(base_d, "verilog/PC.v")
RF_v = path.join(base_d, "verilog/Register.v")
RF_cosim_v = path.join(base_d, "verilog/Register_cosim.v")
RF_cosim_o = path.join(base_d, "bin/Register_cosim.o")
myhdl_vpi = path.join(base_d, "bin/myhdl.vpi")
