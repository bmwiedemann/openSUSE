#
# spec file for package python-pytest-pook
#
# Copyright (c) 2026 SUSE LLC
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


# No tags in git history
%define git_sha a7c2d0ca4287af671ebd065b0f6415bb4110f338
Name:           python-pytest-pook
Version:        1.0.0
Release:        0
Summary:        Pytest plugin for pook
License:        LGPL-3.0
URL:            https://git.sr.ht/~sara/pytest-pook
Source:         https://git.sr.ht/~sara/pytest-pook/archive/%{git_sha}.tar.gz#/pytest_pook-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pook}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest
Requires:       python-pook
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin for pook.

Tests that rely on pook can be marked with @pytest.mark.pook.

%prep
%autosetup -p1 -n pytest-pook-%{git_sha}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_pook
%{python_sitelib}/pytest_pook-%{version}.dist-info

%changelog
