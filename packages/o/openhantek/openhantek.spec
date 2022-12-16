#
# spec file for package openhantek
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


Name:           openhantek
Version:        3.3.1
Release:        0
Summary:        Software for Hantek DSO6022 USB digital signal oscilloscopes
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            http://openhantek.org/
Source:         https://github.com/OpenHantek/OpenHantek6022/archive/refs/tags/%{version}.tar.gz#/%name-%version.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libusb-1.0)

%description
OpenHantek6022 is a free software for Hantek DSO6022 USB digital signal
oscilloscopes that is actively developed on
github.com/OpenHantek/OpenHantek6022 - but only for Hantek 6022BE/BL and
compatible scopes (Voltcraft, Darkwire, Protek, Acetech, etc.).

%prep
%autosetup -n OpenHantek6022-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
%suse_update_desktop_file OpenHantek Development Debugger Education Engineering DataVisualization Qt

%files
%license LICENSE
%doc CHANGELOG README README.md
%{_bindir}/OpenHantek
%{_prefix}/lib/udev/rules.d/60-openhantek.rules
%{_datadir}/applications/OpenHantek.desktop
%{_datadir}/doc/%{name}/
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/OpenHantek.png
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/OpenHantek.svg

%changelog
