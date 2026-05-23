#
# spec file for package unshieldv3
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


Name:           unshieldv3
Version:        0.2.2
Release:        0
Summary:        A Program to Extract InstallShield V3 (Z) archives
License:        Apache-2.0
URL:            https://github.com/wfr/unshieldv3
#Git-Clone:     https://github.com/wfr/unshieldv3.git
Source:         https://github.com/wfr/unshieldv3/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A Program to Extract InstallShield V3 (Z) archives.

InstallShield Z format is a compressed archive format used by
version 3 of the InstallShield installation software.

%prep
%autosetup

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/unshieldv3

%changelog
