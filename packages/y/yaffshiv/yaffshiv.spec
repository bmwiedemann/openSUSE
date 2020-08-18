#
# spec file for package yaffshiv
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           yaffshiv
Version:        0.1+git.20160105
Release:        0
Summary:        A YAFFS file system parser and extractor
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/devttys0/yaffshiv
Source:         %{name}-%{version}.tar.xz
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
A YAFFS file system parser and extractor writte in pure python.

Features:
 - List and/or extract regular files, folders, symlinks, hard
   links, and special device files
 - Automatic detection and/or brute force of YAFFS build parameters
   (page size, spare size, endianess, etc)
 - Support for both big and little endian YAFFS file systems

%prep
%setup -q
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' src/yaffshiv

%build
%python3_build

%install
%python3_install
help2man -h --help %{buildroot}/%{_bindir}/yaffshiv --no-discard-stderr --version-string="%{version}" --no-info | grep -v "not recog" > yaffshiv.1
install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/yaffshiv
%{_mandir}/man1/yaffshiv.1%{?ext_man}
%{python3_sitelib}/yaffshiv*

%changelog
