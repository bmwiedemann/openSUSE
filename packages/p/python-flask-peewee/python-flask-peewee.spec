#
# spec file for package python-flask-peewee
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
Name:           python-flask-peewee
Version:        3.0.5
Release:        0
Summary:        Peewee integration for flask
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/coleifer/flask-peewee/
Source:         https://github.com/coleifer/flask-peewee/archive/refs/tags/%{version}.tar.gz#/flask-peewee-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module peewee >= 3.0.0}
BuildRequires:  %{python_module wtf-peewee}
# End of test requirements
Requires:       python-Flask
Requires:       python-Jinja2
Requires:       python-WTForms
Requires:       python-Werkzeug
Requires:       python-peewee >= 3.0.0
Requires:       python-wtf-peewee
BuildArch:      noarch

%python_subpackages

%description
Flask integration for peewee, including admin, authentication, rest api and more.

%prep
%autosetup -p1 -n flask-peewee-%{version}

rm -Rf example

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flask_peewee
%{python_sitelib}/flask_peewee-%{version}*-info

%changelog
