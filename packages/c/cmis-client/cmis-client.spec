#
# spec file for package cmis-client
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


%define sover 0_5-5
%define incname 0.5
%define _name  libcmis
Name:           cmis-client
Version:        0.5.2
Release:        0
Summary:        Sample CMIS client
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/tdf/libcmis
Source0:        https://github.com/tdf/%{_name}/releases/download/v%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  docbook2X
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libcppunit-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       %{_name}-%{sover} = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_program_options-devel
%else
BuildRequires:  boost-devel >= 1.36
%endif

%description
Sample client to access CMIS-enabled repositories using libcmis.

%package -n %{_name}-%{sover}
Summary:        Library for accessing CMIS-enabled servers
Group:          System/Libraries

%description -n %{_name}-%{sover}
libcmis is a C++ client library for the CMIS (Content Management
Interoperability Services) interface. This library allows C++
applications to connect to any CMIS-enabled repositories.

%package -n %{_name}-devel
Summary:        Development files for libcmis
Group:          Development/Libraries/C and C++
Requires:       %{_name}-%{sover} = %{version}

%description -n %{_name}-devel
Development files for libcmis. libcmis is a C++ client library for
the CMIS interface.

%package -n %{_name}-c-%{sover}
Summary:        C wrapper for libcmis, a library for accessing CMIS-enabled servers
Group:          System/Libraries

%description -n %{_name}-c-%{sover}
libcmis-c is a C client library for the CMIS (Content Management
Interoperability Services) interface. This allows C applications to
connect to any CMIS-enabled repositories. It is only a wrapper for
its C++ sister library libcmis.

%package -n %{_name}-c-devel
Summary:        Development files for libcmis-c
Group:          Development/Libraries/C and C++
Requires:       %{_name}-c-%{sover} = %{version}

%description -n %{_name}-c-devel
Development files for libcmis-c. libcmis-c is a C client library for
the CMIS interface.

%prep
%setup -q -n %{_name}-%{version}

%build
autoreconf -fvi
export CFLAGS="%{optflags} -D_GNU_SOURCE $(getconf LFS_CFLAGS)"
export CXXFLAGS="%{optflags} $(getconf LFS_CFLAGS)"
%configure \
    --disable-silent-rules \
    --disable-static \
    --disable-werror
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
# bypass bug 955832
%ifarch ppc64le
make -k check %{?_smp_mflags} || echo "ignore check error"
%else
make check %{?_smp_mflags}
%endif

%post -n %{_name}-%{sover} -p /sbin/ldconfig
%post -n %{_name}-c-%{sover} -p /sbin/ldconfig
%postun -n %{_name}-%{sover} -p /sbin/ldconfig
%postun -n %{_name}-c-%{sover} -p /sbin/ldconfig

%files
%{_bindir}/cmis-client
%{_mandir}/man1/cmis-client.1%{?ext_man}

%files -n %{_name}-%{sover}
%doc AUTHORS NEWS
%license COPYING.LGPL COPYING.MPL COPYING.GPL
%{_libdir}/%{_name}-%{incname}.so.*

%files -n %{_name}-devel
%{_includedir}/%{_name}-%{incname}
%{_libdir}/pkgconfig/%{_name}-%{incname}.pc
%{_libdir}/%{_name}-%{incname}.so

%files -n %{_name}-c-%{sover}
%doc AUTHORS NEWS
%license COPYING.LGPL COPYING.MPL COPYING.GPL
%{_libdir}/%{_name}-c-%{incname}.so.*

%files -n %{_name}-c-devel
%{_includedir}/%{_name}-c-%{incname}
%{_libdir}/pkgconfig/%{_name}-c-%{incname}.pc
%{_libdir}/%{_name}-c-%{incname}.so

%changelog
