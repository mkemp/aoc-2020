with open('input') as f:
    lines = [(op, int(arg)) for op, _, arg in (line.partition(' ') for line in f.read().strip().split('\n'))]


# Part 1
def run_until_loop(lines):
    idx, executed = 0, set()
    accumulator = 0
    while idx not in executed and idx < len(lines):
        executed.add(idx)
        op, arg = lines[idx]
        if op == 'jmp':
            idx += arg
        else:
            if op == 'acc':
                accumulator += arg
            idx += 1
    return accumulator, idx, executed


print(run_until_loop(lines)[0])


# Part 2
def repair_code(lines):
    accumulator, idx, executed = run_until_loop(lines)
    if idx < len(lines):
        possible_fixes = {
            f_idx: ('jmp' if lines[f_idx][0] == 'nop' else 'nop', lines[f_idx][1])
            for f_idx in executed if lines[f_idx][0] in ('jmp', 'nop')
        }
        for f_idx, instruction in possible_fixes.items():
            f_lines = lines[:]
            f_lines[f_idx] = instruction
            accumulator, idx, _ = run_until_loop(f_lines)
            if idx == len(lines):
                return accumulator
    return 'still broken'


print(repair_code(lines))
