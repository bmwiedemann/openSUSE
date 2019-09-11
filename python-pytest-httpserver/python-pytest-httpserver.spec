#
# spec file for package python-pytest-httpserver
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python2 1
Name:           python-pytest-httpserver
Version:        0.3.4
Release:        0
Summary:        A HTTP server for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.github.com/csernazs/pytest-httpserver
Source:         https://files.pythonhosted.org/packages/source/p/pytest_httpserver/pytest_httpserver-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Werkzeug
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-runner}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_wait_unexpected_request and not test_wait_timeout'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
