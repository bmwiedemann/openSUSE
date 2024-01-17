#
# spec file for package libax25
#
# Copyright (c) 2021 SUSE LLC
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

%define         sover 0
%define src_ver 0.0.12-rc5
Name:           libax25
Version:        0.0.12~rc5
Release:        0
Summary:        AX.25 data link layer protocol library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.linux-ax25.org/wiki/LinuxAX25
Source:         http://www.linux-ax25.org/pub/libax25/libax25-%{src_ver}.tar.gz
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  zlib-devel

%description
Libraries for AX.25. AX.25 (Amateur X.25) is a data link layer
protocol derived from the X.25 protocol suite and designed for use by
amateur radio operators.

%package common
Summary:        Common files for %{name}
Group:          System/Libraries
BuildArch:      noarch

%description common
Libraries for AX.25. AX.25 (Amateur X.25) is a data link layer
protocol derived from the X.25 protocol suite and designed for use by
amateur radio operators.

This package contains common config files for %{name}.

%package -n libax25-%{sover}
Summary:        AX.25 data link layer protocol library
Group:          System/Libraries
Requires:       %{name}-common

%description -n libax25-%{sover}
Libraries for AX.25. AX.25 (Amateur X.25) is a data link layer
protocol derived from the X.25 protocol suite and designed for use by
amateur radio operators.

%package -n libax25io%{sover}
Summary:        AX.25 data link layer protocol library
Group:          System/Libraries
Requires:       %{name}-common

%description -n libax25io%{sover}
Libraries for AX.25. AX.25 (Amateur X.25) is a data link layer
protocol derived from the X.25 protocol suite and designed for use by
amateur radio operators.

%package devel
Summary:        Header files for the AX.25 library
Group:          Development/Libraries/C and C++
Requires:       libax25-%{sover} = %{version}
Requires:       libax25io%{sover} = %{version}

%description devel
Header files for libax25. Used to build packages that are
linked against kernel ax25.

%prep
%setup -q -n %{name}-%{src_ver}

%build
autoreconf -fiv
%configure \
  --disable-static
%make_build

%install
%make_install installconf
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libax25-%{sover} -p /sbin/ldconfig
%post   -n libax25io%{sover} -p /sbin/ldconfig
%postun -n libax25-%{sover} -p /sbin/ldconfig
%postun -n libax25io%{sover} -p /sbin/ldconfig

%files common
%license COPYING
%dir %{_sysconfdir}/ax25
%config %{_sysconfdir}/ax25/axports
%config %{_sysconfdir}/ax25/nrports
%config %{_sysconfdir}/ax25/rsports
%{_mandir}/man5/axports.5%{ext_man}
%{_mandir}/man5/nrports.5%{ext_man}
%{_mandir}/man5/rsports.5%{ext_man}

%files -n libax25-%{sover}
%{_libdir}/libax25.so.%{sover}*

%files -n libax25io%{sover}
%{_libdir}/libax25io.so.%{sover}*

%files devel
%doc AUTHORS ChangeLog README
%{_libdir}/libax25io.so
%{_libdir}/libax25.so
%{_includedir}/netax25
%{_mandir}/man3/ax25.3%{ext_man}
%{_mandir}/man3/rose.3%{ext_man}

%changelog
