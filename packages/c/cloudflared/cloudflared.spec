#
# spec file for package cloudflared
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

Name:           cloudflared
Version:        2024.6.0
Release:        0
Summary:        Cloudflare Tunnel client
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            https://github.com/cloudflare/cloudflared
Source0:        https://github.com/cloudflare/cloudflared/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE 001-skip-test.patch hillwood@opensuse.org
Patch0:         001-skip-test.patch
# PATCH-FIX-OPENSUSE 002-use-pie.patch hillwood@opensuse.org
Patch1:         002-use-pie.patch
# PATCH-FIX-UPSTREAM 003-support-ppc64le.patch hillwood@opensuse.org
Patch2:         003-support-ppc64le.patch
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  golang(API) >= 1.22
BuildRequires:  golang-packaging
AutoReqProv:    Off
%{go_provides}

%description
Contains the command-line client for Cloudflare Tunnel, a tunneling daemon that
proxies traffic from the Cloudflare network to your origins. This daemon sits
between Cloudflare network and your origin (e.g. a webserver). Cloudflare
attracts client requests and sends them to you via this daemon, without
requiring you to poke holes on your firewall --- your origin can remain as
closed as possible. Extensive documentation can be found in the Cloudflare
Tunnel section of the Cloudflare Docs. All usages related with proxying to your
origins are available under cloudflared tunnel help.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}

%build
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
