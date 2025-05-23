#
# spec file for package python-fsspec
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%define skip_python39 1
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without have_pyarrow

%{?sle15_python_module_pythons}
Name:           python-fsspec%{psuffix}
Version:        2024.3.1
Release:        0
Summary:        Filesystem specification package
License:        BSD-3-Clause
URL:            https://github.com/fsspec/filesystem_spec
# the tests are only in the GitHub archive
Source:         https://github.com/fsspec/filesystem_spec/archive/%{version}.tar.gz#/fsspec-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  fuse
BuildRequires:  python-rpm-macros
Requires:       fuse
Suggests:       python-adlfs
Suggests:       python-aiohttp
Suggests:       python-dask
Suggests:       python-distributed
Suggests:       python-dropbox
Suggests:       python-dropboxdrivefs
Suggests:       python-gcsfs
Suggests:       python-paramiko
Suggests:       python-pygit2
Suggests:       python-requests
Suggests:       python-s3fs
Suggests:       python-smbprotocol
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module distributed}
BuildRequires:  %{python_module fastparquet}
BuildRequires:  %{python_module fusepy}
BuildRequires:  %{python_module gcsfs}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module mistune}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module panel}
BuildRequires:  %{python_module paramiko}
%if %{with have_pyarrow}
BuildRequires:  %{python_module pyarrow}
%endif
BuildRequires:  %{python_module pyftpdlib}
BuildRequires:  %{python_module pygit2}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module requests}
BuildRequires:  git-core
# Too tight of a aiobotocore pinning: gh#fsspec/s3fs#615, gh#aio-libs/aiobotocore#971
#BuildRequires:  %%{python_module s3fs}
BuildRequires:  %{python_module smbprotocol}
BuildRequires:  %{python_module zstandard}
# cannot test git and http in the same installation (?)
# BuildRequires:  %%{python_module pygit2}
# BuildRequires:  git-core
%endif
%python_subpackages

%description
A specification for pythonic filesystems.

%prep
%autosetup -p1 -n filesystem_spec-%{version}

%build
%pyproject_wheel

%if ! %{with test}
%install
%pyproject_install
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
# does not like the '.' from the version in the build path
donttest+=" or (test_local and test_make_path_posix)"
# no fuse module loaded
donttest+=" or test_fuse"
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
