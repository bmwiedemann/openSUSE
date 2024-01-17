# https://gist.github.com/unhammer/2c60a9089ec9cc1c6e7d7660bd7d5734

_xsv()
{
    cur=${COMP_WORDS[COMP_CWORD]}
    prev=${COMP_WORDS[COMP_CWORD-1]}
    cmds=$(xsv --list|awk '/Installed/{next}/./{print $1}')

    while read -r cmd; do
        if [[ "${prev}" = "${cmd}" ]]; then
            case "${cur}" in
                -*)
                    opts=$(xsv "$prev" --help|grep -oe "-[^., ')\`]\+") # hacky, but seems to work well[1]
                    COMPREPLY=( $( compgen -W "${opts}" -- "$cur" ) )
                    return
                    ;;
                *)
                    _filedir
                    return
                    ;;
            esac
        fi
    done <<<"${cmds}"

    case "$cur" in
        -*)
            help_parsed=$( _parse_help "$1" )
            COMPREPLY=( $( compgen -W "${help_parsed}" -- "$cur" ) )
            ;;

        *)
            COMPREPLY=( $( compgen -W "${cmds}" -- "$cur" ) )
            ;;
    esac
} &&
complete -o filenames -o bashdefault -F _xsv xsv


# [1] To see the full list we get with this regex, run:
#     xsv --list|awk '/Installed/{next}/./{print $1}' | while read -r cmd; do
#         echo "$cmd"
#         xsv "$cmd" --help|grep -oe "-[^., ')\`]\+"
#     done
