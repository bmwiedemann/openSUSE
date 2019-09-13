#
# spec file for package mailx
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mailx
BuildRequires:  groff
BuildRequires:  krb5-devel
BuildRequires:  man
BuildRequires:  pcre
BuildRequires:  pkg-config
BuildRequires:  postfix
BuildRequires:  update-alternatives
BuildRequires:  pkgconfig(openssl)
Requires(post): update-alternatives
Requires(preun): update-alternatives
Url:            http://heirloom.sourceforge.net/mailx.html
Provides:       mail
Recommends:     smtp_daemon
Version:        12.5
Release:        0
Summary:        A MIME-Capable Implementation of the mailx Command
License:        BSD-4-Clause AND MPL-1.1
Group:          Productivity/Networking/Email/Utilities
Source:         mailx-%{version}.tar.bz2
Patch:          mailx-%{version}.dif
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nail is a mail user agent derived from Berkeley Mail 8.1.  It is
intended to provide the functionality of the POSIX.2 mailx command with
additional support for MIME messages, POP3, and SMTP.  In recent system
environments, nail is Unicode/UTF-8 capable.  Further, it contains some
minor enhancements like the ability to set a "From:" address.

%prep
%setup -q -n mailx-%{version}
%patch1 -p0 -b .path
%patch2 -p0 -b .rplyto
%patch3 -p0 -b .ttychr
%patch4 -p0 -b .toaddr
%patch5 -p0 -b .mime
%patch6 -p0 -b .ssl
%patch7 -p0 -b .par
%patch8 -p0 -b .ipv6
%patch9 -p1 -b .0001
%patch10 -p1 -b .0002
%patch11 -p1 -b .0003
%patch12 -p1 -b .0004
%patch13 -p0 -b .ssl11f
%patch -p1 -b .0

%build
    CC=gcc
    CFLAGS="%{optflags} -pipe -D_GNU_SOURCE -DOPENSSL_NO_SSL_INTERN $(pkg-config --cflags openssl)"
    export CC CFLAGS
    $SHELL ./makeconfig
    make %{?_smp_mflags} PREFIX=/usr CC="$CC" CFLAGS="$CFLAGS"
    tbl < mailx.1 | groff -mandocdb -Tps | grep -v %%%%CreationDate > manual.ps
    gzip -9fn manual.ps

%install
    %make_install PREFIX=/usr
    rm -rf %{buildroot}/bin
    mkdir  %{buildroot}/bin
    mkdir -p %{buildroot}%{_sysconfdir}/alternatives
    ln -sf %{_sysconfdir}/alternatives/binmail %{buildroot}/bin/mail
    ln -sf %{_sysconfdir}/alternatives/Mail    %{buildroot}/usr/bin/Mail
    ln -sf %{_sysconfdir}/alternatives/mail    %{buildroot}/usr/bin/mail
    ln -sf %{_sysconfdir}/alternatives/Mail.1%{?ext_man} %{buildroot}%{_mandir}/man1/Mail.1%{?ext_man}
    ln -sf %{_sysconfdir}/alternatives/mail.1%{?ext_man} %{buildroot}%{_mandir}/man1/mail.1%{?ext_man}
    #
    ln -sf %{_bindir}/mailx %{buildroot}%{_sysconfdir}/alternatives/binmail
    ln -sf %{_bindir}/mailx %{buildroot}%{_sysconfdir}/alternatives/Mail
    ln -sf %{_bindir}/mailx %{buildroot}%{_sysconfdir}/alternatives/mail
    ln -sf %{_mandir}/man1/mailx.1%{?ext_man} %{buildroot}%{_sysconfdir}/alternatives/Mail.1%{?ext_man}
    ln -sf %{_mandir}/man1/mailx.1%{?ext_man} %{buildroot}%{_sysconfdir}/alternatives/mail.1%{?ext_man}
    install -m 0644 mail.rc %{buildroot}/etc
    mkdir -p %{buildroot}%{_defaultdocdir}/%{name}

%post
%{_sbindir}/update-alternatives --quiet --force \
    --install %{_bindir}/mail mail %{_bindir}/mailx 20 \
    --slave   /bin/mail binmail %{_bindir}/mailx \
    --slave   %{_bindir}/Mail Mail %{_bindir}/mailx \
    --slave   %{_mandir}/man1/mail.1%{?ext_man} mail.1%{?ext_man} %{_mandir}/man1/mailx.1%{?ext_man} \
    --slave   %{_mandir}/man1/Mail.1%{?ext_man} Mail.1%{?ext_man} %{_mandir}/man1/mailx.1%{?ext_man}

%preun
if test ! -e %{_bindir}/mailx; then
  %{_sbindir}/update-alternatives --quiet --force --remove mail %{_bindir}/mailx
fi

%files
%defattr(-,root,root)
%license COPYING
%doc README manual.ps.gz nail.rc
/bin/mail
%config /etc/mail.rc
%ghost %config %{_sysconfdir}/alternatives/binmail
%ghost %config %{_sysconfdir}/alternatives/Mail
%ghost %config %{_sysconfdir}/alternatives/mail
%ghost %config %{_sysconfdir}/alternatives/Mail.1%{?ext_man}
%ghost %config %{_sysconfdir}/alternatives/mail.1%{?ext_man}
/usr/bin/Mail
/usr/bin/mail
/usr/bin/mailx
%doc %{_mandir}/man1/Mail.1.gz
%doc %{_mandir}/man1/mail.1.gz
%doc %{_mandir}/man1/mailx.1.gz

%changelog
