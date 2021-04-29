#
# spec file for package python-inspektor
#
# Copyright (c) 2021 SUSE LLC
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
%if 0%{suse_version} >= 1550
# cliff and stevedore are only built for primary python3
%define pythons python3
%endif
%global         pkgname inspektor
Name:           python-%{pkgname}
Version:        0.5.2
Release:        0
Summary:        Program used to verify the code of your python project
License:        GPL-2.0-only
URL:            https://github.com/avocado-framework/inspektor
Source:         https://files.pythonhosted.org/packages/42/8a/9e375ac0bb498760fe2408a2e0f1fe09808933e593d1b6f04193492b9048/inspektor-%{version}.tar.gz
BuildRequires:  %{python_module astroid >= 1.2.1}
BuildRequires:  %{python_module cmd2}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module logutils >= 0.3.3}
BuildRequires:  %{python_module pbr >= 1.4}
BuildRequires:  %{python_module pycodestyle >= 2.0.0}
BuildRequires:  %{python_module pylint >= 1.3.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-cliff
BuildRequires:  python3-stevedore
Requires:       python-astroid >= 1.2.1
Requires:       python-cliff
Requires:       python-cmd2
Requires:       python-logutils >= 0.3.3
Requires:       python-pbr >= 1.4
Requires:       python-pycodestyle >= 2.0.0
Requires:       python-pylint >= 1.3.1
Requires:       python-stevedore
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
BuildRequires:  python3-typed-ast
Requires:       python3-typed-ast
%python_subpackages

%description
Inspektor is a program used to verify the code of a Python project.
It checks code with the help of pylint, checks indentation with
pycodestyle, and checks for PEP8 compliance.

Inspektor can work with Git and SVN checkouts.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%python_build

%check
# No test suite

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/inspekt
%fdupes %{buildroot}

%post
%python_install_alternative inspekt

%postun
%python_uninstall_alternative inspekt

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/inspekt
%{python_sitelib}/*

%changelog
