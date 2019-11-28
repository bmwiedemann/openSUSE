#
# spec file for package python-python-ternary
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
Name:           python-python-ternary
Version:        1.0.6
Release:        0
Summary:        Tool to make ternary plots in python
License:        MIT
URL:            https://github.com/marcharper/python-ternary
Source:         https://github.com/marcharper/python-ternary/archive/%{version}.tar.gz#/python-ternary-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 1.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 1.4}
# /SECTION
%python_subpackages

%description
This is a plotting library for use with matplotlib to make ternary plots plots
in the two dimensional simplex projected onto a two dimensional plane.

The library provides functions for plotting projected lines, curves
(trajectories), scatter plots, and heatmaps.

%prep
%setup -q -n python-ternary-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -s tests

%files %{python_files}
%doc README.md README.txt CITATION.md citations.md
%license LICENSE
%{python_sitelib}/*

%changelog
