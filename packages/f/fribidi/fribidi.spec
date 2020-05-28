#
# spec file for package fribidi
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


%define lname   libfribidi0
Name:           fribidi
Version:        1.0.5
Release:        0
Summary:        An implementation of the Unicode BiDi algorithm
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/fribidi/fribidi
Source:         https://github.com/fribidi/fribidi/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM no-config-h.diff - copied from Debian
Patch1:         no-config-h.diff
# PATCH-FIX-UPSTREAM Truncate-isolate_level-to-FRIBIDI_BIDI_MAX_EXPLICIT_.diff - copied from Debian
Patch2:         Truncate-isolate_level-to-FRIBIDI_BIDI_MAX_EXPLICIT_.diff
BuildRequires:  pkgconfig
#
Provides:       locale(ar;he)
# bug437293
%ifarch ppc64
Obsoletes:      fribidi-64bit
%endif

%description
This library implements the algorithm as described in "Unicode
Standard Annex #9, the Bidirectional Algorithm".

%package -n %{lname}
Summary:        An implementation of the Unicode BiDi algorithm
Group:          System/Libraries

%description -n %{lname}
This library implements the algorithm as described in "Unicode
Standard Annex #9, the Bidirectional Algorithm,
http://www.unicode.org/unicode/reports/tr9/". FriBidi is
tested against the Bidi Reference Code and, to the best of the
developers' knowledge, does not contain any conformance bugs.

The API was inspired by the document "Bi-Di languages support - BiDi
API proposal" by Franck Portaneri, which he wrote as a proposal for
adding BiDi support to Mozilla.

%package devel
Summary:        Development Files for FriBiDi
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package provides headers and manual files for FriBiDi.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc NEWS README
%{_bindir}/fribidi

%files -n %{lname}
%license COPYING
%{_libdir}/libfribidi.so.0*

%files devel
%doc AUTHORS ChangeLog THANKS TODO
%{_mandir}/man3/fribidi_*
%{_includedir}/fribidi/
%{_libdir}/libfribidi.so
%{_libdir}/pkgconfig/fribidi.pc

%changelog
