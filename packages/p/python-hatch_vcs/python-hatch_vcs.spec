#
# spec file for package python-hatch_vcs
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-hatch_vcs
Version:        0.3.0
Release:        0
Summary:        Hatch plugin for versioning with your preferred VCS
License:        MIT
URL:            https://github.com/ofek/hatch-vcs
Source:         https://files.pythonhosted.org/packages/source/h/hatch_vcs/hatch_vcs-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-hatchling >= 0.21.0
# https://github.com/ofek/hatch-vcs/issues/8
Requires:       (python-setuptools_scm >= 6.4.0)
Provides:       python-hatch-vcs = %{version}-%{info}
BuildArch:      noarch
# SECTION build
BuildRequires:  %{python_module hatchling >= 0.21.0}
BuildRequires:  %{python_module pip}
# /SECTION
# SECTION test
BuildRequires:  %{python_module setuptools_scm >= 6.4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  git
# /SECTION
%python_subpackages

%description
This provides a plugin for Hatch that uses your preferred version control system (like Git) to determine project versions.

%prep
%autosetup -n hatch_vcs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/hatch_vcs
%{python_sitelib}/hatch_vcs-%{version}*-info

%changelog
