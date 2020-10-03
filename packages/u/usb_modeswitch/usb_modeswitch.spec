#
# spec file for package usb_modeswitch
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


%define source_name usb-modeswitch
%define date	20191128
%define _udevdir %(pkg-config --variable=udevdir udev)
Name:           usb_modeswitch
Version:        2.6.1
Release:        0
Summary:        A mode switching tool for controlling multiple-device USB gear
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://www.draisberghof.de/usb_modeswitch/
Source0:        https://www.draisberghof.de/usb_modeswitch/%{source_name}-%{version}.tar.bz2
Source1:        https://www.draisberghof.de/usb_modeswitch/%{source_name}-data-%{date}.tar.bz2
Source2:        https://www.draisberghof.de/usb_modeswitch/device_reference.txt
Source3:        https://www.draisberghof.de/usb_modeswitch/parameter_reference.txt
Patch1:         usb_modeswitch-fix_fsf_address.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       tcl >= 8.4
Requires:       usb_modeswitch-data = %{version}
%{?systemd_requires}

%description
USB_ModeSwitch is a mode switching tool for controlling "flip flop"
(multiple device) USB gear. It allows so-called "Zero-CD" devices that
show up as USB storage initially to be switched into their more useful
"application mode". This is most common for UMTS/3G wireless WAN
devices.

%package data
Summary:        Data Files for USB Modeswitch
Group:          Hardware/Mobile
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Data files for usb_modeswitch package.

%prep
%setup -q -a1 -n %{source_name}-%{version}
%patch1

cp %{SOURCE2} .
cp %{SOURCE3} .

%build
CFLAGS="%{optflags}" make

%install
# The install target recreates usb_modeswitch_dispatcher, which is racy in respect to its
# installation. install-common just uses the file from the build phase. boo#998641
make DESTDIR=%{buildroot} install-common %{?_smp_mflags} UDEVDIR=%{buildroot}%{_udevdir}
install -Dm 444 usb_modeswitch@.service %{buildroot}%{_unitdir}/usb_modeswitch@.service

cd %{source_name}-data-%{date}
make DESTDIR=%{buildroot} install %{?_smp_mflags} RULESDIR=%{buildroot}%{_udevdir}/rules.d

%fdupes -s %{buildroot}

%pre
%service_add_pre usb_modeswitch@.service

%post
%service_add_post usb_modeswitch@.service

%preun
%service_del_preun usb_modeswitch@.service

%postun
%service_del_postun usb_modeswitch@.service

%files
%license COPYING
%doc README device_reference.txt parameter_reference.txt
%{_sbindir}/usb_modeswitch
%{_sbindir}/usb_modeswitch_dispatcher
%{_udevdir}/usb_modeswitch
%{_unitdir}/usb_modeswitch@.service
%{_localstatedir}/lib/usb_modeswitch
%config %{_sysconfdir}/usb_modeswitch.conf
%{_mandir}/man1/usb_modeswitch.1%{?ext_man}
%{_mandir}/man1/usb_modeswitch_dispatcher.1%{?ext_man}

%files data
%{_datadir}/usb_modeswitch/
%{_udevdir}/rules.d/40-usb_modeswitch.rules

%changelog
