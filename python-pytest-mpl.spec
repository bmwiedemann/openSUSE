#
# spec file for package python-pytest-mpl
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
Name:           python-pytest-mpl
Version:        0.11
Release:        0
Summary:        pytest plugin for testing Matplotlib figures
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/matplotlib/pytest-mpl
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mpl/pytest-mpl-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-matplotlib
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is a pytest plugin to help with testing figures output from Matplotlib.

%prep
%setup -q -n pytest-mpl-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
