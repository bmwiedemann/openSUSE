#
# spec file for package python-websockify
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
Name:           python-websockify
Version:        0.8.0
Release:        0
Summary:        WebSocket to TCP proxy/bridge
License:        LGPL-3.0-only AND MPL-2.0 AND BSD-2-Clause AND BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/novnc/websockify
Source:         https://github.com/novnc/websockify/archive/v%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM u_Add-support-for-inetd.patch fate#323880 msrb@suse.com -- https://github.com/novnc/websockify/pull/293
Patch1:         u_Add-support-for-inetd.patch
# PATCH-FEATURE-UPSTREAM u_Fix-inetd-mode-on-python-2.patch fate#323880 msrb@suse.com -- https://github.com/novnc/websockify/pull/293
Patch2:         u_Fix-inetd-mode-on-python-2.patch
# PATCH-FEATURE-ALMOST-UPSTREAM u_added_jwt_tokens_capability.patch fate#325762 cbosdonnat@suse.com -- https://github.com/novnc/websockify/pull/372
Patch3:         u_added_jwt_tokens_capability.patch
# PATCH-FIX-OPENSUSE PyJWT-token-plugin.patch fate#325762 cbosdonnat@suse.com -- use PyJWT if jwcrypto is missing
Patch4:         PyJWT-token-plugin.patch
# PATCH-FROM-UPSTREAM:
Patch5:         fix-tests-py3.6.patch
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module mox3}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
Requires:       python-numpy
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-websockify-common = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?suse_version}
# SLES 12 and up to 15SP1 doesn't have python-jwcrypto package and will fallback to
# the PyJWT implementation. However opensuse has jwcrypto since 42.3: use this one
# since it also provides support for JWE (encrypted JWT).
%if 0%{?sle_version}
Recommends:     python-PyJWT
Recommends:     python-cryptography
%else
Recommends:     python-jwcrypto
%endif
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
Group:          Development/Languages/Python
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
%autopatch -p1

# remove unwanted shebang
sed -i '1 { /^#!/ d }' websockify/websocket*.py
# drop unneeded executable bit
chmod -x include/web-socket-js/web_socket.js
# fix mox3 import
sed -e 's:import stubout:from mox3 import stubout:g' \
    -i tests/test_websocketproxy.py \
    -i tests/test_websocket.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/websockify

%check
%python_exec setup.py nosetests

%post
%python_install_alternative websockify

%postun
%python_uninstall_alternative websockify

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt README.md
%python_alternative %{_bindir}/websockify
%{python_sitelib}/*

%files -n python-websockify-common
%license LICENSE.txt
%{_datadir}/websockify

%changelog
