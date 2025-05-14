#
# spec file for package python-Flask-Login
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
Name:           python-Flask-Login
Version:        0.6.3
Release:        0
Summary:        User session management for Flask
License:        MIT
URL:            https://github.com/maxcountryman/flask-login
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Login/Flask-Login-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#maxcountryman/flask-login#815
Patch0:         do-not-use-datetime-utcnow.patch
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module asgiref >= 3.2}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module semantic_version}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
BuildArch:      noarch
%python_subpackages

%description
Flask-Login provides user session management for Flask. It handles the common
tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

Flask-Login is not bound to any particular database system or permissions
model. The only requirement is that your user objects implement a few
methods, and that you provide a callback to the extension capable of
loading users from their ID.

%prep
%autosetup -p1 -n Flask-Login-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/flask_login
%{python_sitelib}/[Ff]lask[_-][Ll]ogin-%{version}.dist-info

%changelog
