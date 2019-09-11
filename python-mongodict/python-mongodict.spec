#
# spec file for package python-mongodict
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


Name:           python-mongodict
Version:        0.3.1
Release:        0
Summary:        MongoDB-backed Python dict-like interface
License:        GPL-3.0
Group:          Development/Languages/Python
Url:            https://github.com/turicas/mongodict/
Source:         https://pypi.python.org/packages/source/m/mongodict/mongodict-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-pymongo
Requires:       python-pymongo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
So you are storing some key-values in a dict but your data became huge than
your memory or you want to persist it on the disk? Then mongodict is for you!

As it uses MongoDB to store the data, you get all cool MongoDB things, like
shardings and replicas. It uses the pickle module available on Python standard
library to serialize/deserialize data and store everything as bson.Binary in
MongoDB.  You can also provide another codec (serializer/deserializer).

%prep
%setup -q -n mongodict-%{version}
# remove unwanted executable bit
chmod -x migrate_data.py

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE CHANGELOG.rst migrate_data.py
%{python_sitelib}/*

%changelog
