#
# spec file for package python-uvicorn
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-uvicorn
Version:        0.17.0
Release:        0
Summary:        An Asynchronous Server Gateway Interface server
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/encode/uvicorn
Source:         https://github.com/encode/uvicorn/archive/%{version}.tar.gz#/uvicorn-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 7.0
Requires:       python-h11 >= 0.8.0
Requires:       python-httptools >= 0.1.0
Requires:       python-typing_extensions
Requires:       python-websockets >= 8.0
Recommends:     python-PyYAML >= 5.1
Suggests:       python-uvloop >= 0.14.0
Suggests:       python-watchgod >= 0.6
Suggests:       python-wsproto >= 0.15.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module asgiref >= 3.4}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module h11 >= 0.8.0}
BuildRequires:  %{python_module httptools >= 0.1.0}
BuildRequires:  %{python_module httpx >= 0.18}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module uvloop >= 0.14.0}
BuildRequires:  %{python_module watchgod >= 0.6}
BuildRequires:  %{python_module websockets >= 8.0}
BuildRequires:  %{python_module wsproto >= 0.15.0}
# /SECTION
%python_subpackages

%description
Uvicorn is an ASGI server implementation, using uvloop and httptools.
It supports HTTP/1.1 and WebSockets only.

%prep
%autosetup -p1 -n uvicorn-%{version}
rm setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/uvicorn
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative uvicorn

%postun
%python_uninstall_alternative uvicorn

%check
# Required for reporting bugs
%python_exec -m uvicorn --version
# Three wsproto upgrade related tests
# https://github.com/encode/uvicorn/issues/868
%pytest -rs -k 'not (test_supported_upgrade_request or test_invalid_upgrade)'

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/uvicorn
%{python_sitelib}/*

%changelog
