#
# spec file for package lomoco
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d
%define udev_scripts_dir %(pkg-config --variable=udevdir udev)
%if 0%{?suse_version}
%define sysconfigfile %{_fillupdir}/sysconfig.logitech_mouse
%else
%define sysconfigfile %{_sysconfdir}/sysconfig/logitech_mouse
%endif
Name:           lomoco
Version:        1.0
Release:        0
Summary:        Tool for setting the special features of some Logitech mice
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://www.lomoco.org/
Source:         lomoco-1.0.tar.gz
Source3:        sysconfig.logitech_mouse
Source4:        tomodalias.awk
Source5:        udev.lomoco
Patch0:         lomoco.diff
Patch1:         lomoco-udev-1030.diff
Patch2:         lomoco-mx518-2-support.patch
Patch3:         lomoco-1.0-stropts.diff
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
Conflicts:      lmctl
Conflicts:      logitech_applet
Provides:       lmctl:%{_bindir}/lmctl
%if 0%{?suse_version} && 0%{?suse_version} > 1100
BuildRequires:  libusb-compat-devel
%else
BuildRequires:  libusb-devel
%endif
%if 0%{?suse_version}
Supplements:    modalias(usb:v046DpC00E*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC00F*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC012*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC01B*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC01D*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC01E*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC024*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC025*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC031*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC041*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC501*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC502*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC503*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC504*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC505*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC506*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC508*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC50E*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC702*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC704*dc*dsc*dp*ic*isc*ip*)
Requires(post): %fillup_prereq
%endif

%description
lomoco can configure vendor-specific options on Logitech USB mice (or
dual-personality mice plugged into the USB port). A number of recent
devices are supported. The program is mostly useful in setting the
resolution to 800 cpi on mice that boot at 400 cpi (such as the
MX-500), and disabling SmartScroll or Cruise Control for those who
would rather use the two extra buttons as ordinary mouse buttons.

You can configure which features should be enabled in
%{_sysconfdir}/sysconfig/logitech_mouse

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1

%build
autoreconf -f -i
%configure
make %{?_smp_mflags}
awk -f udev/toudev.awk < src/lomoco.c \
      | sed 's@RUN="lomoco"@RUN="%{udev_scripts_dir}/lomoco.sh", ENV{ACL_MANAGE}="1"@' \
      > lomoco.rules

%install
%make_install
install -d -m 755 %{buildroot}%{_udevrulesdir}
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 lomoco.rules %{buildroot}%{_udevrulesdir}/40-lomoco.rules
install -d -m 755 %{buildroot}%{udev_scripts_dir}
install -D -m 644 %{SOURCE3} %{buildroot}%{sysconfigfile}
install -m 755 %{SOURCE5} %{buildroot}%{udev_scripts_dir}/lomoco.sh

%if 0%{?suse_version}
%post
%fillup_only -n logitech_mouse
%endif

%files
%doc AUTHORS ChangeLog COPYING README
%{udev_scripts_dir}/lomoco.sh
%{_udevrulesdir}/*.rules
%{_bindir}/lomoco
%{_mandir}/man?/lomoco.?%{ext_man}
%{!?suse_version:%config(noreplace)} %{sysconfigfile}

%changelog
