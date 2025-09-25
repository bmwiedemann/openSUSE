#
# spec file for package python-uvicorn
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-uvicorn
Version:        0.36.0
Release:        0
Summary:        An Asynchronous Server Gateway Interface server
License:        BSD-3-Clause
URL:            https://github.com/encode/uvicorn
Source:         https://github.com/encode/uvicorn/archive/%{version}.tar.gz#/uvicorn-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Ignore the large amount of DeprecationWarnings that websockets 14 gave us
Patch0:         support-websockets-14+.patch
# PATCH-FIX-UPSTREAM small part of https://github.com/Kludex/uvicorn/pull/2548 test on 3.14
Patch1:         py314.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 7.0
Requires:       python-h11 >= 0.8.0
Recommends:     python-PyYAML >= 5.1
Recommends:     python-httptools >= 0.4.0
Recommends:     python-websockets >= 8.0
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module h11 >= 0.8.0}
BuildRequires:  %{python_module httptools >= 0.4.0}
BuildRequires:  %{python_module httpx >= 0.27}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module websockets >= 10.4}
BuildRequires:  %{python_module wsproto >= 1.2.0}
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module uvloop >= 0.14.0}
%endif
# We don't want watchfiles in Ring1
#BuildRequires:  #{python_module watchfiles >= 0.13}
# /SECTION
%python_subpackages

%description
Uvicorn is an ASGI server implementation, using uvloop and httptools.
It supports HTTP/1.1 and WebSockets only.

%prep
%autosetup -p1 -n uvicorn-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/uvicorn
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative uvicorn

%postun
%python_uninstall_alternative uvicorn

%pre
%python_libalternatives_reset_alternative uvicorn

%check
# Required for reporting bugs
%python_exec -m uvicorn --version
# No module python-a2wsgi
ignore="--ignore tests/middleware/test_wsgi.py"
# Disable flacky test in s390x with current python-websockets
%if "%{_arch}" == "s390x"
ignore+=" --ignore tests/protocols/test_websocket.py"
%endif
# no longer raises an exception with Websockets 14+
%pytest $ignore -k 'not test_send_binary_data_to_server_bigger_than_default_on_websockets'

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/uvicorn
%{python_sitelib}/uvicorn
%{python_sitelib}/uvicorn-%{version}.dist-info

%changelog
