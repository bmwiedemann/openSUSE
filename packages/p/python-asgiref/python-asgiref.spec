#
# spec file for package python-asgiref
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-asgiref
Version:        3.11.0
Release:        0
Summary:        ASGI specs, helper code, and adapters
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django/asgiref/
Source:         https://files.pythonhosted.org/packages/source/a/asgiref/asgiref-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
BuildRequires:  %{python_module typing-extensions > 4}
Requires:       python-typing-extensions > 4
%python_subpackages

%description
ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI. You can
read more at https://asgi.readthedocs.io/en/latest/

%prep
%setup -q -n asgiref-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/asgiref
%{python_sitelib}/asgiref-%{version}.dist-info

%changelog
