DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

source "${DIR}/echo_var_func.sh"

echo_dimx
declare -a DimsX=( "--ab" "" )
echo_dimx