#
# spec file for package tidy
#
# Copyright (c) 2020 SUSE LLC
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


%define regression_tests 00f1e38
%define documentation    0ed35c6
Name:           tidy
Version:        5.7.28
Release:        0
Summary:        Utility to Clean Up and Pretty-print HTML, XHTML or XML Markup
License:        W3C
Group:          Productivity/Publishing/HTML/Tools
URL:            https://github.com/htacg/tidy-html5
Source0:        https://github.com/htacg/tidy-html5/archive/%{version}.tar.gz
# Latest version of unit tests
Source1:        https://github.com/htacg/tidy-html5-tests/archive/%{regression_tests}.tar.gz
# Documentation generation files, extracted from
#   https://github.com/htacg/html-tidy.org.api.git/archive/%%{documentation}.tar.gz
# using tidy_fetch_docs.sh
Source2:        tidy-html5-doxygen-%{documentation}.tar.gz
Source10:       tidy_fetch_docs.sh
Patch0:         dynamic_library_build.diff
Patch1:         test_fixes.diff
Patch2:         fix_doxygen_paths.diff
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig

%description
Tidy is a commandline frontend to TidyLib which allows for cleaning up and
pretty printing HTML, XHTML and XML markup in a variety of file encodings. For
HTML variants, it can detect and report proprietary elements as well as many
common coding errors, correct them and produce visually equivalent markup
which is both compliant with W3C standards and works on most browsers.
Furthermore, it can convert plain HTML to XHTML. For generic XML files, Tidy is
limited to correcting basic well-formedness errors and pretty printing.

%package doc
Summary:        Documentation for tidy and libtidy5
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
This package contains the documentation for both tidy and libtidy.

%package -n libtidy5
Summary:        Library to Clean Up and Pretty-print HTML, XHTML or XML Markup
Group:          System/Libraries
Provides:       libtidy = %{version}
Obsoletes:      libtidy <= 1.0

%description -n libtidy5
TidyLib is a library for cleaning up and pretty printing HTML, XHTML and XML
markup in a variety of file encodings. For HTML variants, it can detect and
report proprietary elements as well as many common coding errors, correct them
and produce visually equivalent markup which is both compliant with W3C
standards and works on most browsers. Furthermore, it can convert plain HTML
into XHTML. For generic XML files, Tidy is limited to correcting basic
well-formedness errors and pretty printing.

There is a commandline frontend for this library, contained in the package
"tidy".

%package -n libtidy-devel
Summary:        Development files for libtidy
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libtidy5 = %{version}
Conflicts:      libtidy-0_99-0-devel
Conflicts:      tidy-html5-devel
Obsoletes:      libtidy-0_99-0-devel < %{version}

%description -n libtidy-devel
This package contains all necessary include files and libraries needed
to develop applications using functions provided by the TidyLib library.

%prep
%setup -q -a 1 -a 2 -n tidy-html5-%{version}
mv tidy-html5-tests-* tests
%autopatch -p1

%build
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DINCLUDE_INSTALL_DIR:PATH=include/%{name} \
    -DTIDY_COMPAT_HEADERS:BOOL=ON -DCMAKE_C_FLAGS_RELWITHDEBINFO="-O0 -ggdb3"
%cmake_build
../tidy-html5-doxygen/build_docs.sh

%install
%cmake_install

%post -n libtidy5 -p /sbin/ldconfig
%postun -n libtidy5 -p /sbin/ldconfig

%files
%{_bindir}/tidy
%{_mandir}/man1/tidy.1%{?ext_man}

%files -n tidy-doc
%doc build/docs/api/

%files -n libtidy5
%{_libdir}/libtidy*.so.*

%files -n libtidy-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/tidy.h
%{_includedir}/%{name}/tidybuffio.h
%{_includedir}/%{name}/tidyenum.h
%{_includedir}/%{name}/tidyplatform.h
%{_includedir}/%{name}/buffio.h
%{_includedir}/%{name}/platform.h
%{_libdir}/libtidy.so
%{_libdir}/pkgconfig/*.pc

%changelog
