#
# spec file for package python-pytest-httpbin
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


%{?sle15_python_module_pythons}
Name:           python-pytest-httpbin
Version:        2.1.0
Release:        0
Summary:        Web service for testing HTTP libraries
License:        MIT
URL:            https://github.com/kevin1024/pytest-httpbin
Source:         https://files.pythonhosted.org/packages/source/p/pytest-httpbin/pytest_httpbin-%{version}.tar.gz
Source99:       pytest-httpbin-rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module httpbin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpbin
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
httpbin is a web service for testing HTTP libraries. It has several
endpoints that can test parts needed in a HTTP library.

Pytest-httpbin creates a pytest "fixture" that is
dependency-injected into your tests. It automatically starts up a HTTP server
in a separate thread running httpbin and provides your test with the URL in the
fixture.

%prep
%autosetup -p1 -n pytest_httpbin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md DESCRIPTION.rst
%{python_sitelib}/pytest_httpbin
%{python_sitelib}/pytest_httpbin-%{version}.dist-info

%changelog
