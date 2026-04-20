#
# spec file for package python-packaging-legacy
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


Name:           python-packaging-legacy
Version:        23.0.post0
Release:        0
Summary:        Core utilities for legacy Python packages
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://github.com/di/packaging_legacy
Source:         https://files.pythonhosted.org/packages/source/p/packaging-legacy/packaging_legacy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 40.6.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module packaging >= 23.0}
BuildRequires:  %{python_module pretend}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging >= 23.0
BuildArch:      noarch
%python_subpackages

%description
Core utilities for legacy Python packages

%prep
%autosetup -p1 -n packaging_legacy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.md
%{python_sitelib}/packaging_legacy
%{python_sitelib}/packaging_legacy-%{version}.dist-info

%changelog
