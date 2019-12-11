#
# spec file for package man-pages
#
# Copyright (c) 2019 SUSE LLC
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
Version:        5.04
Release:        0
Summary:        Linux  Manual Pages
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Documentation/Man
URL:            https://www.kernel.org/doc/man-pages/download.html
#Git-Clone:	git://git.kernel.org/pub/scm/docs/man-pages/man-pages
#Git-Web:	http://git.kernel.org/cgit/docs/man-pages/man-pages.git/
Source:         https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/snapshot/man-pages-%{version}.tar.gz
Patch0:         %{name}.eal3.diff
Patch1:         %{name}-remove-ioctl_list-reference.patch
Patch3:         %{name}_gai.conf-reference.patch
Patch5:         %{name}-tty_ioctl.patch
# [bsc#1154701]
Patch6:         man-pages-tcp_fack.patch
BuildRequires:  fdupes
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(postun): update-alternatives
Supplements:    man
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
%patch1 -p1
%patch3
%patch5 -p1
%patch6 -p1
find -name "*.orig" | xargs rm -fv

%build
# not current anymore (list of ioctl calls in Linux/i386 kernel 1.3.27)
# remove-ioctl_list-reference.patch removes references from ioctl.2
rm man2/ioctl_list.2
# glibc
rm man3/{getifaddrs.3,freeifaddrs.3,crypt.3,crypt_r.3}
# remove .so link to bzero.3, conflicts with libbsd
rm man3/explicit_bzero.3

%install
for i in man? ; do
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

# Prepare alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
from=$(readlink -f %{buildroot}%{_mandir}/man7/man.7*)
to=$(echo $from|sed -e 's!\.7$!!')-mp.7
mv -v "$from" "$to"
ln -s -f %{_sysconfdir}/alternatives/man.7 "$from"

# Remove duplicates
%fdupes -s %{buildroot}/%{_prefix}

%post
update-alternatives --install \
   %{_mandir}/man7/man.7%{?ext_man} man.7%{?ext_man} \
   %{_mandir}/man7/man-mp.7%{?ext_man} 500

%preun
if [ $1 -eq 0 ] ; then
   update-alternatives --remove man.7%{?ext_man} %{_mandir}/man7/man-mp.7%{?ext_man}
fi

%files
%defattr(644,root,root,755)
%{_mandir}/man*/*.gz
%ghost %{_sysconfdir}/alternatives/man.7%{?ext_man}
%doc README Changes Changes.old
%doc man-pages-*.Announce
%doc man-pages-*.lsm
%doc Changes

%changelog
