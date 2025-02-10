#
# spec file for package python-fawltydeps
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


%{?sle15_python_module_pythons}
Name:           python-fawltydeps
Version:        0.18.0
Release:        0
Summary:        Find undeclared and unused 3rd-party dependencies in your Python project
License:        MIT
URL:            https://github.com/tweag/FawltyDeps
Source:         https://github.com/tweag/FawltyDeps/archive/refs/tags/v%{version}.tar.gz#/fawltydeps-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 6.0.1}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module importlib-metadata >= 6.6.0}
BuildRequires:  %{python_module isort > 5.10}
BuildRequires:  %{python_module nox}
BuildRequires:  %{python_module packaging >= 24.0}
BuildRequires:  %{python_module pip-requirements-parser >= 32.0.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pydantic >= 1.10.4}
# TEST dependencies
BuildRequires:  %{python_module pytest >= 7.1.0}
BuildRequires:  fdupes
Requires:       python-PyYAML >= 6.0.1
Requires:       python-importlib-metadata >= 6.6.0
Requires:       python-isort > 5.10
Requires:       python-pip-requirements-parser
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-uv
BuildArch:      noarch
%if "%{python_flavor}" < "python311"
BuildRequires:  %{python_module tomli >= 2.0.1}
%endif
%python_subpackages

%description
Find undeclared and unused 3rd-party dependencies in your Python project.

%prep
%autosetup -p1 -n FawltyDeps-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fawltydeps
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
# integration testsuite requires network for downloading project tarballs
# disable tests that require network
skiptests="test_resolve_dependencies_install_deps__via_local_cache"
skiptests+=" or test_resolve_dependencies_install_deps__raises_unresolved_error_on_install_failure"
skiptests+=" or test_resolve_dependencies_install_deps__unresolved_error_only_warns_failing_packages"
skiptests+=" or test_resolve_dependencies_install_deps_on_mixed_packages__raises_unresolved_error"
skiptests+=" or test_resolve_dependencies__generates_expected_mappings"
%pytest -k "not ($skiptests)"

%post
%python_install_alternative fawltydeps

%postun
%python_uninstall_alternative fawltydeps

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/fawltydeps
%{python_sitelib}/fawltydeps
%{python_sitelib}/fawltydeps-%{version}.dist-info

%changelog
