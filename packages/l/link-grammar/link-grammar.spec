#
# spec file for package link-grammar
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define lname liblink-grammar5
Name:           link-grammar
Version:        5.5.0
Release:        0
Summary:        Syntactic parser and grammar checker
License:        LGPL-2.1-only
Group:          Productivity/Text/Spell
URL:            http://www.abisource.com/projects/link-grammar/
Source:         http://www.abisource.com/downloads/link-grammar/5.5.0/%{name}-%{version}.tar.gz
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  hunspell-devel
BuildRequires:  libedit-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python3-devel
Obsoletes:      perl-clinkgrammar < 5.4.3

%description
The Link Grammar Parser is a syntactic parser of English, Russian, Arabic
and Persian (and other languages as well), based on Link Grammar, an
original theory of syntax and morphology. Given a sentence, the system
assigns to it a syntactic structure, which consists of a set of labelled
links connecting pairs of words.

This package contains Link Grammar's utility, its shared library and
some data files.

%package -n  python2-clinkgrammar
Summary:        Python 2 bindings for link-grammar, a grammar checker
Group:          Development/Libraries/Python

%description -n  python2-clinkgrammar
The Link Grammar Parser is a syntactic parser of a number of
languages, based on Link Grammar, an original theory of syntax and
morphology.

This package contains bindings for development with Link Grammar using
Python 2.

%package -n  python3-clinkgrammar
Summary:        Python 3 bindings for link-grammar, a grammar checker
Group:          Development/Libraries/Python

%description -n  python3-clinkgrammar
The Link Grammar Parser is a syntactic parser of a number of
languages, based on Link Grammar, an original theory of syntax and
morphology.

This package contains bindings for development with Link Grammar using
Python 3.

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
%setup -q

%build
# --enable-sat-solver and --enable-corpus-stats are still at the prototype stage
%configure \
    --disable-static \
    --disable-java-bindings
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f "(" -name "*.a" -o -name "*.la" ")" -delete -print
find %{buildroot} ! -type d -size 0 -delete
%fdupes %{buildroot}%{_prefix}

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/*
%{_datadir}/link-grammar
%{_mandir}/man1/link-parser.1%{?ext_man}

%files -n python2-clinkgrammar
%{python_sitelib}/linkgrammar

%files -n python3-clinkgrammar
%{python3_sitelib}/linkgrammar.pth
%{python3_sitelib}/linkgrammar

%files -n %{lname}
%{_libdir}/*.so.*

%files devel
%doc AUTHORS ChangeLog MAINTAINERS
%dir %{_includedir}/link-grammar
%{_includedir}/link-grammar/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
