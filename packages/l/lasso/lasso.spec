#
# spec file for package lasso
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019 Red Hat, Inc., Raleigh, North Carolina, United States of America.
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%global with_wsf 0
# None of these extra bindings are working or wanted right now...
%global configure_args --disable-java --disable-perl --enable-php5=no
%global somajor 3
%global libname lib%{name}%{somajor}
%global devname lib%{name}-devel
%if %{with_wsf}
  %global configure_args %{configure_args} --enable-wsf --with-sasl2=%{_prefix}/sasl2
%endif
Name:           lasso
Version:        2.8.2
Release:        0
Summary:        Liberty Alliance Single Sign On
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://lasso.entrouvert.org/
Source:         https://dev.entrouvert.org/lasso/lasso-%{version}.tar.gz
# Backports from upstream (from Fedora)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
# The Lasso build system requires python, especially the binding generators
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-six
BuildRequires:  swig
BuildRequires:  pkgconfig(xmlsec1) >= 1.2.25
BuildRequires:  pkgconfig(xmlsec1-openssl) >= 1.2.25
BuildRequires:  pkgconfig(zlib)
%if %{with_wsf}
BuildRequires:  pkgconfig(cyrus-sasl)
%endif

%description
Lasso is a library that implements the Liberty Alliance Single Sign On
standards, including the SAML and SAML2 specifications. It allows to handle
the whole life-cycle of SAML based Federations, and provides bindings
for multiple languages.

%package -n %{libname}
Summary:        Lasso runtime libraries
Group:          System/Libraries

%description -n %{libname}
This package contains the runtime libraries for lasso (Liberty Alliance Single Sign On).

%package -n %{devname}
Summary:        Lasso development headers and documentation
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
This package contains the header files, static libraries and development
documentation for Lasso.

%package -n python3-%{name}
Summary:        Liberty Alliance Single Sign On (lasso) Python bindings
Group:          Development/Libraries/Python
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       python3

%description -n python3-%{name}
Python language bindings for the lasso (Liberty Alliance Single Sign On)
library.

%prep
%autosetup -p1

# Remove any python script shebang lines (unless they refer to python3)
sed -i -E -e '/^#![[:blank:]]*(\/usr\/bin\/env[[:blank:]]+python[^3]?\>)|(\/usr\/bin\/python[^3]?\>)/d' \
  `grep -r -l -E '^#![[:blank:]]*(%{_bindir}/python[^3]?)|(%{_bindir}/env[[:blank:]]+python[^3]?)' *`

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1550
# Try to fix build on Leap 15.1...
export LC_ALL="C.UTF-8"
export LANG="C.UTF-8"
%endif

./autogen.sh

%configure %{configure_args} --with-python=python3
%make_build CFLAGS="%{optflags}"

%check
%make_build check

%install
#install -m 755 -d %{buildroot}%{_datadir}/gtk-doc/html

make install exec_prefix=%{_prefix} DESTDIR=%{buildroot}
find %{buildroot} -type f -regex ".*\(.la\|.a\)" -delete -print

# Remove bogus doc files
rm -fr %{buildroot}%{_datadir}/doc/%{name}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/liblasso.so.%{somajor}*
%{_libdir}/liblasso.so.%{somajor}.*

%files -n %{devname}
%{_libdir}/liblasso.so
%{_libdir}/pkgconfig/lasso.pc
%{_includedir}/%{name}

%files -n python3-%{name}
%{python3_sitearch}/lasso.py*
%{python3_sitearch}/_lasso.so

%changelog
