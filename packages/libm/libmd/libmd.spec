#
# spec file for package libmd
#
# Copyright (c) 2023 SUSE LLC
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


%define sover   0
Name:           libmd
Version:        1.1.0
Release:        0
Summary:        Message digest functions from BSD systems
License:        BSD-2-Clause OR BSD-3-Clause OR ISC OR SUSE-Public-Domain
URL:            https://www.hadrons.org/software/libmd/
Source0:        https://archive.hadrons.org/software/libmd/libmd-%{version}.tar.xz
Source1:        https://archive.hadrons.org/software/libmd/libmd-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  pkgconfig

%description
The libmd library provides a few message digest ("hash") functions, as
found on various BSDs on a library with the same name and with a compatible
API.

%package -n %{name}%{sover}
Summary:        Provides message digest functions from BSD systems

%description -n %{name}%{sover}
The libmd library provides a few message digest ("hash") functions, as
found on various BSDs on a library with the same name and with a compatible
API.

Digests supported: MD2/4/5, RIPEMD160, SHA1, SHA2-256/384/512.

%package devel
Summary:        Provides message digest functions from BSD systems
Requires:       %{name}%{sover} = %{version}

%description devel
The libmd library provides a few message digest ("hash") functions, as
found on various BSDs on a library with the same name and with a compatible
API.

Digests supported: MD2/4/5, RIPEMD160, SHA1, SHA2-256/384/512.

%prep
%autosetup

%build
%configure \
  --disable-static \
  --disable-silent-rules
  %make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%{_libdir}/%{name}.so.%{sover}*

%files devel
%license COPYING
%doc ChangeLog README
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libmd.pc
%{_mandir}/man3/*.3%{?ext_man}
%{_mandir}/man7/libmd.7%{?ext_man}

%changelog
