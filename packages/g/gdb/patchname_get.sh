#!/bin/bash



: ${QUILT_DIR=/usr/share/quilt}


if ! [ -r $QUILT_DIR/scripts/patchfns ]
then
        echo "Cannot read library $QUILT_DIR/scripts/patchfns" >&2
        exit 1
fi
. $QUILT_DIR/scripts/patchfns
cd ${SUBDIR:-.}

usage() {
        echo "Usage: ${0##*/} [--fuzz=N] specfile"
        exit 1
}

options=$(getopt -o v --long sourcedir:,fuzz: -n "${0##*/}" -- "$@") || exit

eval set -- "$options"

sourcedir=

while true
do
        case "$1" in
        -v)
		verbose=1
                shift ;;
        --sourcedir)
                sourcedir=${2%/}/
                shift 2 ;;
        --fuzz)
                # Only works with rpm 4.6 and later
                DEFINE_FUZZ="%define _default_patch_fuzz $2"
                shift 2 ;;
        --)
                shift
                break ;;
        esac
done

[ "${sourcedir:0:1}" = / ] || sourcedir=$PWD/$sourcedir

specfile=$1
if [ $# -ne 1 -o ! -f "$specfile" ]
then

        usage
fi
if [ "${specfile:0:1}"  = / ]
then
        specdir=$(dirname "$specfile")
        specfile=${specfile##*/}
else
        specdir=$PWD
fi

tmpdir="$(gen_tempfile -d ${VARTMPDIR:-/var/tmp}/${0##*/})"
mkdir -p $tmpdir || exit 1
add_exit_handler "rm -rf $tmpdir"
mkdir -p $tmpdir/build
mkdir -p $tmpdir/bin

# Older versions of Suse packages have a symbolic release number, and rpmbuild
# won't like that, so change it to something compliant.
if grep -q '^Release:.*[<>]' "$specdir/$specfile"
then
        sed -e '/^Release:/s/[<>]//g' < "$specdir/$specfile" > $tmpdir/"$specfile"  
        specdir=$tmpdir
fi

# Redirect file descriptors
# 5 is used in verbose mode, 4 in non-verbose mode, and 2 for both (real errors)
if [ -n "$verbose" ]
then
        exec 3>&1 5>&2 4>/dev/null
else
        exec 3>&1 4>&2 5>/dev/null
fi



# wrapper script for patch and tar
cat <<-'EOF' > $tmpdir/bin/wrapper
        #! /bin/bash

	# find original data file by md5sum
	original_file() {
	        local file=$1 md5sum

	        set -- $(md5sum < $file)
	        md5sum=$1
	        while read md5sum_ file_
	        do
	                if [ "$md5sum" = "$md5sum_" ]
	                then
	                        echo ${file_#\*}
	                	return 0
	        	fi
	        done < $tmpdir/md5sums
	
	        # Try harder
	        if ! [ -e $tmpdir/more-md5sums ]
		then
	                ( cd $RPM_BUILD_DIR
	                find . -type f \
	                | sed -e 's:^.\/::' \
	                | xargs md5sum \
	        	) > $tmpdir/more-md5sums
	        fi
	                
	        while read md5sum_ file_
		do
		        if [ "$md5sum" = "$md5sum_" ]
		        then
		                echo ${file_#\*}
		        	return 0
	        	fi
	        done < $tmpdir/more-md5sums
		return 1
	}





	# Extract a command line option with or without argument
	cmdline_option() {
		local letter=$1 no_arg=$2
	        shift
	
	        while [ $# -ne 0 ]
	        do
		        if [ "${1:0:2}" = -$letter ]
	                then
	        	        if [ -z "$no_arg" ]
	                        then
	                	        [ "$1" = -$letter ] && set -- "$1$2"
	                        fi
	                        echo $1
	                        break
	                fi
	                shift
		done
	}
	
	
	strip_option() {
	        set -- $(cmdline_option p "$@")
	        [ "$1" != -p1 ] && echo $1
	}

        # Extract the -p option from the command line
        strip_option() {
                set -- $(cmdline_option p "$@")
                [ "$1" != -p1 ] && echo $1
        }
	
	# Extract the -R option from the command line
	reverse_option() {
	        set -- $(cmdline_option R no_arg "$@")
	        echo $1
	}
	
	patch_opt_d() {
	        local subdir=$(cmdline_option d "$@")
	        [ -z "$subdir" ] || echo "${subdir:2}"
	}
	
	
	
	patch_input_file() {
	        while [ $# -gt 0 ]; do
	                case "$1" in
	                -i|--input)
	                        if [ $# -ge 2 ]; then
	                                echo "$2"
	                	        return
	                        fi
	                        ;;
	                -i*)
	                        echo "${1#-i}"
	                        return
	                        ;;
	                --input=*)
	                        echo "${1#--input=}"
	                        return
	                	;;
	                esac
	        	shift
	        done
		return 
	}

        tar_input_file() {
                case "$1" in
                *C*f*)
                        echo "$3"
                        ;;
                *f*)
                        echo "$2"
                        ;;
                esac
        }


        tar_opt_C() {
                case "$1" in
                *C*f*)
                        echo "$2"
                        return ;;
                esac
        }
	
	tmpdir=${RPM_BUILD_DIR%/*}
	rm -f $tmpdir/data
        case "${0##*/}" in
        patch)
                inputfile=$(patch_input_file "$@")
                ;;
        tar)
                inputfile=$(tar_input_file "$@")
                # For tar, file - means read from stdin
                [ "$inputfile" = "-" ] && inputfile=
                ;;
        esac
        if [ -z "$inputfile" ]; then
            # put data from stdin into tmpfile
            cat > $tmpdir/data
        fi
	
	unpackfile="$(original_file ${inputfile:-$tmpdir/data})"
	if [ -n "$unpackfile" ]
	then
                case "${0##*/}" in
                patch)	
			echo -n p >&4
			subdir=$(patch_opt_d "$@")
			if [ -n "$subdir" ]
			then
				dir=$(cd "$subdir" && echo $PWD)
			else
			        dir=$PWD
			fi
			dir=${dir/$RPM_BUILD_DIR}
			dir=${dir##/}
			dir=${dir// /\\ }
			echo "${0##*/} ${dir:-.} $unpackfile" \
			$(strip_option "$@") $(reverse_option "$@") >&3
		;;
                tar)
                        echo -n t >&4
                        subdir=$(tar_opt_C "$@")
                        if [ -n "$subdir" ]
                        then
                                dir=$(cd "$subdir" && echo $PWD)
                        else
                                dir=$PWD
                        fi
                        dir=${dir/$RPM_BUILD_DIR}
                        dir=${dir##/}
                        dir=${dir// /\\ }
                        echo "${0##*/} ${dir:-.} $unpackfile" >&3
                        ;;
                esac
	fi
	
	PATH=${PATH#*:}
	if [ -n "$inputfile" ]; then
	        ${0##*/} "$@"
	else
	        ${0##*/} "$@" < $tmpdir/data
	fi            
	
EOF
	
chmod 755 $tmpdir/bin/wrapper
# If $TMPDIR is mounted with noexec, rpmbuild won't be able to execute
# our wrapper script
if [ ! -x $tmpdir/bin/wrapper ]
then
        printf "Cannot execute %s; filesystem mounted with noexec?\n" \
               $tmpdir/bin/wrapper >&2
        printf "Setting %s in ~/.quiltrc may help\n" "VARTMPDIR" >&2
        exit 1
fi

ln -s wrapper $tmpdir/bin/patch
ln -s wrapper $tmpdir/bin/tar

# let rpm do all the dirty specfile stuff ...
echo -n "### rpmbuild: " >&4

export PATH="$tmpdir/bin:$PATH"
rpmbuild --eval "%define _sourcedir $sourcedir" \
         --eval "%define _specdir   $specdir" \
         --eval "%define _builddir  $tmpdir/build" \
         --eval "%define __patch    $tmpdir/bin/patch" \
         --eval "%define __tar      $tmpdir/bin/tar" \
         --eval "$DEFINE_FUZZ" \
         --nodeps \
         -bp "$specdir/$specfile" < /dev/null >&5 2>&5
status=$?
echo >&4
exit $status
### Local Variables:
### mode: shell-script
### End:
# vim:filetype=sh

