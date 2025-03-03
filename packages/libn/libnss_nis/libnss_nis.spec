#
# spec file for package libnss_nis
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


Name:           libnss_nis
Version:        3.2
Release:        0
Summary:        NSS NIS plugin for glibc
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            http://github.com/thkukuk/libnss_nis
Source:         %{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnsl) >= 1.0.1
BuildRequires:  pkgconfig(libtirpc) >= 1.0.1

%description
The NSS NIS plugin provides NIS support for get*nam() functions from
glibc. This version is IPv6 capable.

%package -n libnss_nis2
Summary:        NSS NIS plugin for glibc
Group:          System/Libraries
Provides:       glibc:/%{_lib}/libnss_nis.so.2

%description -n libnss_nis2
The NSS NIS plugin provides NIS support for get*nam() functions from
glibc. This version is IPv6 capable.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm -v %{buildroot}/%{_libdir}/%{name}.{a,la,so}

%check
make %{?_smp_mflags} check

%post -n libnss_nis2 -p /sbin/ldconfig
%postun -n libnss_nis2 -p /sbin/ldconfig

%files -n libnss_nis2
%license COPYING
%{_libdir}/libnss_nis.so.2*

%changelog
