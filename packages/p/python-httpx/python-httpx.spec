#
# spec file for package python-httpx
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

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-httpx%{psuffix}
Version:        0.28.1
Release:        0
Summary:        Python HTTP client with async support
License:        BSD-3-Clause
URL:            https://github.com/encode/httpx
Source:         https://github.com/encode/httpx/archive/%{version}.tar.gz#/httpx-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio
Requires:       python-certifi
Requires:       python-httpcore >= 0.18.0
Requires:       python-idna >= 2.0
Recommends:     python-Brotli
Recommends:     python-Pygments >= 2
Recommends:     python-click >= 8
Recommends:     python-h2 >= 3.0
Recommends:     python-rich >= 10
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Pygments >= 2}
BuildRequires:  %{python_module chardet >= 5.0}
BuildRequires:  %{python_module click >= 8}
BuildRequires:  %{python_module h2 >= 3.0}
BuildRequires:  %{python_module httpx = %{version}}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 10}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module trustme}
# uvicorn 0.18 fixed an issue in the test suite where http-headers wer not all lowercase as expected
BuildRequires:  %{python_module uvicorn >= 0.18}
BuildRequires:  %{python_module zstandard}
%endif
# /SECTION
%python_subpackages

%description
Python HTTP client with async support.

%prep
%autosetup -p1 -n httpx-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/httpx
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# obs builds offline
donttest="network"
# no socksio
donttest="$donttest or socks"
# test is hardware dependent, fails on OBS
donttest="$donttest or test_write_timeout[trio]"
%pytest -vv -k "not ($donttest)"
%endif

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative httpx

%post
%python_install_alternative httpx

%postun
%python_uninstall_alternative httpx

%if !%{with test}
%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/httpx
%{python_sitelib}/httpx
%{python_sitelib}/httpx-%{version}.dist-info
%endif

%changelog
