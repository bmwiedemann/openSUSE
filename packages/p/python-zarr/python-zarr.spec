#
# spec file for package python-zarr
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-zarr
Version:        2.13.3
Release:        0
Summary:        An implementation of chunked, compressed, N-dimensional arrays for Python
License:        MIT
URL:            https://github.com/zarr-developers/zarr-python
Source:         https://files.pythonhosted.org/packages/source/z/zarr/zarr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  %{python_module setuptools_scm > 1.5.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Needs full python stdlib, base is not enough
Requires:       python >= 3.8
Requires:       python-asciitree
Requires:       python-dbm
Requires:       python-fasteners
Requires:       python-numcodecs >= 0.6.4
Requires:       python-numpy >= 1.7
Suggests:       python-fsspec >= 0.8.4
Suggests:       python-ipytree
Suggests:       python-msgpack
Suggests:       python-notebook
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module asciitree}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module fasteners}
BuildRequires:  %{python_module fsspec >= 0.8.4}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module numcodecs >= 0.6.4}
BuildRequires:  %{python_module numpy >= 1.7}
BuildRequires:  %{python_module pytest}
# Needs full python stdlib, base is not enough
BuildRequires:  %{pythons} >= 3.8
# /SECTION
%python_subpackages

%description
An implementation of chunked, compressed, N-dimensional arrays for Python.

%prep
%autosetup -p1 -n zarr-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/zarr
%{python_sitelib}/zarr-%{version}*-info

%changelog
