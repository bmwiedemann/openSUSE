#
# spec file for package python-pass-git-helper
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


%define modname pass-git-helper
%if 0%{?suse_version} < 1600
%bcond_with test
%else
%bcond_without test
%endif
Name:           python-pass-git-helper
Version:        4.1.0
Release:        0
Summary:        A git credential helper interfacing with pass
License:        LGPL-3.0-or-later
URL:            https://github.com/languitar/pass-git-helper
Source:         https://github.com/languitar/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module dataclasses >= 0.7 if %python-base < 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
# /SECTION
%endif
BuildRequires:  fdupes
Requires:       python-pyxdg
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A git credential helper interfacing with pass, the standard unix password manager.

%prep
%autosetup -p1 -n pass-git-helper-%{version}

sed -i -e '/--cov-config=setup.cfg/d' setup.cfg
sed -i -e '1{\@^#!%{_bindir}/env python@d}' passgithelper.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pass-git-helper
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
%pytest
%endif

%post
%python_install_alternative pass-git-helper

%postun
%python_uninstall_alternative pass-git-helper

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/pass-git-helper
%pycache_only %{python_sitelib}/__pycache__/passgithelper*.pyc
%{python_sitelib}/pass_git_helper-%{version}*-info
%{python_sitelib}/passgithelper.py

%changelog
