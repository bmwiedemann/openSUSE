#
# spec file for package systemtap-dtrace
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


%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
Name:           systemtap-dtrace
Version:        5.1
Release:        0
Summary:        SystemTap dtrace utility
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            http://sourceware.org/systemtap/
Source0:        http://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz
Source1:        http://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz.asc
Source2:        systemtap.keyring
Source3:        README-BEFORE-ADDING-PATCHES
Source4:        README-KEYRING

BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
SystemTap is an instrumentation system for systems running Linux.
This package contains the dtrace utility to build provider and probe
definitions.

%prep
%setup -q -n systemtap-%{version}
%autopatch -p1

%build
# Our binutils always support '?' in the section characters on all
# architectures, no need for configure tests
sed s=@preferred_python@=%{_bindir}/python3= dtrace.in |sed s=@prefix@=%{_prefix}= >dtrace

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 dtrace %{buildroot}%{_bindir}
%python3_fix_shebang

%files
%defattr(-,root,root)
%{_bindir}/dtrace

%changelog
