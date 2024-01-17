#!/bin/bash
# Provided an xml files as arguments, generates a desktop file.
# 2008-2012 Tormod Volden
# 2015 Sorokin Alexei

# Poor man's xml parser "can i haz xml purrser".
get_xml_option () {
    file="$1"
    tag="$2"
    option="$3"

    < "$file" sed -n '/\<'$tag' /s@.* '$option'="\([^"]*\)".*@\1@p'
}

get_xml_entity () {
    file="$1"
    tag="$2"

    < "$file" sed -e ':a; /<'$tag'/N;s/\n/ /; ta' |
      sed -ne 's/.*<'$tag'> *\(.*\)<\/'$tag'>.*/\1/p'
}

extract_entries () {
    export XML="$1"

    export XMLNAME="$(get_xml_option "$XML" 'screensaver' 'name')"
    export XMLARG="$(get_xml_option "$XML" 'command' 'arg' | sed -e ':a; N; s/\n/ /; ta')"
    export XMLEXE="$XMLNAME $XMLARG"

    export XMLLABEL="$(get_xml_option "$XML" 'screensaver' '_label')"
    export XMLGL="$(get_xml_option "$XML" 'screensaver' 'gl')"

    # Delete trailing spaces and years.
    export XMLDES="$(get_xml_entity "$XML" '_description' |
      sed -e 's/   */ /g; s/[;,.] [0-9;,. ]*$/./')"

    # Only get first part of first paragraph.
    export SHORTDES="$(echo "$XMLDES" | sed -e 's/[.:!(].*/./')"
}

OPTIND=1
while getopts "hv" opt; do
    case "$opt" in
      h)
        echo -e "Usage:\n  $(basename $0) [-hvV] XML-DIR DESKTOPS-DIR"
        exit 0
      ;;
      v)
        echo "$(basename $0) 0.1"
      ;;
    esac
done
shift $((OPTIND-1))

if [[ "$1" == "--" ]]; then
    shift 1
fi
if [[ -z "$1" ]]; then
    echo "$(basename $0): xscreensaver hack XML files directory is not specified." >&2
    exit 1
fi

if [ -z "$1" ] || [ ! -d "$1" ] || [ ! -r "$1" ]; then
    echo "$(basename $0): \`$1' is not a readable directory." >&2
    exit 1
elif [ -z "$2" ] || [ ! -d "$2" ]; then
    echo "$(basename $0): \`$2' is not a directory." >&2
    exit 1
fi

ls "$1" | grep '\.xml$' | while read file; do
    extract_entries "$1/$file"
    cat > "$2/$(basename "$1/$file" .xml).desktop" <<- EOF
	[Desktop Entry]
	Name=$XMLLABEL
	Comment=$XMLDES
	Exec=$XMLEXE
	TryExec=$XMLNAME
	StartupNotify=false
	Terminal=false
	Type=Application
	Categories=Screensaver;
	OnlyShowIn=MATE;
	EOF
done
