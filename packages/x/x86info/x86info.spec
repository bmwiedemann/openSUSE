#
# spec file for package x86info
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


Name:           x86info
Version:        1.31+git.20200121
Release:        0
Summary:        Tool to show x86 CPU Information
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://www.codemonkey.org.uk/projects/x86info/
Source:         %{name}-%{version}.tar.xz
Patch0:         use-python3.patch
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(libpci)
ExclusiveArch:  %{ix86} x86_64

%description
Unlike other 'cpuinfo' tools which just parse /proc/cpuinfo, x86info
probes the CPU registers to find out more information. It can discover
the contents of model-specific registers, discover CPU silicon
revisions, and more.

%prep
%autosetup -p1

%build
make CFLAGS="%{optflags} -Iinclude -DVERSION=%{version}" %{?_smp_mflags} V=1
make CFLAGS="%{optflags} -I. -I../include" %{?_smp_mflags} -C lsmsr V=1

%install
install -Dpm 0575 x86info \
  %{buildroot}%{_bindir}/x86info
install -Dpm 0644 x86info.1 \
  %{buildroot}%{_mandir}/man1/x86info.1
install -Dpm 0755 lsmsr/lsmsr \
  %{buildroot}%{_sbindir}/lsmsr
install -Dpm 0644 lsmsr/lsmsr.8 \
  %{buildroot}%{_mandir}/man8/lsmsr.8

%files
%license COPYING
%doc README TODO
%{_bindir}/%{name}
%{_sbindir}/lsmsr
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man8/lsmsr.8%{?ext_man}

%changelog
