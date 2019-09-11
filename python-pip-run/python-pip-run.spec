#
# spec file for package python-pip-run
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
Name:           python-pip-run
Version:        5.3
Release:        0
Summary:        Pip module to install packages and run Python with them
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jaraco/pip-run
Source:         https://files.pythonhosted.org/packages/source/p/pip-run/pip-run-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module pip}
# /SECTION
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-pip
BuildArch:      noarch

%python_subpackages

%description
pip-run provides on-demand dependency resolution, making packages available
for the duration of an interpreter session.

Features include:

- Allowance of declaration of dependencies at runtime.
- Download of missing dependencies and makes their packages available for import.
- Installation of packages to a special staging location such that they are not
  installed after the process exits.
- Reliance on pip to cache downloads of such packages for reuse.
- Supersedence installed packages when required.
- Reliance on packages already satisfied.
- Re-use of the pip tool chain for package installation.

pip-run is not intended to solve production dependency management, but does aim
to address other, one-off scenarios around dependency management.

%prep
%setup -q -n pip-run-%{version}
sed -i 's/--flake8//' pytest.ini

# Replace unpackaged jaraco.mongodb with a packaged low-dependency plugin
# for use in test_entry_points
# However the test is currently disabled below
sed -i 's/jaraco.mongodb/pytest-travis-fold/' pip_run/tests/test_deps.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pip-run

%post
%python_install_alternative pip-run

%postun
%python_uninstall_alternative pip-run

%check
# Two tests require internet.
%pytest -k 'not test_entry_points and not test_pkg_loaded_from_alternate_index'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/pip-run
%{python_sitelib}/*

%changelog
