#
# spec file for package python-gnssanalysis
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
%define pyname ncompress
Name:           python-%{pyname}
Version:        1.0.2
Release:        0
Summary:        LZW compression and decompression in Python and C++
License:        BSD-3-Clause
URL:            https://github.com/valgur/%{pyname}
Source:         https://github.com/valgur/%{pyname}/archive/refs/tags/v%{version}.tar.gz#/%{pyname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module nanobind >= 1.3.2}
BuildRequires:  %{python_module nanobind-devel >= 1.3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-build-core >= 0.4.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake >= 3.18
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
LZW compression and decompression in Python and C++.

Ported with minimal changes from the (N)compress CLI tool.

%prep
%autosetup -n %{pyname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -rs --tb=short

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/%{pyname}
%{python_sitearch}/%{pyname}-%{version}.dist-info

%changelog
