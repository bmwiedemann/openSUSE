#
# spec file for package procmail
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           procmail
Version:        3.24
Release:        0
Summary:        A program for local e-mail delivery
License:        Artistic-1.0 OR GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://github.com/BuGlessRB/procmail/
Source0:        https://github.com/BuGlessRB/procmail/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        procmail-%{version}-patches.tar.bz2
Patch0:         procmail-3.22-mailstat.patch
Patch1:         procmail-3.22.dif
Patch2:         procmail-cflags.dif
Patch3:         procmail-3.22-headerconcat.dif
Patch4:         procmail-3.22-owl-truncate.dif
Patch5:         procmail-3.22-autoconf.dif
Patch6:         procmail-3.22-ipv6.patch
# PATCH-FIX-SUSE Avoid that link() follows symbolic links
Patch7:         procmail-o_nofollow.patch
# PATCH-FIX-SUSE bmwiedemann -- make build reproducible
Patch8:         reproducible.patch
Patch10:        procmail-fix-Werror=return-type.patch
Patch11:        reproducible2.patch
BuildRequires:  pcre-devel
BuildRequires:  postfix
Requires:       /bin/sed
Recommends:     %{_bindir}/mimencode

%description
Sendmail calls procmail to deliver email into a local folder. Procmail
can be configured to store e-mail in different folders.

%prep
%setup -q -b1
for p in ../procmail-%{version}-patches/* ; do
    test -e $p || break
    echo Patch $p
    patch -s -p1 --fuzz=0 < $p
done
%patch -P 0
%patch -P 1
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5
%patch -P 6
%patch -P 7 -b .nofollow
%patch -P 8 -p1
%patch -P 10 -p1
%patch -P 11 -p1
sed -ri '\@^/\*@,\@\*/@{ s@^(/\*[^*]*)(/\*)@\1\*/ \2@; }' config.h
sed -ri '\@^/\*@,\@\*/@{ s@^(/\*[^*]*)(/\*)@\1\*/ \2@; }' src/includes.h
sed -ri '\@^#.*[[:blank:]]+/\*[^/]*$@M,\@\*/$@{ s@(^[[:blank:]]+)/\*@\1  @;}' src/includes.h

%build
%define _lto_cflags %{nil}
    cflags ()
    {
	local flag=$1; shift
	local var=$1; shift
	local gold
	test -n "${flag}" -a -n "${var}" || return
	case "${!var}" in
	*${flag}*) return
	esac
	if type ld.gold > /dev/null 2>&1 ; then
	    gold=-Wl,-fuse-ld=gold
	fi
	case "$flag" in
	-Wl,*)
	    set -o noclobber
	    if echo 'int main () { return 0; }' | \
		${CC:-gcc} %{optflags} -Werror $gold $flag -o /dev/null -xc - > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	    set +o noclobber
	    rm -f ldtest.c
	    ;;
	*)
	    if ${CC:-gcc} -Werror $gold $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	    if ${CXX:-g++} -Werror $gold $flag -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	esac
    }
    RPM_OPT_FLAGS="%{optflags}"
    XCFLAGS="$(getconf LFS_CFLAGS)"
    cflags -fPIE                    RPM_OPT_FLAGS
    cflags -std=c89                 RPM_OPT_FLAGS
    cflags -Wno-parentheses         RPM_OPT_FLAGS
    cflags -Wno-sign-compare        RPM_OPT_FLAGS
    cflags -Wno-unprototyped-calls  RPM_OPT_FLAGS
    cflags -pipe                    RPM_OPT_FLAGS
    cflags -fno-strict-aliasing     XCFLAGS
    cflags -Wl,-O2                  LDFLAGS0
    cflags -Wl,--hash-size=8599     LDFLAGS0
    cflags -pie                     LDFLAGS0
    export RPM_OPT_FLAGS XCFLAGS LDFLAGS0
    %make_build XCFLAGS="${XCFLAGS}" MANDIR=%{_mandir} LDFLAGS0="${LDFLAGS0}"

%install
    mkdir -p %{buildroot}%{_mandir}/man{1,5} %{buildroot}%{_bindir}
    make MANDIR=%{buildroot}%{_mandir} BINDIR=%{buildroot}%{_bindir} install
    install -m 644 man/mailstat.man %{buildroot}%{_mandir}/man1/mailstat.1

%files
%license COPYING
%doc Artistic
%doc FAQ FEATURES README examples
%{_bindir}/formail
%{_bindir}/lockfile
%{_bindir}/mailstat
%{_bindir}/procmail
%{_mandir}/man1/formail.1%{?ext_man}
%{_mandir}/man1/lockfile.1%{?ext_man}
%{_mandir}/man1/procmail.1%{?ext_man}
%{_mandir}/man1/mailstat.1%{?ext_man}
%{_mandir}/man5/procmailex.5%{?ext_man}
%{_mandir}/man5/procmailrc.5%{?ext_man}
%{_mandir}/man5/procmailsc.5%{?ext_man}

%changelog
