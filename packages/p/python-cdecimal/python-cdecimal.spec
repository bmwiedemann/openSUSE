#
# spec file for package python-cdecimal
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 LISA GmbH, Bingen, Germany.
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


# This package doesn't support py3k correctly
%define skip_python3 1
%define modname cdecimal
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        2.3
Release:        0
Summary:        Faster drop-in replacement for Python's "decimal" module
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://www.bytereef.org/mpdecimal/index.html
Source:         http://www.bytereef.org/software/mpdecimal/releases/%{modname}-2.3.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The python-cdecimal package is a faster drop-in replacement for the decimal
module in Python's standard library for Python version above 2.4 and below 3.3.

It provides a complete implementation of Mike Cowlishaw/IBM's General Decimal
Arithmetic Specification.

Since cdecimal is compatible with decimal, the official documentation is valid:
http://docs.python.org/library/decimal.html

For the few remaining differences, see:
http://www.bytereef.org/mpdecimal/doc/cdecimal/index.html

Please note: cdecimal has been integrated into CPython 3.3, where it supersedes
the pure Python version. If you need maximum decimal performance, you should
use that Python version.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install

# Most of the tests do not have a redistribution license, so
# they are not included in mpdecimal.

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.txt README.txt
%{python_sitearch}/*

%changelog
