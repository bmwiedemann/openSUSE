#
# spec file for package libmwaw
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


%define libname libmwaw-0_3-3
Name:           libmwaw
Version:        0.3.16
Release:        0
Summary:        Pre Mac OSX text file formats parser library
License:        (LGPL-2.1-or-later OR MPL-2.0) AND GPL-2.0-or-later
URL:            https://sourceforge.net/p/libmwaw/wiki/Home/
Source:         http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
Libmwaw is a project for converting many pre-OSX MAC text formats.

%package -n %{libname}
Summary:        Pre Mac OSX text file formats parser library

%description -n %{libname}
Libmwaw is a new project for converting many pre-OSX MAC text formats.

%package devel
Summary:        Files for Developing with libmwaw
Requires:       %{libname} = %{version}

%description devel
Libmwaw is a new project for converting many pre-OSX MAC text formats.
This package contains the libmwaw development files.

%package devel-doc
Summary:        Documentation for the libmwaw API
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libmwaw API.

%package tools
Summary:        Tools to work with publications in pre MAC OSX text file-formats

%description tools
Command line tools to work with publications in pre MAC OSX text file-formats.

%prep
%setup -q
# doxygen needles rebuild
sed -i \
	-e 's:on $datetime::g' \
	docs/doxygen/footer.html.in

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p COPYING.* %{buildroot}%{_docdir}/%{name}
# docs have duped pictures
%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmwaw*.pc
%{_includedir}/libmwaw-*

%files devel-doc
%doc %{_docdir}/%{name}/html

%files tools
%{_bindir}/*
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/[A-Z]*

%changelog
