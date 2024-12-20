#
# spec file for package python-websocket-client
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-websocket-client
Version:        1.8.0
Release:        0
Summary:        WebSocket client implementation
License:        LGPL-2.1-only
URL:            https://github.com/liris/websocket-client/releases
Source0:        https://files.pythonhosted.org/packages/source/w/websocket_client/websocket_client-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 6.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx_rtd_theme >= 1.1}
BuildRequires:  %{python_module websockets}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Provides:       python-websocket-client-test = %{version}
Obsoletes:      python-websocket-client-test < %{version}
BuildArch:      noarch
%python_subpackages

%description
The websocket-client module is a WebSocket client for Python. This provides the
low-level APIs for WebSocket. All APIs are synchronous functions.

Websocket-client supports only hybi-13.

%prep
%setup -q -n websocket_client-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/wsdump

%check
%pyunittest discover -v

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative wsdump

%post
%python_install_alternative wsdump

%postun
%python_uninstall_alternative wsdump

%files %{python_files}
%license LICENSE
%doc README.md ChangeLog
%python_alternative %{_bindir}/wsdump
%{python_sitelib}/websocket/
%{python_sitelib}/websocket_client-%{version}.dist-info

%changelog
