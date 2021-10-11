import pdb

# For Debugging

def seq(n):
    for i in range(n):
        pdb.set_trace()  # breakpoint | halt
        print(i)
    return

seq(4)