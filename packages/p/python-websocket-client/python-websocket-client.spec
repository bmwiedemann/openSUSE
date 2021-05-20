#
# spec file for package python-websocket-client
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_without python2
Name:           python-websocket-client
Version:        0.58.0
Release:        0
Summary:        WebSocket client implementation
License:        LGPL-2.1-only
URL:            https://github.com/liris/websocket-client/releases
Source0:        https://files.pythonhosted.org/packages/source/w/websocket_client/websocket_client-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-websocket-client-test = %{version}
Obsoletes:      python-websocket-client-test < %{version}
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-backports.ssl_match_hostname
%endif
%ifpython2
Requires:       python-backports.ssl_match_hostname
%endif
%python_subpackages

%description
The websocket-client module is a WebSocket client for Python. This provides the
low-level APIs for WebSocket. All APIs are synchronous functions.

Websocket-client supports only hybi-13.

%prep
%setup -q -n websocket_client-%{version}
sed -i '1 i #!/usr/bin/python' bin/wsdump.py

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
