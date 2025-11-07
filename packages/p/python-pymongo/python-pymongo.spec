#
# spec file for package python-pymongo
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-pymongo
Version:        4.15.3
Release:        0
Summary:        Python driver for MongoDB
License:        Apache-2.0
URL:            https://github.com/mongodb/mongo-python-driver
Source:         https://files.pythonhosted.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz
# PATCH-FIX-SUSE: upstream does not care about 32bit
Patch0:         mongodb-skip-test.patch
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module dnspython >= 2.6.1}
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio >= 0.24.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Suggests:       mongodb
%endif
Requires:       python-dnspython >= 2.6.1
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
%autosetup -p1  -n pymongo-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
# do we really need C sources installed?
%python_expand rm -v %{buildroot}%{$python_sitearch}/bson/*.{c,h}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# tests rely on working DNS which is not available during build
rm -v test/asynchronous/test_client.py
rm -v test/asynchronous/test_srv_polling.py
rm -v test/test_srv_polling.py
rm -v test/test_uri_spec.py
%pytest_arch -k 'not (test_connection_timeout_ms_propagates_to_DNS_resolver or test_detected_environment_logging or test_detected_environment_warning)'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/pymongo
%{python_sitearch}/pymongo-%{version}.dist-info
%{python_sitearch}/bson
%{python_sitearch}/gridfs

%changelog
