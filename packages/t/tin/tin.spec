#
# spec file for package tin
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011-2016 dnh@opensuse.org
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


Name:           tin
Version:        2.6.4
Release:        0
Summary:        Threaded NNTP and spool-based UseNet news reader
License:        BSD-3-Clause
Group:          Productivity/Networking/News/Clients
URL:            http://www.tin.org/
# OBS bots have problems reaching the ftp server, see <https://build.opensuse.org/requests/1286405>
# Source0:        ftp://ftp.tin.org/pub/news/clients/tin/stable/%%{name}-%%{version}.tar.xz
# Source1:        ftp://ftp.tin.org/pub/news/clients/tin/stable/%%{name}-%%{version}.tar.xz.sign
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.sign
Patch0:         tin-2.6.0-unread-not-lines.patch
Patch1:         tin-2.0.0_toggle_rot_key.patch
BuildRequires:  bison
BuildRequires:  gpg2
BuildRequires:  pkgconfig
BuildRequires:  smtp_daemon
BuildRequires:  xz
# JFTR: tin does NOT check for or use Cyrus-SASL! So keep GNU SASL!
BuildRequires:  pkgconfig(libgsasl)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
Recommends:     gpg2
Recommends:     mutt
Recommends:     smtp_daemon

%description
tin is a full-screen Usenet news reader for the console. It can read
news locally (/var/spool/news) or remotely via an NNTP server. It
supports threading, scoring, different charsets and support for
different languages. It automatically utilizes NOV newsoverview(5)
style index files if available locally or via the NNTP [X]OVER
command.

This version contains two patches by dnh@opensuse.org changing the
default key for toggling rot13 from '%' to 'd' and displaying the
number of unread posts instead of lines in the threadlist. If you, as
a user, disagree with these patches, do contact dnh.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -DUSE_CANLOCK=1"

# Do not enable FORGERY, doc/INSTALL suggests "[FORGERY] should not be used in a free accessible tin"
export CFLAGS="$CFLAGS $(ncursesw6-config --cflags)"

# without LDFLAGS ld searches %%{_lib} first, and finds %%{_lib}libncursesw.so
# before trying %%{_lib}/ncurses6/ from ncursesw6-config.
export LDFLAGS="$(ncursesw6-config --libs)"

%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --enable-echo \
    --verbose \
    --enable-debug \
    --enable-prototypes \
    --enable-warnings \
    --enable-flock \
    --with-nntp-default-server="localhost" \
    --with-mailer="mutt" \
    --with-local-charset="UTF-8" \
    --with-mime-default-charset="UTF-8" \
    --disable-mime-strict-charset \
    --with-iso-to-ascii="-1" \
    --with-screen="ncursesw" \
    --enable-mh-mail-handling \
    --enable-break-long-lines \
    --enable-cancel-locks \
    --enable-ipv6 \
    --enable-long-article-numbers \
    --with-coffee \
    --with-pcre2-config \
    --with-nntps=openssl

%make_build

%install
%make_install
%make_build DESTDIR=%{buildroot} install_sysdefs

install -d -m 755 %{buildroot}%{_mandir}/man3
install -m 755 doc/wildmat.3 %{buildroot}%{_mandir}/man3
install -m 755 doc/newsoverview.5 %{buildroot}%{_mandir}/man5
rm -f %{buildroot}%{_mandir}/man5/mbox.5
rm -f %{buildroot}%{_mandir}/man5/mmdf.5
find "%{buildroot}%{_mandir}" -type f -not -name '*.gz' -exec chmod 644 {} + -exec gzip -vf {} +
bzip2 -vkf doc/CHANGES.old

%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%doc README doc/CHANGES doc/CHANGES.old.bz2 doc/CREDITS doc/TODO doc/WHATSNEW
%doc doc/*.txt doc/config-anomalies doc/filtering doc/good-netkeeping-seal
%doc doc/*.sample tools/expiretover
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_mandir}/man?/*.?%{?ext_man}

%changelog
