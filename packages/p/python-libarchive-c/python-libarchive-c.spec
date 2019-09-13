#
# spec file for package python-libarchive-c
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without test
Name:           python-libarchive-c
Version:        2.8
Release:        0
Summary:        Python interface to libarchive
License:        CC0-1.0
Group:          Development/Languages/Python
URL:            https://github.com/Changaco/python-libarchive-c
Source:         https://files.pythonhosted.org/packages/source/l/libarchive-c/libarchive-c-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libarchive-devel
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  libarchive-devel
%endif
%python_subpackages

%description
A Python interface to libarchive. It uses the standard ctypes_ module to
dynamically load and access the C library.

%prep
%setup -q -n libarchive-c-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.md
%{python_sitelib}/*

%changelog
