/^[ \t]*[A-Z0-9_]+[ \t]*=/ {
    ident = $0
    sub(/^[[:blank:]]*/, "", ident)
    sub(/[[:blank:]]*=.*/, "", ident)

    val = $0
    sub(/^.*=[[:blank:]]*/, "", val)
    sub(/[[:blank:]]*$/, "", val)
    gsub(/;/, ":", val)

    VAR[ident] = val
}

END {
    for (ident in VAR) {
	val = VAR[ident]
	split(val, pieces, /[:,]/)
	for (one in pieces) {
	    match(pieces[one], /\$\{?([[:upper:]]+)\}?/, arr)
	    if (RSTART == 0)
		continue
	    if (arr[1] ~ /OSFONTDIR/)
		continue
	    if (VAR[arr[1]] ~ /\$/)
		continue
	    gsub(/\$\{?arr[1]\}?/, VAR[arr[1]], val)
	}
	print "#ifndef DEFAULT_" ident
	print "#define DEFAULT_" ident " \"" val "\""
	print "#endif"
	print ""
    }
}
