#
# spec file for package fetchmail
#
# Copyright (c) 2023 SUSE LLC
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
Version:        6.4.35
Release:        0
Summary:        Full-Featured POP and IMAP Mail Retrieval Daemon
License:        GPL-2.0-or-later
URL:            https://www.fetchmail.info/
Source0:        https://sourceforge.net/projects/%{name}/files/branch_6.4/%{name}-%{version}.tar.xz
Source1:        https://sourceforge.net/projects/%{name}/files/branch_6.4/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.logrotate
Source3:        sysconfig.%{name}
Source5:        %{name}.keyring
Source6:        %{name}.service
Source7:        %{name}.tmpfiles
Source8:        %{name}.exec
Source9:        %{name}.sysusers
Patch0:         fetchmail-6.3.8-smtp_errors.patch
Patch1:         fetchmail-add-imap-oauthbearer-support.patch
Patch2:         fetchmail-support-oauthbearer-xoauth2-with-pop3.patch
Patch3:         fetchmail-add-passwordfile-and-passwordfd-options.patch
Patch4:         fetchmail-add-contrib-fetchnmail-oauth2.py-token-acquisition-u.patch
Patch5:         fetchmail-FAQ-list-gmail-options-including-oauthbearer-and-app.patch
Patch6:         fetchmail-give-each-ctl-it-s-own-copy-of-password.patch
Patch7:         fetchmail-re-read-passwordfile-on-every-poll.patch
Patch8:         fetchmail-add-query_to64_outsize-utility-function.patch
Patch9:         fetchmail-chase-and-integrate-interface-change.patch
Patch10:        fetchmail-oauth2-c-calculate-and-pass-in-correct-buffer-size-to-to64frombits.patch
Patch11:        fetchmail-increase-max-password-length-to-handle-oauth-tokens.patch
Patch12:        fetchmail-bump-max-passwordlen-to-1bytes.patch
Patch13:        fetchmail-add-readme-oauth2-issue-27.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  opie
BuildRequires:  postfix
BuildRequires:  procmail
BuildRequires:  python3-base
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  xz
Requires:       logrotate
Requires(pre):  %fillup_prereq
Suggests:       smtp_daemon
%sysusers_requires

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
Requires:       python3 >= 3.7
Requires:       python3-future
Requires:       python3-tk

%description -n fetchmailconf
A GUI configuration utility for generating fetchmail configuration
files (.fetchmailrc).

%prep
%autosetup -p1
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
    --with-ssl=%{_prefix} \
    --with-python=%{bindir}/python3
%make_build LDFLAGS="-pie"
%sysusers_generate_pre %{SOURCE9} fetchmail

%install
%make_install
ln -sf fetchmail.1.gz %{buildroot}%{_mandir}/man1/fetchmailconf.1.gz
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
cp fetchmail.logrotate %{buildroot}%{_distconfdir}/logrotate.d/fetchmail
%else
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp fetchmail.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/fetchmail
%endif
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_sysusersdir}
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE6}
install -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
install -m 0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -m 0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/%{name}.conf
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
# Deduplicate Python files
%fdupes %{buildroot}%{python3_sitelib}
# we don't need this, it's aimed at fetchmail developers
# and rpmlint is complaining that we have a binary in /usr/share
rm -r contrib/gai*
%find_lang %{name}

%pre -f fetchmail.pre
%service_add_pre %{name}.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/fetchmail ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%post
%fillup_only
%tmpfiles_create %{name}.conf
%service_add_post %{name}.service

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/fetchmail ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%check
%make_build check

%files -f %{name}.lang
%license COPYING
%doc FAQ FEATURES NEWS NOTES OLDNEWS README README.NTLM README.OAUTH2 README.SSL README.SSL-SERVER TODO contrib *.html *.txt *.pdf
%{_bindir}/fetchmail
%dir %attr(0700, fetchmail, fetchmail) %{_localstatedir}/lib/fetchmail
%ghost %attr(0600, fetchmail, root) %{_localstatedir}/log/fetchmail
%{_mandir}/man1/fetchmail.1%{?ext_man}
%ghost %config(noreplace) %attr(0600, fetchmail, root) %{_sysconfdir}/fetchmailrc
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/fetchmail
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/fetchmail
%endif
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_libexecdir}/%{name}-systemd-exec
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%{_fillupdir}/sysconfig.%{name}

%files -n fetchmailconf
%{_bindir}/fetchmailconf
%{_mandir}/man1/fetchmailconf.1%{?ext_man}

%if 0%{suse_version} > 1500
%{python3_sitelib}/fetchmailconf.*
%{python3_sitelib}/__pycache__/fetchmailconf*
%endif

%changelog
