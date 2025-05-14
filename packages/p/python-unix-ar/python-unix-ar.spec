#
# spec file for package python-unix_ar
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-unix-ar
Version:        0.2.1
Release:        0
Summary:        AR file handling
License:        BSD-3-Clause
URL:            https://github.com/getninjas/unix_ar
Source:         https://files.pythonhosted.org/packages/source/u/unix-ar/unix_ar-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
AR file handling

%prep
%autosetup -p1 -n unix_ar-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%{python_sitelib}/unix_ar.py
%{python_sitelib}/unix_ar-%{version}.dist-info
%{python_sitelib}/__pycache__/*

%changelog
