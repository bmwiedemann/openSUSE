#
# spec file for package R-rlang
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


%global packname  rlang
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        0.4.0
Release:        0
Summary:        Functions for Base Types and Core R and 'Tidyverse' Features
License:        GPL-3.0-only
Group:          Development/Libraries/Other
URL:            http://cran.r-project.org/web/packages/%{packname}
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-base-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-base

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/rlang/html
%{rlibdir}/rlang/libs
%{rlibdir}/rlang/Meta
%{rlibdir}/rlang/INDEX
%{rlibdir}/rlang/NAMESPACE
%{rlibdir}/rlang/DESCRIPTION
%{rlibdir}/rlang/R
%{rlibdir}/rlang/help
%{rlibdir}/rlang/NEWS.md

%changelog
