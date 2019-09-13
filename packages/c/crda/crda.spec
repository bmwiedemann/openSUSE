#
# spec file for package crda
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


%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d }

Url:            http://linuxwireless.org/en/developers/Regulatory/CRDA

Name:           crda
Summary:        802.11 central regulatory domain agent
License:        SUSE-Copyleft-Next-0.3.0
Group:          Hardware/Wifi
Version:        3.18
Release:        0
Source:         http://kernel.org/pub/software/network/crda/crda-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  python-m2crypto
BuildRequires:  wireless-regdb
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(udev)
Requires:       wireless-regdb
Supplements:    kernel >= 2.6.29
# PATCH-FIX-OPENSUSE gcc6-fix-errors.patch -- Fix errors seen by GCC6.
Patch0:         gcc6-fix-errors.patch

%description
The crda binary provides access to the wireless-regdb to the kernel
through udev.

%prep
%setup -q
%patch0 -p1
# make install calls 'ldconfig' and fails if it cannot run it...
ln -s /bin/true ldconfig

%build
export CFLAGS="%{optflags}"
make all_noverify %{?_smp_mflags} V=1

%install
# to find ldconfig...
export PATH=.:$PATH
make DESTDIR=$RPM_BUILD_ROOT SBINDIR=%{_sbindir}/ UDEV_RULE_DIR=%{_udevrulesdir} LIBDIR=%{_libdir} install
#UsrMerge
mkdir $RPM_BUILD_ROOT/sbin
ln -sf %{_sbindir}/{crda,regdbdump} $RPM_BUILD_ROOT/sbin
#EndUserMerge

# clean up unneeded stuff...
rm -r %{buildroot}/usr/include/reglib

%files
%defattr(-,root,root)
%_sbindir/crda
%_sbindir/regdbdump
%_libdir/libreg.so
#UsrMerge
/sbin/crda
/sbin/regdbdump
#EndUserMerge
%{_udevrulesdir}/85-regulatory.rules
%{_mandir}/man8/crda.8.gz
%{_mandir}/man8/regdbdump.8.gz

%post
%{?udev_rules_update:%udev_rules_update}

%changelog
