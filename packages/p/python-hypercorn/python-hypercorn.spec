#
# spec file for package python-hypercorn
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


Name:           python-hypercorn
Version:        0.17.3
Release:        0
Summary:        A ASGI Server based on Hyper libraries and inspired by Gunicorn
License:        MIT
URL:            https://github.com/pgjones/hypercorn/
Source:         https://github.com/pgjones/hypercorn/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module h11}
BuildRequires:  %{python_module h2 >= 3.1.0}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  %{python_module priority}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module taskgroup if %python-base < 3.11}
BuildRequires:  %{python_module trio >= 0.22.0}
BuildRequires:  %{python_module wsproto >= 0.14.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h11
Requires:       python-h2 >= 3.1.0
Requires:       python-priority
Requires:       python-wsproto >= 0.14.0
%if %{python_version_nodots} < 311
Requires:       python-exceptiongroup >= 1.1
Requires:       python-taskgroup
Requires:       python-tomli
Requires:       python-typing-extensions
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Hypercorn is an `ASGI and WSGI web server based on the sans-io hyper, h11, h2,
and wsproto libraries and inspired by Gunicorn. Hypercorn supports HTTP/1,
HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI, and WSGI specifications.
Hypercorn can utilise asyncio, uvloop, or trio worker types.

%prep
%autosetup -p1 -n hypercorn-%{version}
sed -i 's/--no-cov-on-fail//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}
%python_clone -a %{buildroot}/%{_bindir}/hypercorn
%python_expand chmod -x %{buildroot}/%{$python_sitelib}/hypercorn/protocol/__init__.py
%python_expand chmod -x %{buildroot}/%{$python_sitelib}/hypercorn/protocol/h11.py
%python_expand chmod -x %{buildroot}/%{$python_sitelib}/hypercorn/protocol/h2.py

%check
# Broken with new trio
%pytest -k 'not test_startup_failure'

%post
%python_install_alternative hypercorn

%postun
%python_uninstall_alternative hypercorn

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/hypercorn
%{python_sitelib}/hypercorn-%{version}.dist-info
%python_alternative %{_bindir}/hypercorn

%changelog
