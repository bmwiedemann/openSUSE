fudo() {
	[ "$#" -gt 0 -a "${1:0:1}" != '-' ] || { echo "Usage: ${FUNCNAME[0]} COMMAND [ARGS...]"; return 1; }
	set -- "$(type -P "$1")" "${@:2}"
	[ -n "$1" ] || { echo "invalid command" >&2; return 1; }
	machinectl shell -q .host "$@"
}
# take over sudo if the real one is not installed
type -P sudo >/dev/null || alias sudo=fudo
