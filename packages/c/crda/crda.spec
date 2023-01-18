#
# spec file for package crda
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


%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d }
%define skip_python2 1

Name:           crda
Summary:        802.11 central regulatory domain agent
License:        SUSE-Copyleft-Next-0.3.0
Group:          Hardware/Wifi
URL:            https://wireless.wiki.kernel.org/en/developers/Regulatory/CRDA
Version:        4.14
Release:        0
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/mcgrof/crda.git/snapshot/crda-%{version}.tar.gz
Source1:        crda.default
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  python3-pycrypto
BuildRequires:  wireless-regdb
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(udev)
Requires:       wireless-regdb
Supplements:    kernel >= 2.6.29
# PATCH-FIX-OPENSUSE gcc6-fix-errors.patch -- Fix errors seen by GCC6.
Patch0:         gcc6-fix-errors.patch
# PATCH-FIX-OPENSUSE python2 is gone, port to python3
Patch1:         crda-python3.patch
# PATCH-FIX-UPSTREAM crda-67f1e6ddbdfade357e234c9d58a30fe0a283fe60.patch
Patch2:         crda-67f1e6ddbdfade357e234c9d58a30fe0a283fe60.patch
# PATCH-FIX-UPSTREAM crda-f4ef2531698fb9ba006e8b31a223b3269be8bc7c.patch
Patch3:         crda-f4ef2531698fb9ba006e8b31a223b3269be8bc7c.patch
# PATCH-FIX-SUSE crda-default.patch
Patch4:         crda-default.patch

%description
The crda binary provides access to the wireless-regdb to the kernel
through udev.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# make install calls 'ldconfig' and fails if it cannot run it...
ln -s /bin/true ldconfig

%build
export CFLAGS="%{optflags}"
make all_noverify %{?_smp_mflags} V=1

%install
# to find ldconfig...
export PATH=.:$PATH
make DESTDIR=$RPM_BUILD_ROOT SBINDIR=%{_sbindir}/ UDEV_RULE_DIR=%{_udevrulesdir} LIBDIR=%{_libdir} install
mkdir -p %{buildroot}%{_prefix}%{_sysconfdir}/default
install -m 644 %{S:1} %{buildroot}%{_prefix}%{_sysconfdir}/default/%{name}
%if 0%{?suse_version} < 1550
mkdir $RPM_BUILD_ROOT/sbin
ln -sf %{_sbindir}/{crda,regdbdump} $RPM_BUILD_ROOT/sbin
%endif

# clean up unneeded stuff...
rm -r %{buildroot}/usr/include/reglib

%files
%defattr(-,root,root)
%_sbindir/crda
%_sbindir/regdbdump
%_libdir/libreg.so
%if 0%{?suse_version} < 1550
/sbin/crda
/sbin/regdbdump
%endif
%if 0%{?suse_version} < 1550
%dir %{_prefix}%{_sysconfdir}/
%dir %{_prefix}%{_sysconfdir}/default/
%endif
%{_prefix}%{_sysconfdir}/default/%{name}
%{_udevrulesdir}/85-regulatory.rules
%{_mandir}/man8/crda.8.gz
%{_mandir}/man8/regdbdump.8.gz

%post
%{?udev_rules_update:%udev_rules_update}

%changelog
