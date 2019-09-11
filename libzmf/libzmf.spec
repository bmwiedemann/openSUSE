#
# spec file for package libzmf
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libzmf-0_0-0
Name:           libzmf
Version:        0.0.2
Release:        0
Summary:        A library for import of Zoner document formats
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            http://wiki.documentfoundation.org/DLP/Libraries/libzmf
Source:         http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
%{name} is a library for generating Zoner documents. It is directly
pluggable into import filters based on librevenge.

%package -n %{libname}
Summary:        An ZMF generator library
Group:          System/Libraries

%description -n %{libname}
%{name} is a library for generating Zoner documents. It is directly
pluggable into import filters based on librevenge.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
%{name} is a library for generating Zoner documents. It is directly
pluggable into import filters based on librevenge.

This package contains the %{name} development files.

%package devel-doc
Summary:        Documentation of %{name} API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary:        Tools for converting the Zoner ZMF files
Group:          Productivity/Publishing/Word

%description tools
Tools to work with the Zoner ZMF files, based on librevenge.

%prep
%setup -q

%build
%configure \
    --disable-werror \
    --disable-static \
    --docdir=%{_docdir}/%{name} \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p AUTHORS COPYING ChangeLog %{buildroot}%{_docdir}/%{name}

%fdupes -s %{buildroot}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make %{?_smp_mflags} check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/%{name}-*.so.*

%files devel
%{_includedir}/%{name}-*
%{_libdir}/%{name}-*.so
%{_libdir}/pkgconfig/%{name}-*.pc

%files devel-doc
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}

%files tools
%{_bindir}/*

%changelog
