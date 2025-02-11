#
# spec file for package libcoap
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 3
# Can only have one. TODO: multibuild flavors
%bcond_without  openssl
%bcond_with gnutls
%bcond_without manpages
# TODO: docs contain the current date
%bcond_with docs
Name:           libcoap
Version:        4.3.5
Release:        0
Summary:        C-Implementation of CoAP
License:        BSD-2-Clause
URL:            https://libcoap.net/
Source:         https://github.com/obgm/libcoap/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if %{with manpages}
BuildRequires:  asciidoc
BuildRequires:  fdupes
%endif
%if %{with openssl}
BuildRequires:  pkgconfig(libcrypto)
%endif
%if %{with gnutls}
BuildRequires:  pkgconfig(gnutls)
%endif
%if %{with docs}
BuildRequires:  doxygen >= 1.7.0
# for dot
BuildRequires:  graphviz >= 2.26.0
%endif

%description
libcoap implements a lightweight application-protocol for devices that are
constrained their resources such as computing power, RF range, memory,
bandwith, or network packet sizes.

%package -n %{name}%{sover}-%{sover}
Summary:        C-Implementation of CoAP

%description -n %{name}%{sover}-%{sover}
libcoap implements a lightweight application-protocol for devices that are
constrained their resources such as computing power, RF range, memory,
bandwith, or network packet sizes.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover}-%{sover} = %{version}

%description devel
libcoap implements a lightweight application-protocol for devices that are
constrained their resources such as computing power, RF range, memory,
bandwith, or network packet sizes.

This package contains files required for building with %{name}.

%package utils
Summary:        C-Implementation of CoAP

%description utils
libcoap implements a lightweight application-protocol for devices that are
constrained their resources such as computing power, RF range, memory,
bandwith, or network packet sizes.

This package contains command line utilities.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--enable-dtls \
%if %{with openssl}
	--with-openssl \
%endif
%if %{with gnutls}
	--with-gnutls \
%endif
%if %{with manpages}
	--enable-manpages \
%else
	--disable-manpages \
%endif
%if %{with docs}
	--enable-doxygen \
%else
	--disable-doxygen \
%endif
	--docdir=%{_docdir}/%{name} \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
# remove static lib and symlink, note that spec-cleaner "fixes" f,l
find %{buildroot} -type f,l -name "*.la" -delete -print
find %{buildroot} -type f,l -name "*.a" -delete -print
# installed via %%license macro
rm %{buildroot}/%{_docdir}/%{name}/{COPYING,LICENSE}
# these are duplicates
rm %{buildroot}/%{_datadir}/%{name}/examples/{COPYING,LICENSE}
# keeo them together
mv %{buildroot}/%{_datadir}/%{name}/examples %{buildroot}/%{_docdir}/%{name}
#
%if %{with manpages}
%fdupes -s %{buildroot}/%{_mandir}
%endif

%ldconfig_scriptlets -n %{name}%{sover}-%{sover}

%files -n %{name}%{sover}-%{sover}
%license COPYING LICENSE
%if %{with openssl}
%{_libdir}/libcoap-%{sover}-openssl.so.%{sover}
%{_libdir}/libcoap-%{sover}-openssl.so.%{sover}.*
%endif
%if %{with gnutls}
%{_libdir}/libcoap-%{sover}-gnutls.so.%{sover}
%{_libdir}/libcoap-%{sover}-gnutls.so.%{sover}.*
%endif

%files devel
%license COPYING LICENSE
%{_docdir}/libcoap/
%{_includedir}/coap3
%{_libdir}/libcoap-3.so
%if %{with openssl}
%{_libdir}/libcoap-3-openssl.so
%endif
%if %{with gnutls}
%{_libdir}/libcoap-3-gnutls.so
%endif
%{_libdir}/pkgconfig/*.pc
%if %{with manpages}
%{_mandir}/man3/*.3%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}
%endif

%files utils
%license COPYING LICENSE
%{_bindir}/coap-client
%{_bindir}/coap-rd
%{_bindir}/coap-server
%if %{with openssl}
%{_bindir}/coap-client-openssl
%{_bindir}/coap-rd-openssl
%{_bindir}/coap-server-openssl
%endif
%if %{with gnutls}
%{_bindir}/coap-client-gnutls
%{_bindir}/coap-rd-gnutls
%{_bindir}/coap-server-gnutls
%endif
%if %{with manpages}
%{_mandir}/man5/*.5%{?ext_man}
%endif

%changelog
