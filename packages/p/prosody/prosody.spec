#
# spec file for package prosody
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


%define _piddir /run
Name:           prosody
Version:        0.12.2
Release:        0
Summary:        Communications server for Jabber/XMPP
License:        MIT
Group:          Productivity/Networking/Other
URL:            http://prosody.im/
Source:         http://prosody.im/downloads/source/%{name}-%{version}.tar.gz
Source2:        http://prosody.im/downloads/source/%{name}-%{version}.tar.gz.asc
Source3:        %{name}.keyring
Source4:        %{name}.service
Source5:        prosody.tmpfile
# Make prosody work on systems that have lua 5.1 AND 5.2 installed
Patch0:         prosody-lua51coexist.patch
Patch1:         prosody-configure.patch
# PATCH-FIX-OPENSUSE marguerite@opensuse.org - enable Unix features
Patch3:         prosody-cfg.patch
BuildRequires:  libicu-devel
BuildRequires:  libidn-devel
BuildRequires:  libopenssl-devel
BuildRequires:  lua51-devel
BuildRequires:  systemd-rpm-macros
Requires:       lua51
Requires:       lua51-BitOp
Requires:       lua51-luaexpat
Requires:       lua51-luafilesystem
Requires:       lua51-luasec
Requires:       lua51-luasocket
Requires(pre):  permissions
Requires(pre):  shadow
Recommends:     lua51-luadbi
Recommends:     lua51-luaevent
Recommends:     lua51-zlib
%{?systemd_requires}

%description
Prosody is a communications server for Jabber/XMPP written in Lua.

Prosody can link up with other Prosody installations and other
XMPP-compatible services to form an open communication network,
whilst allowing control over who they connect to, and who they share
data with.

%prep
%autosetup -p1

sed -i 's|@@INCLUDEDIR@@|%{_includedir}|g;' configure
sed -i 's|@@INCLUDEDIR@@|%{_includedir}|g;' makefile
sed -i 's|@@PIDDIR@@|%{_piddir}|g;' prosody.cfg.lua.dist

%build
# CFLAGS need to keep -fPIC for shared modules
./configure \
    --lua-suffix="5.1" \
    %if 0%{?suse_version} >= 1500
    --with-lua-include=%{lua_incdir} \
    --cflags="%{optflags} -fPIC" \
    %else
    --cflags="%{optflags} -fPIC -std=c99" \
    %endif
    --c-compiler=gcc \
    --libdir=%{_libdir}

%make_build

%install
%make_install

install -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
# tmpfiles.d
install -D -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcprosody

# mkdir read/write by prosody
mkdir -p %{buildroot}%{_piddir}/prosody
mkdir -p %{buildroot}%{_localstatedir}/log/prosody

# clean up for rpmlint
chmod 644 %{buildroot}/%{_libdir}/prosody/prosody.version
chmod -R g+rX,o= %{buildroot}%{_sysconfdir}/prosody

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s/sbin/nologin -c "user for %{name}" %{name}
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf ||:

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%config(noreplace) %attr(-,root,prosody) %{_sysconfdir}/prosody/
%{_bindir}/prosody
%{_bindir}/prosodyctl
%dir %{_libdir}/prosody
%{_libdir}/prosody/core
%{_libdir}/prosody/modules/
%{_libdir}/prosody/net
%{_libdir}/prosody/prosody.version
%{_libdir}/prosody/util
%{_mandir}/man1/prosodyctl.1%{?ext_man}
%dir %attr(-,prosody,prosody) %{_localstatedir}/lib/prosody
%dir %attr(-,prosody,prosody) %{_localstatedir}/log/prosody
%{_sbindir}/rcprosody
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755,prosody,prosody) %ghost %{_piddir}/prosody

%changelog
