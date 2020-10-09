#
# spec file for package jpcre2
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


Name:           jpcre2
Version:        10.32.01
Release:        0
Summary:        C++ wrapper for the PCRE2 library (header only)
License:        BSD-3-Clause AND SUSE-Public-Domain
URL:            https://github.com/jpcre2/jpcre2
Source0:        https://github.com/jpcre2/jpcre2/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libpcre2-posix)

%description
C++ wrapper for PCRE2 library (header only).
Provides some C++ wrapper classes/functions to perform regex operations
such as regex match and regex replace.

%package        devel
Summary:        C++ wrapper for the PCRE2 library (header only)
BuildRequires:  pkgconfig(libpcre2-posix)

%description    devel
C++ wrapper for PCRE2 library (header only).
Provides some C++ wrapper classes/functions to perform regex operations
such as regex match and regex replace.

%prep
%autosetup

%build
autoreconf -fiv
%configure \
  --disable-silent-rules \
  --docdir=%{_defaultdocdir}/%{name}-devel
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_defaultdocdir}/%{name}-devel/COPYING

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_includedir}/jpcre2.hpp

%changelog
