#
# spec file for package python-flask-peewee
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-flask-peewee
Version:        3.0.3
Release:        0
License:        MIT
Summary:        Peewee integration for flask
Url:            http://github.com/coleifer/flask-peewee/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/flask-peewee/flask-peewee-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/coleifer/flask-peewee/master/runtests.py
Patch0:         0001-Clarify-that-project-uses-MIT.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# Test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module peewee >= 3.0.0}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module wtf-peewee}
BuildRequires:  %{python_module WTForms}
# End of test requirements
Requires:       python-Flask
Requires:       python-Jinja2
Requires:       python-peewee >= 3.0.0
Requires:       python-Werkzeug
Requires:       python-wtf-peewee
Requires:       python-WTForms
BuildArch:      noarch

%python_subpackages

%description
Flask integration for peewee, including admin, authentication, rest api and more.

%prep
%setup -q -n flask-peewee-%{version}
%patch0 -p1
rm -Rf example
cp %{S:1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
