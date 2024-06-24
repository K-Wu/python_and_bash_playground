# From https://stackoverflow.com/a/30026641/5555077
# The meaning of the formal OPTSTRING is explained at https://stackoverflow.com/a/34531699/5555077

function print_usage {
  echo "Usage: $0 [options] [arguments]"
  echo "Options:"
  echo "  -h, --help    Print this help message"
  echo "  -n, --number  A number"
  echo "  -r, --rest    A flag"
  echo "  -w, --ws      A flag"
}

# Transform long options to short ones
for arg in "$@"; do
  shift
  case "$arg" in
    '--help')   set -- "$@" '-h'   ;;
    '--number') set -- "$@" '-n'   ;;
    '--rest')   set -- "$@" '-r'   ;;
    '--ws')     set -- "$@" '-w'   ;;
    "--"*)      echo "Unrecognized argument $arg"; print_usage; exit 2;;
    *)          set -- "$@" "$arg" ;;
  esac
done

# Default behavior
number=0; rest=false; ws=false

# Parse short options
OPTIND=1
while getopts "hn:rw" opt
do
  case "$opt" in
    'h') print_usage; exit 0 ;;
    'n') number=${OPTARG} ;;
    'r') rest=true ;;
    'w') ws=true ;;
    '?') print_usage >&2; exit 1 ;;
  esac
done
shift $(expr $OPTIND - 1) # remove options from positional parameters
echo "number+1=$((number+1)), rest=$rest, ws=$ws, args=$@"