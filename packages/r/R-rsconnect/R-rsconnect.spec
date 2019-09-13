#
# spec file for package R-rsconnect
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


%global packname  rsconnect
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.8.12
Release:        0
Summary:        Deployment Interface for R Markdown Documents and Shiny Applications
License:        GPL-2.0
Group:          Development/Libraries/Other
URL:            https://github.com/rstudio/rsconnect
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-openssl
BuildRequires:  R-RCurl
BuildRequires:  R-jsonlite
BuildRequires:  R-packrat
BuildRequires:  R-yaml
BuildRequires:  R-rstudioapi
BuildRequires:  fdupes
BuildRequires:  texinfo
BuildRequires:  texlive
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif
Requires:       R-openssl
Requires:       R-RCurl
Requires:       R-jsonlite
Requires:       R-packrat
Requires:       R-yaml
Requires:       R-rstudioapi

%description
Programmatic deployment interface for 'RPubs', 'shinyapps.io', and
'RStudio Connect'. Supported content types include R Markdown documents,
Shiny applications, plots, and static web content.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/cert
%{rlibdir}/%{packname}/help

%changelog
