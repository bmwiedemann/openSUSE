#
# spec file for package bridge-utils
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bridge-utils
Version:        1.6
Release:        0
Summary:        Utilities for Configuring the Linux Ethernet Bridge
License:        GPL-2.0+
Group:          Productivity/Networking/Routing
Url:            http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge
Source:         http://www.kernel.org/pub/linux/utils/net/bridge-utils/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.5-hz.diff
Patch1:         %{name}-1.5-optflags.patch
Patch2:         bridge-utils-1.5-ip6.patch
BuildRequires:  automake
BuildRequires:  libsysfs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains utilities for configuring the Linux ethernet
bridge. The Linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connection is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
The %{name} devel package contains files needed for development.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -d -m 755 %{buildroot}/sbin
install -D -m 644 libbridge/libbridge.h %{buildroot}%{_includedir}/libbridge.h
install -D -m 644 libbridge/libbridge.a %{buildroot}%{_libdir}/libbridge.a

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README THANKS TODO doc/[FHPRSW]*
%{_mandir}/man?/*
%{_sbindir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/lib*

%changelog
