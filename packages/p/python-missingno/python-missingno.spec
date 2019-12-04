#
# spec file for package python-missingno
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-missingno
Version:        0.4.2
Release:        0
Summary:        Missing data visualization module for Python
License:        MIT
URL:            https://github.com/ResidentMario/missingno
Source:         https://github.com/ResidentMario/missingno/archive/%{version}.tar.gz#/missingno-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-scipy
Requires:       python-seaborn
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module seaborn}
# /SECTION
%python_subpackages

%description
 missingno provides a toolset of missing data visualizations and
 utilities that allows you to get a visual summary of the completeness
 (or lack thereof) of your dataset.

%prep
%setup -q -n missingno-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/*_tests.py

%files %{python_files}
%doc CONFIGURATION.md README.md
%doc QuickStart.ipynb
%doc paper.bib paper.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
