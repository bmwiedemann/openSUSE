#
# spec file for package hobbits
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2021-2024, Martin Hauke <mardnh@gmx.de>
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


%define pffft_hash d7a4c02
Name:           hobbits
Version:        0.55.0
Release:        0
Summary:        A GUI for bit-based analysis, processing, and visualization
License:        MIT
URL:            https://github.com/Mahlet-Inc/hobbits
Source:         https://github.com/Mahlet-Inc/hobbits/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://bitbucket.org/jpommier/pffft/get/%{pffft_hash}.zip#/pffft-%{pffft_hash}.zip
Patch0:         hobbits-dont-hardcode-python3-version.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpcap-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libusb-1.0)
Provides:       bundled(pffft)

%description
A GUI for bit-based analysis, processing, and visualization.

%package devel
Summary:        Development files for hobbits
Requires:       %{name} = %{version}

%description devel
A GUI for bit-based analysis, processing, and visualization.

This subpackage contains files for developing applications thatwant to make use of hobbits.

%prep
%autosetup -p1

# 3rd party
cd external/pffft/
unzip -j %{SOURCE1}

%build
# bitarray.cpp initialises char[] bit masks with negative literals
# (-128, -65, ...), a narrowing error where char is unsigned (aarch64,
# ppc, s390x, ...); build with signed char to match the code's assumption.
export CXXFLAGS="%{optflags} -fsigned-char"
# Generate a Ninja build (faster for this multi-plugin Qt build)
%define __builder ninja
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/hobbits
%{_bindir}/hobbits-runner
%dir %{_libdir}/hobbits
%dir %{_libdir}/hobbits/plugins
%{_libdir}/hobbits/plugins/analyzers/
%{_libdir}/hobbits/plugins/analyzers/
%{_libdir}/hobbits/plugins/displays/
%{_libdir}/hobbits/plugins/importerexporters/
%{_libdir}/hobbits/plugins/operators/
%{_libdir}/libhobbits-core.so
%{_libdir}/libhobbits-python.so
%{_libdir}/libhobbits-widgets.so
%{_datadir}/applications/Hobbits.desktop
# FIXME: icons too large
%dir %{_datadir}/icons/hicolor/624x624/
%dir %{_datadir}/icons/hicolor/624x624/apps/
%{_datadir}/icons/hicolor/624x624/apps/HobbitsRingSmall.png

%files devel
%{_includedir}/hobbits/

%changelog
