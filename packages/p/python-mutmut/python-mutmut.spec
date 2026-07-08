#
# spec file for package python-mutmut
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-mutmut
Version:        3.6.0
Release:        0
Summary:        Python mutation testing
License:        BSD-3-Clause
URL:            https://github.com/boxed/mutmut
Source:         https://github.com/boxed/mutmut/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 8.0.0
Requires:       python-coverage >= 7.3.0
Requires:       python-libcst >= 1.8.5
Requires:       python-pytest >= 6.2.5
Requires:       python-setproctitle >= 1.1.0
Requires:       python-textual >= 1.0.0
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.0.0}
BuildRequires:  %{python_module coverage >= 7.3.0}
BuildRequires:  %{python_module inline-snapshot}
BuildRequires:  %{python_module libcst >= 1.8.5}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module setproctitle >= 1.1.0}
BuildRequires:  %{python_module textual >= 1.0.0}
# /SECTION
%python_subpackages

%description
Python mutation testing.

%prep
%autosetup -p1 -n mutmut-%{version}
sed -i '1{/^#!/d}' src/mutmut/__main__.py
# Factory ships a newer uv-build than upstream's <0.10.0 build-backend pin
sed -i -E 's/"uv_build>=[0-9.]+,<[0-9.]+"/"uv_build"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mutmut
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the e2e type-checking tests shell out to the mypy and pyrefly type checkers
# (pyrefly is not packaged) and assert on version-specific snapshot output
%pytest --ignore tests/e2e/test_e2e_type_checking.py

%post
%python_install_alternative mutmut

%postun
%python_uninstall_alternative mutmut

%pre
%python_libalternatives_reset_alternative mutmut

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/mutmut
%{python_sitelib}/mutmut
%{python_sitelib}/mutmut-%{version}.dist-info

%changelog
