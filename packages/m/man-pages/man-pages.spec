#
# spec file for package man-pages
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


Name:           man-pages
Version:        6.14
Release:        0
Summary:        Linux Manual Pages
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Documentation/Man
URL:            https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/
#Git-Clone:	git://git.kernel.org/pub/scm/docs/man-pages/man-pages
#Git-Web:	http://git.kernel.org/cgit/docs/man-pages/man-pages.git/
Source0:        https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz
Source1:        https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.sign
# https://lore.kernel.org/all/1257e092-79af-3624-2f6a-fb5fd69e5c18@gmail.com/#t
Source2:        %{name}.keyring
Patch0:         %{name}.eal3.diff
Patch1:         %{name}_gai.conf-reference.patch
# [bsc#1154701]
Patch2:         man-pages-tcp_fack.patch
BuildRequires:  fdupes
Supplements:    (man and patterns-base-documentation)
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
%autosetup -p1

%build
# glibc
rm man3/{getifaddrs.3,freeifaddrs.3,crypt.3,crypt_r.3}
# remove .so link to bzero.3, conflicts with libbsd
rm man3/explicit_bzero.3
# bsc#1188724
rm man5/motd.5
# conflicts with mandoc; man.7 is not so link on groff_man.7,
# which is part of groff-full
rm man7/man.7

%install
for i in man[0-9]*; do
  mkdir -p "%{buildroot}/%{_mandir}/$i"
  cp -p "$i"/* "%{buildroot}/%{_mandir}/$i/"
done
cd "%{buildroot}/%{_mandir}/"
RETVAL=0
ARE_MISSING=""
for i in */* ; do
    so_ref="$(grep '^.so man' $i | awk '{print $2}')"
    if [ -n $so_ref ] ; then
      if [ ! -f $so_ref ]; then
	ARE_MISSING="$i $ARE_MISSING ($so_ref missing)"
        RETVAL=1
      fi
    fi
done
echo ""
echo "The following manual pages have wrong .so reference:"
echo "$ARE_MISSING"
echo ""
if [ "$RETVAL" -ne 0 ] ; then
  exit "$RETVAL"
fi

# Remove duplicates
%fdupes -s %{buildroot}/%{_prefix}

%files
%defattr(644,root,root,755)
%doc README Changes Changes.old CONTRIBUTING lsm
%license LICENSES/*.txt
%dir %{_mandir}/man2type
%dir %{_mandir}/man3const
%dir %{_mandir}/man3head
%dir %{_mandir}/man3type
%dir %{_mandir}/man2const
%{_mandir}/man*/*.gz

%changelog
