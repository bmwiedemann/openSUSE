#
# spec file for package alsa-oss
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


Name:           alsa-oss
Version:        1.1.8
Release:        0
Summary:        LD_PRELOAD-able library that translates OSS into ALSA calls
License:        GPL-2.0-or-later
Group:          System/Libraries
Url:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/oss-lib/alsa-oss-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  alsa-devel
BuildRequires:  libtool

%description
A preloadable library that intercepts Open Sound System API calls
in applications and translates them into ALSA API calls.
A convenience script to launch such applications with the preloaded
library is provided as well, called "aoss".

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
# remove unneeded files
rm -f %{buildroot}%{_libdir}/*.*a
rm -f %{buildroot}%{_libdir}/libalsatoss.so
rm -f %{buildroot}%{_includedir}/*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
# .so must be in the main package because aoss requires it
%{_libdir}/libaoss.so*
%{_libdir}/libalsatoss.so.*
%{_bindir}/*
%{_mandir}/man*/*

%changelog
