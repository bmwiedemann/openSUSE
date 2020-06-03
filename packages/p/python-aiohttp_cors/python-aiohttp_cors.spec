#
# spec file for package python-aiohttp_cors
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-aiohttp_cors
Version:        0.7.0
Release:        0
Summary:        Asynchronous HTTP client/server framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/aiohttp-cors
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp-cors/aiohttp-cors-%{version}.tar.gz
Patch0:         0001-Fix-tests.patch
Patch1:         0001-215-fixing-exception-message-216.patch
Patch2:         278.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python >= 3.4.2
Requires:       python-async_timeout >= 2.0.0
Requires:       python-chardet
Requires:       python-multidict >= 3.3.0
Requires:       python-yarl >= 0.13.0
Recommends:     python-aiodns
Recommends:     python-cChardet
Suggests:       %{name}-doc
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 1.1 }
BuildRequires:  %{python_module async_timeout >= 2.0.0}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module multidict >= 3.3.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module yarl >= 0.13.0}
# /SECTION
# SECTION docs
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinxcontrib-asyncio
BuildRequires:  python3-sphinxcontrib-newsfeed
# /SECTION
%python_subpackages

%description
Asynchronous HTTP client/server framework for Python.

- Supports both the client and server side of HTTP protocol.
- Supports both client and server WebSockets out-of-the-box.
- Web-server has middleware and pluggable routing.

%prep
%setup -q -n aiohttp-cors-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%python_build

%install
%python_install

%check
%pytest tests/unit

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/aiohttp_cors*

%changelog
