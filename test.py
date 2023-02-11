
def isSectionFull(section):
    for stack in section:
        print(stack)
    for stack in section:
        if stack[-1] == [0, 0]:
            return False
    return True

section = [[[40+5,40+5],[40+10,40+10],[0,0]], [[40+14,40+14],[20+11,20+11],[20+11,20+5]]]

print(isSectionFull(section))