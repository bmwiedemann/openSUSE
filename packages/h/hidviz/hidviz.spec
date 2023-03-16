#
# spec file for package hidviz
#
# Copyright (c) 2023 SUSE LLC
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


Name:           hidviz
Version:        0.2
Release:        0
Summary:        A tool for in-depth analysis of USB HID devices communication
License:        GPL-3.0-or-later
URL:            https://hidviz.org/
Source0:        https://github.com/hidviz/hidviz/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE hidviz-libexec_path.patch
Patch0:         hidviz-libexec_path.patch
BuildRequires:  ImageMagick
BuildRequires:  asio-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(protobuf)

%description
Hidviz is a GUI application for in-depth analysis of USB HID class devices.
The 2 main usecases of this application are reverse-engineering existing
devices and developing new USB HID devices.

%prep
%autosetup -p1
sed -i 's|__LIBEXECDIR__|%{_libexecdir}|' libhidx/libhidx/src/Connector.cc

%build
%cmake \
    -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
    -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libexecdir}/libhidx_server_daemon

%changelog
