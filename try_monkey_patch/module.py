var = "please print me"
def _monkey_patch_print():
    global var
    print(var)

def print_():
    pass