#
# spec file for package python-blobfile
#
# Copyright (c) 2026 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-blobfile
Version:        3.3.0
Release:        0
Summary:        Read GCS, ABS and local paths with the same interface
License:        Unlicense
URL:            https://github.com/blobfile/blobfile
Source:         https://files.pythonhosted.org/packages/source/b/blobfile/blobfile-%{version}.tar.gz
BuildRequires:  %{python_module filelock >= 3.0}
BuildRequires:  %{python_module lxml >= 4.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycryptodomex >= 3.8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 69}
BuildRequires:  %{python_module urllib3 >= 2}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-filelock >= 3.0
Requires:       python-lxml >= 4.9
Requires:       python-pycryptodomex >= 3.8
Requires:       python-urllib3 >= 2
BuildArch:      noarch
%python_subpackages

%description
A Python library that provides an open()-like interface for reading
local and remote files (Google Cloud Storage and Azure Blob Storage),
plus os.path- and shutil-like helpers that also accept GCS (gs://)
and Azure (az://) paths. Inspired by TensorFlow's gfile, but not an
exact clone of that API.

%prep
%autosetup -p1 -n blobfile-%{version}
# Tests live inside the importable blobfile package; keep the self-contained
# XML parser tests for %%check and drop the cloud-integration suite so it is
# not shipped.
mkdir tests
mv blobfile/_xml_test.py tests/
rm -f blobfile/_ops_test.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The main suite (_ops_test.py) talks to GCS and Azure and needs provider
# accounts (and typically docker); it cannot run in the offline OBS build.
# The XML parser tests are self-contained.
%pytest tests/_xml_test.py
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import blobfile"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/blobfile
%{python_sitelib}/blobfile-%{version}.dist-info

%changelog
