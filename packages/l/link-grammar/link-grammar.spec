#
# spec file for package link-grammar
#
# Copyright (c) 2025 SUSE LLC
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


%define lname liblink-grammar5
Name:           link-grammar
Version:        5.12.5
Release:        0
Summary:        Syntactic parser and grammar checker
License:        LGPL-2.1-only
Group:          Productivity/Text/Spell
URL:            https://opencog.github.io/link-grammar-website/
Source:         https://www.gnucash.org/link-grammar/downloads/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc

BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  minisat-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Obsoletes:      perl-clinkgrammar < 5.4.3

%description
The Link Grammar Parser is a syntactic parser of English, Russian, Arabic
and Persian (and other languages as well), based on Link Grammar, an
original theory of syntax and morphology. Given a sentence, the system
assigns to it a syntactic structure, which consists of a set of labelled
links connecting pairs of words.

This package contains Link Grammar's utility, its shared library and
some data files.

%package -n %{lname}
Summary:        An English grammar checker
Group:          System/Libraries

%description -n %{lname}
The Link Grammar Parser is a syntactic parser of a number of
languages, based on Link Grammar, an original theory of syntax and
morphology.

%package devel
Summary:        Development files for link-grammar, an English grammar checker
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The Link Grammar Parser is a syntactic parser of a number of
languages, based on Link Grammar, an original theory of syntax and
morphology.

This package contains the development files for development with
Link Grammar.

%prep
%autosetup

%build
%configure \
    --disable-static \
    --disable-python-bindings \
    --disable-java-bindings
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f "(" -name "*.a" -o -name "*.la" ")" -delete -print
find %{buildroot} ! -type d -size 0 -delete
%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets -n %{lname}

%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/*
%{_datadir}/link-grammar
%{_mandir}/man1/link-parser.1%{?ext_man}
%{_mandir}/man1/link-generator.1%{?ext_man}

%files -n %{lname}
%{_libdir}/*.so.*

%files devel
%doc AUTHORS MAINTAINERS
%dir %{_includedir}/link-grammar
%{_includedir}/link-grammar/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
