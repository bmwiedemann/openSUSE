#
# spec file for package python-pymongo
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-pymongo
Version:        4.3.3
Release:        0
Summary:        Python driver for MongoDB
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mongodb/mongo-python-driver
Source:         https://files.pythonhosted.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz
# PATCH-FIX-SUSE: upstream does not care about 32bit
Patch0:         mongodb-skip-test.patch
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Suggests:       mongodb
%endif
# Same namespace, different implementation (https://github.com/py-bson/bson)
Conflicts:      python-bson
%python_subpackages

%description
The PyMongo distribution contains tools for interacting with MongoDB
database from Python.  The bson package is an implementation of
the BSON format for Python. The pymongo package is a native Python
driver for MongoDB. The gridfs package is a gridfs
implementation on top of pymongo.

%prep
%setup -q -n pymongo-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/pymongo
%{python_sitearch}/pymongo-%{version}*-info
%{python_sitearch}/bson
%{python_sitearch}/gridfs

%changelog
