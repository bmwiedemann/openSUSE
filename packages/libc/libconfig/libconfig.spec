#
# spec file for package libconfig
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


%define _soversion 11
Name:           libconfig
Version:        1.7.2
Release:        0
Summary:        A library for manipulating structured configuration files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://hyperrealm.github.io/libconfig
Source:         https://hyperrealm.github.io/libconfig/dist/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  makeinfo
BuildRequires:  pkgconfig

%description
libconfig is a library for manipulating structured configuration
files. The supported file format is more compact and more readable
than XML. Unlike XML, it is type-aware, so it is not necessary to do
string parsing in application code.

The library includes bindings for both the C and C++ languages.

%package -n libconfig%{_soversion}
Summary:        C API of libconfig
Group:          System/Libraries

%description -n libconfig%{_soversion}
libconfig is a library for manipulating structured configuration
files. The supported file format is more compact and more readable
than XML. Unlike XML, it is type-aware, so it is not necessary to do
string parsing in application code.

This package contains the shared libraries for libconfig.

%package devel
Summary:        C bindings development files for libconfig
Group:          Development/Languages/C and C++
Requires:       libconfig%{_soversion} = %{version}
Recommends:     libconfig-doc = %{version}

%description devel
libconfig is a library for manipulating structured configuration
files. The supported file format is more compact and more readable
than XML. Unlike XML, it is type-aware, so it is not necessary to do
string parsing in application code.

This package contains the C bindings development files.

%package -n libconfig++%{_soversion}
Summary:        C++ API of libconfig
Group:          System/Libraries

%description -n libconfig++%{_soversion}
libconfig is a library for manipulating structured configuration
files. The supported file format is more compact and more readable
than XML. Unlike XML, it is type-aware, so it is not necessary to do
string parsing in application code.

This package contains the shared libraries for libconfig.

%package -n libconfig++-devel
Summary:        C++ bindings development files for libconfig
Group:          Development/Languages/C and C++
Requires:       libconfig++%{_soversion} = %{version}
Requires:       libconfig-devel = %{version}
Recommends:     libconfig-doc = %{version}

%description -n libconfig++-devel
libconfig is a library for manipulating structured configuration
files. The supported file format is more compact and more readable
than XML. Unlike XML, it is type-aware, so it is not necessary to do
string parsing in application code.

This package contains the C++ bindings development files.

%prep
%setup -q

%build
%configure \
  --disable-silent-rules \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_docdir}

%check
make %{?_smp_mflags} check

%post -n libconfig%{_soversion} -p /sbin/ldconfig
%postun -n libconfig%{_soversion} -p /sbin/ldconfig
%post -n libconfig++%{_soversion} -p /sbin/ldconfig
%postun -n libconfig++%{_soversion} -p /sbin/ldconfig

%files -n libconfig%{_soversion}
%license COPYING*
%doc AUTHORS README
%{_libdir}/libconfig.so.*

%files -n libconfig++%{_soversion}
%license COPYING*
%doc AUTHORS README
%{_libdir}/libconfig++.so.*

%files devel
%doc ChangeLog TODO
%{_includedir}/libconfig.h
%{_libdir}/libconfig.so
%{_libdir}/pkgconfig/libconfig.pc

%post -n libconfig++-devel
%install_info --info-dir=%{_infodir} %{_infodir}/libconfig.info%{ext_info}

%postun -n libconfig++-devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libconfig.info%{ext_info}

%files -n libconfig++-devel
%doc ChangeLog TODO
%{_includedir}/libconfig.h++
%{_libdir}/libconfig++.so
%{_libdir}/pkgconfig/libconfig++.pc
%{_infodir}/libconfig.info%{?ext_info}
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/libconfig
%dir %{_libdir}/cmake/libconfig++
%{_libdir}/cmake/libconfig++/libconfig++Config.cmake
%{_libdir}/cmake/libconfig/libconfigConfig.cmake

%changelog
