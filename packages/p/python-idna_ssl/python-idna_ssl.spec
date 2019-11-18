#
# spec file for package python-idna_ssl
#
# Copyright (c) 2019 SUSE LLC.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-idna_ssl%{psuffix}
Version:        1.1.0
Release:        0
Summary:        Library that patches sslmatch_hostname for Unicode/IDNA domain support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/idna_ssl
Source:         https://github.com/aio-libs/idna-ssl/archive/v%{version}.tar.gz
BuildRequires:  %{python_module idna >= 2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-idna >= 2.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module idna_ssl = %{version}}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
This patches ssl.match_hostname for Unicode/IDNA domain support.
The ssl.match_hostname issue is fixed (as of January 27 2018) in upcoming
Python 3.7, but IDNA2008 (RFC 5895) is still broken.

%prep
%setup -q -n idna-ssl-%{version}
# no need for coverage/etc
sed -i -e '/addopts/d' setup.cfg

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest -k "not test_aiohttp_py370"
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%endif

%changelog
