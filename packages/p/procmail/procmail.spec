#
# spec file for package procmail
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.22
Release:        0
Summary:        A program for local e-mail delivery
License:        Artistic-1.0 OR GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            http://www.procmail.org/
Source0:        ftp://ftp.informatik.rwth-aachen.de/pub/packages/procmail/procmail-%{version}.tar.gz
Source1:        procmail-%{version}-patches.tar.bz2
Patch0:         procmail-%{version}-mailstat.patch
Patch1:         procmail-%{version}.dif
Patch2:         procmail-cflags.dif
Patch3:         procmail-%{version}-headerconcat.dif
Patch4:         procmail-%{version}-owl-truncate.dif
Patch5:         procmail-%{version}-autoconf.dif
Patch6:         procmail-%{version}-ipv6.patch
# PATCH-FIX-SUSE bmwiedemann -- make build reproducible
Patch8:         reproducible.patch
Patch10:        procmail-fix-Werror=return-type.patch
BuildRequires:  pcre-devel
BuildRequires:  postfix
Requires:       /bin/sed
Recommends:     /usr/bin/mimencode
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p1
%patch8 -p1
%patch10 -p1
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
	set -o noclobber
	case "$flag" in
	-Wl,*)
	    if echo 'int main () { return 0; }' | \
		${CC:-gcc} $RPM_OPT_FLAGS -Werror $gold $flag -o /dev/null -xc - > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
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
	set +o noclobber
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
    make %{?_smp_mflags} XCFLAGS="${XCFLAGS}" MANDIR=%{_mandir} LDFLAGS0="${LDFLAGS0}"

%install
    mkdir -p %{buildroot}%{_mandir}/man{1,5} %{buildroot}%{_prefix}/bin
    make MANDIR=%{buildroot}%{_mandir} BINDIR=%{buildroot}%{_bindir} install
    install -m 644 man/mailstat.man %{buildroot}%{_mandir}/man1/mailstat.1

%files
%defattr(-,root,root)
%doc Artistic COPYING
%doc FAQ FEATURES README examples
%{_bindir}/formail
%{_bindir}/lockfile
%{_bindir}/mailstat
%{_bindir}/procmail
%{_mandir}/man1/formail.1.gz
%{_mandir}/man1/lockfile.1.gz
%{_mandir}/man1/procmail.1.gz
%{_mandir}/man1/mailstat.1.gz
%{_mandir}/man5/procmailex.5.gz
%{_mandir}/man5/procmailrc.5.gz
%{_mandir}/man5/procmailsc.5.gz

%changelog
