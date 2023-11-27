from architecture import OPS as ops
import sys


class Disassembler:
    def __init__(self, lines, writer):
        self.lines = lines[:-1]
        self.writer = writer
        res = self.run()
        self.write_to_file(res)

    # loops fehled no
    def disassemble(self, line):
        print(line)
        assert len(line) == 6, f"not correct format"
        size = 2
        arr = [line[i : i + size] for i in range(0, 6, size)]
        op, arg1, arg2 = int(arr[2], 16), int(arr[1], 16), int(arr[0], 16)
        assert op in ops, f"{op} is not a valid operation"
        operation = ops[op]["code"]
        form = ops[op]["fmt"]
        a, b = "", ""
        if form == "r-":
            a = self.translate_params(arg1)
        elif form == "rr":
            a = self.translate_params(arg1)
            b = self.translate_params(arg2)
        elif form == "rv":
            a = self.translate_params(arg1)
            b = int(str(arg2), 10)
        return [operation, a, b]

    def run(self):
        res = []
        for x in self.lines:
            res.append(self.disassemble(x))
        return res

    @staticmethod
    def translate_params(arg1):
        arg1 = int(str(arg1), 10)
        assert arg1 < 4, f"register with number {arg1} does not exist"
        return "R" + str(arg1)

    def write_to_file(self, res):
        for x in res:
            self.writer.writelines(f"{x[0]} {x[1]} {x[2]}\n")


if __name__ == "__main__":
    assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} input|- output|-"
    reader = open(sys.argv[1], "r") if (sys.argv[1] != "-") else sys.stdin
    writer = open(sys.argv[2], "w") if (sys.argv[2] != "-") else sys.stdout
    Disassembler(reader.read().split("\n"), writer)
