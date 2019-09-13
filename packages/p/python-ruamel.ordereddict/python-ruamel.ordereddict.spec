#
# spec file for package python-ruamel.ordereddict
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-ruamel.ordereddict
Version:        0.4.14
Release:        0
Summary:        Ordered dictionary
License:        MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/ruamel/ordereddict
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.ordereddict/ruamel.ordereddict-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-ruamel.base
BuildRequires:  python-setuptools
Requires:       python-ruamel.base
Provides:       python2-ruamel.ordereddict = %{version}

%description
This is an implementation of an ordered dictionary with Key Insertion Order
(KIO: updates of values do not affect the position of the key), Key Value
Insertion Order (KVIO, an existing key’s position is removed and put at the
back). The standard library module OrderedDict, implemented later, implements
a subset of ordereddict functionality.

Sorted dictionaries are also provided. Currently only with Key Sorted Order
(KSO, no sorting function can be specified, but you can specify a transform to
apply on the key before comparison (e.g. string.lower)).

%prep
%setup -q -n ruamel.ordereddict-%{version}
rm -rf *egg-info

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
