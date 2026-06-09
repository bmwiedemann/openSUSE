#
# spec file for package python-smart-open
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        7.6.1
Release:        0
Summary:        Python utils for streaming large files
License:        MIT
URL:            https://github.com/piskvorky/smart_open
Source:         https://github.com/piskvorky/smart_open/archive/refs/tags/v%{version}.tar.gz#/smart_open-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-common
Requires:       python-azure-core
Requires:       python-azure-storage-blob >= 12.7.0
Requires:       python-boto3 >= 1.9.17
Requires:       python-google-cloud-storage >= 2.6.0
Requires:       python-requests
Requires:       python-wrapt
%if 0%{?python_version_nodots} < 314
Requires:       python-backports.zstd
%endif
Suggests:       python-paramiko
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module azure-common}
BuildRequires:  %{python_module azure-core}
BuildRequires:  %{python_module azure-storage-blob >= 12.7.0}
BuildRequires:  %{python_module backports.zstd if %python-base < 3.14}
BuildRequires:  %{python_module boto3 >= 1.9.17}
BuildRequires:  %{python_module google-cloud-storage >= 2.6.0}
BuildRequires:  %{python_module moto >= 1.3.4}
BuildRequires:  %{python_module moto-server}
BuildRequires:  %{python_module paramiko}
# From pytest-xdist[psutil]
BuildRequires:  %{python_module psutil >= 3.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Python utils for streaming large files.
Includes support for S3, HDFS, gzip, bz2, etc.

%prep
%autosetup -p1 -n smart_open-%{version}
# Requires network, and they're self-contained
rm -rf integration-tests
# They cause havoc with our pytest macros
rm -rf ci_helpers

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/smart_open
%{python_sitelib}/smart_open-%{version}.dist-info

%changelog
