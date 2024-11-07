#
# spec file for package python-Quart
#
# Copyright (c) 2024 SUSE LLC
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


# Can't build for Python 3.10 due to missing hypercorn
%define skip_python310 1
Name:           python-Quart
Version:        0.19.8
Release:        0
Summary:        A Python ASGI web microframework with the same API as Flask
License:        MIT
URL:            https://github.com/pallets/quart/
Source:         https://github.com/pallets/quart/archive/refs/tags/%{version}.tar.gz#/quart-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 3.0}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module Werkzeug >= 3.0}
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module blinker >= 1.6}
BuildRequires:  %{python_module click >= 8.0}
BuildRequires:  %{python_module hypercorn >= 0.11.2}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 3.0
Requires:       python-Jinja2
Requires:       python-MarkupSafe
Requires:       python-Werkzeug >= 3.0
Requires:       python-aiofiles
Requires:       python-blinker >= 1.6
Requires:       python-click >= 8.0
Requires:       python-hypercorn >= 0.11.2
Requires:       python-itsdangerous
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Quart is an async Python web microframework. Using Quart you can,

* render and serve HTML templates,
* write (RESTful) JSON APIs,
* serve WebSockets,
* stream request and response data,
* do pretty much anything over the HTTP or WebSocket protocols.

%prep
%autosetup -p1 -n quart-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/quart
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative quart

%postun
%python_uninstall_alternative quart

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%python_alternative %{_bindir}/quart
%{python_sitelib}/quart
%{python_sitelib}/quart-%{version}.dist-info

%changelog
