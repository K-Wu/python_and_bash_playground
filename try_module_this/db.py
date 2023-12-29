# From https://stackoverflow.com/a/35904211/5555077
import sys

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

# we can explicitly make assignments on it
this.db_name = None

this.test_an_undefined_variable: list


def initialize_db(name):
    this.test_define_an_undefined_variable = "hello world"
    if this.db_name is None:
        # also in local function scope. no scope specifier like global is needed
        this.db_name = name
        # also the name remains free for local use
        db_name = "Locally scoped db_name variable. Doesn't do anything here."
    else:
        msg = "Database is already initialized to {0}."
        raise RuntimeError(msg.format(this.db_name))
