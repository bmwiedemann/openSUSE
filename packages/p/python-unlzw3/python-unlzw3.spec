#
# spec file for package python-unlzw3
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define pyname unlzw3
Name:           python-%{pyname}
Version:        0.2.3
Release:        0
Summary:        Pure Python decompression module for .Z files
License:        BSD-3-Clause
URL:            https://github.com/scivision/%{pyname}
Source:         https://github.com/scivision/%{pyname}/archive/refs/tags/v%{version}.tar.gz#/%{pyname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pure Python decompression module for .Z files compressed using Unix
compress utility. Unlike the faster but Linux-specific unlzw using
Python CFFI, unlzw3 is slower but works on any platform that runs
Python including Windows.

%prep
%autosetup -n %{pyname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -rs --tb=short

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{pyname}
%{python_sitelib}/%{pyname}-%{version}.dist-info

%changelog
