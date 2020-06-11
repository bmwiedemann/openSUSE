#
# spec file for package python-websockify
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
Name:           python-websockify
Version:        0.9.0
Release:        0
Summary:        WebSocket to TCP proxy/bridge
License:        LGPL-3.0-only AND MPL-2.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/novnc/websockify
Source:         https://github.com/novnc/websockify/archive/v%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module jwcrypto}
BuildRequires:  %{python_module mox3}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34
%endif
%if 0%{?suse_version}
Recommends:     python-jwcrypto
Recommends:     python-redis
Recommends:     python-simplejson
%endif
%python_subpackages

%description
websockify was formerly named wsproxy and was part of the
noVNC project.

At the most basic level, websockify just translates WebSockets traffic
to normal socket traffic. Websockify accepts the WebSockets handshake,
parses it, and then begins forwarding traffic between the client and
the target in both directions.

%package -n python-websockify-common
Summary:        Common data files for the Websockify TCP proxy/bridge
Provides:       %{python_module websockify-common = %{version}}

%description -n python-websockify-common
websockify was formerly named wsproxy and was part of the
noVNC project.

At the most basic level, websockify just translates WebSockets traffic
to normal socket traffic. Websockify accepts the WebSockets handshake,
parses it, and then begins forwarding traffic between the client and
the target in both directions.

This package contains common files.

%prep
%setup -q -n websockify-%{version}
# remove unwanted shebang
sed -i '1 { /^#!/ d }' websockify/websock*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/websockify

%check
%pytest

%post
%python_install_alternative websockify

%postun
%python_uninstall_alternative websockify

%files %{python_files}
%license COPYING
%doc CHANGES.txt README.md
%python_alternative %{_bindir}/websockify
%{python_sitelib}/*

%changelog
