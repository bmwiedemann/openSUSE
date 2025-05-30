#
# spec file for package python-interrogate
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-interrogate
Version:        1.7.0
Release:        0
Summary:        Interrogate a codebase for docstring coverage
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/econchick/interrogate
Source:         https://files.pythonhosted.org/packages/source/i/interrogate/interrogate-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-click
Requires:       python-colorama
Requires:       python-py
Requires:       python-tabulate
Requires(post): alts
Requires(postun): alts
BuildArch:      noarch
%if 0%{python_version_nodots} < 311
Requires:       python-tomli
%endif
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module tomli if %python-version < 3.11}
# /SECTION
%python_subpackages

%description
Interrogate a codebase for docstring coverage.

%prep
%setup -q -n interrogate-%{version}
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/interrogate
%{python_sitelib}/interrogate-%{version}*-info

%changelog
