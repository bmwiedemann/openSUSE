#
# spec file for package python-sgmllib3k
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sgmllib3k
Version:        1.0.0
Release:        0
Summary:        Python 3 port of sgmllib
License:        Python-2.0 and BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/hsoft/sgmllib
Source:         https://files.pythonhosted.org/packages/source/s/sgmllib3k/sgmllib3k-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/hsoft/sgmllib/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python2-devel
BuildRequires:  python3-testsuite
BuildRequires:  python3-tools
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python 3 port of Python 2's standard library `sgmllib`.

%prep
%setup -q -n sgmllib3k-%{version}
cp %{SOURCE1} .

cp %{_libdir}/python2.7/test/test_sgmllib.py .
cp %{_libdir}/python2.7/test/sgml_input.html .
sed -i 's/from test import test_support/from test import support as test_support/' test_sgmllib.py

# Disable one test failing with
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 2873: invalid continuation byte
sed -i 's/test_read_chunks/_test_read_chunks/' test_sgmllib.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/*

%changelog
