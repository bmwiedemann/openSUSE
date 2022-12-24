#
# spec file for package python-pyppmd
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pyppmd
Version:        1.0.0
Release:        0
Summary:        PPMd compression/decompression library
License:        LGPL-2.1-or-later
URL:            https://codeberg.org/miurahr/pyppmd
Source:         https://files.pythonhosted.org/packages/source/p/pyppmd/pyppmd-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 58.0}
BuildRequires:  %{python_module setuptools_scm >= 6.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-timeout}
# /SECTION
%python_subpackages

%description
The pyppmd module provides classes and functions for compressing and
decompressing text data, using PPM(Prediction by partial matching)
compression algorithm which has several variations of implementations.
PPMd is the implementation by Dmitry Shkarin. PyPPMD use Igor Pavlov's
range coder introduced in 7-zip.

The API is similar to Python's bz2/lzma/zlib module.

Some parts of th codes are derived from 7-zip, pyzstd and ppmd-cffi.

%prep
%setup -q -n pyppmd-%{version}
# increase test deadline for slow obs executions (e.g. on s390x)
echo "

import hypothesis
hypothesis.settings.register_profile(
    'obs',
    deadline=5000,
    suppress_health_check=[hypothesis.HealthCheck.too_slow]
)
" >> tests/conftest.py
sed -i 's/milliseconds=300/milliseconds=5000/g' tests/test_fuzzer.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch --hypothesis-profile=obs

%files %{python_files}
%doc Changelog.rst README.rst
%license LICENSE
%{python_sitearch}/pyppmd
%{python_sitearch}/pyppmd-%{version}.dist-info

%changelog
