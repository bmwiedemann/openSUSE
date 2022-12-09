#
# spec file for package python-pick
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


Name:           python-pick
Version:        2.2.0
Release:        0
Summary:        Curses-based interactive selection list module
License:        MIT
URL:            https://github.com/wong2/pick
Source0:        https://github.com/wong2/pick/archive/v%{version}.tar.gz#/pick-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
pick is a Python library to help create curses-based
interactive selection list in the terminal.

%prep
%setup -q -n pick-%{version}

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
%{python_sitelib}/*

%changelog
