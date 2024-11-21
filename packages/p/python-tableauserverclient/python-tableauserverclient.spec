#
# spec file for package python-tableauserverclient
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


Name:           python-tableauserverclient
Version:        0.34
Release:        0
Summary:        Python library for working with the Tableau Server REST API
License:        MIT
URL:            https://github.com/tableau/server-client-python
Source:         https://github.com/tableau/server-client-python/archive/refs/tags/v%{version}.tar.gz#/tableauserverclient-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml >= 0.7.1
Requires:       python-packaging >= 23.
Requires:       python-requests >= 2.31
Requires:       python-typing-extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module defusedxml >= 0.7.1}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module requests >= 2.31}
BuildRequires:  %{python_module requests-mock >= 1.0}
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
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/tableauserverclient
%{python_sitelib}/tableauserverclient-%{version}.dist-info

%changelog
