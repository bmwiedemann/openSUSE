#
# spec file for package fetchmail
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           fetchmail
Version:        6.4.12
Release:        0
Summary:        Full-Featured POP and IMAP Mail Retrieval Daemon
License:        GPL-2.0-or-later
URL:            https://www.fetchmail.info/
Source:         https://sourceforge.net/projects/%{name}/files/branch_6.4/%{name}-%{version}.tar.xz
Source1:        https://sourceforge.net/projects/%{name}/files/branch_6.4/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.logrotate
Source3:        sysconfig.%{name}
Source5:        %{name}.keyring
Source6:        %{name}.service
Source7:        %{name}.tmpfiles
Source8:        %{name}.exec
Patch0:         fetchmail-6.3.8-smtp_errors.patch
BuildRequires:  automake
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  opie
BuildRequires:  postfix
BuildRequires:  procmail
BuildRequires:  python3-base
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires:       logrotate
Requires(pre):  %fillup_prereq
Requires(pre):  coreutils
Requires(pre):  group(daemon)
Requires(pre):  shadow
Suggests:       smtp_daemon
%{?systemd_requires}

%description
Fetchmail is a robust and well-documented remote mail retrieval and
forwarding utility intended to be used over on-demand TCP/IP links
(such as SLIP or PPP connections).

Fetchmail retrieves mail from remote mail servers and forwards it to
your local machine's delivery system, so it can be read by normal mail
user agents, such as mutt, elm, pine, (x)emacs/gnus, or mailx.

fetchmailconf, an interactive GUI configurator suitable for end-users,
is included in the fetchmailconf package.

%package -n fetchmailconf
Summary:        Fetchmail Configuration Utility
Requires:       %{name} = %{version}
Requires:       python3-future
Requires:       python3-tk

%description -n fetchmailconf
A GUI configuration utility for generating fetchmail configuration
files (.fetchmailrc).

%prep
%setup -q
%patch0 -p1
cp -a %{SOURCE2} %{SOURCE3} .

ACLOCAL="aclocal -I m4 -I m4-local" autoreconf -fvi

%build
export CFLAGS="%{optflags} -fPIE"
%configure \
	--enable-POP2 \
	--enable-RPA \
	--enable-NTLM \
	--enable-SDPS \
	--enable-opie \
	--with-kerberos5 \
        --with-gssapi \
	--with-ssl=%{_prefix}
%make_build LDFLAGS="-pie"

%install
%make_install
ln -sf fetchmail.1.gz %{buildroot}%{_mandir}/man1/fetchmailconf.1.gz
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp fetchmail.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/fetchmail
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE6}
install -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
install -m 0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_libexecdir}
install -m 0755 %{SOURCE8} %{buildroot}%{_libexecdir}/%{name}-systemd-exec
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rc%{name}
touch %{buildroot}%{_sysconfdir}/fetchmailrc
mkdir -p %{buildroot}%{_fillupdir}
cp sysconfig.%{name} %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/fetchmail
mkdir -p %{buildroot}%{_localstatedir}/lib/fetchmail
# we don't need this, it's aimed at fetchmail developers
# and rpmlint is complaining that we have a binary in /usr/share
rm -r contrib/gai*
%find_lang %{name}

%pre
%{_bindir}/getent passwd fetchmail >/dev/null || \
  %{_sbindir}/useradd -r -g daemon -s /bin/false \
  -c "mail retrieval daemon" -d %{_localstatedir}/lib/fetchmail fetchmail || :
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service
if [ -x %{_bindir}/systemd-tmpfiles ]; then
	systemd-tmpfiles --create %{name}.conf || :
fi
# Ensure that all files are readable by fetchmail with non-root UID.
touch var/log/fetchmail
chown fetchmail var/log/fetchmail
chmod 0600 var/log/fetchmail

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
if [ $1 = 0 ]; then
    rm -rf var/lib/fetchmail
fi

%check
%make_build check

%files -f %{name}.lang
%license COPYING
%doc FAQ FEATURES NEWS NOTES OLDNEWS README README.NTLM README.SSL README.SSL-SERVER TODO contrib *.html *.txt *.pdf
%{_bindir}/fetchmail
%dir %attr(0700, fetchmail, root) %{_localstatedir}/lib/fetchmail
%ghost %attr(0600, fetchmail, root) %{_localstatedir}/log/fetchmail
%{_mandir}/man1/fetchmail.1%{?ext_man}
%ghost %config(noreplace) %attr(0600, fetchmail, root) %{_sysconfdir}/fetchmailrc
%config(noreplace) %{_sysconfdir}/logrotate.d/fetchmail
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_libexecdir}/%{name}-systemd-exec
%{_tmpfilesdir}/%{name}.conf
%{_fillupdir}/sysconfig.%{name}

%files -n fetchmailconf
%{_bindir}/fetchmailconf
%{_mandir}/man1/fetchmailconf.1%{?ext_man}
%{python3_sitelib}/fetchmailconf.*
%{python3_sitelib}/__pycache__/fetchmailconf*

%changelog
