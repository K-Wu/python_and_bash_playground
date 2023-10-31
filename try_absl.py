# From https://abseil.io/docs/python/quickstart
# pip install absl-py
from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string("name", "Jane Random", "Your name.")


def main(argv):
    print("Happy, ", FLAGS.name)


if __name__ == "__main__":
    app.run(main)
