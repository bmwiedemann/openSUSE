#
# spec file for package python-pyftpdlib
#
# Copyright (c) 2023 SUSE LLC
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
%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-pyftpdlib
Version:        1.5.7
Release:        0
Summary:        Asynchronous FTP server library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/giampaolo/pyftpdlib/
Source:         https://files.pythonhosted.org/packages/source/p/pyftpdlib/pyftpdlib-%{version}.tar.gz
Source1:        keycert.pem
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pysendfile}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyOpenSSL
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-pysendfile
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-ipaddress
BuildRequires:  python-mock
%endif
%ifpython2
Requires:       python-ipaddress
%endif
%python_subpackages

%description
The Python FTP server library provides a high-level interface to
write very asynchronous FTP servers with Python.

%prep
%setup -q -n pyftpdlib-%{version}
sed -i '1 {/env python/ d}' pyftpdlib/test/*.py pyftpdlib/_compat.py
cp %{SOURCE1} pyftpdlib/test

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ftpbench
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Note: Do not remove tests. Other packages import them

%check
## # Tests reported as randomly failing in 2016 against v1.5.0:
## # https://github.com/giampaolo/pyftpdlib/issues/386
## # If they re-occur, please update the issue with backtraces,
## # and disable only related tests.
## donttest="(TestFtpStoreDataTLSMixin and test_rest_on_stor)"
## donttest+=" or (TestFtpStoreDataTLSMixin and test_stor_ascii)"
## # https://github.com/giampaolo/pyftpdlib/issues/550
## donttest+=" or test_masquerade_address"
## ignorebuild="--ignore build"
## %%{python_expand # expand to python flavor, not to the binary name, then strip the trailing _
## builddir=_build.$python_
## ignorebuild+=" --ignore ${builddir%%_}"
## }
## cat > pytest.ini <<EOF
## [pytest]
## addopts =
##   -rs -v
##   -k "not ($donttest)"
##   $ignorebuild
## EOF
## %%{python_expand # pytest macro does not work. The tests parse CLI args and fail if there are any unknown program args
## export PYTHONPATH=%%{buildroot}%%{$python_sitelib}
## export PYTHONDONTWRITEBYTECODE=1
## # gh#giampaolo/pyftpdlib#540
## export PYTEST_ADDOPTS="-k 'not (TestFtpListingCmdsTLSMixin or TestConfigurableOptions or TestFtpStoreDataTLSMixin)'"
## # gh#giampaolo/pyftpdlib#478
## export TZ=GMT+1
## $python -m pytest
## }

%post
%python_install_alternative ftpbench

%postun
%python_uninstall_alternative ftpbench

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/ftpbench
%{python_sitelib}/*

%changelog
