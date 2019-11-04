#
# spec file for package python-random2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-random2
Version:        1.0.1
Release:        0
Summary:        A Session and Caching library with WSGI Middleware
License:        Python-2.0
URL:            https://pypi.python.org/pypi/random2
Source:         https://files.pythonhosted.org/packages/source/r/random2/random2-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
This package provides a Python 3 ported version of Python 2.7's random module.
It has also been back-ported to work in Python 2.6.

In Python 3, the implementation of randrange() was changed, so that even with
the same seed you get different sequences in Python 2 and 3. Note that several
high-level functions such as randint() and choice() use randrange().

In my testing code I heavily rely on stable random generator results and it
makes porting code to Python 3 a lot harder, if all those tests have to be
adjusted. This package fixes that.

%prep
%setup -q -n random2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt README.txt PKG-INFO
%{python_sitelib}/*

%changelog
