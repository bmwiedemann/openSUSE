#
# spec file for package python-pytest-httpserver
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


%{?sle15_python_module_pythons}
Name:           python-pytest-httpserver
Version:        1.0.6
Release:        0
Summary:        A HTTP server for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.github.com/csernazs/pytest-httpserver
Source:         https://files.pythonhosted.org/packages/source/p/pytest_httpserver/pytest_httpserver-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module toml >= 0.10}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Werkzeug >= 2
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Werkzeug >= 2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
This library is for testing HTTP clients without contacting the real
HTTP server. In other words, it is a fake HTTP server which is
accessible via localhost can be started with the pre-defined expected
HTTP requests and their responses.

%prep
%setup -q -n pytest_httpserver-%{version}

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
%{python_sitelib}/pytest_httpserver
%{python_sitelib}/pytest_httpserver-%{version}*-info

%changelog
