#
# spec file for package colm
#
# Copyright (c) 2021 SUSE LLC
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


%define sonum 0_14_7
Name:           colm
Version:        0.14.7
Release:        0
Summary:        The Colm programming language
License:        MIT
Group:          Development/Languages/Other
URL:            https://www.colm.net/open-source/colm/
#Git-Clone:     https://github.com/adrian-thurston/colm
Source:         https://www.colm.net/files/colm/%name-%version.tar.gz
Patch1:         fix-library.patch
Patch2:         reproducible.diff
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Colm is a programming language designed for the analysis and
transformation of computer languages.

%package -n libcolm-%sonum
Summary:        The Colm programming language runtime
Group:          System/Libraries

%description -n libcolm-%sonum
Colm is a programming language designed for the analysis and
transformation of computer languages.

%package -n libfsm-%sonum
Summary:        The Colm programming language runtime
Group:          System/Libraries

%description -n libfsm-%sonum
Colm is a programming language designed for the analysis and
transformation of computer languages.

%package devel
Summary:        The Colm programming language environment
Group:          Development/Languages/Other
Requires:       gcc
Requires:       libcolm-%sonum = %version-%release
Requires:       libfsm-%sonum = %version-%release
Obsoletes:      ragel-devel
Provides:       ragel-devel

%description devel
Colm is a programming language designed for the analysis and
transformation of computer languages. It has a type system based on
formal languages. Rather than define classes or data structures, one
defines grammars. A parser is constructed automatically from the
grammar, and the parser is used for two purposes: to parse the input
language, and to parse the structural patterns in the program that
performs the analysis.

%package doc
Summary:        Documentation for the Colm programming language
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Colm is a programming language designed for the analysis and
transformation of computer languages.

This subpackage contains the documentation in HTML format.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --docdir="%_docdir/%name" \
	--datadir="%_datadir/%name"
%make_build

%install
%make_install
b="%buildroot"
c="$b/%_datadir/vim/site/syntax"
mkdir -p "$c"
mv "$b/%_docdir/%name"/*.vim "$c/"
rm -fv "$b/%_libdir"/*.la

%post   -n libcolm-%sonum -p /sbin/ldconfig
%postun -n libcolm-%sonum -p /sbin/ldconfig
%post   -n libfsm-%sonum -p /sbin/ldconfig
%postun -n libfsm-%sonum -p /sbin/ldconfig

%files -n libcolm-%sonum
%license COPYING
%_libdir/libcolm*-0.14*.so

%files -n libfsm-%sonum
%_libdir/libfsm-0.14*.so

%files devel
%_bindir/colm
%_bindir/colm-wrap
%_includedir/*
%_libdir/libcolm.so
%_libdir/libfsm.so
%_datadir/%name/
%_datadir/vim/

%files doc
%_docdir/%name/

%changelog
