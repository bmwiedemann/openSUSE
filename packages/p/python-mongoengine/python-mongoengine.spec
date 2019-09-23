#
# spec file for package python-mongoengine
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-mongoengine
Version:        0.15.3
Release:        0
Summary:        Python Object-Document Mapper for working with MongoDB
License:        MIT
Group:          Development/Languages/Python
Url:            http://mongoengine.org/
Source:         https://files.pythonhosted.org/packages/source/m/mongoengine/mongoengine-%{version}.tar.gz
Patch0:         fix-requirements.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pymongo >= 2.7.1
Requires:       python-six
Suggests:       python-python-dateutil
BuildArch:      noarch

%python_subpackages

%description
MongoEngine is an ORM-like layer on top of PyMongo.
MongoEngine is a Python Object-Document Mapper for working with MongoDB
built on top of PyMongo.

%prep
%setup -q -n mongoengine-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
