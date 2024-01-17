#
# spec file for package rang
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


Name:           rang
Version:        3.2
Release:        0
Summary:        A C++ library for color emission in the terminal
# The Unlicense, see LICENSE file
License:        SUSE-Public-Domain
URL:            https://agauniyal.github.io/rang
Source0:        https://github.com/agauniyal/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
A minimal, header only C++ library for emitting colors in the terminal.

%package devel
Summary:        A C++ library for color emission in the terminal

%description devel
A minimal, header only C++ library for emitting colors in the terminal.

%prep
%autosetup -p1

%build
# no build required

%install
install -D -m0644 include/rang.hpp %{buildroot}%{_includedir}/rang.hpp
# creates support file for pkg-config
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name:           %{name}
Description: A C++ library for color emission in the terminal
Version:        %{version}
Cflags: -I${includedir}
EOF

%files devel
%doc README.md
%license LICENSE
%{_includedir}/rang.hpp
%{_libdir}/pkgconfig/%{name}.pc

%changelog
