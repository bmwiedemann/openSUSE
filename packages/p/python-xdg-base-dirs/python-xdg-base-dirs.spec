#
# spec file for package python-xdg-base-dirs
#
# Copyright (c) 2024 SUSE LLC
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
%define modname xdg-base-dirs
Name:           python-xdg-base-dirs
Version:        6.0.1
Release:        0
Summary:        Variables defined by the XDG Base Directory Specification
License:        ISC
URL:            https://github.com/srstevenson/xdg-base-dirs
Source:         https://github.com/srstevenson/%{modname}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Provides:       python-xdg = %{version}-%{release}
Obsoletes:      python-xdg < %{version}-%{release}
%python_subpackages

%description
xdg is a Python module which provides the variables defined by the
XDG Base Directory Specification, to save you from duplicating the
same snippet of logic in every Python utility you write that deals
with user cache, configuration, or data files. It has no external
dependencies.

%prep
%autosetup -p1 -n %{modname}-%{version}

sed -i -e '/addopts.*--cov/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%{python_sitelib}/xdg_base_dirs
%{python_sitelib}/xdg_base_dirs-%{version}*-info

%changelog
