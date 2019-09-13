#
# spec file for package ragel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ragel
Version:        7.0.0.12
Release:        0
Summary:        Finite state machine compiler
License:        MIT
Group:          Development/Tools/Other
URL:            https://www.colm.net/open-source/ragel/

#Git-Clone:	git://colm.net/ragel
Source:         https://www.colm.net/files/ragel/%name-%version.tar.gz
Source2:        %name.keyring
BuildRequires:  automake
BuildRequires:  colm = 0.13.0.7
BuildRequires:  gcc-c++
BuildRequires:  kelbt
BuildRequires:  libtool

%description
Ragel compiles finite state machines from regular languages into
executable C, C++, Objective-C, or D code. Ragel state machines can
not only recognize byte sequences as regular expression machines do,
but can also execute code at arbitrary points in the recognition of a
regular language. Code embedding is done using inline operators that
do not disrupt the regular language syntax.

%package -n libfsm0
Summary:        Library implementing a finite state machine
Group:          System/Libraries

%description -n libfsm0
libfsm is one of ragel's component libraries.
Ragel compiles finite state machines from regular languages into
executable C, C++, Objective-C, or D code.

%package -n libragel0
Summary:        Ragel parser support library
Group:          System/Libraries

%description -n libragel0
libragel contains the parse tree and other parsing support code -
everything except the reducers, which are specific to the frontends.

%package devel
Summary:        Development files for ragel, a finite state machine compiler library
Group:          Development/Libraries/C and C++
Requires:       libfsm0 = %version-%release

%description devel
Ragel compiles finite state machines from regular languages into
executable C, C++, Objective-C, or D code.
This package contains the C headers for libragel.

%prep
%autosetup -p1

%build
autoreconf -fiv
export CXXFLAGS="%optflags -Wno-narrowing"
# Banish terribly namespaced files into a separate dir
%configure --docdir="%_docdir/%name" --includedir="%_includedir/ragel" \
	--disable-static
make %{?_smp_mflags} V=1

%check
make check

%install
%make_install
b="%buildroot"
c="$b/%_datadir/vim/site/syntax"
mkdir -p "$c"
install -pm0644 ragel*.vim "$c/"
rm -Rf "%buildroot/%_libdir"/*.la

%post   -n libfsm0 -p /sbin/ldconfig
%postun -n libfsm0 -p /sbin/ldconfig
%post   -n libragel0 -p /sbin/ldconfig
%postun -n libragel0 -p /sbin/ldconfig

%files
%license COPYING
%doc %_docdir/%name
%_bindir/ragel*
%_mandir/man1/ragel.1*
%_datadir/vim/
%_datadir/ragel*

%files -n libfsm0
%_libdir/libfsm.so.0*

%files -n libragel0
%_libdir/libragel.so.0*

%files devel
%_libdir/*.so
%_includedir/ragel/

%changelog
