#
# spec file for package z
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2009 - 2014 Pascal Bleser pascal.bleser@opensuse.org
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


Name:           z
Version:        2.7.3
Release:        0
Summary:        Frontend for compressing and uncompressing
License:        GPL-2.0-only
Group:          Productivity/Archiving/Compression
URL:            https://www.cs.indiana.edu/~kinzler/z/
Source:         http://www.cs.indiana.edu/~kinzler/z/z-%{version}.tgz
BuildArch:      noarch

%description
Z is a frontend for the compress/uncompress, gzip, bzip2, tar, and zip/unzip
utilities to compress and uncompress files and directories.

%prep
%autosetup

%build

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
make \
	 BINDIR="%{buildroot}%{_bindir}" \
	 MANDIR="%{buildroot}%{_mandir}/man1" \
	 install \
	 install.man

%files
%license COPYING
%doc README
%{_bindir}/z
%{_mandir}/man1/z.1%{?ext_man}

%changelog
