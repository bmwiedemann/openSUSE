#
# spec file for package R-crayon
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


%global packname  crayon
%global rlibdir  %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.3.4
Release:        0
Summary:        Colored Terminal Output
License:        MIT
Group:          Development/Libraries/Other
URL:            http://cran.r-project.org/web/packages/%{packname}/index.html
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-devel
BuildRequires:  R-grDevices
BuildRequires:  R-methods
BuildRequires:  R-utils
BuildRequires:  texlive-latex
Requires:       R-base
Requires:       R-methods
Requires:       R-utils

%description
Colored terminal output on terminals that support 'ANSI' color and
highlight codes. It also works in 'Emacs' 'ESS'. 'ANSI' color support is
automatically detected. Colors and highlighting can be combined and
nested. New styles can also be created easily. This package was inspired
by the 'chalk' 'JavaScript' project.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.markdown
%dir %{rlibdir}/%{packname}
%{rlibdir}/%{packname}/logo.png
%{rlibdir}/%{packname}/logo.svg.gz
%{rlibdir}/%{packname}/ANSI-256-OSX.png
%{rlibdir}/%{packname}/ANSI-8-OSX.png
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

%changelog
