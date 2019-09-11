#
# spec file for package torsocks
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


%define _name  libtorsocks
Name:           torsocks
Version:        2.2.0
Release:        0
Summary:        Use SOCKS-friendly applications with Tor
License:        GPL-2.0
Group:          Productivity/Networking/Security
Url:            https://github.com/dgoulet/torsocks
Source0:        https://github.com/dgoulet/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Recommends:     libcap-progs
Requires:       tor
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Torsocks allows you to use most applications in a safe way with Tor.
It ensures that DNS requests are handled safely and explicitly rejects
any traffic other than TCP from the application you're using.

Torsocks is an ELF shared library that is loaded before all others.
The library overrides every needed Internet communication libc function
calls such as connect(2) or gethostbyname(3).

This process is transparent to the user and if torsocks detects any
communication that can't go through the Tor network such as UDP traffic,
for instance, the connection is denied. If, for any reason, there is no way
for torsocks to provide the Tor anonymity guarantee to your application,
torsocks will force the application to quit and stop everything.

Adjust when needed /etc/tor/torsocks.conf and use Torsocks with

    torsocks application

So, for example you can use ssh to a some.ssh.com by doing

    torsocks ssh -p SSH-Port -i ~/.ssh/ssh-key.rsa username@some.ssh.com

You can use in /etc/bash.bashrc.local or /etc/zsh.zshrc.local alias

    alias slogin-='torsocks slogin'

And can ajust ~/.ssh/config with your data for server or PC and then use simple

    slogin- server

or add too an alias

    alias slogin-server='slogin- server'

and use simple

    slogin-server

%prep
%setup -q

%build
autoreconf -fi

%configure --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

# Remove not needed static libraries
rm %{buildroot}/%{_libdir}/%{name}/lib%{name}.{a,la}

%post   -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog README.md gpl-2.0.txt doc/socks/SOCKS5 doc/socks/socks-extensions.txt doc/notes/DEBUG extras/torsocks-bash_completion extras/torsocks-zsh_completion
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man5/%{name}.conf.5%{ext_man}
%{_mandir}/man8/%{name}.8%{ext_man}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{_name}.so*
%config(noreplace) %{_sysconfdir}/tor/%{name}.conf
%dir %attr(0755,root,tor) %{_sysconfdir}/tor

%changelog
