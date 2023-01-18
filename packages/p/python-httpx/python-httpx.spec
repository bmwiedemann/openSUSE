#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-httpx%{psuffix}
Version:        0.23.3
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
Requires:       python-certifi
Requires:       python-httpcore >= 0.15.0
Requires:       python-idna >= 2.0
Requires:       python-rfc3986 >= 1.3
Requires:       python-sniffio
Recommends:     python-Brotli
Recommends:     python-Pygments >= 2
Recommends:     python-click >= 8
Recommends:     python-h2 >= 3.0
Recommends:     python-rich >= 10
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%endif
# /SECTION
%python_subpackages

%description
Python HTTP client with async support.

%prep
%autosetup -p1 -n httpx-%{version}
# remove turning pytest warnings into error
sed -i '/tool.pytest/,$ {/error/d}' setup.cfg

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
%pytest -vv -k "not ($donttest)" --asyncio-mode=strict
%endif

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
%{python_sitelib}/httpx-%{version}*-info
%endif

%changelog
