#
# spec file for package R-packrat
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global packname  packrat
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.5.0
Release:        1
Summary:        A Dependency Management System for Projects and their R Package Dependencies
Group:          Development/Libraries/Other
License:        GPL-2.0
URL:            https://rstudio.github.io/packrat/
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-base
Requires:       R-tools
Requires:       R-utils
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif
BuildRequires:  R-base-devel 
BuildRequires:  R-tools
BuildRequires:  R-utils

%description
Manage the R packages your project depends on in an isolated, portable,
and reproducible way.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/rstudio

%changelog
