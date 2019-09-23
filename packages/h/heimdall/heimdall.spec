#   
# spec file for package heimdall
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           heimdall
Summary:        Samsung Mobile Device Firmware Flasher
Version:        1.4.2
Release:        0
License:        MIT
Group:          Hardware/Mobile
Url:            https://github.com/Benjamin-Dobell/Heimdall
Source0:        https://github.com/Benjamin-Dobell/Heimdall/archive/v1.4.2.tar.gz
Source1:        heimdall.desktop
Source11:       %{name}_32.png
Source12:       %{name}_48.png
Source99:       %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  cmake > 2.8.11
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  libusb-1_0-devel >= 1.0.14
BuildRequires:  zlib-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

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
Group:          Hardware/Mobile
Requires:       %{name} = %{version}

%description frontend
Heimdall is a tool suite used to flash firmware (aka ROMs) onto
Samsung Galaxy S devices.

This package contains a graphical user interface for Heimdall.

%prep
%setup -q -n Heimdall-1.4.2

%build
%cmake
%make_jobs

%install
install -D -m0755 build/bin/heimdall          %{buildroot}/%{_bindir}/%{name}
install -D -m0755 build/bin/heimdall-frontend %{buildroot}/%{_bindir}/%{name}-frontend
install -D -m0644 heimdall/60-heimdall.rules %{buildroot}/usr/lib/udev/rules.d/60-%{name}.rules
install -D -m0644 %{S:1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m0644 %{S:1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m0644 %{S:11} %{buildroot}/%{_datadir}/pixmaps/%{name}_32.png
install -D -m0644 %{S:12} %{buildroot}/%{_datadir}/pixmaps/%{name}_48.png
%if 0%{?suse_version}
%suse_update_desktop_file -r "%{name}" HardwareSettings Settings
%endif

%files
%defattr(-,root,root)
%doc Linux/README
%{_bindir}/%{name}
/usr/lib/udev

%files frontend
%defattr(-,root,root)
%doc Linux/README
%{_bindir}/%{name}-frontend
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_*.png

%changelog
