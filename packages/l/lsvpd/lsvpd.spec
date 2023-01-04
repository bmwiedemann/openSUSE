#
# spec file for package lsvpd
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


Name:           lsvpd
Version:        1.7.14
Release:        0
Summary:        VPD Hardware Inventory Utilities for Linux
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/power-ras/lsvpd
Source:         https://github.com/power-ras/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  librtas-devel
BuildRequires:  libtool
BuildRequires:  libvpd-devel
BuildRequires:  sg3_utils-devel
BuildRequires:  zlib-devel
Requires:       /bin/sed
Recommends:     hwdata
ExclusiveArch:  ppc ppc64 ppc64le

%description
The lsvpd package contains both the lsvpd, lscfg and lsmcode commands.
These commands, along with a boot-time scanning script called
update-device-tree, constitute a simple hardware inventory system. The
lsvpd command provides Vital Product Data (VPD) about hardware
components to higher-level serviceability tools. The lscfg command
provides a more human-readable format of the VPD, as well as some
system-specific information.  lsmcode lists microcode and firmware
levels.

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags} -UPCI_IDS -DPCI_IDS='\"%{_datadir}/hwdata/pci.ids\"' -UUSB_IDS -DUSB_IDS='\"%{_datadir}/hwdata/usb.ids\"'"
export CXXFLAGS="%{optflags} -UPCI_IDS -DPCI_IDS='\"%{_datadir}/hwdata/pci.ids\"' -UUSB_IDS -DUSB_IDS='\"%{_datadir}/hwdata/usb.ids\"'"
sh bootstrap.sh
%configure
make %{?_smp_mflags}
chmod 644 README* COPYING NEWS

%install
%make_install
%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
for i in lscfg lsmcode lsvio lsvpd update-lsvpd-db
do
 if test -f %{buildroot}%{_sbindir}/$i
 then
   ln -sfvbn ..%{_sbindir}/$i %{buildroot}/sbin/$i
 fi
done
%endif
if [ -e %{_sysconfdir}/udev/rules.d/99-lsvpd.rules ] ; then
	rm %{_sysconfdir}/udev/rules.d/99-lsvpd.rules
fi
if [ -e %{_sysconfdir}/udev/rules.d/99-lsvpd.disabled ] ; then
	rm %{_sysconfdir}/udev/rules.d/99-lsvpd.disabled
fi

%post
if [ -d %{_localstatedir}/lib/lsvpd ] ; then
  rm -rf %{_localstatedir}/lib/lsvpd
fi
%{_sbindir}/vpdupdate
exit 0

%files
%license COPYING
%doc README NEWS
%dir %{_sysconfdir}/lsvpd
%attr (644,root,root) %config %{_sysconfdir}/lsvpd/*
%if 0%{?suse_version} < 1550
/sbin/*
%endif
%attr (755,root,root) %{_sbindir}/*
%{_mandir}/*/*

%changelog
