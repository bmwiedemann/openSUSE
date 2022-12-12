#
# spec file for package python-ansible-compat
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


%if 0%{?suse_version} < 1550
# Leap15, SLES15
%define pythons python310
%else
# Tumbleweed
# only works with the python version which the package 'ansible' uses
%define pythons python3
%endif

Name:           python-ansible-compat
Version:        2.2.7
Release:        0
Summary:        Compatibility shim for Ansible 2.9 and newer
License:        MIT
URL:            https://github.com/ansible-community/ansible-compat
Source:         https://files.pythonhosted.org/packages/source/a/ansible-compat/ansible-compat-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module jsonschema >= 4.5.1}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module subprocess-tee}
BuildRequires:  ansible
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
%{?python_enable_dependency_generator}
Requires:       python-subprocess-tee
BuildArch:      noarch
%python_subpackages

%description
Facilitate working with various versions of Ansible 2.9 and newer.

%prep
%setup -q -n ansible-compat-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# excluding tests requiring internet connection
%pytest -k 'not (test_runtime_example or test_require_collection_no_cache_dir or test_upgrade_collection or test_install_collection_dest or test_install_collection or test_require_collection or test_require_collection_wrong_version or test_prerun_reqs_v2 or test_prerun_reqs_v1 or test_prepare_environment_with_collections or test_runtime_require_module)'

%files %{python_files}
%{python_sitelib}/ansible_compat*
%doc README.md
%license LICENSE

%changelog
