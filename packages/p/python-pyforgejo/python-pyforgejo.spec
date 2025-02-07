#
# spec file for package python-pyforgejo
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
Name:           python-pyforgejo
Version:        2.0.0
Release:        0
Summary:        A client library for accessing the Forgejo API
License:        MIT
URL:            https://codeberg.org/harabat/pyforgejo
Source0:        https://files.pythonhosted.org/packages/source/p/pyforgejo/pyforgejo-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module httpx >= 0.20}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pydantic >= 2.9.2}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-annotated-types >= 0.6.0
Requires:       python-anyio
Requires:       python-attrs
Requires:       python-certifi
Requires:       python-click >= 5.0
Requires:       python-colorama
Requires:       python-exceptiongroup
Requires:       python-h11
Requires:       python-httpcore
Requires:       python-httpx
Requires:       python-idna
Requires:       python-iniconfig
Requires:       python-packaging
Requires:       python-pluggy
Requires:       python-pydantic
Requires:       python-pydantic-core
Requires:       python-python-dateutil
Requires:       python-python-dotenv
Requires:       python-sniffio
Requires:       python-tomli
Requires:       python-typing-extensions >= 4.12.2
%python_subpackages

%description
A client library for accessing the Forgejo API.
%{name} was generated with the help of openapi-python-client, and doesn't
try to be compatible with gitea.

%prep
%autosetup -p1 -n pyforgejo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests at this point

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pyforgejo
%{python_sitelib}/pyforgejo-%{version}.dist-info

%changelog
