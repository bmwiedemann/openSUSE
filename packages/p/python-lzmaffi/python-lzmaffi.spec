#
# spec file for package python-lzmaffi
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lzmaffi
Version:        0.3.0
Release:        0
Summary:        Port of Python 3.3's 'lzma' module for XZ/LZMA compressed files to cffi
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/r3m0t/backports.lzma
Source:         https://files.pythonhosted.org/packages/source/l/lzmaffi/lzmaffi-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/r3m0t/backports.lzma/v0.0.3/LICENSE
BuildRequires:  %{python_module cffi >= 0.6}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
BuildRequires:  xz-devel
Requires:       python-cffi >= 0.6
%python_subpackages

%description
This is a port of the 'lzma' module included in Python 3.3 or later
by Nadeem Vawda and Per Oyvind Karlsen, which provides a Python wrapper for XZ Utils
(aka LZMA Utils v2) by Igor Pavlov.

Unlike backports.lzma which is a straight backport, this version uses cffi which means
it runs on PyPy without having to use the (very slow) CPyExt. It also runs perfectly
well on CPython 2.6, 2.7 or 3.

%prep
%setup -q -n lzmaffi-%{version}
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd test
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test_lzma.py

%files %{python_files}
%license LICENSE
%{python_sitearch}/lzmaffi-%{version}-py*.egg-info
%{python_sitearch}/lzmaffi/
%{python_sitearch}/_lzmaffi_mods/

%changelog
