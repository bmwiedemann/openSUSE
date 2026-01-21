#
# spec file for package nuspell
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%bcond_with tests
%else
%bcond_without tests
%endif
# Ring1 package, avoid pandoc requirement by disabling man file generation
%bcond_with man
Name:           nuspell
Version:        5.1.7
Release:        0
Summary:        A spell checker library and command-line tool
License:        LGPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://nuspell.github.io/
Source:         https://github.com/nuspell/nuspell/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
%if 0%{?suse_version} < 1550
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  /usr/bin/ronn
BuildRequires:  graphviz
BuildRequires:  libicu-devel
BuildRequires:  pkgconfig
Requires:       hunspell
%if %{with man}
BuildRequires:  pandoc
%endif
%if %{with tests}
BuildRequires:  pkgconfig(catch2) >= 3.3.2
%endif

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
       -DCMAKE_CXX_COMPILER:STRING=g++-10 \
       -DCMAKE_CXX_FLAGS:STRING="%{optflags} -std=c++17" \
%endif
       -DBUILD_TESTING:BOOL=%{?with_tests:ON}%{!?with_tests:OFF}  \
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DBUILD_API_DOCS=ON \
       -DBUILD_MAN=%{?with_man:ON}%{!?with_man:OFF} \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}-doc \
       %{nil}
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_docdir}/%{name}-doc/

%ldconfig_scriptlets -n %{libname}%{sonum}

%if %{with tests}
%check
%ctest
%endif

%files -n %{name}
%doc README.md CHANGELOG.md AUTHORS
%license COPYING.LESSER COPYING
%{_bindir}/nuspell
%if %{with man}
%{_mandir}/man1/nuspell.1%{?ext_man}
%endif

%files -n %{libname}%{sonum}
%license COPYING.LESSER COPYING
%{_libdir}/%{libname}.so.*
%if 0%{?suse_version} < 1650 && 0%{?sle_version} <= 150500
%exclude %{_datadir}/doc/nuspell/README.md
%endif

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
