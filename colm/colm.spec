#
# spec file for package colm
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           colm
Version:        0.13.0.6
Release:        0
%define lname	libcolm-0_13_0_6
Summary:        The Colm programming language
License:        MIT
Group:          Development/Languages/Other
Url:            http://www.colm.net/open-source/colm/

Source:         http://www.colm.net/files/colm/%name-%version.tar.gz
Patch1:         shadow.diff
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Colm is a programming language designed for the analysis and
transformation of computer languages.

%package -n %lname
Summary:        The Colm programming language runtime
Group:          System/Libraries

%description -n %lname
Colm is a programming language designed for the analysis and
transformation of computer languages.

%package devel
Summary:        The Colm programming language environment
Group:          Development/Languages/Other
Requires:       %lname = %version
Requires:       gcc
Provides:       colm = %version-%release

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

%description doc
Colm is a programming language designed for the analysis and
transformation of computer languages.

This subpackage contains the documentation in HTML format.

%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fi
%configure --disable-static --docdir="%_docdir/%name"
make %{?_smp_mflags} V=1

%install
%make_install
b="%buildroot"
c="$b/%_datadir/vim/site/syntax"
mkdir -p "$c"
mv "$b/%_docdir/%name"/*.vim "$c/"
rm -f "$b/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libcolm*-0.13*.so

%files devel
%defattr(-,root,root)
%doc COPYING
%_bindir/colm
%_includedir/*
%_libdir/libcolm.so
%_datadir/vim/

%files doc
%defattr(-,root,root)
%_docdir/%name/

%changelog
