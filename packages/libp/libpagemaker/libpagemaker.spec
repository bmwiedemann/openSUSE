#
# spec file for package libpagemaker
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


%define libname libpagemaker-0_0-0
Name:           libpagemaker
Version:        0.0.4
Release:        0
Summary:        A library to import Adobe PageMaker documents
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            http://wiki.documentfoundation.org/DLP/Libraries/libpagemaker
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
libpagemaker is library providing ability to interpret and import
Adobe PageMaker documents into various applications.

%package -n %{libname}
Summary:        A library to import Adobe PageMaker documents
Group:          System/Libraries

%description -n %{libname}
libpagemaker is library providing ability to interpret and import
Adobe PageMaker documents into various applications.

%package devel
Summary:        Files for Developing with libpagemaker
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libpagemaker is library providing ability to interpret and import
Adobe PageMaker documents into various applications.

This package contains the libpagemaker development files.

%package devel-doc
Summary:        Documentation for the libpagemaker API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libpagemaker API.

%package tools
Summary:        Tools to transform Adobe PageMaker documents into other formats
Group:          Productivity/Publishing/Word

%description tools
Tools to transform Adobe PageMaker documents into other formats.
Currently supported: SVG, raw.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
    --disable-silent-rules \
    --disable-werror \
    --disable-static \
    --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p AUTHORS COPYING ChangeLog %{buildroot}%{_docdir}/%{name}

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc NEWS COPYING ChangeLog
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpagemaker*.pc
%{_includedir}/libpagemaker-*

%files devel-doc
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html

%files tools
%{_bindir}/*
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/[A-Z]*

%changelog
