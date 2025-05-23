#
# spec file for package python-Flask-HTTPAuth
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2024 Dr. Axel Braun
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
Name:           python-Flask-HTTPAuth
Version:        4.8.0
Release:        0
Summary:        Basic and Digest HTTP authentication for Flask routes
License:        MIT
URL:            https://github.com/miguelgrinberg/flask-httpauth/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-HTTPAuth/Flask-HTTPAuth-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module asgiref >= 3.2}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Recommends:     python-asgiref >= 3.2
BuildArch:      noarch
%python_subpackages

%description
Simple extension that provides Basic and Digest HTTP authentication for Flask routes.

%prep
%setup -q -n Flask-HTTPAuth-%{version}

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
%{python_sitelib}/flask_httpauth.py*
%{python_sitelib}/[Ff]lask_[Hh][Tt][Tt][Pp][Aa]uth-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
