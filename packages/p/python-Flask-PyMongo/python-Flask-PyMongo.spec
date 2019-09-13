#
# spec file for package python-Flask-PyMongo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Dr. Axel Braun
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
%ifarch x86_64
%bcond_without		test
%endif
Name:           python-Flask-PyMongo
Version:        2.3.0
Release:        0
Summary:        PyMongo support for Flask applications
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://github.com/dcrosta/flask-pymongo
Source:         https://files.pythonhosted.org/packages/source/F/Flask-PyMongo/Flask-PyMongo-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/dcrosta/flask-pymongo/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.11
Requires:       python-pymongo
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Flask >= 0.11}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest}
BuildRequires:  mongodb-server
%endif
%python_subpackages

%description
MongoDB is a database that stores flexible JSON-like “documents” that
can have any number, name, or hierarchy of fields within, instead of
rows of data as in a relational database. In the context of Python,
MongoDB can be thought of as a persistent, searchable repository of
dictionaries (and, in fact, this is how PyMongo represents MongoDB
documents).

Flask-PyMongo bridges Flask and PyMongo, so that Flask’s normal
mechanisms can be used to configure and connect to MongoDB.

%prep
%setup -q -n Flask-PyMongo-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
mkdir -p /tmp/mongodb
%{_sbindir}/mongod --dbpath /tmp/mongodb > /tmp/mongo.log &
%python_exec setup.py test
%{_sbindir}/mongod --dbpath /tmp/mongodb --shutdown
%endif

%files %{python_files}
%doc docs/* CONTRIBUTING.md README.md version.txt MANIFEST.in examples/*
%license LICENSE
%dir %{python_sitelib}/flask_pymongo
%{python_sitelib}/flask_pymongo/*
%dir %{python_sitelib}/Flask_PyMongo-%{version}-py*.egg-info
%{python_sitelib}/Flask_PyMongo-%{version}-py*.egg-info

%changelog
