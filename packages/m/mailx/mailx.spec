#
# spec file for package mailx
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           mailx
BuildRequires:  groff
BuildRequires:  krb5-devel
BuildRequires:  man
BuildRequires:  pkg-config
BuildRequires:  postfix
BuildRequires:  update-alternatives
BuildRequires:  pkgconfig(openssl)
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
URL:            http://heirloom.sourceforge.net/mailx.html
Provides:       mail
Recommends:     smtp_daemon
Version:        12.5
Release:        0
Summary:        A MIME-Capable Implementation of the mailx Command
License:        BSD-4-Clause AND MPL-1.1
Group:          Productivity/Networking/Email/Utilities
Source:         mailx-%{version}.tar.bz2
Patch0:         mailx-%{version}.dif
Patch1:         nail-11.25-path.dif
Patch2:         mailx-%{version}-replyto.patch
Patch3:         nail-11.25-ttychar.dif
Patch4:         nail-11.25-toaddr.dif
Patch5:         mailx-%{version}-mime.dif
Patch6:         mailx-fix-openssl.patch
#PATCH-FIX-OPENSUSE: Try to tranquilize gcc warning about parentheses (please check!)
Patch7:         mailx-12.5-parentheses.dif
#PATCH-FIX-SUSE: Fix IPv6 address handling
Patch8:         mailx-12.5-ipv6.dif
#PATCH-FIX-SUSE: bsc#909208 -- CVE-2004-2771, CVE-2014-7844: mailx: shell command injection via crafted email addresses
Patch9:         0001-outof-Introduce-expandaddr-flag.patch
#PATCH-FIX-SUSE: bsc#909208 -- CVE-2004-2771, CVE-2014-7844: mailx: shell command injection via crafted email addresses
Patch10:        0002-unpack-Disable-option-processing-for-email-addresses.patch
#PATCH-FIX-SUSE: bsc#909208 -- CVE-2004-2771, CVE-2014-7844: mailx: shell command injection via crafted email addresses
Patch11:        0003-fio.c-Unconditionally-require-wordexp-support.patch
#PATCH-FIX-SUSE: bsc#909208 -- CVE-2004-2771, CVE-2014-7844: mailx: shell command injection via crafted email addresses
Patch12:        0004-globname-Invoke-wordexp-with-WRDE_NOCMD-CVE-2004-277.patch
#PATCH-FIX-SUSE: bsc#1042663 -- mailx fails to build with openssl-1.1
Patch13:        mailx-12.5-openssl-1.1.0f.patch
#PATCH-FIX-SUSE: bsc#1180355 -- mailx calls sendmail with wrong name
Patch14:        fix-sendmail-name.patch
#PATCH-FIX-SUSE: bsc#1192916 - mailx does not send mails unless run via strace or in verbose mode
Patch15:        mailx-12.5-systemd.patch
#Moving /etc/mailrc to /usr/etc/mail.rc
Patch16:        mailx-usr-etc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nail is a mail user agent derived from Berkeley Mail 8.1.  It is
intended to provide the functionality of the POSIX.2 mailx command with
additional support for MIME messages, POP3, and SMTP.  In recent system
environments, nail is Unicode/UTF-8 capable.  Further, it contains some
minor enhancements like the ability to set a "From:" address.

%prep
%setup -q -n mailx-%{version}
%patch -P 1 -p0 -b .path
%patch -P 2 -p0 -b .rplyto
%patch -P 3 -p0 -b .ttychr
%patch -P 4 -p0 -b .toaddr
%patch -P 5 -p0 -b .mime
%patch -P 6 -p0 -b .ssl
%patch -P 7 -p0 -b .par
%patch -P 8 -p0 -b .ipv6
%patch -P 9 -p1 -b .0001
%patch -P 10 -p1 -b .0002
%patch -P 11 -p1 -b .0003
%patch -P 12 -p1 -b .0004
%patch -P 13 -p0 -b .ssl11f
%patch -P 14 -p1 -b .sendmail
%patch -P 15 -p0 -b .systemd
%patch -P 0 -p1 -b .0
%patch -P 16 -p1 -b .usretc

%build
    CC=gcc
    CFLAGS="%{optflags} -pipe -D_GNU_SOURCE -DOPENSSL_NO_SSL_INTERN $(pkg-config --cflags openssl)"
    export CC CFLAGS
    $SHELL ./makeconfig
%if 0%{?suse_version} > 1500
    make %{?_smp_mflags} PREFIX=/usr CC="$CC" CFLAGS="$CFLAGS" DISTCONF="-DDISTCONFMAILRC=\"\\\"/usr/etc/mail.rc\\\"\""
%else
    make %{?_smp_mflags} PREFIX=/usr CC="$CC" CFLAGS="$CFLAGS"
%endif
    tbl < mailx.1 | groff -mandocdb -Tps | grep -v %%%%CreationDate > manual.ps
    gzip -9fn manual.ps

%install
    %make_install PREFIX=/usr
    rm -rf %{buildroot}/bin
    mkdir  %{buildroot}/bin
