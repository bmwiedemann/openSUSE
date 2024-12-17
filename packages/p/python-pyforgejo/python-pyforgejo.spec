#
# spec file for package python-pyforgejo
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
Name:           python-pyforgejo
Version:        1.0.4
Release:        0
Summary:        A client library for accessing the Forgejo API
License:        MIT
URL:            https://codeberg.org/harabat/pyforgejo
Source0:        https://files.pythonhosted.org/packages/source/p/pyforgejo/pyforgejo-%{version}.tar.gz
BuildRequires:  %{python_module attrs >= 21.3.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module httpx >= 0.20}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-attrs
Requires:       python-httpx
Requires:       python-python-dateutil
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
