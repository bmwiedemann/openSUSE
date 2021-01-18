#
# spec file for package nuspell
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


%define sonum   4
%define libname libnuspell
Name:           nuspell
Version:        4.2.0
Release:        0
Summary:        A spell checker library and command-line tool
License:        LGPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://nuspell.github.io/
Source:         https://github.com/nuspell/nuspell/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Catch2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  rubygem(%{rb_default_ruby_abi}:ronn)
Requires:       hunspell

%description
Nuspell is a spell checker written in C++. It supports languages with
rich morphology and complex word compounding.

Main features are:
 - Full unicode support backed by ICU
 - Backward compatibility with Hunspell dictionary file format
 - Twofold affix stripping (for agglutinative languages, like Azeri,
   Basque, Estonian, Finnish, Hungarian, Turkish, etc.)
 - Support complex compounds (for example, Hungarian, Germand and Dutch)
 - Support language specific features (for example, special casing of
   Azeri and Turkish dotted i, or German sharp s)
 - Handle conditional affixes, circumfixes, fogemorphemes, forbidden
   words, pseudoroots and homonyms.

%package -n %{libname}%{sonum}
Summary:        A spell checker library and command-line tool
Group:          System/Libraries

%description -n %{libname}%{sonum}
Nuspell is a spell checker written in C++. It supports languages with
rich morphology and complex word compounding.

Main features are:
 - Full unicode support backed by ICU
 - Backward compatibility with Hunspell dictionary file format
 - Twofold affix stripping (for agglutinative languages, like Azeri,
   Basque, Estonian, Finnish, Hungarian, Turkish, etc.)
 - Support complex compounds (for example, Hungarian, Germand and Dutch)
 - Support language specific features (for example, special casing of
   Azeri and Turkish dotted i, or German sharp s)
 - Handle conditional affixes, circumfixes, fogemorphemes, forbidden
   words, pseudoroots and homonyms.

%package devel
Summary:        Files for developing with Nuspell
Group:          Development/Libraries/C and C++
Requires:       nuspell = %{version}-%{release}

%description devel
Header files and definitions for developing with Nuspell.

%prep
%autosetup

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON \
       -DBUILD_TESTING:BOOL=ON  \
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
 ..

%cmake_build

pushd ../
doxygen
popd

%install
%cmake_install

%post -n %{libname}%{sonum} -p /sbin/ldconfig
%postun -n %{libname}%{sonum} -p /sbin/ldconfig

%check
%ctest

%files -n %{name}
%{_bindir}/nuspell

%files -n %{libname}%{sonum}
%doc README.md CHANGELOG.md AUTHORS
%license COPYING.LESSER COPYING
%{_libdir}/%{libname}.so.%{version}
%exclude %{_datadir}/doc/nuspell/README.md

%files devel
%{_includedir}/%{name}
%{_libdir}/%{libname}.so
%{_libdir}/%{libname}.so.%{sonum}
%{_libdir}/pkgconfig/nuspell.pc
%{_libdir}/cmake/%{name}

%changelog
