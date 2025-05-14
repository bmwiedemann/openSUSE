#
# spec file for package python-Flask-Cors
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
Name:           python-Flask-Cors
Version:        5.0.1
Release:        0
Summary:        A Flask extension adding a decorator for CORS support
License:        MIT
URL:            https://github.com/corydolphin/flask-cors
Source:         https://github.com/corydolphin/flask-cors/archive/refs/tags/%{version}.tar.gz#/flask_cors-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.9
Requires:       python-Werkzeug >= 0.7
BuildArch:      noarch
%python_subpackages

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%prep
%setup -q -n flask-cors-%{version}
# https://github.com/corydolphin/flask-cors/issues/387
sed -ie 's/"0.0.1"$/"%{version}"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flask_cors
%{python_sitelib}/[Ff]lask_[Cc]ors-%{version}.dist-info

%changelog
