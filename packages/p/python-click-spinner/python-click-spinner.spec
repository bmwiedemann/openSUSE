#
# spec file for package python-click-spinner
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


Name:           python-click-spinner
# tests and LICENSE included in sdist 0.1.9 not yet released
Version:        0.1.10
Release:        0
License:        MIT
Summary:        Spinner for Click
URL:            https://github.com/click-contrib/click-spinner
Source:         https://github.com/click-contrib/click-spinner/archive/v%{version}.tar.gz#/click-spinner-%{version}.tar.gz
Patch0:         python-click-spinner-remove-six.patch
# PATCH-FIX-UPSTREAM Based on gh#click-contrib/click-spinner#39
Patch1:         update-versioneer.patch
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch

%python_subpackages

%description
Spinner for Click.

%prep
%autosetup -p1 -n click-spinner-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/click_spinner
%{python_sitelib}/click_spinner-%{version}.dist-info

%changelog
