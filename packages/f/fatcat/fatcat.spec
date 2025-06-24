#
# spec file for package fatcat
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           fatcat
Version:        1.1.1
Release:        0
Summary:        FAT filesystems explore, extract, repair, and forensic tool
License:        MIT
URL:            https://github.com/Gregwar/fatcat
Source:         %{name}-%{version}.tar.xz
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
This tool is designed to manipulate FAT filesystems, in order to explore,
extract, repair, recover and forensic them. It currently supports FAT12, FAT16
and FAT32.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -D -m 0644 man/fatcat.1 %{buildroot}%{_mandir}/man1/fatcat.1

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/fatcat
%{_mandir}/man1/fatcat.1%{?ext_man}

%changelog
