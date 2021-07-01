#
# spec file for package appx-util
#
# Copyright (c) 2021 Neal Gompa <ngompa13@gmail.com>.
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


Name:           appx-util
Version:        0.4
Release:        0
Summary:        Utility to create Microsoft .appx packages

# See LICENSING.md for details
License:        MPL-2.0 and BSD-3-Clause
URL:            https://github.com/OSInside/appx-util
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.11
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# For tests
BuildRequires:  python3

# Replacement fork of fb-util-for-appx
Obsoletes:     fb-util-for-appx < %{version}-%{release}
Provides:      fb-util-for-appx = %{version}-%{release}

%description
appx is a tool which creates and optionally signs
Microsoft Windows APPX packages.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE* LICENSING.md
%doc README.md CONTRIBUTING.md
%{_bindir}/appx


%changelog
