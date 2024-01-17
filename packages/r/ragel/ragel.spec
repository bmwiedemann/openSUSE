#
# spec file for package ragel
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


Name:           ragel
Version:        7.0.4
Release:        0
Summary:        Finite state machine compiler
License:        MIT
Group:          Development/Tools/Other
URL:            https://www.colm.net/open-source/ragel/

#Git-Clone:	https://github.com/adrian-thurston/ragel
Source:         https://www.colm.net/files/ragel/%name-%version.tar.gz
Source2:        %name.keyring
Patch1:         paths.patch
BuildRequires:  automake
BuildRequires:  colm-devel = 0.14.7
BuildRequires:  gcc-c++
BuildRequires:  kelbt
BuildRequires:  libtool
Obsoletes:      libragel0 < %version-%release

%description
Ragel compiles finite state machines from regular languages into
executable C, C++, Objective-C, or D code. Ragel state machines can
not only recognize byte sequences as regular expression machines do,
but can also execute code at arbitrary points in the recognition of a
regular language. Code embedding is done using inline operators that
do not disrupt the regular language syntax.

%prep
%autosetup -p1

%build
autoreconf -fiv
export CXXFLAGS="%optflags -Wno-narrowing"
%configure --docdir="%_docdir/%name" --includedir="%_includedir/ragel" \
	--datadir="%_datadir" --disable-static --disable-manual
%make_build

%check
make check

%install
%make_install
b="%buildroot"
c="$b/%_datadir/vim/site/syntax"
mkdir -p "$c"
install -pm0644 ragel*.vim "$c/"
rm -Rf "$b/%_libdir"/*.la
# no headers available
rm -f "$b/%_libdir/libragel.so"

mkdir -p "$b/%_datadir/colm"
mv "$b/%_datadir"/*.lm "$b/%_datadir/colm/"

%files
%license COPYING
%doc %_docdir/%name
%_bindir/ragel*
%_mandir/man1/ragel.1*
%_datadir/vim/
%_datadir/colm/
%_libdir/libragel.so.0*

%changelog
