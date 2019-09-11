#
# spec file for package python-pyftpdlib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 LISA GmbH, Bingen, Germany.
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
# Tests randomly fail: https://github.com/giampaolo/pyftpdlib/issues/386
%bcond_with     test
Name:           python-pyftpdlib
Version:        1.5.5
Release:        0
Summary:        Asynchronous FTP server library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/giampaolo/pyftpdlib/
Source:         https://files.pythonhosted.org/packages/source/p/pyftpdlib/pyftpdlib-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pysendfile}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-ipaddress
BuildRequires:  python-mock
BuildRequires:  python-rpm-macros
Requires:       python-pyOpenSSL
Recommends:     python-pysendfile
%ifpython2
Requires:       python-ipaddress
%endif
BuildArch:      noarch
%python_subpackages

%description
The Python FTP server library provides a high-level interface to
write very asynchronous FTP servers with Python.

%prep
%setup -q -n pyftpdlib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export PYTHONPATH=$PWD
%python_exec pyftpdlib/test/runner.py
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/ftpbench
%{python_sitelib}/*

%changelog
