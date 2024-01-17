#
# spec file for package libeot
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libeot0
Name:           libeot
Version:        0.01
Release:        0
Summary:        A library for parsing Embedded OpenType font files
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            https://github.com/umanwizard/libeot
Source:         http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package -n %{libname}
Summary:        A library for parsing Embedded OpenType font files
Group:          System/Libraries

%description -n %{libname}
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package devel
Summary:        A library for parsing Embedded OpenType font files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package tools
Summary:        Tools to transform EOT font files into other formats
Group:          Productivity/Publishing/Word

%description tools
Tools to transform EOT font files into other formats. Only TTF is
supported currently.

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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/libe*.pc
%{_includedir}/libe*

%files tools
%defattr(-,root,root)
%doc LICENSE PATENTS
%{_bindir}/*

%changelog
