#
# spec file for package systemtap-headers
#
# Copyright (c) 2024 SUSE LLC
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


# Note: this separate package systemtap-headers exists so that ring0
# packages can make use of the SDT headers without pulling in all
# build requirements of the normal systemtap package.  Normal use
# outside of BuildRequires in ring0 packages should use systemtap-sdt-devel
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
Name:           systemtap-headers
Version:        5.1
Release:        0
Summary:        SystemTap headers
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            http://sourceware.org/systemtap/
Source0:        https://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz
Source1:        https://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz.asc
Source2:        systemtap.keyring
Source3:        README-BEFORE-ADDING-PATCHES
Source4:        README-KEYRING
Source5:        stap-server.conf
Patch1:         systemtap-build-source-dir.patch

# sdt-devel provides the same header files as us, so we
# must conflict
Conflicts:      systemtap-sdt-devel

%description
SystemTap is an instrumentation system for systems running Linux.
This package contains only the headers for static system probes and
exists only to limit build cycles.  Normally you should install
systemtap-sdt-devel, which also contains these headers.

%prep
%setup -q -n systemtap-%{version}
%autopatch -p1

%build
# Our binutils always support '?' in the section characters on all
# architectures, no need for configure tests
sed -e 's/@support_section_question@/1/' < includes/sys/sdt-config.h.in > includes/sys/sdt-config.h

%install
mkdir -p %{buildroot}%{_includedir}/sys
cp -rp includes/sys/*.h %{buildroot}%{_includedir}/sys/

%files
%defattr(-,root,root)
%{_includedir}/sys/*.h

%changelog
