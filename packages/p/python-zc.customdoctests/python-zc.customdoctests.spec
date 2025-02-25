#
# spec file for package python-zc.customdoctests
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-zc.customdoctests
Version:        1.0.1
Release:        0
Summary:        Use doctest with other languages
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/zc.customdoctests
Source:         https://files.pythonhosted.org/packages/source/z/zc.customdoctests/zc.customdoctests-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
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
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -r %{buildroot}%{$python_sitelib}/zc.customdoctests-%{version}-py3.12-nspkg.pth

%check
%{python_expand export PYTHONPATH='.:%{buildroot}%{$python_sitelib}'
$python -m unittest -v zc.customdoctests.tests.test_suite
$python -m doctest -v src/zc/customdoctests/tests.py
}

%files %{python_files}
%license LICENSE.txt
%doc README.txt
%dir %{python_sitelib}/zc
%{python_sitelib}/zc/customdoctests
%{python_sitelib}/zc.customdoctests-%{version}*info

%changelog
