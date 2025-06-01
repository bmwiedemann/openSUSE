#
# spec file for package libconfig
#
# Copyright (c) 2025 SUSE LLC
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


%define _soversion 15
Name:           libconfig
Version:        1.8.1
Release:        0
Summary:        A library for manipulating structured configuration files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://hyperrealm.github.io/libconfig
Source:         https://github.com/hyperrealm/libconfig/archive/refs/tags/v%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         autoconf2.60.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkg-config

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

%package -n libconfig++%{_soversion}
Summary:        C++ API of libconfig
Group:          System/Libraries

%description -n libconfig++%{_soversion}
libconfig is a library for manipulating structured configuration
files. The supported file format is more compact and more readable
than XML. Unlike XML, it is type-aware, so it is not necessary to do
string parsing in application code.

This package contains the shared libraries for libconfig.

%package devel
Summary:        Headers for libconfig
Group:          Development/Languages/C and C++
Requires:       libconfig%{_soversion} = %{version}
Requires:       libconfig++%{_soversion} = %{version}
Recommends:     libconfig-doc = %{version}
Obsoletes:      libconfig++-devel < %{version}-%{release}
Provides:       libconfig++-devel = %{version}-%{release}

%description devel
libconfig is a library for manipulating structured configuration
files. The supported file format is more compact and more readable
than XML. Unlike XML, it is type-aware, so it is not necessary to do
string parsing in application code.

This package contains the headers and cmake files for both
the C and C++ APIs.

%prep
%autosetup -p1
%if 0%{?suse_version} >= 1600
%patch -P 1 -R -p1
%endif

%build
if ! test -f configure; then
	autoreconf -fi
fi
export CFLAGS="%{optflags} -std=gnu11"
%configure \
  --disable-silent-rules \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_docdir}

%check
%make_build check

%ldconfig_scriptlets -n libconfig%{_soversion}
%ldconfig_scriptlets -n libconfig++%{_soversion}

%files -n libconfig%{_soversion}
%license COPYING*
%doc AUTHORS README
%{_libdir}/libconfig.so.*

%files -n libconfig++%{_soversion}
%license COPYING*
%{_libdir}/libconfig++.so.*

%files devel
%doc AUTHORS ChangeLog README TODO
%{_includedir}/libconfig*
%{_libdir}/libconfig.so
%{_libdir}/libconfig++.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/libconfig*
%{_libdir}/cmake/

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/libconfig.info%{ext_info}

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libconfig.info%{ext_info}

%changelog
