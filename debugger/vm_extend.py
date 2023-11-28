import sys

from architecture import VMState
from vm_step import VirtualMachineStep


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.handlers = {
            "d": self._do_disassemble,
            "dis": self._do_disassemble,
            "i": self._do_ip,
            "ip": self._do_ip,
            "m": self._do_memory,
            "memory": self._do_memory,
            "q": self._do_quit,
            "quit": self._do_quit,
            "r": self._do_run,
            "run": self._do_run,
            "s": self._do_step,
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
                elif command[0] not in self.handlers:
                    self.write(f"Unknown command {command[0]}")
                else:
                    interacting = self.handlers[command[0]](self.ip) if len(command) == 1 else self.handlers[command[0]](int(command[1]))
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]

    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, *args):
        if len(args) == 1:
            addr = int(args[0], 16)
            self.write(f"{addr:06x}: {self.ram[addr]:06x}")
        elif len(args) == 2:
            start_addr = int(args[0], 16)
            end_addr = int(args[1], 16)
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
