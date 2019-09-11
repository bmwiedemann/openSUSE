#!/usr/bin/sed -nf

/^\s*cache_dir\s\+[[:alnum:]]\+\s\+\([[:graph:]\/]\+\)\s.*/ {
    s//\1\/00/p
    q
}

