#
# spec file for package python-google-resumable-media
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-google-resumable-media
Version:        2.7.1
Release:        0
Summary:        Utilities for Google Media Downloads and Resumable Uploads
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googleapis/google-resumable-media-python
Source:         https://files.pythonhosted.org/packages/source/g/google-resumable-media/google-resumable-media-%{version}.tar.gz
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module google-crc32c}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.18.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-crc32c
Recommends:     python-aiohttp
Recommends:     python-requests >= 2.18.0
BuildArch:      noarch
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-google-resumable-media < %{version}
%endif
%python_subpackages

%description
Utilities for Google Media Downloads and Resumable Uploads

%prep
%setup -q -n google-resumable-media-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_ADDOPTS="--import-mode=importlib"
# skip online tests
donttest="test_brotli"
donttest="$donttest or test_constructor"
donttest="$donttest or test_decompress"
%pytest tests/unit -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/google_resumable_media*-info
%{python_sitelib}/google/resumable_media*
%{python_sitelib}/google/_async_resumable_media*

%changelog
