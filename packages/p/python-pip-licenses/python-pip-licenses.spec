#
# spec file for package python-pip-licenses
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pip-licenses
Version:        4.4.0
Release:        0
Summary:        Python packages license list
License:        MIT
URL:            https://github.com/raimon49/pip-licenses
Source:         https://files.pythonhosted.org/packages/source/p/pip-licenses/pip-licenses-%{version}.tar.gz
BuildRequires:  %{python_module importlib_metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable
Requires:       python-pip
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
Dump the software license list of Python packages installed with pip.

%prep
%autosetup -p1 -n pip-licenses-%{version}

sed -i '/addopts/d' setup.cfg
sed -i '/pytest-/d' setup.cfg
sed -i '1{/^#!/d}' piplicenses.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pip-licenses
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# gh#raimon49/pip-licenses#120 for test_from_all
donttest="test_from_all"
%pytest -k "not ($donttest)"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %{buildroot}%{_bindir}/pip-licenses-%{$python_bin_suffix} -s

%post
%python_install_alternative pip-licenses

%postun
%python_uninstall_alternative pip-licenses

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/pip-licenses
%{python_sitelib}/piplicenses.py
%{python_sitelib}/pip_licenses-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/piplicenses.*pyc

%changelog
