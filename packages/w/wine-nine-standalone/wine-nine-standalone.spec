#
# spec file for package wine-nine-standalone
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


Name:           wine-nine-standalone
Version:        0.7
Release:        0
Summary:        Wine Gallium Nine Standalone version
License:        LGPL-2.1-or-later
Group:          System/Emulators/PC
URL:            https://github.com/iXit/wine-nine-standalone
Source0:        https://github.com/iXit/wine-nine-standalone/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  Mesa-libd3d-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  meson
BuildRequires:  wine
BuildRequires:  wine-devel
Obsoletes:      wine-nine < 4.2
ExclusiveArch:  %{ix86} x86_64

%description
Gallium Nine allows to run any Direct3D 9 application with nearly no CPU
overhead, which provides a smoother gaming experience and increased FPS.

Gallium Nine Standalone, as the name implies, is a standalone version of the WINE parts of Gallium Nine.

This decouples Gallium Nine from the WINE tree, so that it can be used
with any WINE version. There is no need for any WINE patches. A stable,
development, or staging WINE release is sufficient.

Gallium Nine Standalone consists of two parts:

* d3d9-nine.dll: Gallium Nine Direct3D 9 library
* ninewinecfg.exe: GUI to enable/disable Gallium Nine with some additional info about the current state

%prep
%setup -q

%build

sed "s/@PKG_CONFIG@/pkg-config/" \
        < tools/cross-wine32.in \
        > tools/cross-wine32

sed "s/@PKG_CONFIG@/pkg-config/" \
        < tools/cross-wine64.in \
        > tools/cross-wine64

CROSS=tools/cross-wine64
[ %{_lib} == "lib" ] && CROSS=tools/cross-wine32

%meson --cross-file $CROSS --bindir=%{_libdir}/wine --libdir=%{_libdir}/wine || cat /home/abuild/rpmbuild/BUILD/wine-nine-standalone-0.4/build/meson-logs/meson-log.txt
%meson_build

%install
%meson_install

mkdir %{buildroot}/%{_libdir}/wine/fakedlls
mv %{buildroot}/%{_libdir}/wine/d3d9-nine.dll.fake %{buildroot}/%{_libdir}/wine/fakedlls/d3d9-nine.dll
mv %{buildroot}/%{_libdir}/wine/ninewinecfg.exe.fake %{buildroot}/%{_libdir}/wine/fakedlls/ninewinecfg.exe

%files
%license LICENSE
%doc README.rst
%dir %{_libdir}/wine
%{_libdir}/wine/*.so
%dir %{_libdir}/wine/fakedlls
%{_libdir}/wine/fakedlls/*

%changelog
