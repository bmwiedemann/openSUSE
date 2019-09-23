#
# spec file for package setserial
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


Name:           setserial
Version:        2.17
Release:        0
Summary:        A utility for configuring serial ports
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://setserial.sourceforge.net
Source0:        ftp://tsx-11.mit.edu/pub/linux/sources/sbin/setserial-%{version}.tar.bz2
Patch0:         %{name}-%{version}-autoconf.diff
Patch1:         %{name}-%{version}-error.diff
Patch2:         %{name}-%{version}-prototypes.diff
Patch3:         %{name}-%{version}-nohayes.diff
Patch4:         %{name}-%{version}-binaryInUsr.patch
BuildRequires:  groff
Requires:       /sbin/isserial
Provides:       util:/sbin/setserial
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Setserial is a basic system utility for displaying or setting serial
port information. Setserial can reveal and allow you to alter the I/O
port and IRQ that a particular serial device is using.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1
%patch4

chmod -x rc.serial

%build
CFLAGS="%{optflags} -Wall" \
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sbindir}
%make_install STRIP=:

%files
%defattr(-,root,root)
%doc README setserial.lsm rc.serial
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
