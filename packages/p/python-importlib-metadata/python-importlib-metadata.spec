#
# spec file for package python-importlib-metadata
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if %{python3_version_nodots} >= 38
%define skip_python3 1
%endif
Name:           python-importlib-metadata
Version:        0.21
Release:        0
Summary:        Tool to read metadata from Python packages
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://gitlab.com/python-devs/importlib_metadata
Source:         https://files.pythonhosted.org/packages/source/i/importlib_metadata/importlib_metadata-%{version}.tar.gz
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zipp >= 0.5}
BuildRequires:  fdupes
BuildRequires:  python-importlib_resources
BuildRequires:  python-rpm-macros
BuildRequires:  python2-configparser
BuildRequires:  python2-contextlib2
Requires:       python-zipp >= 0.5
Provides:       python-importlib_metadata = %{version}
BuildArch:      noarch
%if %{?suse_version} <= 1500
BuildRequires:  python3-importlib_resources
%endif
%if 0%{?suse_version} < 1500
BuildRequires:  %{python_module pathlib2}
%else
BuildRequires:  python-pathlib2
%endif
%if %{python3_version_nodots} < 35
Requires:       python-pathlib2
%endif
%ifpython2
Requires:       python-configparser
Requires:       python-contextlib2
Requires:       python-pathlib2
%endif
%python_subpackages

%description
importlib_metadata is a library to access the metadata for a Python
package.  It is intended to be ported to Python 3.8.

%prep
%setup -q -n importlib_metadata-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
