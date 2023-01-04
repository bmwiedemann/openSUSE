#
# spec file for package udhcp
#
# Copyright (c) 2021 SUSE LLC
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


Name:           udhcp
Version:        0.9.8
Release:        0
Summary:        Micro DHCP client / server
License:        GPL-2.0-only
Group:          System/Emulators/PC
URL:            http://udhcp.busybox.net
Source0:        %{name}-%{version}.tar.gz
Patch0:         oracle-rpmbuild-makefile-changes.patch
Patch1:         %{name}_usermac.patch
Patch2:         %{name}-outputpy.patch
Patch3:         %{name}-update-scripts.patch
# PATCH-FIX-UPSTREAM: do not strip binaries (bnc#890844)
Patch4:         udhcp-do-not-strip.patch
Patch5:         ifconfig_path.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Udhcp is a small dhcp client / server mainly used to support Xen
para-virtualized PXE booting.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
make %{?_smp_mflags}

%install
%make_install SBINDIR=%{buildroot}/%{_sbindir}
pushd %{buildroot}/%{_mandir}
find . -type f -exec chmod -x {} \;
popd
%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
ln -s %{_sbindir}/udhcpc %{buildroot}/sbin
%endif

%files
%defattr(-,root,root)
%if 0%{?suse_version} < 1550
/sbin/*
%endif
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man?/*
%dir %{_datadir}/udhcpc
%{_datadir}/udhcpc/*

%changelog
