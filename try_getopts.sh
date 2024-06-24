# From https://stackoverflow.com/a/30026641/5555077
# The meaning of the formal OPTSTRING is explained at https://stackoverflow.com/a/34531699/5555077

# Transform long options to short ones
for arg in "$@"; do
  shift
  case "$arg" in
    '--help')   set -- "$@" '-h'   ;;
    '--number') set -- "$@" '-n'   ;;
    '--rest')   set -- "$@" '-r'   ;;
    '--ws')     set -- "$@" '-w'   ;;
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