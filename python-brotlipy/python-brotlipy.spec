#
# spec file for package python-brotlipy
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
Name:           python-brotlipy
Version:        0.7.0
Release:        0
Summary:        Python binding to the Brotli library
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/python-hyper/brotlipy
Source0:        https://pypi.io/packages/source/b/brotlipy/brotlipy-%{version}.tar.gz
# Copy of https://github.com/google/brotli/tree/46c1a881b41bb638c76247558aa04b1591af3aa7/tests/testdata
Source1:        testdata.tgz
Source2:        https://raw.githubusercontent.com/python-hyper/brotlipy/master/test/conftest.py
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-enum34
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.0.0
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
This library contains Python bindings for the reference Brotli
encoder/decoder.
This allows Python software to use the Brotli compression algorithm
directly from Python code.

%prep
%setup -q -n brotlipy-%{version}
mv libbrotli/LICENSE LICENSE.libbrotli
cp %{SOURCE2} test/
cd libbrotli
mkdir -p tests
cd tests
tar -xzf %{SOURCE1}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# the skipped tests are benchmarks which can be flaky in OBS
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m pytest -k 'not (test_streaming_compression or test_streaming_compression_flush)'

%files %{python_files}
%license LICENSE LICENSE.libbrotli
%doc README.rst
%{python_sitearch}/brotli
%{python_sitearch}/brotlipy-%{version}-py%{py_ver}.egg-info

%changelog
