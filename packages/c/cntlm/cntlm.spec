#
# spec file for package cntlm
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2007 Scorpio IT, Deidesheim, Germany
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


Name:           cntlm
Version:        0.94.0
Release:        0
Summary:        Fast NTLM authentication proxy with tunneling
License:        GPL-2.0-or-later
URL:            https://github.com/versat/cntlm
Source0:        https://github.com/versat/cntlm/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        %{name}.sysconfig
Source3:        %{name}.service
Source4:        %{name}.tmpfiles
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
Requires(pre):  %fillup_prereq
Requires(pre):  grep
Requires(pre):  group(nogroup)
Requires(pre):  shadow
Provides:       user(%{name})
# PAC-file support links a bundled copy of the duktape JS engine
Provides:       bundled(duktape) = 2.7.0
%{?systemd_requires}

%description
Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling,
authenticated connection caching, ACLs, proper daemon logging and behaviour
and much more. It has up to ten times faster responses than similar NTLM
proxies, while using by orders or magnitude less RAM and CPU. Manual page
contains detailed information.

%prep
%autosetup -p1
# Do not let upstream's "install -s" strip the binary at install time — it
# empties the -debuginfo package; let the rpm debuginfo machinery handle it.
sed -i 's/install -D -m 755 -s/install -D -m 755/' Makefile
# The bundled duktape JS engine (PAC support) trips -Werror=uninitialized under
# the distro's LTO (cross-unit maybe-uninitialized false positives); demote it.
sed -i 's/-Werror=uninitialized/-Wno-error=uninitialized -Wno-error=maybe-uninitialized/' Makefile

%build
# cntlm ships a hand-written configure (not autotools) that rejects the standard
# autotools flags and then skips generating config/config.h, so run it plainly.
# The Makefile already targets /usr and appends CFLAGS, so just export the flags.
export CFLAGS="%{optflags}"
./configure
%make_build

%install
%make_install PREFIX=%{_prefix}

install -d %{buildroot}%{_localstatedir}/run/%{name}
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%pre
# user cntlm
if [ -z "`%{_bindir}/getent passwd "%{name}"`" ]; then
  %{_sbindir}/useradd -c "CNTLM Proxy Auth" -d %{_localstatedir}/run/%{name} -g nogroup \
	-r -s /bin/false %{name};
fi
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%fillup_only
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%postun
%service_del_postun %{name}.service

%files
%license COPYRIGHT LICENSE
%doc README VERSION
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%ghost %dir %attr(755,%{name},root) /run/%{name}
%{_sbindir}/*
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_fillupdir}/sysconfig.%{name}

%changelog
