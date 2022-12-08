#
# spec file for package utf8proc
#
# Copyright (c) 2022 SUSE LLC
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


%define lib_ver 2
Name:           utf8proc
Version:        2.8.0
Release:        0
Summary:        Library for processing UTF-8 encoded Unicode strings
License:        MIT
Group:          System/Libraries
URL:            https://julialang.org/utf8proc/
Source:         https://github.com/JuliaStrings/utf8proc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
utf8proc is a library for processing UTF-8 encoded Unicode strings.
Some features are Unicode normalization, stripping of default ignorable
characters, case folding and detection of grapheme cluster boundaries.
A special character mapping is available, which converts for example
the characters “Hyphen” (U+2010), “Minus” (U+2212) and “Hyphen-Minus
(U+002D, ASCII Minus) all into the ASCII minus sign, to make them
equal for comparisons.

%package     -n lib%{name}%{lib_ver}
Summary:        Library for processing UTF-8 encoded Unicode strings
Group:          System/Libraries

%description -n lib%{name}%{lib_ver}
utf8proc is a library for processing UTF-8 encoded Unicode strings.
Some features are Unicode normalization, stripping of default ignorable
characters, case folding and detection of grapheme cluster boundaries.
A special character mapping is available, which converts for example
the characters “Hyphen” (U+2010), “Minus” (U+2212) and “Hyphen-Minus
(U+002D, ASCII Minus) all into the ASCII minus sign, to make them
equal for comparisons.

%package        devel
Summary:        Library for processing UTF-8 encoded Unicode strings
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{lib_ver} = %{version}

%description    devel
utf8proc is a library for processing UTF-8 encoded Unicode strings.
Some features are Unicode normalization, stripping of default ignorable
characters, case folding and detection of grapheme cluster boundaries.
A special character mapping is available, which converts for example
the characters “Hyphen” (U+2010), “Minus” (U+2212) and “Hyphen-Minus
(U+002D, ASCII Minus) all into the ASCII minus sign, to make them
equal for comparisons.

This package provides libraries and header files for developing applications
that use utf8proc.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build

%install
make %{?_smp_mflags} \
	DESTDIR=%{buildroot} \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	install
find %{buildroot}/%{_libdir} -type f -name "*.a" -print -delete

%post -n lib%{name}%{lib_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{lib_ver} -p /sbin/ldconfig

%files -n lib%{name}%{lib_ver}
%license LICENSE.md
%doc lump.md NEWS.md README.md
%{_libdir}/libutf8proc.so.*

%files devel
%{_includedir}/utf8proc.h
%{_libdir}/libutf8proc.so
%{_libdir}/pkgconfig/libutf8proc.pc

%changelog
