#
# spec file for package libstaroffice
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname librvngabw-0_0-0
Name:           librvngabw
Version:        0.0.1
Release:        0
Summary:        An AbiWord document generator library
License:        LGPL-2.1+ and MPL-2.0+
Group:          Productivity/Publishing/Word
Url:            https://sourceforge.net/projects/librvngabw/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} is a library for generating AbiWord documents. It is directly
pluggable into import filters based on librevenge.


%package -n %{libname}
Summary:        An AbiWord document generator library
Group:          System/Libraries

%description -n %{libname}
%{name} is a library for generating AbiWord documents. It is directly
pluggable into import filters based on librevenge.


%package devel
Summary:        An AbiWord document generator library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
%{name} is a library for generating AbiWord documents. It is directly
pluggable into import filters based on librevenge.

%package devel-doc
Summary:        Documentation for the librvngabw API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the librvngabw API.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}-devel/html \
	--with-sharedptr=c++11
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc ChangeLog
%doc COPYING.LGPL
%doc COPYING.MPL
%doc NEWS

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/librvngabw*.pc
%{_includedir}/librvngabw*

%files devel-doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-devel
%doc %{_docdir}/%{name}-devel/html/

%changelog
