#
# spec file for package python-WSME
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
Name:           python-WSME
Version:        0.12.1
Release:        0
Summary:        Web Services Made Easy
License:        MIT
URL:            https://packages.python.org/WSME/
Source:         https://files.pythonhosted.org/packages/source/W/WSME/WSME-%{version}.tar.gz
# Test requirements:
BuildRequires:  %{python_module WebOb >= 1.2.3}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module netaddr >= 0.7.12}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pecan}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplegeneric}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WebOb >= 1.2.3
Requires:       python-importlib-metadata
Requires:       python-netaddr >= 0.7.12
Requires:       python-pytz
Requires:       python-simplegeneric
BuildArch:      noarch
%python_subpackages

%description
Web Service Made Easy (WSME) is a way to implement webservices
in Python web applications.
It is originally a rewrite of TGWebServices
with focus on extensibility, framework-independence and improved type handling.

%prep
%setup -q -n WSME-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/pecantest

%files %{python_files}
%license LICENSE
%doc README.rst examples
%{python_sitelib}/wsme
%{python_sitelib}/wsmeext
%{python_sitelib}/WSME-%{version}.dist-info
%{python_sitelib}/WSME-%{version}-py*-nspkg.pth

%changelog
