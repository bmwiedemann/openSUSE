#
# spec file for package bandwidth
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


Name:           bandwidth
Version:        1.9.4
Release:        0
Summary:        Memory and network benchmark program
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            https://zsmith.co/bandwidth.php
Source:         https://zsmith.co/archives/%{name}-%{version}.tar.gz
BuildRequires:  nasm
ExclusiveArch:  %{ix86} x86_64

%description
bandwidth is an artificial benchmark primarily for measuring memory bandwidth
on x86 and x86_64 based computers, useful for identifying weaknesses in a
computer's memory subsystem, in the bus architecture, in the cache architecture
and in the processor itself.

%prep
%setup -q

%build
# currently fails with No rule to make target 'routines-arm-32bit.asm', needed by 'bandwidth-arm32'
%ifarch %{arm}
%make_build bandwidth-arm32
%endif

%ifarch %{ix86}
%make_build bandwidth32 CFLAGS="%{optflags}"
mv bandwidth32 %{name}
%endif

%ifarch x86_64
%make_build bandwidth64 CFLAGS="%{optflags}"
mv bandwidth64 %{name}
%endif

%install
install -Dsm 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license GPL.txt
%doc README.txt
%{_bindir}/%{name}

%changelog
