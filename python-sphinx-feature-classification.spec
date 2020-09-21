#
# spec file for package python-sphinx-feature-classification
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-sphinx-feature-classification
Version:        1.1.0
Release:        0
Summary:        Sphinx extension to generate a matrix of pluggable drivers
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://www.openstack.org/
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-feature-classification/sphinx-feature-classification-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module ddt >= 1.0.1}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr >= 2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils >= 0.11
Requires:       python-pbr >= 2.0
BuildArch:      noarch
%python_subpackages

%description
An extension to Sphinx to generate a matrix of pluggable drivers and
their support to an API.

%prep
%setup -q -n sphinx-feature-classification-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest sphinx_feature_classification/tests

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%{python_sitelib}/*

%changelog
