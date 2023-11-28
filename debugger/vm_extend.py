import sys

from architecture import VMState
from vm_step import VirtualMachineStep


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.handlers = {
            "dis": self._do_disassemble,
            "ip": self._do_ip,
            "memory": self._do_memory,
            "quit": self._do_quit,
            "run": self._do_run,
            "step": self._do_step,
        }
    # [/init]

    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        while interacting:
            try:
                command = self.read(f"{addr:06x} [{prompt}]> ")
                assert len(command) == 1 or len(command) == 2, f"to many arguments\n"
                if not command:
                    continue
                else:
                    arg = self.__check_if_in_ops(command[0])
                    interacting = self.handlers[arg](self.ip) if len(command) == 1 else self.handlers[arg](int(command[1]))
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]
    def __check_if_in_ops(self, arg):
        inOps = False
        val = ""
        for key in self.handlers:
            if key.startswith(arg):
                val = key
                inOps = True
        assert inOps, f"operation: {arg} not a valid operation\n"
        return val
    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, *args):
        if len(args) == 1:
            addr = int(str(args[0]), 16)
            self.write(f"{addr:06x}: {self.ram[addr]:06x}")
        elif len(args) == 2:
            start_addr = int(str(args[0]), 16)
            end_addr = int(str(args[1]), 16)
            for addr in range(start_addr, end_addr + 1):
                self.write(f"{addr:06x}: {self.ram[addr]:06x}")
        else:
            self.show()
    # [/memory]

    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    # [step]
    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
    # [/step]


if __name__ == "__main__":
    VirtualMachineExtend.main()
