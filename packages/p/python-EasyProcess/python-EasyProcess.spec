#
# spec file for package python-EasyProcess
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
Name:           python-EasyProcess
Version:        0.2.7
Release:        0
Summary:        Python subprocess interface
License:        BSD-2-Clause
URL:            https://github.com/ponty/easyprocess
Source:         https://github.com/ponty/EasyProcess/archive/%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  iputils
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
BuildArch:      noarch
%python_subpackages

%description
EasyProcess is a Python subprocess interface.

Features include:
 - layer on top of subprocess module
 - starting and stopping of programs
 - retrieval of standard output/error, return code of programs
 - command can be list or string
 - logging
 - timeout
 - unit-tests
 - cross-platform, development on linux
 - global config file with program aliases
 - unicode support
 - supported python versions: 2.5, 2.6, 2.7, 3.1, 3.2, PyPy

Limitations:
 - shell is not supported
 - pipes are not supported
 - stdout/stderr is set only after the subprocess has finished
 - stop() does not kill whole subprocess tree

%prep
%setup -q -n EasyProcess-%{version}
# https://github.com/ponty/EasyProcess/issues/18
sed -i "s/from easyprocess import EasyProcess/from easyprocess import EasyProcess;import sys/" easyprocess/examples/*.py
sed -i "s/'python /sys.executable + ' /" easyprocess/examples/*.py
sed -i "s/'python'/sys.executable/" easyprocess/examples/*.py

# requires pyvirtualdisplay which is mostly dead package
rm -f tests/coverage/fast/test_deadlock.py
2to3 -w easyprocess/examples/log.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v tests/coverage/

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
