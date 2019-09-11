#
# spec file for package python-websocket-client
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
# RHEL provides this backport in its own repository
%if 0%{?rhel} == 7
%define ssl_match_hostname python-backports-ssl_match_hostname
%else
%define ssl_match_hostname python-backports.ssl_match_hostname
%endif
Name:           python-websocket-client
Version:        0.56.0
Release:        0
Summary:        WebSocket client implementation
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/liris/websocket-client/releases
Source0:        https://files.pythonhosted.org/packages/source/w/websocket_client/websocket_client-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{ssl_match_hostname}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-websocket-client-test = %{version}
Obsoletes:      python-websocket-client-test < %{version}
BuildArch:      noarch
%ifpython2
Requires:       %{ssl_match_hostname}
%endif
%python_subpackages

%description
The websocket-client module is a WebSocket client for Python. This provides the
low-level APIs for WebSocket. All APIs are synchronous functions.

Websocket-client supports only hybi-13.

%prep
%setup -q -n websocket_client-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/wsdump.py

%check
%python_exec websocket/tests/test_websocket.py

%post
%python_install_alternative wsdump.py

%postun
%python_uninstall_alternative wsdump.py

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%python_alternative %{_bindir}/wsdump.py
%{python_sitelib}/websocket/
%{python_sitelib}/websocket_client-%{version}-py*.egg-info

%changelog
