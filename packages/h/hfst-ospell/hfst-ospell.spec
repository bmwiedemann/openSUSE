#
# spec file for package hfst-ospell
#
# Copyright (c) 2024 SUSE LLC
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


%define _name hfst-ospell
%define libname libhfstospell11
Name:           hfst-ospell
Version:        0.5.4
Release:        0
Summary:        Spell checker library and tool based on HFST
License:        Apache-2.0
Group:          Productivity/Text/Spell
URL:            https://hfst.github.io/
Source0:        https://github.com/hfst/%{name}/releases/download/v%{version}/%{_name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libarchive)

%description
Minimal HFST optimized lookup format based spell checker library and
a demonstrational implementation of command line based spell checker.

%package -n %{libname}
Summary:        HFST spell checker runtime libraries
Group:          System/Libraries
Provides:       libhfstospell = %{version}-%{release}
Obsoletes:      libhfstospell < %{version}-%{release}

%description -n %{libname}
HFST spell checker Runtime libraries for hfst-ospell

%package -n hfst-ospell-devel
Summary:        HFST spell checker development files
Group:          Development/Libraries/C and C++
Requires:       hfst-ospell = %{version}-%{release}

%description -n hfst-ospell-devel
Development headers and libraries for hfst-ospell

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
# disable libxml++ as upstream requires version 2.6
# disable tinyxml2 as upstream requires version < 3.0
export CXXFLAGS="%{optflags} -DU_USING_ICU_NAMESPACE=1"
NO_CONFIGURE=1 ./autogen.sh
%configure \
    --disable-static \
    --disable-silent-rules \
    --without-libxmlpp \
    --without-tinyxml2
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc AUTHORS NEWS
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%license COPYING
%{_libdir}/*.so.*

%files -n hfst-ospell-devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

%changelog
