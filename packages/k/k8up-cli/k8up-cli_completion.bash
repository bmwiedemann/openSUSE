_k8up_complete() {
    local cur
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "$(k8up --generate-bash-completion)" -- "${cur}") )
    return 0
}
complete -F _k8up_complete k8up
