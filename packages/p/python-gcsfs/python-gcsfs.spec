#
# spec file for package python-gcsfs
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-gcsfs
Version:        0.7.1
Release:        0
Summary:        Filesystem interface over GCS
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/dask/gcsfs
Source:         https://files.pythonhosted.org/packages/source/g/gcsfs/gcsfs-%{version}.tar.gz
# PATCH-FIX-UPSTREAM avoid_network_tests.patch gh#dask/gcsfs#292 mcepl@suse.com
# skip tests which require network connection
Patch0:         avoid_network_tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp
Requires:       python-decorator
Requires:       python-fsspec >= 0.8.0
Requires:       python-google-auth >= 1.2
Requires:       python-google-auth-oauthlib
Requires:       python-requests
Recommends:     dask
Recommends:     python-gcsfs-fuse = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module fsspec >= 0.8.0}
BuildRequires:  %{python_module fusepy}
BuildRequires:  %{python_module google-auth >= 1.2}
BuildRequires:  %{python_module google-auth-oauthlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module vcrpy}
BuildRequires:  libfuse2
# /SECTION
%python_subpackages

%description
File-system interface for Google Cloud Storage.

%package        fuse
Summary:        Filesystem interface over GCS - FUSE interface
Group:          Development/Languages/Python
Requires:       libfuse2
Requires:       python-click
Requires:       python-fusepy
Requires:       python-pandas

%description    fuse
File-system interface for Google Cloud Storage.

This package provides the optional FUSE interface.

%prep
%setup -q -n gcsfs-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests test_map_simple, test_map_with_data and test_map_clear_empty require a network connection
%pytest -k "not network" gcsfs/tests

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/gcsfs-%{version}-py*.egg-info
%{python_sitelib}/gcsfs/
%exclude %{python_sitelib}/gcsfs/cli/

%files %{python_files fuse}
%license LICENSE.txt
%{python_sitelib}/gcsfs/cli/

%changelog
