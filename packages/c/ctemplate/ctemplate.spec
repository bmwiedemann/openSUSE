#
# spec file for package ctemplate
#
# Copyright (c) 2021 SUSE LLC
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


%define sover   3
%define libname lib%{name}%{sover}
Name:           ctemplate
Version:        2.4
Release:        0
Summary:        Library for a C++ templating language
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/OlafvdSpek/ctemplate
Source:         https://github.com/OlafvdSpek/ctemplate/archive/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CTemplate is a template language for C++. It emphasizes separating
logic from presentation: it is impossible to embed application logic
in this template language.

%package -n %{libname}
Summary:        Library for a C++ template languaging
Group:          Development/Libraries/C and C++

%description -n %{libname}
CTemplate is a template language for C++. It emphasizes separating
logic from presentation: it is impossible to embed application logic
in this template language.

%package -n libctemplate-devel
Summary:        Development files for ctemplate, a C++ language templating library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n libctemplate-devel
CTemplate is a template language for C++. It emphasizes separating
logic from presentation: it is impossible to embed application logic
in this template language.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
./autogen.sh
%configure \
  --disable-static \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# remove not needed documentation
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
make check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{_libdir}/libctemplate.so.%{sover}*
%{_libdir}/libctemplate_nothreads.so.%{sover}*

%files -n libctemplate-devel
%defattr(-,root,root)
%doc doc/*.html ChangeLog AUTHORS
%license COPYING
%{_bindir}/diff_tpl_auto_escape
%{_bindir}/make_tpl_varnames_h
%{_bindir}/template-converter
%dir %{_includedir}/ctemplate
%{_includedir}/ctemplate/*.h
%{_libdir}/libctemplate.so
%{_libdir}/libctemplate_nothreads.so
%{_libdir}/pkgconfig/libctemplate.pc
%{_libdir}/pkgconfig/libctemplate_nothreads.pc

%changelog
