#
# spec file for package python-reno
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
# uses openstack packages: build and depend on default python3 provider only
%define pythons python3
Name:           python-reno
Version:        3.5.0
Release:        0
Summary:        RElease NOtes manager
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/r/reno/reno-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module dulwich >= 0.15.0}
BuildRequires:  %{python_module openstackdocstheme >= 2.2.1}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  gpg2
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.10
Requires:       python-Sphinx
Requires:       python-docutils
Requires:       python-dulwich >= 0.15.0
Requires:       python-pbr
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Reno is a release notes manager for storing release notes in a git
repository and then building documentation from them.

%prep
%autosetup -n reno-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/reno/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/reno

%post
%python_install_alternative reno

%postun
%python_uninstall_alternative reno

%check
rm -rf .git
git init .
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/reno
%{python_sitelib}/reno
%{python_sitelib}/*.egg-info

%changelog
