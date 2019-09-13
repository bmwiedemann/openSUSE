#
# spec file for package proxychains-ng
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           proxychains-ng
Version:        4.11
Release:        0
Summary:        Redirect connection through proxy servers
License:        GPL-2.0
Group:          Productivity/Networking/Security
Url:            http://sourceforge.net/projects/proxychains-ng/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.bz2
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
make %{?_smp_mflags}

%install
%make_install install-config
install -Dm 0755 src/proxyresolv %{buildroot}%{_bindir}/proxyresolv4

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{_bindir}/proxychains4
%{_bindir}/proxyresolv4
%{_libdir}/libproxychains4.so
%config %{_sysconfdir}/proxychains.conf

%changelog
