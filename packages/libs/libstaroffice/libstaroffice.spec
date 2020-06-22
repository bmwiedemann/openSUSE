#
# spec file for package libstaroffice
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libstaroffice-0_0-0
Name:           libstaroffice
Version:        0.0.7
Release:        0
Summary:        A library for import of StarOffice documents
License:        LGPL-2.1-or-later AND MPL-2.0+
URL:            https://github.com/fosnola/libstaroffice/wiki
Source:         https://github.com/fosnola/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(zlib)

%description
%{name} is a library for import of StarOffice documents.

%package -n %{libname}
Summary:        A library for import of StarOffice documents

%description -n %{libname}
%{name} is a library for import of StarOffice documents.

%package devel
Summary:        A library for import of StarOffice documents
Requires:       %{libname} = %{version}
Requires:       libstdc++-devel

%description devel
%{name} is a library for import of StarOffice documents.

%package devel-doc
Summary:        Documentation for the libstaroffice API
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libstaroffice API.

%package tools
Summary:        Tools to work with documents in StarOffice formats

%description tools
This package contains tools to work with documents in StarOffice file-format.

%prep
%setup -q
# fix date in documentation
sed -i \
    -e 's/on $datetime //g' \
    docs/doxygen/footer.html.in

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}-devel/html \
	--with-sharedptr=c++11

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*
%doc ChangeLog
%license COPYING.LGPL
%license COPYING.MPL
%doc NEWS

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libstaroffice*.pc
%{_includedir}/libstaroffice*

%files devel-doc
%dir %{_docdir}/%{name}-devel
%doc %{_docdir}/%{name}-devel/html/

%files tools
%{_bindir}/sd2raw
%{_bindir}/sd2svg
%{_bindir}/sd2text
%{_bindir}/sdc2csv
%{_bindir}/sdw2html

%changelog
