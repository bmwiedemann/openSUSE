#
# spec file for package snowball
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


%define library_name libstemmer0d

Name:           snowball
Version:        2.1.0
Release:        0
Summary:        Snowball compiler and stemming algorithms
License:        BSD-3-Clause
URL:            https://snowballstem.org
Source:         https://github.com/snowballstem/snowball/archive/v%{version}.tar.gz#/snowball-%{version}.tar.gz
Source1:        libstemmer.ver
Patch0:         build-options.diff
Patch1:         shared-library.diff
Patch2:         python-dist.diff
Provides:       libstemmer-tools = %{version}-%{release}

%description
Snowball is a small string processing language for creating stemming algorithms
for use in Information Retrieval, plus a collection of stemming algorithms
implemented using it.

Snowball was originally designed and built by Martin Porter. Martin retired
from development in 2014 and Snowball is now maintained as a community project.
Martin originally chose the name Snowball as a tribute to SNOBOL, the excellent
string handling language from the 1960s. It now also serves as a metaphor for
how the project grows by gathering contributions over time.

The Snowball compiler translates a Snowball program into source code in another
language - currently ISO C, C#, Go, Java, Javascript, Object Pascal, Python and
Rust are supported.

%package -n %{library_name}
Summary:        Shared library for libstemmer

%description -n  %{library_name}
Snowball is a small string processing language for creating stemming algorithms
for use in Information Retrieval, plus a collection of stemming algorithms
implemented using it.

Snowball was originally designed and built by Martin Porter. Martin retired
from development in 2014 and Snowball is now maintained as a community project.
Martin originally chose the name Snowball as a tribute to SNOBOL, the excellent
string handling language from the 1960s. It now also serves as a metaphor for
how the project grows by gathering contributions over time.

The Snowball compiler translates a Snowball program into source code in another
language - currently ISO C, C#, Go, Java, Javascript, Object Pascal, Python and
Rust are supported.

This package holds the shared library for libstemmer.

%package devel
Summary:        Development files libstemmer
Requires:       %{library_name} = %{version}
Provides:       libstemmer-devel = %{version}-%{release}

%description devel
Snowball is a small string processing language for creating stemming algorithms
for use in Information Retrieval, plus a collection of stemming algorithms
implemented using it.

Snowball was originally designed and built by Martin Porter. Martin retired
from development in 2014 and Snowball is now maintained as a community project.
Martin originally chose the name Snowball as a tribute to SNOBOL, the excellent
string handling language from the 1960s. It now also serves as a metaphor for
how the project grows by gathering contributions over time.

The Snowball compiler translates a Snowball program into source code in another
language - currently ISO C, C#, Go, Java, Javascript, Object Pascal, Python and
Rust are supported.

This package holds the development files for libstemmer.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}"

%install
install -D -m 0755 -d                   %{buildroot}%{_libdir}
cp -a              libstemmer.so*       %{buildroot}%{_libdir}
install -D -m 0644 include/libstemmer.h %{buildroot}%{_includedir}/libstemmer.h
install -D -m 0755 stemwords            %{buildroot}%{_bindir}/stemwords

%post   -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS CONTRIBUTING.rst NEWS
%doc doc/libstemmer_c_README
%{_bindir}/stemwords

%files -n %{library_name}
%license COPYING
%{_libdir}/libstemmer.so.*

%files devel
%license COPYING
%doc AUTHORS CONTRIBUTING.rst NEWS
%doc doc/libstemmer_c_README
%{_includedir}/libstemmer.h
%{_libdir}/libstemmer.so

%changelog
