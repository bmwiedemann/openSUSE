#
# spec file for package adjtimex
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           adjtimex
Version:        1.29
Release:        0
Summary:        Kernel time variables configuration utility
License:        GPL-2.0+
Group:          System/Base
Source:         http://ftp.debian.org/debian/pool/main/a/adjtimex/%{name}_%{version}.orig.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       util-linux:/usr/sbin/adjtimex

%description
This program gives you raw access to the kernel time variables. For
a machine connected to the Internet, or equipped with a precision
oscillator or radio clock, the best way to keep the system clock
correct is with ntpd. However, for a standalone or intermittently
connected machine, you may use adjtimex instead to at least correct
for systematic drift. adjtimex can optionally adjust the system clock
using the CMOS clock as a reference, and can log times for long-term
estimation of drift rates.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man8
install adjtimex %{buildroot}%{_sbindir}/
install -m0644 adjtimex.8 %{buildroot}%{_mandir}/man8/

%files
%defattr(-,root,root)
%doc COPYING COPYRIGHT
%{_sbindir}/adjtimex
%{_mandir}/man8/adjtimex.8*

%changelog
