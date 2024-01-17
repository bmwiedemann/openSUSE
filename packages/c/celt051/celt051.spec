#
# spec file for package celt051
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           celt051
%define _name celt
Version:        0.5.1.3
Release:        1
License:        BSD-3-Clause
Summary:        CELT is a very low delay audio codec
Url:            http://www.celt-codec.org/
Group:          System/Libraries
Source:         http://downloads.us.xiph.org/releases/%{_name}/%{_name}-%{version}.tar.gz
BuildRequires:  libogg-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CELT is a very low delay audio codec designed for high-quality communications.
Its potential uses include video-conferencing and network music performance.

This is a maintained branch of the 0.5.1 prerelease of CELT.

%package -n libcelt051-0
Group: System/Libraries
Summary: CELT is a very low delay audio codec

%description -n libcelt051-0
CELT is a very low delay audio codec designed for high-quality communications.
Its potential uses include video-conferencing and network music performance.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       libcelt051-0 = %{version}

%description devel
CELT is a very low delay audio codec designed for high-quality communications.
Its potential uses include video-conferencing and network music performance.

This package contains development files for %{name}.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure \
    --disable-static \
    --disable-oggtest
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print

%clean
[ %{buildroot} != "/" ] && rm -rf %{buildroot}

%post -n libcelt051-0 -p /sbin/ldconfig

%postun -n libcelt051-0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*

%files -n libcelt051-0
%defattr(-, root, root)
%doc COPYING README
%{_libdir}/libcelt051.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so


%changelog
