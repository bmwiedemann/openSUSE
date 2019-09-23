#
# spec file for package python-flask-mongoengine
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
Name:           python-flask-mongoengine
Version:        0.9.5
Release:        0
License:        BSD-3-Clause
Summary:        A Flask extension that provides integration with MongoEngine and WTForms
Url:            https://github.com/mongoengine/flask-mongoengine
Group:          Development/Languages/Python
# The Pypi version doesn't include tests
#Source:         https://files.pythonhosted.org/packages/source/f/flask-mongoengine/flask-mongoengine-%%{version}.tar.gz
Source:         https://github.com/MongoEngine/flask-mongoengine/archive/v%{version}.tar.gz
Patch0:         fix-requirements.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# Test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module rednose}
BuildRequires:  %{python_module Flask >= 0.8}
BuildRequires:  %{python_module Flask-WTF >= 0.13}
BuildRequires:  %{python_module mongoengine >= 0.8.0}
BuildRequires:  %{python_module six}
BuildRequires:  mongodb-server
# End of test requirements
Requires:       python-Flask >= 0.8
Requires:       python-Flask-WTF >= 0.13
Requires:       python-mongoengine >= 0.8.0
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
Flask-MongoEngine is a Flask extension that provides integration with MongoEngine.
It handles connection management for apps and also integrates with WTForms
as model forms for models.

%prep
%setup -q -n flask-mongoengine-%{version}
%patch0 -p1
chmod -x README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mkdir -p /tmp/mongodb
/usr/sbin/mongod --dbpath /tmp/mongodb > /tmp/mongo.log &
%python_exec setup.py test
/usr/sbin/mongod --dbpath /tmp/mongodb --shutdown

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
