#
# spec file for package pnm2ppa
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Bernhard M. Wiedemann
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


Name:           pnm2ppa
Version:        1.13
Release:        0
Summary:        HP PPA GhostScript filter
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://sourceforge.net/projects/pnm2ppa/
Source0:        https://sourceforge.net/projects/pnm2ppa/files/pnm2ppa/%{version}/%{name}-%{version}.tar.gz

%description
pnm2ppa is a Ghostscript print filter which allows owners of HP DeskJet
710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, or 1000Cxi printers to
print PostScript Level 2.

%prep
%autosetup
chmod a-x docs/en/LICENSE
sed -i -e 's/\r//' docs/en/LICENSE

%build
export CFLAGS="%{optflags} -fcommon"
%configure
%make_build

%install
rm -f docs/en/INSTALL*
%make_install

%files
%license docs/en/LICENSE
%doc docs/en
%config(noreplace) %{_sysconfdir}/pnm2ppa.conf
%{_bindir}/*ppa
%{_mandir}/man1/pnm2ppa.1%{?ext_man}

%changelog
