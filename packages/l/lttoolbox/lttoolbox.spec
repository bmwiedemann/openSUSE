#
# spec file for package lttoolbox
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


Name:           lttoolbox
%define lname   liblttoolbox3
Summary:        Toolbox for lexical processing and morphological analysis
Version:        3.7.1
Release:        0
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://apertium.org/

Source:         https://github.com/apertium/lttoolbox/archive/v%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  utfcpp-devel
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libxml-2.0)

%description
lttoolbox is a toolbox for lexical processing, morphological analysis
and generation of words. Analysis is the process of splitting a word
(e.g. cats) into its lemma 'cat' and the grammatical information
<neutrum,plural>. Generation is the opposite process.

The package provides three programs, lt-comp, the compiler,
lt-proc, the processor, and lt-expand, which generates all possible
mappings between surface forms and lexical forms in the dictionary.

%package -n %lname
Summary:        Library for lexical processing and morphological analysis
Group:          System/Libraries

%description -n %lname
lttoolbox is a toolbox for lexical processing, morphological analysis
and generation of words. Analysis is the process of splitting a word
(e.g. cats) into its lemma 'cat' and the grammatical information
<neutrum,plural>. Generation is the opposite process.

%package devel
Summary:        Development files for the Lexical Toolbox
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
lttoolbox is a toolbox for lexical processing, morphological analysis
and generation of words. Analysis is the process of splitting a word
(e.g. cats) into its lemma 'cat' and the grammatical information
<neutrum,plural>. Generation is the opposite process.

This subpackage contains the development files for lttoolbox.

%prep
%autosetup -p1

%build
autoreconf -fiv
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --disable-static --includedir="%_includedir/%name" CPPFLAGS="-I%_includedir/utf8cpp"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/lt-*
%_bindir/lsx-*
%_datadir/lttoolbox
%_mandir/man1/lsx-*.1*
%_mandir/man1/lt-*.1*
%doc README
%license COPYING

%files -n %lname
%_libdir/liblttoolbox.so.*

%files devel
%_includedir/%name/
%_libdir/liblttoolbox.so
%_libdir/pkgconfig/*.pc

%changelog
