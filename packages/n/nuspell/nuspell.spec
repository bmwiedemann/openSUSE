#
# spec file for package nuspell
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


%define sonum   5
%define libname libnuspell
# Due to std::filesystem and std::charconv used by code, at least gcc-c++ >= 10 and std=c++17 is required
%if 0%{?suse_version} < 1550
%define gcc_ver 10
%endif
Name:           nuspell
Version:        5.1.2
Release:        0
Summary:        A spell checker library and command-line tool
License:        LGPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://nuspell.github.io/
Source:         https://github.com/nuspell/nuspell/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  graphviz
BuildRequires:  libicu-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(catch2) < 3
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
Requires:       %{libname}%{sonum} = %{version}
Recommends:     %{name}-doc = %{version}

%description devel
Header files and definitions for developing with Nuspell.

%package doc
Summary:        API documentation for Nuspell
BuildArch:      noarch

%description doc
This package provides API documentation for Nuspell.

%prep
%autosetup

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON \
%if 0%{?suse_version} < 1550
       -DCMAKE_CXX_COMPILER:STRING=g++-%{?gcc_ver} \
       -DCMAKE_CXX_FLAGS:STRING="%{optflags} -std=c++17" \
%endif
       -DBUILD_TESTING:BOOL=ON  \
       -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build

cd ../
doxygen

%install
%cmake_install

# Install API doc manually so we can run fdupes on buildroot
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pR doxygen/html %{buildroot}%{_docdir}/%{name}-doc/
%fdupes %{buildroot}%{_docdir}/%{name}-doc/

%post -n %{libname}%{sonum} -p /sbin/ldconfig
%postun -n %{libname}%{sonum} -p /sbin/ldconfig

%check
%ctest

%files -n %{name}
%doc README.md CHANGELOG.md AUTHORS
%license COPYING.LESSER COPYING
%{_bindir}/nuspell

%files -n %{libname}%{sonum}
%license COPYING.LESSER COPYING
%{_libdir}/%{libname}.so.*
%exclude %{_datadir}/doc/nuspell/README.md

%files devel
%license COPYING.LESSER COPYING
%{_includedir}/%{name}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/nuspell.pc
%{_libdir}/cmake/%{name}

%files doc
%license COPYING.LESSER COPYING
%doc %{_docdir}/%{name}-doc/

%changelog
