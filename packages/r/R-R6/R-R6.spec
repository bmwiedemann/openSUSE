#
# spec file for package R-R6
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


%global packname  R6
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        2.4.0
Release:        0
Summary:        Classes with reference semantics
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/wch/R6/
Source:         https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-base-devel
BuildRequires:  R-crayon
BuildRequires:  fdupes
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-base
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif

%description
The R6 package allows the creation of classes with reference semantics,
similar to R's built-in reference classes. Compared to reference classes,
R6 classes are simpler and lighter-weight, and they are not built on S4
classes so they do not require the methods package. These classes allow
public and private members, and they support inheritance, even when the
classes are defined in different packages.

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
%doc %{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

%changelog
