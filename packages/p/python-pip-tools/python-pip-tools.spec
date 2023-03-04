#
# spec file for package python-pip-tools
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


%define skip_python2 1
Name:           python-pip-tools
Version:        6.12.2
Release:        0
Summary:        Tool to keep pinned dependencies up to date
License:        BSD-3-Clause
URL:            https://github.com/jazzband/pip-tools/
Source:         https://files.pythonhosted.org/packages/source/p/pip-tools/pip-tools-%{version}.tar.gz
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pip >= 22.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-build
Requires:       python-click >= 8
Requires:       python-pip >= 22.2
Requires:       python-setuptools
Requires:       python-wheel
Recommends:     git-core
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  ca-certificates
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
pip-tools keeps pinned dependencies inside a project up to date.

%prep
%autosetup -p1 -n pip-tools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pip-compile
%python_clone -a %{buildroot}%{_bindir}/pip-sync
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pip-compile pip-sync

%postun
%python_uninstall_alternative pip-compile pip-sync

%check
export LANG=en_US.UTF-8
donttest="network"
# test_direct_reference_with_extras also requires network access
donttest+=" or test_direct_reference_with_extras"
# test_local_duplicate_subdependency_combined also requires network
donttest+=" or test_local_duplicate_subdependency_combined"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%python_alternative %{_bindir}/pip-compile
%python_alternative %{_bindir}/pip-sync
%{python_sitelib}/piptools
%{python_sitelib}/pip_tools-%{version}*-info

%changelog
