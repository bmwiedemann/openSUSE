#
# spec file for package msmtp
#
# Copyright (c) 2024 SUSE LLC
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


Name:           msmtp
Version:        1.8.26
Release:        0
BuildRequires:  gnutls-devel >= 3.4
BuildRequires:  libidn2-devel
BuildRequires:  pkg-config
BuildRequires:  xz
%if 0%{?suse_version} || 0%{?centos_version} == 700
# keyring integration for recent openSUSE and CentOS
BuildRequires:  libsecret-devel
%endif
%if 0%{?suse_version}
BuildRequires:  libgsasl-devel >= 2.1.0
%endif
# for the directory
%if 0%{?centos_version}
BuildRequires:  vim-common
%requires_eq    vim-common
%else
BuildRequires:  vim-base
%requires_eq    vim-base
%endif #centos_version
%if 0%{?suse_version}
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%endif
Summary:        Lightweight SMTP Client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            https://marlam.de/msmtp/
Source:         https://marlam.de/msmtp/releases/msmtp-%{version}.tar.xz
Source1:        https://marlam.de/msmtp/releases/msmtp-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
msmtp is an SMTP client that can be used as a plug-in for Mutt and
other mail user agents.  It forwards mail to an SMTP server that does
the delivery.  msmtp supports multiple accounts.

%lang_package

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
msmtp is an SMTP client that can be used as a plug-in for Mutt and
other mail user agents.  It forwards mail to an SMTP server that does
the delivery.  msmtp supports multiple accounts.

This subpackage contains the documentation for %{name}, including
examples and sample configuration files.

%package mta
Summary:        MTA based on %{name}
Group:          Productivity/Networking/Email/Servers
Requires:       %{name} = %{version}
Conflicts:      exim
Conflicts:      postfix
Conflicts:      postfix-bdb
Conflicts:      sendmail
Conflicts:      sendmail-tls
Provides:       smtp_daemon

%description mta
msmtp is an SMTP client that can be used as a plug-in for Mutt and
other mail user agents.  It forwards mail to an SMTP server that does
the delivery.  msmtp supports multiple accounts.

This subpackage provides a mail transfer agent that can be used as
a minimalistic replacement of sendmail and a minimal SMTP server.

%prep
%setup -q
# fix bash and sh scripts shebang while preserving mtime
for i in scripts/msmtpqueue/*.sh \
         scripts/msmtpq/msmtpq \
         scripts/msmtpq/msmtp-queue \
         scripts/set_sendmail/*.sh \
         scripts/find_alias/*.sh; do
    sed '1 s|#!/usr/bin/env \(.*\)|#!/bin/\1|' $i > $i.new
    touch -r $i $i.new
    mv $i.new $i
done

%build
%configure --docdir="%{_docdir}/%{name}" --with-tls=gnutls --with-libgsasl
%make_build

%install
%make_install V=1
%find_lang %{name}
for i in README ChangeLog ; do
    cp scripts/msmtpqueue/$i ${i}.msmtpqueue
done
cp scripts/msmtpq/README.msmtpq    README.msmtpq
cp scripts/vim/README              README.vim

install -m 0755 \
        scripts/msmtpqueue/*.sh \
        scripts/msmtpq/msmtpq \
        scripts/msmtpq/msmtp-queue \
        scripts/set_sendmail/*.sh \
        scripts/find_alias/*.sh \
    %{buildroot}%{_bindir}

# find where to install vim syntax
# start with the "site" directory, then "current" and finally any "vim??"
for vimsyntax in %{_datadir}/vim/{site,current,vim[0-9][0-9]}/syntax; do
    if [ -d $vimsyntax ]; then
        break
    fi
done
install -D -m 0644 scripts/vim/msmtp.vim %{buildroot}$vimsyntax/msmtp.vim

# main package doc files
for f in \
COPYING\
; do
    install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$f"
done

# doc files
echo -n >docfiles.lst
for f in \
AUTHORS ChangeLog* NEWS README README.msmtpqueue README.msmtpq THANKS \
doc/*.example \
scripts/set_sendmail/set_sendmail.conf \
; do
    ff="${f##*/}"
    install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$ff"
    echo "%doc %{_docdir}/%{name}/$ff" >>docfiles.lst
done

# mta files
install -d %{buildroot}%{_sbindir}
ln -s %{_bindir}/msmtp %{buildroot}%{_sbindir}/sendmail
ln -s %{_mandir}/man1/msmtp.1%{ext_man} %{buildroot}%{_mandir}/man1/sendmail.1%{ext_man}

# not properly ignored on Fedora 10:
rm -f "%{buildroot}%{_infodir}/dir"

%if 0%{?suse_version}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/msmtp.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/msmtp.info%{ext_info}
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}

%post
[ "$1" = "1" ] && /sbin/install-info "%{_infodir}/%{name}.info%{ext_info}" || :

%preun
[ "$1" = "0" ] && /sbin/install-info --delete "%{_infodir}/%{name}.info%{ext_info}" || :
%endif # fedora

%files
%doc %dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/COPYING
%{_bindir}/msmtp
%{_bindir}/msmtpq
%{_bindir}/msmtp-queue
%{_bindir}/msmtp-enqueue.sh
%{_bindir}/msmtp-runqueue.sh
%{_bindir}/msmtp-listqueue.sh
%{_bindir}/set_sendmail.sh
%{_bindir}/find_alias_for_msmtp.sh
%{_mandir}/man1/msmtp.1%{?ext_man}
%{_infodir}/msmtp.info%{?ext_info}
%{_datadir}/vim/*/syntax/msmtp.vim

%files lang -f %{name}.lang

%files doc -f docfiles.lst
%doc %dir %{_docdir}/%{name}

%files mta
%{_bindir}/msmtpd
%{_sbindir}/sendmail
%{_mandir}/man1/msmtpd.1%{?ext_man}
%{_mandir}/man1/sendmail.1%{?ext_man}

%changelog
