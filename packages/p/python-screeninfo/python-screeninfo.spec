#
# spec file for package python-screeninfo
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


Name:           python-screeninfo
Version:        0.8.1
Release:        0
Summary:        Fetch location and size of physical screens
License:        MIT
URL:            https://github.com/rr-/screeninfo
Source0:        https://github.com/rr-/screeninfo/archive/refs/tags/%{version}.tar.gz#/screeninfo-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Cython
Suggests:       python-dataclasses
Suggests:       python-pyobjc-framework-Cocoa
BuildArch:      noarch
%if 0%{?suse_version} <= 1500
BuildRequires:  %{python_module dataclasses}
%endif
%python_subpackages

%description
Python module to fetch location and size of physical screens.

%prep
%autosetup -p1 -n screeninfo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/screeninfo
%{python_sitelib}/screeninfo-%{version}*-info

%changelog
