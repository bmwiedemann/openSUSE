#
# spec file for package python-userpath
#
# Copyright (c) 2025 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-userpath%{psuffix}
Version:        1.9.2
Release:        0
Summary:        Tool for adding locations to the user PATH
License:        MIT
URL:            https://github.com/ofek/userpath
Source:         https://files.pythonhosted.org/packages/source/u/userpath/userpath-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module userpath = %{version}}
%endif
# /SECTION
%python_subpackages

%description
Cross-platform tool for adding locations to the user PATH,
with no elevated privileges required.

%prep
%autosetup -p1 -n userpath-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/userpath
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LC_ALL=C.UTF-8
%pytest
%endif

%if !%{with test}
%post
%python_install_alternative userpath

%postun
%python_uninstall_alternative userpath

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/userpath
%{python_sitelib}/userpath
%{python_sitelib}/userpath-%{version}*-info
%endif

%changelog
