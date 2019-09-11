#
# spec file for package icmpinfo
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


Name:           icmpinfo
Version:        1.11
Release:        0
Summary:        A Tool for Looking at ICMP Messages
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
Url:            http://www.demailly.com/~dl/softs.html
Source:         icmpinfo-%{version}.tar.gz
Source1:        COPYRIGHT
Patch0:         icmpinfo-%{version}.dif
Requires:       netcfg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A tool for looking at the ICMP messages received on the running host.

%prep
%setup -q
%patch0

%build
make CFLAGS="-D_GNU_SOURCE -fvisibility=hidden %{optflags}" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} MANDIR=%{_mandir} install
cp %{SOURCE1} .

%files
%defattr(-,root,root)
%doc README NocTools.Infos TODO CHANGES COPYRIGHT
%{_mandir}/man?/*
%{_sbindir}/icmpinfo

%changelog
