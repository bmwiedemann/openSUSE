#
# spec file for package python-smart-open
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


Name:           python-smart-open
Version:        7.0.2
Release:        0
Summary:        Python utils for streaming large files
License:        MIT
URL:            https://github.com/piskvorky/smart_open
Source:         https://github.com/piskvorky/smart_open/archive/refs/tags/v%{version}.tar.gz#/smart_open-%{version}.tar.gz
Patch0:         skip-gzip-tests-python312.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-common
Requires:       python-azure-core
Requires:       python-azure-storage-blob
Requires:       python-boto3
Requires:       python-google-cloud-storage
Requires:       python-requests
Requires:       python-wrapt
Requires:       python-zstandard
Suggests:       python-paramiko
BuildArch:      noarch
# see https://github.com/piskvorky/smart_open/issues/784
BuildRequires:  %{python_module urllib3 < 2}
Requires:       python-urllib3 < 2
# SECTION test requirements
BuildRequires:  %{python_module azure-common}
BuildRequires:  %{python_module azure-core}
BuildRequires:  %{python_module azure-storage-blob}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module google-cloud-storage}
BuildRequires:  %{python_module moto >= 1.3.4}
BuildRequires:  %{python_module moto-server}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module zstandard}
# /SECTION
%python_subpackages

%description
Python utils for streaming large files.
Includes support for S3, HDFS, gzip, bz2, etc.

%prep
%autosetup -p1 -n smart_open-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
moto_server -p5000 2>/dev/null &
server_pid=$!
export SO_ENABLE_MOTO_SERVER=1
# Requires network
%pytest -rs -k 'not (test_http_gz or test_s3_gzip_compress_sanity)' smart_open/
kill $server_pid

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/smart_open
%{python_sitelib}/smart_open-%{version}.dist-info

%changelog
