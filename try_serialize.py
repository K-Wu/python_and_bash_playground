from ...kernel_search import utils
import argparse
from ...kernel_search.configs import get_triton_gemm_argparser


def main(args: argparse.Namespace):
    state = utils.SearchState()
    state.config = utils.SearchConfig("test", args)
    print(state.config)
    utils.store_checkpoint(state, ".", "try_serialize")
    loaded_state = utils.load_last_checkpoint(".", "try_serialize")
    print(loaded_state)


if __name__ == "__main__":
    argparser: argparse.ArgumentParser = get_triton_gemm_argparser()
    args: argparse.Namespace = argparser.parse_args()
    print(args)

    main(args)
