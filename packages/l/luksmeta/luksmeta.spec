#
# spec file for package luksmeta
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


%define so_ver 0

Name:           luksmeta
Version:        9
Release:        0
Summary:        Utility for storing metadata in a LUKSv1 header
License:        LGPL-2.1-or-later
URL:            https://github.com/latchset/luksmeta
Source0:        https://github.com/latchset/luksmeta/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcryptsetup) >= 1.5.1

%description
The luksmeta utility enables an administrator to store metadata in the gap
between the end of the LUKSv1 header and the start of the encrypted data.

%package -n lib%{name}%{so_ver}
Summary:        Simple library for storing metadata in the LUKSv1 header

%description -n lib%{name}%{so_ver}
LUKSMeta is a simple library for storing metadata in the LUKSv1 header.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{so_ver} = %{version}
Requires:       pkgconfig(libcryptsetup) >= 1.5.1

%description -n lib%{name}-devel
The lib%{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/*
%{_mandir}/man8/*

%files -n lib%{name}%{so_ver}
%license COPYING
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
