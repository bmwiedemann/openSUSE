#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define         skip_python2 1
%define ghversion 2021.05.0
Name:           python-fsspec%{psuffix}
Version:        2021.5.0
Release:        0
Summary:        Filesystem specification package
License:        BSD-3-Clause
URL:            https://github.com/intake/filesystem_spec
# the tests are only in the GitHub archive
Source:         %{url}/archive/%{ghversion}.tar.gz#/fsspec-%{ghversion}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module importlib_metadata if %python-base < 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib_metadata
%endif
Suggests:       python-adlfs
Suggests:       python-aiohttp
Suggests:       python-pygit2
Suggests:       python-dropboxdrivefs
Suggests:       python-dropbox
Suggests:       python-dask
Suggests:       python-distributed
Suggests:       python-gcsfs
Suggests:       python-paramiko
Suggests:       python-requests
Suggests:       python-s3fs
Suggests:       python-smbprotocol
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module fusepy}
BuildRequires:  %{python_module gcsfs}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pyftpdlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module s3fs}
BuildRequires:  %{python_module smbprotocol}
BuildRequires:  %{python_module zstandard}
BuildRequires:  %{python_module distributed if (%python-base without python36-base)}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
BuildRequires:  %{python_module panel if (%python-base without python36-base)}
# cannot test git and http in the same installation (?)
# BuildRequires:  %%{python_module pygit2}
# BuildRequires:  git-core
%endif
%python_subpackages

%description
A specification for pythonic filesystems.

%prep
%setup -q -n filesystem_spec-%{ghversion}
# don't test nonexistent python36-numpy
sed -i -e '/^import numpy as np/ d' -e '/^import pytest/ a np = pytest.importorskip("numpy")' fsspec/tests/test_spec.py

%build
%python_build

%if ! %{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# test_basic relies on speed of FS and timeouts in OBS
donttest="test_basic"
# test_not_cached needs sockets
donttest+=" or test_not_cached"
# wants to open a socket connection to "my_instance.com"
donttest+=" or test_dbfs"
# wants to connect to ftp.fau.de
donttest+=" or test_find"
%pytest -rfEs  -k "not ($donttest)"
%endif

%if ! %{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fsspec
%{python_sitelib}/fsspec-%{version}*-info
%endif

%changelog
