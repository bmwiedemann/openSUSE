#
# spec file for package python-click-aliases
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


%{?sle15_python_module_pythons}
Name:           python-click-aliases
Version:        1.0.4
Release:        0
Summary:        Command aliases for Click
License:        MIT
URL:            https://github.com/click-contrib/click-aliases
Source:         https://github.com/click-contrib/click-aliases/archive/refs/tags/v%{version}.tar.gz#/click-aliases-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch
# SECTION test requirements
# See https://github.com/click-contrib/click-aliases/issues/5
# for problems with click 6.7 currently on Leap.
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Command aliases for Click.

%prep
%setup -q -n click-aliases-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# test_invalid fails with new click as the quotes in output changed from single to regular ones
%pytest -k 'not test_invalid'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/click_aliases
%{python_sitelib}/click_aliases-%{version}.dist-info

%changelog
