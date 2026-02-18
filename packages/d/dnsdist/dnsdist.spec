#
# spec file for package dnsdist
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


%if 0%{?suse_version} == 1500
%global force_gcc_version 14
%endif
%if 0%{?suse_version}
%bcond_without  apparmor
%else
%bcond_with     apparmor
%endif
%if 0%{?%{is_backports}} || 0%{?suse_version} >= 1599
%bcond_without  dnsdist_re2
%else
%bcond_with     dnsdist_re2
%endif
%ifarch ppc64le
%bcond_with     dnsdist_luajit
%else
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1599
%bcond_without  dnsdist_luajit
%else
%bcond_with     dnsdist_luajit
%endif
%endif
#
# this should only be needed if we have to patch the ragel files
# in which case it might be faster to just run it locally and put the regenerated file into the tarball
%bcond_with     dnsdist_ragel
%bcond_with     dnsdist_yaml_config
%bcond_with     dnsdist_quiche
%bcond_with     dnsdist_xdp
Name:           dnsdist
Version:        2.0.2
Release:        0
Summary:        A highly DNS-, DoS- and abuse-aware loadbalancer
License:        GPL-2.0-only
Group:          Productivity/Networking/DNS/Servers
URL:            https://www.powerdns.com/
Source0:        https://downloads.powerdns.com/releases/dnsdist-%{version}.tar.xz
Source1:        https://downloads.powerdns.com/releases/dnsdist-%{version}.tar.xz.sig
Source2:        https://dnsdist.org/_static/dnsdist-keyblock.asc#/dnsdist.keyring
Source3:        vendor.tar.xz
Source10:       dnsdist.user
Source11:       dnsdist.lua
Source12:       usr.sbin.dnsdist
Source13:       local.usr.sbin.dnsdist
Source99:       series
Source100:      README.md
Patch1:         fix_compilation.patch
BuildRequires:  gcc%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  libboost_headers-devel
# Because meson failure detecting boost without a linkable binary, even if we do not need one
BuildRequires:  libboost_filesystem-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libfstrm)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  pkgconfig(netsnmp)
BuildRequires:  pkgconfig(systemd)
%if %{with dnsdist_yaml_config}
BuildRequires:  cargo
%endif
%if %{with dnsdist_xdp}
BuildRequires:  pkgconfig(libxdp)
%endif
%if %{with apparmor}
BuildRequires:  apparmor-profiles
%endif
%if %{with dnsdist_ragel}
BuildRequires:  ragel
%endif
%if %{with dnsdist_re2}
BuildRequires:  pkgconfig(re2)
%endif
%if %{with dnsdist_luajit}
BuildRequires:  pkgconfig(luajit)
%else
BuildRequires:  pkgconfig(lua)
%endif
BuildRequires:  python3-PyYAML
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
%systemd_ordering
%sysusers_requires

%description
dnsdist is a highly DNS-, DoS- and abuse-aware loadbalancer. Its goal in life
is to route traffic to the best server, delivering top performance to
legitimate users while shunting or blocking abusive traffic.

dnsdist is dynamic, in the sense that its configuration can be changed at
runtime, and that its statistics can be queried from a console-like interface.

%prep
%autosetup -p1 -a 3 -n %{name}-%{version}

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%meson \
  --bindir=%{_sbindir} \
  --sysconfdir=%{_sysconfdir}/%{name} \
  -Ddnscrypt=enabled \
  -Dlibcap=enabled \
  -Dlibedit=enabled \
  -Dlibsodium=enabled \
  -Dtls-gnutls=enabled \
  -Dtls-libssl-engines=true \
  -Dtls-libssl-providers=true \
%if %{with dnsdist_luajit}
  -Dlua=luajit \
%else
  -Dlua=lua \
%endif
  -Dipcipher=enabled \
  -Dreproducible=true \
  -Dsnmp=enabled \
  -Ddnstap=enabled \
  -Dnghttp2=enabled \
  -Dcdb=disabled \
  -Dlmdb=enabled \
%if %{with dnsdist_quiche}
  -Dquiche=enabled \
  -Ddns-over-http3=enabled \
  -Ddns-over-quic=enabled \
%else
  -Dquiche=disabled \
  -Ddns-over-http3=disabled \
  -Ddns-over-quic=disabled \
%endif
%if %{with dnsdist_re2}
  -Dre2=enabled \
%else
  -Dre2=disabled \
%endif
%if %{with dnsdist_xdp}
  -Dxsk=enabled \
%else
  -Dxsk=disabled \
%endif
  -Debpf=enabled \
%if %{with dnsdist_yaml_config}
  -Dyaml=enabled \
%else
  -Dyaml=disabled \
%endif
  -Dman-pages=true \
%nil

%meson_build
%sysusers_generate_pre %{SOURCE10} %{name}

%install
%meson_install
#
%if 0%{?suse_version}
  ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif
%if %{with apparmor}
install -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.dnsdist
install -D -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.sbin.dnsdist
%endif

install -m 0640 %{SOURCE11} %{buildroot}%{_sysconfdir}/%{name}/dnsdist.conf

install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/dnsdist.conf

rm -rv \
  docs/*.py \
  docs/manpages \
  docs/requirements.* \
  docs/_static \
  docs/_templates
find docs -type f -executable -print0 | xargs -r0 chmod -v a-x
perl -p -i -e 's|\r\n|\n|g ; s|\r|\n|g' docs/reference/logging.rst

%check
%meson_test

%pre -f %{name}.pre
%service_add_pre %{name}.service %{name}@.service

%preun
%service_del_preun %{name}.service %{name}@.service

%post
%service_add_post %{name}.service %{name}@.service

%postun
%service_del_postun %{name}.service %{name}@.service

%files
%doc README.md
%license COPYING
%doc docs/
%{_sbindir}/dnsdist
%{_mandir}/man1/dnsdist.1%{?ext_man}
%{_unitdir}/%{name}*.service
%{_sysusersdir}/dnsdist.conf
%if 0%{?suse_version}
%{_sbindir}/rc%{name}
%endif
%if %{with apparmor}
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.dnsdist
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.sbin.dnsdist
%endif
%config(noreplace) %attr(-,root,%{name}) %{_sysconfdir}/%{name}/

%changelog
