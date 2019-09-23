#
# spec file for package python2-pandas
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
%define         skip_python3 1
%define         oldpython python
Name:           python2-pandas
Version:        0.24.2
Release:        0
Summary:        Python data structures for data analysis, time series, and statistics
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pandas.pydata.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pandas/pandas-%{version}.tar.gz
Patch0:         pandas-tests-memory.patch
BuildRequires:  %{python_module Cython >= 0.28.2}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module XlsxWriter}
BuildRequires:  %{python_module beautifulsoup4 >= 4.2.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy-devel >= 1.15.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.5}
BuildRequires:  %{python_module pytz >= 2011k}
BuildRequires:  %{python_module setuptools >= 24.2.0}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xlrd}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       python2-Cython >= 0.28.2
Requires:       python2-Tempita
Requires:       python2-lxml
Requires:       python2-numpy >= 1.15.0
Requires:       python2-python-dateutil >= 2.5
Requires:       python2-pytz >= 2011k
Requires:       python2-six
Recommends:     python2-Bottleneck
Recommends:     python2-Jinja2
Recommends:     python2-SQLAlchemy >= 0.8.1
Recommends:     python2-XlsxWriter
Recommends:     python2-backports.lzma
Recommends:     python2-beautifulsoup4 >= 4.2.1
Recommends:     python2-blosc
Recommends:     python2-boto
Recommends:     python2-google-api-python-client
Recommends:     python2-html5lib
Recommends:     python2-matplotlib
Recommends:     python2-numexpr >= 2.1
Recommends:     python2-oauth2client
Recommends:     python2-openpyxl >= 2.4
Recommends:     python2-pandas-gbq
Recommends:     python2-python-gflags
Recommends:     python2-s3fs
Recommends:     python2-scipy
Recommends:     python2-tables >= 3.0.0
Recommends:     python2-xarray >= 0.7.0
Recommends:     python2-xlrd
Recommends:     python2-xlwt
Recommends:     xclip
Obsoletes:      python2-pandas-doc < %{version}
Provides:       python2-pandas-doc = %{version}
Obsoletes:      %{oldpython}-pandas-doc < %{version}
Provides:       %{oldpython}-pandas-doc = %{version}
Obsoletes:      %{oldpython}-pandas < %{version}
Provides:       %{oldpython}-pandas = %{version}
%python_subpackages

%description
Pandas is a Python package providing data structures designed for
working with structured (tabular, multidimensional, potentially
heterogeneous) and time series data. It is a high-level building
block for doing data analysis in Python.


%prep
%setup -q -n pandas-%{version}
%patch0 -p1
sed -i -e '/^#!\//, 1d' pandas/core/computation/eval.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# skip test that tries to compile stuff in buildroot test_oo_optimizable
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} xvfb-run py.test-%{$python_version} -v %{buildroot}%{$python_sitearch}/pandas/tests -k 'not test_oo_optimizable'

%files %{python_files}
%license LICENSE
%doc doc/README.rst RELEASE.md
%{python_sitearch}/pandas/
%{python_sitearch}/pandas-%{version}-py*.egg-info

%changelog
