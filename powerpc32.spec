#
# spec file for package powerpc32
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


Name:           powerpc32
Version:        1.2
Release:        0
Summary:        PowerPC32 compilation environment for PowerPC64
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
Source:         powerpc32-%{version}.tar.bz2
Patch0:         powerpc32-1.2.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  ppc ppc64

%description
Powerpc32 is a simple utility for compiling PowerPC32 packages on
PowerPC64 machines. Powerpc32 creates an environment for the specified
program (shell) and all child processes. In the created environment,
uname -m returns ppc, so you can create 32 bit PowerPC programs.


%prep
%autosetup -p0

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
make install PREFIX=$RPM_BUILD_ROOT MANDIR=%{_mandir}
strip $RPM_BUILD_ROOT/usr/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/*
%doc %{_mandir}/man8/*

%changelog
