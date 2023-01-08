#
# spec file for package python-sphinx-inline-tabs
#
# Copyright (c) 2023 SUSE LLC
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
%global skip_python2 1
Name:           python-sphinx-inline-tabs
Version:        2022.1.2b11
Release:        0
Summary:        Add inline tabbed content to your Sphinx documentation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_inline_tabs/sphinx_inline_tabs-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 3
BuildArch:      noarch
%python_subpackages

%description
Add inline tabbed content to your Sphinx documentation.

%prep
%setup -q -n sphinx_inline_tabs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/sphinx_inline_tabs*

%changelog
