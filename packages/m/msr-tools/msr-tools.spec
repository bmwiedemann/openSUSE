#
# spec file for package msr-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           msr-tools
Version:        1.3.git10
Release:        0
Summary:        Tool for reading and writing MSRs (model specific register)
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/01org/msr-tools
Source:         %{name}-%{version}.tar.xz
Source1:        COPYING
Patch1:         %{name}-xen_physical_msr_support.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Tool to read and write MSRs (model specific registers). You have to
load the "msr" module manually ("modprobe msr").

%prep
%autosetup -p1

%build
./autogen.sh
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}/%{_sbindir}
cp %{SOURCE1} .
install -m 0755 rdmsr wrmsr msr-cpuid %{buildroot}/%{_sbindir}

%files
%defattr(-,root,root)
%license COPYING
%{_sbindir}/*

%changelog
