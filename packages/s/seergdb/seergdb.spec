#
# spec file for package seergdb
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global optflags %{?optflags} -fpie
%global build_ldflags %{?build_ldflags} -pie

%if 0%{?suse_version} && 0%{?suse_version} < 1550
%global force_gcc_version 12
%endif

Name:           seergdb
Version:        2.6
Release:        0
Summary:        A GUI front-end for GNU gdb
License:        GPL-3.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://github.com/epasveer/seer
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/seergdb-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-charts-devel
BuildRequires:  qt6-svg-devel
Requires:       gdb
Recommends:     libQt6Svg6

%description
A GUI front-end for GNU gdb written in modern C++.

%prep
%setup -q -n seer-%{version}

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
cd src
%cmake
%cmake_build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 src/build/%{name} %{buildroot}/%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 src/resources/%{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -m 0644 src/resources/%{name}_32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -m 0644 src/resources/%{name}_64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 0644 src/resources/%{name}_128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 0644 src/resources/%{name}_256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -m 0644 src/resources/%{name}_512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor

%changelog
