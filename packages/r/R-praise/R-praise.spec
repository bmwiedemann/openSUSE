#
# spec file for package R-praise
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global packname  praise
%global rlibdir  %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.0.0
Release:        0
Summary:        Build friendly R packages
License:        MIT
Group:          Development/Libraries/Other
URL:            http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:        http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-devel
BuildRequires:  texlive-latex
Requires:       R-base
Recommends:     R-testthat

%description
Build friendly R packages that praise their users if they have done
something good, or they just need it to feel better.

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
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.*
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

%changelog
