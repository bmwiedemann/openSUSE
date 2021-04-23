#
# spec file for package python-python-lzo
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-python-lzo
Version:        1.12
Release:        0
Summary:        Python bindings for the LZO data compression library
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/jd-boyd/python-lzo
Source:         https://files.pythonhosted.org/packages/source/p/python-lzo/python-lzo-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  lzo-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This module provides Python bindings for the LZO data compression library.

LZO is a lossless data compression library. Decompression requires no
memory. Different compression levels can be used to achieve better
ratios at the expense of time.

%prep
%setup -q -n python-lzo-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests/test.py

%files %{python_files}
%doc NEWS
%license COPYING
%{python_sitearch}/*

%changelog
