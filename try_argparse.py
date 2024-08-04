#!/usr/bin/env python3
import argparse


def my_add_argument(parser):
    parser.add_argument(
        "--sort_by_src", action="store_true", help="sort by src"
    )
    parser.add_argument(
        "--default_true_arg",
        default=True,
        action="store_false",
        help="sort by src",
    )
    parser.add_argument(
        "--str_arg", type=str, help="str arg", default="str_arg"
    )
    parser.add_argument(
        "--take_in_list_test",
        nargs="+",
        type=int,
        help="take in list test",
        default=[10, 25],
    )
    parser.add_argument(
        "--enable-nsys",
        action="store_true",
        help="Enable nsys profiling",
    )
    parser.add_argument(
        "--nsys-duration",
        type=int,
        default=0,
        help="The duration of nsys profiling. It is useful only when nsys profiling is turned on \
                If it is set to 0, nsys profile until the program ends. \
                Otherwise, nsys profiling is enabled and the duration is the time in seconds.",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RGCN")
    my_add_argument(parser)

    parser2 = argparse.ArgumentParser(description="RGCN")
    args = parser.parse_args([])
    print(args)
    print(vars(args))
    print(args.sort_by_src)
    print(vars(args)["sort_by_src"])
    args.sort_by_src = True
    args.sort_by_src = False

    args = parser.parse_args()
    print(args)
    print(parser2.parse_args())
