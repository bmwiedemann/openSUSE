#
# spec file for package python-gcsfs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-gcsfs
Version:        0.3.0
Release:        0
License:        BSD-3-Clause
Summary:        Filesystem interface over GCS
Url:            https://github.com/dask/gcsfs
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/g/gcsfs/gcsfs-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module fsspec >= 0.2.2}
BuildRequires:  %{python_module fusepy}
BuildRequires:  %{python_module google-auth >= 1.2}
BuildRequires:  %{python_module google-auth-oauthlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module vcrpy}
BuildRequires:  libfuse2
# /SECTION
BuildRequires:  fdupes
Requires:       python-decorator
Requires:       python-fsspec >= 0.2.2
Requires:       python-google-auth >= 1.2
Requires:       python-google-auth-oauthlib
Requires:       python-requests
Recommends:     dask
Recommends:     python-gcsfs-fuse = %{version}
BuildArch:      noarch

%python_subpackages

%description
File-system interface for Google Cloud Storage.

%package        fuse
Summary:        Filesystem interface over GCS - FUSE interface
Requires:       libfuse2
Requires:       python-click
Requires:       python-fusepy
Requires:       python-pandas

%description    fuse
File-system interface for Google Cloud Storage.

This package provides the optional FUSE interface.

%prep
%setup -q -n gcsfs-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests require a network connection
# %%check
# %%python_expand pytest-%%{$python_bin_suffix} -vv -x  gcsfs

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
