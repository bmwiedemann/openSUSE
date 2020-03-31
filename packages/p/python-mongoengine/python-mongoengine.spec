#
# spec file for package python-mongoengine
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
Name:           python-mongoengine
Version:        0.19.1
Release:        0
Summary:        Python Object-Document Mapper for working with MongoDB
License:        MIT
Group:          Development/Languages/Python
URL:            http://mongoengine.org/
Source:         https://github.com/MongoEngine/mongoengine/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blinker
Requires:       python-pymongo >= 3.4
Requires:       python-six >= 1.10.0
Suggests:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
MongoEngine is an ORM-like layer on top of PyMongo.
MongoEngine is a Python Object-Document Mapper for working with MongoDB
built on top of PyMongo.

%prep
%setup -q -n mongoengine-%{version}

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
