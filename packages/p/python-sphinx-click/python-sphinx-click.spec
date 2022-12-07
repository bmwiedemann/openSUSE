#
# spec file for package python-sphinx-click
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
Name:           python-sphinx-click
Version:        4.4.0
Release:        0
Summary:        Sphinx extension that automatically documents click applications
License:        MIT
URL:            https://github.com/stephenfin/sphinx-click
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_click/sphinx-click-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
BuildRequires:  python-rpm-generators
%{?python_enable_dependency_generator}
%python_subpackages

%description
A Sphinx plugin that allows to automatically extract documentation from click-based applications and include it in documentation.

%prep
%setup -q -n sphinx-click-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/sphinx_click*

%changelog
