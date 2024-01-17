#
# spec file for package python-pygdbmi
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-pygdbmi
Version:        0.11.0.0
Release:        0
Summary:        Parse gdb machine interface output with Python
License:        MIT
URL:            https://github.com/cs01/pygdbmi
Source:         https://github.com/cs01/pygdbmi/archive/refs/tags/v%{version}.tar.gz#/pygdbmi-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Parse gdb machine interface output with Python

%prep
%autosetup -p1 -n pygdbmi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/pygdbmi
%{python_sitelib}/pygdbmi-%{version}.dist-info

%changelog
