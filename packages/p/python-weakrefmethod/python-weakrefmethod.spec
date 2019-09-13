#
# spec file for package python-weakrefmethod
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


Name:           python-weakrefmethod
Version:        1.0.3
Release:        0
Summary:        A WeakMethod class for storing bound methods using weak references
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://github.com/twang817/weakrefmethod
Source:         https://files.pythonhosted.org/packages/source/w/weakrefmethod/weakrefmethod-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
# test requirements
BuildRequires:  python-unittest2
Provides:       python2-weakrefmethod = %{version}
BuildArch:      noarch

%description
Python 3.4 include a ``WeakMethod`` class, for storing bound methods using weak references
(see the `Python weakref module <http://docs.python.org/library/weakref.html>`_).

This project is a backport of the WeakMethod class, and tests, for Python 2.6. The tests
require the `unittest2 package <http://pypi.python.org/pypi/unittest2>`_.

* Github repository & issue tracker: https://github.com/twang817/weakrefmethod

%prep
%setup -q -n weakrefmethod-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python setup.py test

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
