#
# spec file for package python-interrogate
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
Name:           python-interrogate
Version:        1.2.0
Release:        0
Summary:        Interrogate a codebase for docstring coverage
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/econchick/interrogate
Source:         https://files.pythonhosted.org/packages/source/i/interrogate/interrogate-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-click
Requires:       python-colorama
Requires:       python-py
Requires:       python-tabulate
Requires:       python-toml
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module toml}
# /SECTION
%python_subpackages

%description
Interrogate a codebase for docstring coverage.

%prep
%setup -q -n interrogate-%{version}
rm tox.ini

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/interrogate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative interrogate

%postun
%python_uninstall_alternative interrogate

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/interrogate
%{python_sitelib}/*

%changelog
