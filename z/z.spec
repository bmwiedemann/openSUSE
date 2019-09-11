#
# spec file for package z
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           z
Version:        2.7.1
Release:        0
Summary:        Frontend for compressing and uncompressing
License:        GPL-2.0
Group:          Productivity/Archiving/Compression
URL:            http://www.cs.indiana.edu/~kinzler/z/
Source:         http://www.cs.indiana.edu/~kinzler/z/z-%{version}.tgz
BuildArch:      noarch

%description
Z is a frontend for the compress/uncompress, gzip, bzip2, tar, and zip/unzip
utilities to compress and uncompress files and directories.

%prep
%setup -q

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
%doc README COPYING
%{_bindir}/z
%{_mandir}/man1/z.1%{?ext_man}

%changelog
