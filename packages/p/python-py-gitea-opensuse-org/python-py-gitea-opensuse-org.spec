#
# spec file for package python-py-gitea-opensuse-org
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
Name:           python-py-gitea-opensuse-org
Version:        1.22.4
Release:        0
Summary:        Gitea API
License:        MIT
URL:            https://github.com/dcermak/py-gitea-opensuse-org
Source:         https://github.com/dcermak/py-gitea-opensuse-org/archive/refs/tags/%{version}.tar.gz#/py-gitea-opensuse-org-%{version}-gh.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.8.4}
BuildRequires:  %{python_module aiohttp-retry >= 2.8.3}
BuildRequires:  %{python_module mypy >= 1.4.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2}
BuildRequires:  %{python_module pytest-randomly >= 3.12.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module types-python-dateutil >= 2.8.19}
BuildRequires:  %{python_module typing-extensions >= 4.7.1}
BuildRequires:  %{python_module urllib3 >= 1.25.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aenum >= 3.1.11
Requires:       python-aiohttp >= 3.8.4
Requires:       python-aiohttp-retry >= 2.8.3
Requires:       python-pydantic >= 1.10.5
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-urllib3 >= 1.25.3
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for src.opensuse.org

%prep
%autosetup -p1 -n py-gitea-opensuse-org-%{version}

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/py_gitea_opensuse_org
%{python_sitelib}/py_gitea_opensuse_org-*.dist-info

%changelog
