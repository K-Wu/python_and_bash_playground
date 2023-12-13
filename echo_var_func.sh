echo_dimx() {
  DimsX=${DimsX:- 128 32}
  # Get the index to preserve empty string: if we do foreach element, empty string will be skipped
  for dimxIdx in ${!DimsX[@]}; do
    dimx=${DimsX[$dimxIdx]}
    echo $dimx
  done
}