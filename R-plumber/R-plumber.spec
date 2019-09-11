#
# spec file for package R-plumber
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

%global packname  plumber
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.4.6
Release:        0
Summary:        An API Generator for R
Group:          Development/Libraries/Other
License:        MIT
URL:            https://www.rplumber.io
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-R6 >= 2.0.0, R-stringi >= 0.3.0, R-jsonlite >= 0.9.16, R-httpuv >= 1.2.3, R-crayon
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif
BuildRequires:  R-base-devel
BuildRequires:  R-R6 >= 2.0.0, R-stringi >= 0.3.0, R-jsonlite >= 0.9.16, R-httpuv >= 1.2.3, R-crayon

%description
Gives the ability to automatically generate and serve an HTTP API
from R functions using the annotations in the R documentation
around your functions.

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
%{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/examples/
%{rlibdir}/%{packname}/examples/01-append/
%{rlibdir}/%{packname}/examples/02-filters/
%{rlibdir}/%{packname}/examples/03-github/
%{rlibdir}/%{packname}/examples/04-mean-sum/
%{rlibdir}/%{packname}/examples/05-static/
%{rlibdir}/%{packname}/examples/06-sessions/
%{rlibdir}/%{packname}/examples/07-mailgun/
%{rlibdir}/%{packname}/examples/08-identity/
%{rlibdir}/%{packname}/examples/09-content-type/
%{rlibdir}/%{packname}/examples/10-welcome/
%{rlibdir}/%{packname}/examples/11-car-inventory/
%{rlibdir}/%{packname}/examples/12-entrypoint/
%{rlibdir}/%{packname}/hosted/
%{rlibdir}/%{packname}/server/
%{rlibdir}/%{packname}/swagger-ui/
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

%changelog
