#
# spec file for package python-sphinxcontrib-copybutton
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-sphinxcontrib-copybutton
Version:        0.5.1
Release:        0
Summary:        Add a copy button to each of your code cells
License:        MIT
URL:            https://github.com/executablebooks/sphinx-copybutton
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-copybutton/sphinx-copybutton-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.8
Suggests:       python-ipython
Suggests:       python-myst-nb
Suggests:       python-pre-commit = 2.12.1
Suggests:       python-sphinx
Suggests:       python-sphinx-book-theme
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 1.8}
# /SECTION
%python_subpackages

%description
Add a copy button to each of your code cells.

%prep
%setup -q -n sphinx-copybutton-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
