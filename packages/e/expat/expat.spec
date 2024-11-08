#
# spec file for package expat
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global unversion 2_6_4
%define sover 1
Name:           expat
Version:        2.6.4
Release:        0
Summary:        XML Parser Toolkit
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://libexpat.github.io
Source0:        https://github.com/libexpat/libexpat/releases/download/R_%{unversion}/expat-%{version}.tar.xz
Source1:        https://github.com/libexpat/libexpat/releases/download/R_%{unversion}/expat-%{version}.tar.xz.asc
Source2:        baselibs.conf
Source3:        %{name}faq.html
# https://www.gentoo.org/inside-gentoo/developers/index.html#sping
# https://github.com/libexpat/libexpat/issues/537#issuecomment-1003796884
Source4:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3176ef7db2367f1fca4f306b1f9b0e909af37285#/expat.keyring
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig

%description
Expat is an XML parser library written in C. It is a stream-oriented
parser in which an application registers handlers for things the
parser might find in the XML document (like start tags).

%package -n libexpat%{sover}
Summary:        XML Parser Toolkit
Group:          System/Libraries

%description -n libexpat%{sover}
Expat is an XML parser library written in C. It is a stream-oriented
parser in which an application registers handlers for things the
parser might find in the XML document (like start tags).

%package -n libexpat-devel
Summary:        Development files for expat, an XML parser toolkit
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libexpat%{sover} = %{version}

%description -n libexpat-devel
Expat is an XML parser library written in C. It is a stream-oriented
parser in which an application registers handlers for things the
parser might find in the XML document (like start tags).

This package contains the development headers for the library found
in libexpat.

%prep
%autosetup -p1
cp %{SOURCE3} .

%build
%configure \
  --disable-silent-rules \
  --docdir="%{_docdir}/%{name}" \
  --disable-static \
  --without-docbook

%if 0%{?do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}" LDFLAGS="%{optflags} %{cflags_profile_generate}"
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}" LDFLAGS="%{optflags} %{cflags_profile_generate}" check
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CFLAGS="%{optflags}"
%endif

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libexpat%{sover}

%files
%license COPYING
%doc AUTHORS README.md expatfaq.html
%doc doc/reference.html doc/*.css
%doc examples/*.c examples/Makefile.am examples/Makefile.in
%doc changelog
%{_bindir}/xmlwf
%{_mandir}/man1/xmlwf.1%{?ext_man}

%files -n libexpat1
%license COPYING
%{_libdir}/libexpat.so.%{sover}
%{_libdir}/libexpat.so.%{sover}.*

%files -n libexpat-devel
%license COPYING
%{_includedir}/*
%{_libdir}/libexpat.so
%{_libdir}/pkgconfig/expat.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/expat-%{version}

%changelog
