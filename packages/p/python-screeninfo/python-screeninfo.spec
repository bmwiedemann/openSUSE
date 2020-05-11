#
# spec file for package python-screeninfo
#
# Copyright (c) 2020 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-screeninfo
Version:        0.6.5
Release:        0
Summary:        Fetch location and size of physical screens
License:        MIT
URL:            https://github.com/rr-/screeninfo
Source0:        https://github.com/rr-/screeninfo/archive/%{version}.tar.gz#/screeninfo-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/rr-/screeninfo/pull/36 -- Use dataclass when needed
Patch0:         use_dataclasses_when_needed.patch
BuildRequires:  %{python_module setuptools}
%if 0%{?suse_version} <= 1500
BuildRequires:  %{python_module dataclasses}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python module to fetch location and size of physical screens.

%prep
%setup -q -n screeninfo-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# upstream does not provide any tests

%files %{python_files}
%license LICENSE.md
%doc README.md
%dir %{python_sitelib}/screeninfo/
%dir %{python_sitelib}/screeninfo/enumerators/
%{python_sitelib}/screeninfo-%{version}-py%{python_version}.egg-info/
%{python_sitelib}/screeninfo/*.py*
%{python_sitelib}/screeninfo/enumerators/*.py*
%pycache_only %{python_sitelib}/screeninfo/__pycache__/
%pycache_only %{python_sitelib}/screeninfo/enumerators/__pycache__/

%changelog
