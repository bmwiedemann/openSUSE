#
# spec file for package python-gitlabcis
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-gitlabcis
Version:        1.15.13
Release:        0
Summary:        An automated tool that assesses the GitLab CIS benchmarks against a project
License:        MIT
URL:            https://gitlab.com/gitlab-security-oss/cis/gitlabcis/
Source:         https://files.pythonhosted.org/packages/source/g/gitlabcis/gitlabcis-%{version}.tar.gz
BuildRequires:  python-rpm-macros
# SECTION build requirements
BuildRequires:  %{python_module pip}
# Relax constraint
# https://gitlab.com/gitlab-security-oss/cis/gitlabcis/-/blob/main/pyproject.toml?ref_type=heads#L73
BuildRequires:  %{python_module setuptools >= 78.0}
# Relax constraint
# https://gitlab.com/gitlab-security-oss/cis/gitlabcis/-/blob/main/pyproject.toml?ref_type=heads#L76
BuildRequires:  %{python_module setuptools_scm >= 8.2.0}
BuildRequires:  %{python_module twine >= 6.1.0}
BuildRequires:  %{python_module wheel >= 0.45.1}
# /SECTION
# SECTION runtime requirements
# https://gitlab.com/gitlab-security-oss/cis/gitlabcis/-/blob/main/pyproject.toml?ref_type=heads#L61
BuildRequires:  %{python_module PyYAML >= 6.0.2}
BuildRequires:  %{python_module defusedxml >= 0.7.1}
BuildRequires:  %{python_module gql >= 3.5.3}
BuildRequires:  %{python_module python-dateutil >= 2.9.0.post0}
BuildRequires:  %{python_module python-gitlab >= 6.3.0}
BuildRequires:  %{python_module tabulate >= 0.9.0}
BuildRequires:  %{python_module tqdm >= 4.67.1}
# /SECTION
# SECTION test requirements
# BuildRequires:  python_module pytest >= 8.3.4}
# BuildRequires:  python_module yamllint >= 1.35.1}
# BuildRequires:  python_module bandit >= 1.8.3}
# /SECTION
BuildRequires:  fdupes
# https://gitlab.com/gitlab-security-oss/cis/gitlabcis/-/blob/main/pyproject.toml?ref_type=heads#L61
Requires:       python-PyYAML >= 6.0.2
Requires:       python-defusedxml >= 0.7.1
Requires:       python-gql >= 3.5.3
Requires:       python-python-dateutil >= 2.9.0.post0
Requires:       python-python-gitlab >= 6.3.0
Requires:       python-tabulate >= 0.9.0
Requires:       python-tqdm >= 4.67.1
BuildArch:      noarch
%python_subpackages

%description
An automated tool that assesses the GitLab CIS benchmarks against a project.

%prep
%autosetup -p1 -n gitlabcis-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gitlabcis
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative gitlabcis

%postun
%python_uninstall_alternative gitlabcis

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/gitlabcis
%{python_sitelib}/gitlabcis
%{python_sitelib}/gitlabcis-%{version}.dist-info

%changelog
