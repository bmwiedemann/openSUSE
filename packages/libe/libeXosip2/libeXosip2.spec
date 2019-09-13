#
# spec file for package libeXosip2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname libeXosip2-12

Name:           libeXosip2
Version:        5.0.0
Release:        0
Summary:        Extended osip2 library
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
Url:            http://savannah.nongnu.org/projects/exosip/
Source:         http://download.savannah.nongnu.org/releases/exosip/libexosip2-%{version}.tar.gz
Patch0:         openssl110-fix.patch
BuildRequires:  glibc-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libosip2) >= 5.0.0
BuildRequires:  pkgconfig(openssl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Extended library for the osip2 protocol.

%package -n %{soname}
Summary:        Extended osip2 library
Group:          System/Libraries
Provides:       libeXosip2 = %{version}

%description -n %{soname}
Extended library for the osip2 protocol.

%package devel
Summary:        Extended osip2 library
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}
Requires:       glibc-devel
Requires:       pkgconfig(libosip2)
Requires:       pkgconfig(openssl)
Provides:       %{soname}-devel = %{version}

%description devel
Extended library for the osip2 protocol.

%prep
%setup -q -n libexosip2-%{version}
%if 0%{?suse_version} >= 1330 
%patch0 -p0
%endif

%build
%configure \
  --disable-static \
  --disable-debug
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname} -p /sbin/ldconfig

%postun -n %{soname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/sip_reg

%files -n %{soname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/eXosip2/*.h
%dir %{_includedir}/eXosip2
%{_libdir}/lib*.so

%changelog
