#
# spec file for package python-pyproject-parser
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-pyproject-parser%{psuffix}
Version:        0.14.0
Release:        0
Summary:        Parser for 'pyproject.toml'
License:        MIT
URL:            https://github.com/repo-helper/pyproject-parser
Source:         https://github.com/repo-helper/pyproject-parser/archive/refs/tags/v%{version}.tar.gz#/pyproject-parser-%{version}.tar.gz
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-apeye-core >= 1.0.0
Requires:       python-attrs >= 20.3.0
Requires:       python-dom-toml >= 2.0.0
Requires:       python-domdf-python-tools >= 2.8.0
Requires:       python-license-expression
Requires:       python-natsort >= 7.1.1
Requires:       python-packaging >= 20.9
Requires:       python-shippinglabel >= 1.0.0
Requires:       python-typing-extensions >= 3.7.4.3
Suggests:       python-click >= 7.1.2
Suggests:       python-consolekit >= 1.4.1
Suggests:       python-docutils >= 0.16
Suggests:       python-readme-renderer >= 27.0
Suggests:       python-sdjson >= 0.3.1
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module consolekit}
BuildRequires:  %{python_module pyproject-examples}
BuildRequires:  %{python_module pyproject-parser = %{version}}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sdjson}
%endif
# /SECTION
%python_subpackages

%description
Parser for 'pyproject.toml'

%prep
%autosetup -p1 -n pyproject-parser-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyproject-parser
%python_clone -a %{buildroot}%{_bindir}/check-pyproject
%python_clone -a %{buildroot}%{_bindir}/pyproject-fmt
%python_clone -a %{buildroot}%{_bindir}/pyproject-info
%python_group_libalternatives pyproject-parser check-pyproject pyproject-fmt pyproject-info
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative pyproject-parser

%post
%python_install_alternative pyproject-parser check-pyproject pyproject-fmt pyproject-info

%postun
%python_uninstall_alternative pyproject-parser
%endif

%check
%if %{with test}
# Broken with click 8.2.0
%pytest -k 'not test_handle_tracebacks_ignored_exceptions_click'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pyproject-parser
%python_alternative %{_bindir}/check-pyproject
%python_alternative %{_bindir}/pyproject-fmt
%python_alternative %{_bindir}/pyproject-info
%{python_sitelib}/pyproject_parser
%{python_sitelib}/pyproject_parser-%{version}.dist-info
%endif

%changelog
