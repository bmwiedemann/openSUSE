#
# spec file for package python-aiohttp-asgi
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


Name:           python-aiohttp-asgi
Version:        0.5.2
Release:        0
Summary:        Adapter to running ASGI applications on aiohttp
License:        Apache-2.0
URL:            https://github.com/mosquito/aiohttp-asgi
Source:         https://github.com/mosquito/aiohttp-asgi/archive/refs/tags/%{version}.tar.gz#/aiohttp-asgi-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-aiohttp < 4
BuildArch:      noarch
%python_subpackages

%description
Adapter to running ASGI applications on aiohttp.

%prep
%setup -q -n aiohttp-asgi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/aiohttp-asgi
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative aiohttp-asgi

%postun
%python_uninstall_alternative aiohttp-asgi

%check
%pytest

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/aiohttp-asgi
%{python_sitelib}/aiohttp_asgi
%{python_sitelib}/aiohttp_asgi-%{version}.dist-info

%changelog
