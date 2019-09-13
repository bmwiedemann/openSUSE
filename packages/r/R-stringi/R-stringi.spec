#
# spec file for package R-stringi
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


%global packname  stringi
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.2.4
Release:        0
Summary:        Character String Processing Facilities
License:        BSD-3-Clause AND ICU AND MIT
Group:          Development/Libraries/Other
URL:            https://cran.r-project.org/package=%{packname}
Source:         https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-base-devel >= 2.14
BuildRequires:  R-stats
BuildRequires:  R-tools
BuildRequires:  R-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkgconfig(icu-uc) > 52
BuildRequires:  texinfo
BuildRequires:  texlive
%if 0%{?sle_version} > 120400 || 0%{?is_opensuse}
BuildRequires:  tex(inconsolata.sty)
%endif
Requires:       R-base >= 2.14
Requires:       R-stats
Requires:       R-tools
Requires:       R-utils

%description
Allows for fast, correct, consistent, portable, as well as convenient
character string/text processing in every locale and any native encoding.
Owing to the use of the 'ICU' library, the package provides 'R' users with
platform-independent functions known to 'Java', 'Perl', 'Python', 'PHP',
and 'Ruby' programmers. Available features include: pattern searching
(e.g., with 'Java'-like regular expressions or the 'Unicode' collation
algorithm), random string generation, case mapping, string
transliteration, concatenation, Unicode normalization, date-time
formatting and parsing, and many more.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
Development files and headers needed to build software using %{name}.

%prep
%setup -q -c -n %{packname}

%build
#Not needed

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html/
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/libs/

%files devel
%{rlibdir}/%{packname}/include/

%changelog
