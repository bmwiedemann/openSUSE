#
# spec file for package SpeedTest++
#
# Copyright (c) 2022 SUSE LLC
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


Name:           SpeedTest++
Version:        1.11+git20210829.0f63cfb
Release:        0
Summary:        Yet another unofficial speedtest.net client cli interface
License:        MIT
URL:            https://github.com/taganaka/SpeedTest
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Yet another unofficial speedtest.net client cli interface.

It supports the new (undocumented) raw TCP protocol for better accuracy.

%prep
%autosetup -p1
#rename executable to match project name
sed -e '/add_executable/s/SpeedTest/%{name}/' \
    -e '/target_link_libraries/s/SpeedTest/%{name}/' \
    -e '/install/s/SpeedTest/%{name}/' \
    -i CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/%{name}

%changelog
