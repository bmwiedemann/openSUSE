#
# spec file for package celt
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           celt
Version:        0.11.3
Release:        0
Summary:        Ultra-Low Delay Audio Codec
License:        BSD-2-Clause
Group:          Productivity/Multimedia/Other
Url:            http://www.celt-codec.org/
Source:         http://downloads.xiph.org/releases/celt/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
Requires:       libcelt0-2 = %{version}-%{release}
# Patch configure.ac to remove the "0" suffix from libcelt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The CELT codec is an experimental audio codec for use in low-delay
speech and audio communication.

%package -n libcelt-devel
Summary:        Ultra-Low Delay Audio Codec
Group:          Development/Libraries/C and C++
Requires:       celt = %{version}-%{release}
Requires:       glibc-devel
Requires:       libcelt0-2 = %{version}-%{release}
Requires:       pkg-config

%description -n libcelt-devel
The CELT codec is an experimental audio codec for use in low-delay
speech and audio communication.

%package -n libcelt0-2
Summary:        Ultra-Low Delay Audio Codec
Group:          System/Libraries

%description -n libcelt0-2
The CELT codec is an experimental audio codec for use in low-delay
speech and audio communication.

%prep
%setup -q

%build
autoreconf -fiv
%configure\
	--disable-static\
	--with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libcelt0-2 -p /sbin/ldconfig

%postun -n libcelt0-2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING TODO
%{_bindir}/celt*

%files -n libcelt-devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/celt.pc

%files -n libcelt0-2
%defattr(-,root,root)
%{_libdir}/libcelt0.so.2*

%changelog
