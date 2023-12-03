
from architecture import OPS, VMState, NUM_REG
from vm_extend import VirtualMachineExtend


class VirtualMachineBreak(VirtualMachineExtend):
    # [init]
    def __init__(self):
        super().__init__()
        self.breaks = {}
        self.watchpoints = []
        self.handlers |= {
            "break": self._do_add_breakpoint,
            "clear": self._do_clear_breakpoint,
            "watchpoint": self._do_add_watchpoint,
            "erasewatchpoint": self._do_erase_watchpoint
        }
    # [/init]

    # [show]
    def show(self):
        super().show()
        if self.breaks:
            self.write("-" * 6)
            for key, instruction in self.breaks.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")
    # [/show]

    # [run]
    def run(self):
        self.state = VMState.STEPPING
        while self.state != VMState.FINISHED:
            watchpoint_reached = self._check_watchpoints()
            self._update_watchpoints()
            instruction = self.ram[self.ip]
            op, arg0, arg1 = self.decode(instruction)

            if op == OPS["brk"]["code"]:
                original = self.breaks[self.ip]
                op, arg0, arg1 = self.decode(original)
                self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)

            else:
                if watchpoint_reached:
                    super().show()
                    self.state = VMState.STEPPING
                if self.state == VMState.STEPPING:
                    self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)
    # [/run]

    # [add]
    def _do_add_breakpoint(self, addr):
        if self.ram[addr] == OPS["brk"]["code"]:
            return True
        self.breaks[addr] = self.ram[addr]
        self.ram[addr] = OPS["brk"]["code"]
        return True
    # [/add]

    # [clear]
    def _do_clear_breakpoint(self, addr):
        if self.ram[addr] != OPS["brk"]["code"]:
            return True
        self.ram[addr] = self.breaks[addr]
        del self.breaks[addr]
        return True
    # [/clear]

    def _do_add_watchpoint(self, addr):
        assert addr < len(self.ram), f"addr not valid in memory nor registers\n"

        if addr < len(self.ram):
            val = self.ram[addr]
            self.watchpoints.append([addr, val, True])
        if addr < len(self.reg):
            val = self.reg[addr]
            self.watchpoints.append([addr, val, False])
        return True

    def _do_erase_watchpoint(self, addr):
        for i in range(len(self.watchpoints) -1, -1, -1):
            curr = self.watchpoints[i][0]
            if curr == addr:
                self.watchpoints.pop(i)
        return True

    def _update_watchpoints(self):
        for x in self.watchpoints:
            x[1] = self.ram[x[0]] if x[2] else self.reg[x[0]]

    def _check_watchpoints(self):
        for x in self.watchpoints:
            if x[1] != self.ram[x[0]] and x[2]:
                self.write(f"old: {x[1]} new: {self.ram[x[0]]}")
                return True
            if x[0] < NUM_REG and x[1] != self.reg[x[0]] and not x[2]:
                self.write(f"old: {x[1]} new: {self.reg[x[0]]}")
                return True
        return False

if __name__ == "__main__":
    VirtualMachineBreak.main()
