#
# spec file for package heimdall
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2011 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2011 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           heimdall
Version:        2.2.2
Release:        0
Summary:        Samsung Mobile Device Firmware Flasher
License:        MIT
URL:            https://git.sr.ht/~grimler/Heimdall
Source0:        https://git.sr.ht/~grimler/Heimdall/archive/v%{version}.tar.gz
Source1:        heimdall.desktop
Source11:       %{name}_32.png
Source12:       %{name}_48.png
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++
BuildRequires:  libusb-1_0-devel >= 1.0.14
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  qt6-widgets-devel
BuildRequires:  zlib-devel

%description
Heimdall is a tool suite used to flash firmware (aka ROMs) onto
Samsung Mobile devices.

Official supported devices (but not limited to) are:
 * GT-I9000
 * GT-I9100[T]
 * GT-I9300
 * GT-I9505
 * SGH-I727
 * SGH-I777
 * SGH-I927
 * SGH-I797

%package frontend
Summary:        Samsung Galaxy S Device Firmware Flasher
Requires:       %{name} = %{version}

%description frontend
Heimdall is a tool suite used to flash firmware (aka ROMs) onto
Samsung Galaxy S devices.

This package contains a graphical user interface for Heimdall.

%prep
%setup -q -n Heimdall-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
install -D -m0644 heimdall/60-heimdall.rules %{buildroot}%{_udevrulesdir}/60-%{name}.rules
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m0644 %{SOURCE11} %{buildroot}%{_datadir}/pixmaps/%{name}_32.png
install -D -m0644 %{SOURCE12} %{buildroot}%{_datadir}/pixmaps/%{name}_48.png

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_udevrulesdir}/60-%{name}.rules

%files frontend
%license LICENSE
%doc README.md
%{_bindir}/%{name}-frontend
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_*.png

%changelog
