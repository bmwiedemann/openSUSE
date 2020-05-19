#
# spec file for package demumble
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


Name:           demumble
Version:        1.2.2
Release:        0
Summary:        A better c++filt and a better undname.exe, in one binary
License:        Apache-2.0
URL:            https://github.com/nico/demumble
Source:         https://github.com/nico/demumble/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         pie.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.14.0
BuildRequires:  ninja
BuildRequires:  python3-base

%description
demumble demangles both Itanium and Visual Studio symbols. It runs on both POSIX and Windows.

%prep
%setup -q
%autopatch -p1

%build
%define __builder ninja
%cmake
%cmake_build

%check
cd build
cp ../demumble_test.py .
python3 ./demumble_test.py

%install
install -D -m 0755 build/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
