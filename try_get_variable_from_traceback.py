# From https://stackoverflow.com/questions/36579554/how-can-i-extract-local-variables-from-a-stack-trace
import sys
import traceback


def boom(x, y):
    x / y


def main():
    x = 2
    y = 0
    boom(x, y)


def main2():
    import inspect

    print(traceback.format_stack())
    # len(traceback.format_stack()) == 3, and traceback.format_stack()[len(traceback.format_stack()) -1 - 2] is the frame of the caller at if __name__=="__main__". The traceback is '  File "/home/kwu/HET/hrt/misc/playground/try_get_variable_from_traceback.py", line 41, in <module>\n    main2_wrapper()\n'

    # Therefore we need to call .f_back twice to get the frame of the caller at if __name__=="__main__"
    frame = inspect.currentframe().f_back.f_back
    print(frame.f_locals)


def main2_wrapper():
    main2()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Most debuggers allow you to just do .post_mortem()
        # but see https://github.com/gotcha/ipdb/pull/94
        tb = sys.exc_info()[2]
        print(e)
        print(type(tb))
        print(tb.tb_next.tb_frame.f_locals["x"])

    ddd = 5
    main2_wrapper()
