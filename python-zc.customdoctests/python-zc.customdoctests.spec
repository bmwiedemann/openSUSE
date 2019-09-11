#
# spec file for package python-zc.customdoctests
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-zc.customdoctests
Version:        1.0.1
Release:        0
License:        ZPL-2.1
Summary:        zc.customdoctests -- Use doctest with other languages
Url:            http://pypi.python.org/pypi/zc.customdoctests
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/z/zc.customdoctests/zc.customdoctests-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module manuel}
BuildRequires:  unzip
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
doctest (and recently manuel) provide hooks for using custom doctest
parsers.  `zc.customdoctests` helps to leverage this to support other
languages, such as JavaScript::

    js> function double (x) {
    ...     return x*2;
    ... }
    js> double(2)
    4

And with `manuel <http://pypi.python.org/pypi/manuel>`_, it
facilitates doctests that mix multiple languages, such as Python,
JavaScript, and sh.

%prep
%setup -q -n zc.customdoctests-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license ../../SOURCES/LICENSE.txt
%doc README.txt
%{python_sitelib}/*

%changelog
