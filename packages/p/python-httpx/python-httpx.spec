#
# spec file
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-httpx%{psuffix}
Version:        0.22.0
Release:        0
Summary:        Python HTTP client with async support
License:        BSD-3-Clause
URL:            https://github.com/encode/httpx
Source:         https://github.com/encode/httpx/archive/%{version}.tar.gz#/httpx-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-brotlicffi
Requires:       python-certifi
Requires:       python-chardet >= 3.0
Requires:       python-charset-normalizer >= 2.0.6
Requires:       python-h11 >= 0.8.0
Requires:       python-h2 >= 3.0
Requires:       python-hstspreload >= 2019.8.27
Requires:       python-httpcore >= 0.14.0
Requires:       python-idna >= 2.0
Requires:       python-rfc3986 >= 1.3
Requires:       python-sniffio
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module brotlicffi}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module chardet >= 3.0}
BuildRequires:  %{python_module charset-normalizer >= 2.0.6}
BuildRequires:  %{python_module h11 >= 0.8.0}
BuildRequires:  %{python_module h2 >= 3.0}
BuildRequires:  %{python_module hstspreload >= 2019.8.27}
BuildRequires:  %{python_module httpcore >= 0.14.0}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module idna >= 2.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rfc3986 >= 1.3}
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module uvloop}
%endif
# /SECTION
%python_subpackages

%description
Python HTTP client with async support.

%prep
%setup -q -n httpx-%{version}
rm setup.cfg

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/httpx
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest -k 'not (network or socks or test_main or response_no_charset or test_text_decoder)'
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
%{python_sitelib}/httpx*
%endif

%changelog
