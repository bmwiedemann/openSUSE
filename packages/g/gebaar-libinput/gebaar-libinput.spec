#
# spec file for package gebaar-libinput
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpptoml 0.1.1
%define cxxopts 2.1.2
Name:           gebaar-libinput
Version:        0.0.5
Release:        0
Summary:        WM Independent Touchpad Gesture Daemon for libinput
License:        GPL-3.0-or-later
Group:          System/Daemons
URL:            https://github.com/Coffee2CodeNL/gebaar-libinput
Source0:        https://github.com/Coffee2CodeNL/gebaar-libinput/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/skystrife/cpptoml/archive/v%{cpptoml}.tar.gz#/cpptoml-%{cpptoml}.tar.gz
Source2:        https://github.com/jarro2783/cxxopts/archive/v%{cxxopts}.tar.gz#/cxxopts-%{cxxopts}.tar.gz
Patch0: 		cmake-version.patch
BuildRequires:  cmake
%if 0%{?suse_version} == 1500
BuildRequires:  gcc8
BuildRequires:  gcc8-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(zlib)

%description
gebaar-libinput is a window manager independent touchpad gesture
daemon for libinput. Unlike other gesture daemons, such as
libinput-gestures and fusuma, which parse the output of libinput
debug-events, gebaar-libinput interfaces with libinput directly.

%prep
%setup -q
%patch0
tar -xzf %{SOURCE1} -C libs/cpptoml --strip-components=1
tar -xzf %{SOURCE2} -C libs/cxxopts --strip-components=1

%build
%if 0%{?suse_version} == 1500
	%cmake -DCMAKE_CXX_COMPILER=/usr/bin/g++-8
%else
	%cmake
%endif
make %{?_smp_mflags}

%install
install -Dm0755 build/gebaard %{buildroot}%{_bindir}/gebaard

%files
%license LICENSE
%doc README.md
%{_bindir}/gebaard

%changelog
