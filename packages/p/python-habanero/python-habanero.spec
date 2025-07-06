#
# spec file for package python-habanero
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


Name:           python-habanero
Version:        2.3.0
Release:        0
Summary:        Low Level Client for Crossref Search API
License:        MIT
URL:            https://github.com/sckott/habanero
Source:         https://files.pythonhosted.org/packages/source/h/habanero/habanero-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.2
Requires:       python-httpx >= 0.27.2
Requires:       python-packaging >= 24.1
Requires:       python-tqdm >= 4.66.5
Requires:       python-urllib3 >= 2.2.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-recording}
BuildRequires:  %{python_module httpx >= 0.27.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tqdm >= 4.66.5}
BuildRequires:  %{python_module urllib3 >= 2.2.2}
# /SECTION
%python_subpackages

%description
Low Level Client for Crossref Search API

%prep
%autosetup -p1 -n habanero-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not vcr'

%files %{python_files}
%doc Changelog.rst README.rst
%license LICENSE.md
%{python_sitelib}/habanero
%{python_sitelib}/habanero-%{version}.dist-info

%changelog
