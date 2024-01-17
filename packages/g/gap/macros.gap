#
# In noarch package, we can just move all the data - this is cheap.
# For arch-dependent packages however, the source needs to reside at
# its original position for debuginfo to be properly generated, and
# thus we do a cp there instead.
# The macro sets $gapmoddir.
#
%gappkg_simple_install() \
	set -x; \
	moddir="$(readlink -f .)"; \
	if [ "%_target_cpu" = "noarch" ]; then \
		moddir="%gap_sitelib/${moddir##*/}"; \
		stopdir="%gap_sitelib_anchor"; \
		mkdir -pv "%buildroot/$moddir"; \
		mv -v * "%buildroot/$moddir/"; \
	else \
		moddir="%gap_sitearch/${moddir##*/}"; \
		stopdir="%gap_sitearch_anchor"; \
		mkdir -pv "%buildroot/$moddir"; \
		cp -av * "%buildroot/$moddir/"; \
	fi; \
	\
	fmoddir="${moddir#/}"; \
	( \
		echo "$moddir"; \
		cd "%buildroot"; \
		find "$fmoddir" -type f "(" -iname "LICENCE*" -o -iname "LICENSE*" -o -iname "COPYING*" -o -iname "GPL*" ")" -printf "%%%%license /%%p\\n"; \
	) >>"%name.files"; \
	d="${moddir%/*}"; \
	while [ -n "$d" ] && [ "$d" != "/" ] && [ "$d" != "$stopdir" ]; do \
		echo "%%dir $d" >>"%name.files"; \
		d="${d%/*}"; \
	done; \
	unset d; \
	unset stopdir;
