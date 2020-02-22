#
# spec file for package python-Flask-Login
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without  test
Name:           python-Flask-Login
Version:        0.5.0
Release:        0
Summary:        User session management for Flask
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/maxcountryman/flask-login
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Login/Flask-Login-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Flask}
%endif
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
%setup -q -n Flask-Login-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/flask_login
%{python_sitelib}/Flask_Login-%{version}-py*.egg-info

%changelog
