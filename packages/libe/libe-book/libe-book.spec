#
# spec file for package libe-book
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


Name:           libe-book
Version:        0.1.3
Release:        0
Summary:        A library to import non-HTML reflowable e-book formats
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            https://sourceforge.net/projects/libebook/
Source:         http://downloads.sourceforge.net/libebook/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(liblangtag)
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
%{name} is a library to import non-HTML reflowable e-book formats.
Currently supported are PalmDoc, TealDoc, Plucker eBook, eReader eBook,
FictionBook v.2, TCR, zTXT.

%define libname libe-book-0_1-1

%package -n %{libname}
Summary:        A library to import non-HTML reflowable e-book formats
Group:          System/Libraries

%description -n %{libname}
%{name} is a library to import non-HTML reflowable e-book formats.
Currently supported are PalmDoc, TealDoc, Plucker eBook, eReader eBook,
FictionBook v.2, TCR, zTXT.

%package devel
Summary:        A library to import non-HTML reflowable e-book formats
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libstdc++-devel

%description devel
%{name} is a library to import non-HTML reflowable e-book formats.
Currently supported are PalmDoc, TealDoc, Plucker eBook, eReader eBook,
FictionBook v.2, TCR, zTXT.

%package devel-doc
Summary:        Documentation for the libe-book API
Group:          Documentation/Other
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libe-book API.

%package tools
Summary:        Tools to transform e-books into other formats
Group:          Productivity/Publishing/Word

%description tools
Tools to transform e-books into other formats.
Currently supported: XHTML, raw, text.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-werror \
	--enable-tests \
	--disable-static \
	--docdir=%{_docdir}/%{name} \
	--disable-silent-rules
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_datadir}/%{name}/html*.css
%fdupes -s %{buildroot}%{_docdir}/%{name}/html

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%doc COPYING NEWS TODO ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/libe*.pc
%{_includedir}/libe*

%files devel-doc
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}

%files tools
%{_bindir}/*

%changelog
