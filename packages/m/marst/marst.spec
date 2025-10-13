#
# spec file for package marst
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


%define sover 0
Name:           marst
Version:        2.8
Release:        0
Summary:        Algol-to-C translator
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/marst/
Source:         https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz.sig
# https://savannah.gnu.org/users/mao
Source3:        %{name}.keyring

%description
MARST is an Algol-to-C translator. It automatically translates programs written
on the algorithmic language Algol 60 to the C programming language.

%package -n libalgol%{sover}
Summary:        Shared libraries for marst, an Algol-to-C translator

%description -n libalgol%{sover}
MARST is an Algol-to-C translator. It automatically translates programs written
on the algorithmic language Algol 60 to the C programming language.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}, an Algol-to-C translator
Requires:       libalgol%{sover} = %{version}

%description devel
MARST is an Algol-to-C translator. It automatically translates programs written
on the algorithmic language Algol 60 to the C programming language.

This package contains the files needed to develop using %{name}.

%prep
%autosetup -p1
chmod -x AUTHORS ChangeLog NEWS README COPYING

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# we would normally build with --disable-static, but this breaks tests
find %{buildroot} -type f -name "*.a" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n libalgol%{sover}

%files
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{_bindir}/macvt
%{_bindir}/marst

%files -n libalgol%{sover}
%license COPYING
%{_libdir}/libalgol.so.%{sover}{,.*}

%files devel
%license COPYING
%{_includedir}/algol.h
%{_libdir}/libalgol.so

%changelog
