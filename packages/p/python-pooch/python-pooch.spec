#
# spec file for package python-pooch
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
%define skip_python2 1
Name:           python-pooch
Version:        1.3.0
Release:        0
Summary:        Manager for Python libraries' sample data files
License:        BSD-3-Clause
URL:            https://github.com/fatiando/pooch
Source:         https://files.pythonhosted.org/packages/source/p/pooch/pooch-%{version}.tar.gz
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
Requires:       python-packaging
Requires:       python-requests
Suggests:       python-paramiko
Suggests:       python-tqdm
BuildArch:      noarch
%python_subpackages

%description
Pooch manages sample data files for Python libraries. It automatically
downloads and stores them in a local directory, with support for versioning
and checks for corruption.

%prep
%autosetup -p1 -n pooch-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# These test the online functionality
donttest+=" or (test_core and test_retrieve)"
donttest+=" or (test_core and test_retrieve_fname)"
donttest+=" or (test_core and test_retrieve_default_path)"
donttest+=" or (test_core and test_pooch_custom_url)"
donttest+=" or (test_core and test_pooch_download)"
donttest+=" or (test_core and test_pooch_download_retry_off_by_default)"
donttest+=" or (test_core and test_pooch_download_retry)"
donttest+=" or (test_core and test_pooch_download_retry_fails_eventually)"
donttest+=" or (test_core and test_pooch_logging_level)"
donttest+=" or (test_core and test_pooch_update)"
donttest+=" or (test_core and test_pooch_corrupted)"
donttest+=" or (test_core and test_check_availability)"
donttest+=" or (test_core and test_check_availability_on_ftp)"
donttest+=" or (test_core and test_fetch_with_downloader)"
donttest+=" or (test_core and test_stream_download)"
donttest+=" or (test_integration and test_create_and_fetch)"
donttest+=" or (test_processors and test_decompress)"
donttest+=" or (test_processors and test_extractprocessor_fails)"
donttest+=" or (test_processors and Unzip or Untar)"
donttest+=" or (test_processors and test_processor_multiplefiles)"
donttest+=" or (test_downloaders and test_ftp_downloader)"
%pytest -k "not (${donttest:4})"

%files %{python_files}
%doc AUTHORS.md README.rst
%license LICENSE.txt
%{python_sitelib}/pooch
%{python_sitelib}/pooch-%{version}*-info

%changelog
