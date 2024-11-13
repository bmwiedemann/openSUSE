#
# spec file for package opensaml
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


%define libvers 13
%define pkgdocdir %{_docdir}/%{name}
Name:           opensaml
Version:        3.3.0
Release:        0
Summary:        Security Assertion Markup Language library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://wiki.shibboleth.net/confluence/display/OpenSAML/
Source0:        https://shibboleth.net/downloads/c++-opensaml/%{version}/%{name}-%{version}.tar.bz2
Source1:        https://shibboleth.net/downloads/c++-opensaml/%{version}/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Patch0:         opensaml-2.5.5-doxygen_timestamp.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  liblog4shib-devel >= 1.0.4
BuildRequires:  libxerces-c-devel >= 3.2
BuildRequires:  libxml-security-c-devel >= 2.0.0
BuildRequires:  libxmltooling-devel >= 3.1.0
BuildRequires:  pkgconfig

%description
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

%package -n opensaml-bin
Summary:        Utilities for OpenSAML library
Group:          Development/Libraries/C and C++

%description -n opensaml-bin
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

This package contains the utility programs.

%package -n libsaml%{libvers}
Summary:        Security Assertion Markup Language library
Group:          System/Libraries
Provides:       opensaml = %{version}-%{release}
Obsoletes:      opensaml < %{version}-%{release}

%description -n libsaml%{libvers}
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

This package contains just the shared library.

%package -n libsaml-devel
Summary:        OpenSAML development Headers
Group:          Development/Libraries/C and C++
Requires:       liblog4shib-devel >= 1.0.4
Requires:       libsaml%{libvers} = %{version}-%{release}
Requires:       libxerces-c-devel >= 3.2
Requires:       libxml-security-c-devel >= 2.0.0
Requires:       libxmltooling-devel >= 3.1.0
Provides:       opensaml-devel = %{version}-%{release}
Obsoletes:      opensaml-devel < %{version}-%{release}

%description -n libsaml-devel
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

This package includes files needed for development with OpenSAML.

%package -n opensaml-schemas
Summary:        OpenSAML schemas and catalog
Group:          Development/Libraries/C and C++

%description -n opensaml-schemas
OpenSAML is an open source implementation of the OASIS Security Assertion
Markup Language Specification. It contains a set of open source C++ classes
that support the SAML 1.0, 1.1, and 2.0 specifications.

This package includes XML schemas and related files.

%prep
%autosetup -p1

%build
# The default C++ standard used in GCC-11 is C++17,
# which does not support opensaml codebase.
CXXFLAGS="-std=c++11 %{optflags}"
export CXXFLAGS
%configure
%make_build

%install
make install DESTDIR=%{buildroot} pkgdocdir=%{pkgdocdir}
# Don't package unit tester if present.
rm -f %{buildroot}/%{_bindir}/samltest
rm -f %{buildroot}/%{_libdir}/libsaml.la

%check
%make_build check

%post -n libsaml%{libvers} -p /sbin/ldconfig
%postun -n libsaml%{libvers} -p /sbin/ldconfig

%files -n opensaml-bin
%{_bindir}/samlsign

%files -n libsaml%{libvers}
%{_libdir}/libsaml.so.*

%files -n opensaml-schemas
%dir %{_datadir}/xml/opensaml
%{_datadir}/xml/opensaml/*

%files -n libsaml-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/opensaml.pc
%doc %{pkgdocdir}

%changelog
