#
# spec file for package proxychains-ng
#
# Copyright (c) 2022 SUSE LLC
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


Name:           proxychains-ng
Version:        4.16
Release:        0
Summary:        Redirect connection through proxy servers
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://github.com/rofl0r/proxychains-ng
Source0:        https://ftp.barfooze.de/pub/sabotage/tarballs/proxychains-ng-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  make
Obsoletes:      proxychains < %{version}
Provides:       proxychains = %{version}

%description
ProxyChains NG is based on ProxyChains.

ProxyChains NG hooks network-related (TCP only) libc functions in dynamically
linked programs via a preloaded DSO (dynamic shared object) and redirects the
connections through one or more SOCKS4a/5 or HTTP proxies.

Since Proxy Chains NG relies on the dynamic linker, statically linked binaries
are not supported.

Adjust ~/.proxychains/proxychains.conf for your Proxy and use ProxyChains NG
with

    proxychains4 application

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install install-config
install -Dm 0755 src/proxyresolv %{buildroot}%{_bindir}/proxyresolv4

%files
%doc AUTHORS README TODO
%license COPYING
%{_bindir}/proxychains4
%{_bindir}/proxychains4-daemon
%{_bindir}/proxyresolv4
%{_libdir}/libproxychains4.so
%config %{_sysconfdir}/proxychains.conf

%changelog
