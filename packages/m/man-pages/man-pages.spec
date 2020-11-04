#
# spec file for package man-pages
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


Name:           man-pages
Version:        5.08
Release:        0
Summary:        Linux  Manual Pages
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Documentation/Man
URL:            https://www.kernel.org/doc/man-pages/download.html
#Git-Clone:	git://git.kernel.org/pub/scm/docs/man-pages/man-pages
#Git-Web:	http://git.kernel.org/cgit/docs/man-pages/man-pages.git/
Source:         https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/snapshot/man-pages-%{version}.tar.gz
Patch0:         %{name}.eal3.diff
Patch3:         %{name}_gai.conf-reference.patch
Patch5:         %{name}-tty_ioctl.patch
# [bsc#1154701]
Patch6:         man-pages-tcp_fack.patch
# [bsc#1173382]
Patch7:         man-pages-openat2.h-location.patch
BuildRequires:  fdupes
Supplements:    packageand(man:patterns-base-documentation)
BuildArch:      noarch

%description
A large collection of man pages (documentation) from the Linux
Documentation Project (LDP).  The man pages are organized into the
following sections: Section 1, user commands (intro only); Section 2,
system calls; Section 3, libc calls; Section 4, devices (e.g., hd, sd);
Section 5, file formats and protocols (e.g., wtmp, %{_sysconfdir}/passwd, nfs);
Section 6, games (intro only); Section 7, conventions, macro packages,
etc. (e.g., nroff, ascii); and Section 8, system administration (intro
only).

%prep
%setup -q
%patch0 -p2
%patch3
%patch5 -p1
%patch6 -p1
%patch7 -p1
find -name "*.orig" | xargs rm -fv

%build
# glibc
rm man3/{getifaddrs.3,freeifaddrs.3,crypt.3,crypt_r.3}
# remove .so link to bzero.3, conflicts with libbsd
rm man3/explicit_bzero.3
# already in bpftool package
rm man7/bpf-helpers.7
# conflicts with mandoc
mkdir man7mp
mv man7/man.7 man7mp/man.7mp

%install
for i in man[0-9]*; do
  mkdir -p "%{buildroot}/%{_mandir}/$i"
  cp -p "$i"/* "%{buildroot}/%{_mandir}/$i/"
done
cd "%{buildroot}/%{_mandir}/"
RETVAL=0
ARE_MISSING=""
for i in */* ; do
    FOUND=0
    grep "^.so man" "$i" && FOUND=1
    if [ "$FOUND" == 1 ] ; then
      if [ ! -f `grep "^.so man" "$i" | awk '{print $2}'` ]; then
	ARE_MISSING="$i $ARE_MISSING"
        RETVAL=1
      fi
    fi
done
echo ""
echo "The following manual pages are now missing (for .so reference):"
echo "$ARE_MISSING"
echo ""
if [ "$RETVAL" -ne 0 ] ; then
  exit "$RETVAL"
fi

# Remove duplicates
%fdupes -s %{buildroot}/%{_prefix}

%files
%defattr(644,root,root,755)
%dir %{_mandir}/man7mp
%{_mandir}/man*/*.gz
%doc README Changes Changes.old
%doc man-pages-*.Announce
%doc man-pages-*.lsm
%doc Changes

%changelog
