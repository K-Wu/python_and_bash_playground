# From https://stackoverflow.com/a/30026641/5555077
# The meaning of the formal OPTSTRING is explained at https://stackoverflow.com/a/34531699/5555077

function print_usage {
  echo "Usage: $0 [options] [arguments]"
  echo "Options:"
  echo "  -h, --help    Print this help message"
  echo "  -n, --number  A number"
  echo "  -m, --model  A string"
  echo "  -r, --rest    A flag"
  echo "  -w, --ws      A flag"
}

# Transform long options to short ones
for arg in "$@"; do
  shift
  case "$arg" in
    '--help')   set -- "$@" '-h'   ;;
    '--number') set -- "$@" '-n'   ;;
    '--model') set -- "$@" '-m'   ;;
    '--rest')   set -- "$@" '-r'   ;;
    '--ws')     set -- "$@" '-w'   ;;
    "--"*)      echo "Unrecognized argument $arg"; print_usage; exit 2;;
    *)          set -- "$@" "$arg" ;;
  esac
done

# Default behavior
number=0; model=""; rest=false; ws=false
PYTORCH_CUDA_ALLOC_CONF=backend:cudaMallocAsync,pinned_use_cuda_host_register:True,pinned_num_register_threads:8

# Parse short options
OPTIND=1
while getopts "hn:m:rw" opt
do
  case "$opt" in
    'h') print_usage; exit 0 ;;
    'n') number=${OPTARG} ;;
    'm') model=${OPTARG} ;;
    'r') rest=true ;;
    'w') ws=true ;;
    '?') print_usage >&2; exit 1 ;;
  esac
done
shift $(expr $OPTIND - 1) # remove options from positional parameters
echo "number+1=$((number+1)), rest=$rest, ws=$ws, args=$@"
( 
  export PYTORCH_CUDA_ALLOC_CONF
  # Find the script path
  DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
  source "${DIR}/try_getopts_subshell.sh"
)

# if model is "336M", print 336 million; if model is 175b, print 175 billion; else print the model
case $model in
  "336M") echo "336 million" ;;
  "175b") echo "175 billion" ;;
  *) echo $model ;;
esac