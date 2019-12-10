#
# spec file for package python-chartify
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
Name:           python-chartify
Version:        2.7.0
Release:        0
Summary:        Python library for plotting charts
License:        Apache-2.0
URL:            https://github.com/spotify/chartify
Source:         https://github.com/spotify/chartify/archive/%{version}.tar.gz#/chartify-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 4.3.0
Requires:       python-bokeh >= 0.12.16
Requires:       python-colour >= 0.1.5
Requires:       jupyter >= 1.0.0
Requires:       python-pandas >= 0.21.0
Requires:       python-scipy >= 1.0.0
Requires:       python-selenium >= 3.7.0
Recommends:     python-ipython
Recommends:     python-ipykernel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 4.3.0}
BuildRequires:  %{python_module bokeh >= 0.12.16}
BuildRequires:  %{python_module colour >= 0.1.5}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module pandas >= 0.21.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module scipy >= 1.0.0}
BuildRequires:  %{python_module selenium >= 3.7.0}
BuildRequires:  jupyter >= 1.0.0
# /SECTION
%python_subpackages

%description
Chartify is a Python library for creating charts.

%prep
%setup -q -n chartify-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
