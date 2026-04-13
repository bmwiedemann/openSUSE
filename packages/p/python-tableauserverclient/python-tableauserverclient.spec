#
# spec file for package python-tableauserverclient
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-tableauserverclient
Version:        0.40
Release:        0
Summary:        Python library for working with the Tableau Server REST API
License:        MIT
URL:            https://github.com/tableau/server-client-python
Source:         https://github.com/tableau/server-client-python/archive/refs/tags/v%{version}.tar.gz#/tableauserverclient-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml >= 0.7.1
Requires:       python-packaging >= 23.1
Requires:       python-requests >= 2.32
Requires:       python-typing-extensions >= 4.0
Requires:       python-urllib3 >= 2.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module defusedxml >= 0.7.1}
BuildRequires:  %{python_module packaging >= 23.1}
BuildRequires:  %{python_module pytest >= 7.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-subtests if %python-pytest < 9}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module requests >= 2.32}
BuildRequires:  %{python_module requests-mock >= 1.0}
BuildRequires:  %{python_module typing-extensions >= 4.0}
# /SECTION
%python_subpackages

%description
A Python module for working with the Tableau Server REST API.

%prep
%setup -q -n server-client-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm %{buildroot}%{$python_sitelib}/_version.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/tableauserverclient
%{python_sitelib}/tableauserverclient-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/_version*

%changelog