%if ! %{with libalternatives}
    # create symlinks for update-alternatives
    mkdir -p %{buildroot}%{_sysconfdir}/alternatives
%if 0%{?suse_version} < 1550
    ln -sf %{_sysconfdir}/alternatives/binmail %{buildroot}/bin/mail
%endif
    ln -sf %{_sysconfdir}/alternatives/Mail    %{buildroot}/usr/bin/Mail
    ln -sf %{_sysconfdir}/alternatives/mail    %{buildroot}/usr/bin/mail
    ln -sf %{_sysconfdir}/alternatives/Mail.1%{?ext_man} %{buildroot}%{_mandir}/man1/Mail.1%{?ext_man}
    ln -sf %{_sysconfdir}/alternatives/mail.1%{?ext_man} %{buildroot}%{_mandir}/man1/mail.1%{?ext_man}
    #
%if 0%{?suse_version} < 1550
    ln -sf %{_bindir}/mailx %{buildroot}%{_sysconfdir}/alternatives/binmail
%endif
    ln -sf %{_bindir}/mailx %{buildroot}%{_sysconfdir}/alternatives/Mail
    ln -sf %{_bindir}/mailx %{buildroot}%{_sysconfdir}/alternatives/mail
    ln -sf %{_mandir}/man1/mailx.1%{?ext_man} %{buildroot}%{_sysconfdir}/alternatives/Mail.1%{?ext_man}
    ln -sf %{_mandir}/man1/mailx.1%{?ext_man} %{buildroot}%{_sysconfdir}/alternatives/mail.1%{?ext_man}
%else
    ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/Mail
%if 0%{?suse_version} < 1550
    ln -sf %{_bindir}/alts %{buildroot}/bin/Mail
%endif
    mkdir -p %{buildroot}%{_datadir}/libalternatives/Mail
    cat > %{buildroot}%{_datadir}/libalternatives/Mail/20.conf <<EOF
binary=%{_bindir}/mailx
man=mailx.1
group=mail, Mail
EOF
    ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/mail
%if 0%{?suse_version} < 1550
    ln -sf %{_bindir}/alts %{buildroot}/bin/mail
%endif
    mkdir -p %{buildroot}%{_datadir}/libalternatives/mail
    cat > %{buildroot}%{_datadir}/libalternatives/mail/20.conf <<EOF
binary=%{_bindir}/mailx
man=mailx.1
group=mail, Mail
EOF
%endif

%if 0%{?suse_version} > 1500
    mkdir -p %{buildroot}%{_distconfdir}
    install -m 0644 mail.rc %{buildroot}%{_distconfdir}
    rm %{buildroot}/etc/mail.rc
%else
    install -m 0644 mail.rc %{buildroot}/etc
%endif
    mkdir -p %{buildroot}%{_defaultdocdir}/%{name}

%if ! %{with libalternatives}
%post
%{_sbindir}/update-alternatives --quiet --force \
    --install %{_bindir}/mail mail %{_bindir}/mailx 20 \
%if 0%{?suse_version} < 1550
    --slave   /bin/mail binmail %{_bindir}/mailx \
%endif
    --slave   %{_bindir}/Mail Mail %{_bindir}/mailx \
    --slave   %{_mandir}/man1/mail.1%{?ext_man} mail.1%{?ext_man} %{_mandir}/man1/mailx.1%{?ext_man} \
    --slave   %{_mandir}/man1/Mail.1%{?ext_man} Mail.1%{?ext_man} %{_mandir}/man1/mailx.1%{?ext_man}

%postun
if test ! -e %{_bindir}/mailx; then
  %{_sbindir}/update-alternatives --quiet --force --remove mail %{_bindir}/mailx
fi
%endif

%pre
echo "Calling pre installation script"
%if %{with libalternatives}
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
  %{_sbindir}/update-alternatives --quiet --force --remove mail %{_bindir}/mailx
fi
%endif
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in mail.rc; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in mail.rc; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc README manual.ps.gz nail.rc
%if 0%{?suse_version} > 1500
%{_distconfdir}/mail.rc
%else
%config /etc/mail.rc
%endif
%if 0%{?suse_version} < 1550
/bin/mail
%endif
/usr/bin/Mail
/usr/bin/mail
%if ! 0%{with libalternatives}
%if 0%{?suse_version} < 1550
%ghost %config %{_sysconfdir}/alternatives/binmail
%endif
%ghost %config %{_sysconfdir}/alternatives/Mail
%ghost %config %{_sysconfdir}/alternatives/mail
%ghost %config %{_sysconfdir}/alternatives/Mail.1%{?ext_man}
%ghost %config %{_sysconfdir}/alternatives/mail.1%{?ext_man}
%doc %{_mandir}/man1/Mail.1.gz
%doc %{_mandir}/man1/mail.1.gz
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/mail
%dir %{_datadir}/libalternatives/Mail
%{_datadir}/libalternatives/Mail/20.conf
%{_datadir}/libalternatives/mail/20.conf
%endif

/usr/bin/mailx
%doc %{_mandir}/man1/mailx.1.gz

%changelog
