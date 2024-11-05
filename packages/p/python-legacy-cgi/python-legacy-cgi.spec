#
# spec file for package python-legacy-cgi
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
Name:           python-legacy-cgi
Version:        2.6.1
Release:        0
Summary:        Fork of the standard library cgi and cgitb modules
License:        Python-2.0
URL:            https://github.com/jackrosenthal/legacy-cgi
Source:         https://files.pythonhosted.org/packages/source/l/legacy-cgi/legacy_cgi-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a fork of the standard library modules ``cgi`` and ``cgitb``.
They are slated to be removed from the Python standard libary in
Python 3.13 by PEP-594_.

%prep
%autosetup -p1 -n legacy_cgi-%{version}
# We don't want or a need a shebang
sed -i '1,11d' cgi.py
chmod -x cgi.py

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
%{python_sitelib}/cgi.py
%{python_sitelib}/cgitb.py
%pycache_only %{python_sitelib}/__pycache__/cgi.*.pyc
%pycache_only %{python_sitelib}/__pycache__/cgitb.*.pyc
%{python_sitelib}/legacy_cgi-%{version}.dist-info

%changelog
