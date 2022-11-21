#
# spec file for package python-gcsfs
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-gcsfs
Version:        2022.11.0
Release:        0
Summary:        Filesystem interface over GCS
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/fsspec/gcsfs
# Use the GitHub tarball for test data
Source:         https://github.com/fsspec/gcsfs/archive/refs/tags/%{version}.tar.gz#/gcsfs-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp
Requires:       python-decorator > 4.1.2
Requires:       python-fsspec = %{version}
Requires:       python-google-auth >= 1.2
Requires:       python-google-auth-oauthlib
Requires:       python-google-cloud-storage
Requires:       python-requests
Recommends:     dask
Recommends:     python-gcsfs-fuse = %{version}
Suggests:       python-crcmod
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module decorator > 4.1.2}
BuildRequires:  %{python_module fsspec == %{version}}
BuildRequires:  %{python_module fusepy}
BuildRequires:  %{python_module google-api-core}
BuildRequires:  %{python_module google-api-python-client}
BuildRequires:  %{python_module google-auth >= 1.2}
BuildRequires:  %{python_module google-auth-oauthlib}
BuildRequires:  %{python_module google-cloud-storage}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  fake-gcs-server
# /SECTION
%python_subpackages

%description
File-system interface for Google Cloud Storage.

%package        fuse
Summary:        Filesystem interface over GCS - FUSE interface
Group:          Development/Languages/Python
Requires:       python-click
Requires:       python-fusepy

%description    fuse
File-system interface for Google Cloud Storage.

This package provides the optional FUSE interface.

%prep
%autosetup -p1 -n gcsfs-%{version}
sed -i 's/--color=yes//' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/fsspec/gcsfs/blob/main/docs/source/developer.rst
fake-gcs-server \
  -backend memory \
  -scheme http \
  -public-host http://localhost:4443 \
  -external-url http://localhost:4443 \
  >$PWD/fake-gcs-server.stdout 2>$PWD/fake-gcs-server.stderr &
trap "jobs; kill %1 || true" EXIT
export STORAGE_EMULATOR_HOST=http://localhost:4443
export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/gcsfs/tests/fake-secret.json
# Don't test fuse, it hangs on mounting inside obs
donttest="test_fuse"
# finds an existing path on the non-first multiflavor test runs"
donttest+=" or test_mkdir_with_path"
%pytest -rfEs -k "not ($donttest)"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/gcsfs-%{version}*-info
%{python_sitelib}/gcsfs/
%exclude %{python_sitelib}/gcsfs/cli/

%files %{python_files fuse}
%license LICENSE.txt
%{python_sitelib}/gcsfs/cli/

%changelog
