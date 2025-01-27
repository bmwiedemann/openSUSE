#
# spec file for package python-id
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
Name:           python-id
Version:        1.5.0
Release:        0
Summary:        A tool for generating OIDC identities
License:        Apache-2.0
URL:            https://github.com/di/id
Source:         https://github.com/di/id/archive/v%{version}.tar.gz#/id-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
id is a Python tool for generating OIDC identities. It can automatically
detect and produce OIDC credentials on a number of environments, including
GitHub Actions, GitLab pipelines and Google Cloud.

%prep
%autosetup -p1 -n id-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/id
%{python_sitelib}/id-%{version}.dist-info

%changelog
