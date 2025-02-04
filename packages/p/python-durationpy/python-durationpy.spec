#
# spec file for package python-durationpy
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

%{?sle15_python_module_pythons}
Name:           python-durationpy
Version:        0.9 
Release:        0
Summary:        Module for converting between datetime.timedelta and Go's Duration strings
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
URL:            https://github.com/icholy/durationpy
Source:         https://github.com/icholy/durationpy/archive/refs/tags/%{version}.tar.gz#/durationpy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 21.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Module for converting between datetime.timedelta and Go's Duration strings.

%prep
%autosetup -p1 -n durationpy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test.py


%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/durationpy
%{python_sitelib}/durationpy-%{version}.dist-info

%changelog
