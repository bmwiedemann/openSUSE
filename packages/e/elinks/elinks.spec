#
# spec file for package elinks
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
%bcond_without js
%else
%bcond_with js
%endif

Name:           elinks
Version:        0.16.1.1
Release:        0
Summary:        An advanced and well-established feature-rich text mode web browser
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            http://elinks.or.cz/
Source0:        https://github.com/rkd77/elinks/releases/download/v%{version}/elinks-%{version}.tar.xz
Patch0:         0006-elinks-0.16.0-libidn2.patch
BuildRequires:  gcc-c++
BuildRequires:  gpm-devel
%if %{with js}
BuildRequires:  pkgconfig(libcss)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml++-5.0)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(sqlite3)
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  krb5-devel
BuildRequires:  libbz2-devel
BuildRequires:  libexpat-devel
BuildRequires:  libidn2-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  ruby-devel
BuildRequires:  tre-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(luajit)
Provides:       web_browser
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%perl_requires
%requires_eq    perl

%description
ELinks is an advanced and well-established feature-rich text mode web
(HTTP/FTP/..) browser. ELinks can render both frames and tables, is highly
customizable and can be extended via Lua or Guile scripts. It is very portable
and runs on a variety of platforms. Check the about page for a more complete
description.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
# Remove build time references so build-compare can do its work
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/vernum.c
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/vernum.c

%build
# required for ruby patch
sh ./autogen.sh
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --sysconfdir=%{_sysconfdir}/elinks \
    --enable-bittorrent \
    --enable-cgi \
    --enable-finger \
    --disable-fsp \
    --enable-gopher \
    --enable-nntp \
    --disable-smb \
    --enable-88-colors \
    --enable-256-colors \
    --enable-true-color \
    --enable-exmode \
    --enable-html-highlight \
    --enable-fastmem \
    --with-xterm \
%if %{without js}
    --without-mujs \
%else
    --with-mujs \
%endif
    --without-lzma \
    --with-gssapi \
    --without-guile \
    --with-perl \
    --without-python \
    --with-luapkg=luajit \
    --with-ruby \
    --without-gnutls \
    --without-x
# Makefile is not parallel-safe
make MAKE_COLOR= V=1

%install
%make_install

# Remove unneeded file
rm -f %{buildroot}%{_datadir}/locale/locale.alias

%find_lang %{name}

# Install documentation
%define _pkgdocdir %{buildroot}%{_docdir}/%{name}
install -Dd -m 0755 %{_pkgdocdir}
install -pm 0644 AUTHORS BUGS COPYING ChangeLog NEWS SITES THANKS TODO features.conf %{_pkgdocdir}
cp -a doc/ %{_pkgdocdir}
rm -rf %{_pkgdocdir}/doc/{.deps/,.gitignore,Doxyfile.in,Makefile,man/,tools/}
install -Dd -m 0755 %{_pkgdocdir}/contrib/
install -pm 0644 contrib/*.conf contrib/*.vim contrib/*.css contrib/TIPS-AND-TRICKS %{_pkgdocdir}/contrib/
install -Dd -m 0755 %{_pkgdocdir}/scripts/
install -pm 0644 contrib/wipe-out-ssl* contrib/conv/* %{_pkgdocdir}/scripts/
rm -f %{_pkgdocdir}/scripts/conv/.gitignore
# Install only the languages that are compiled
for lang in lua perl smjs ruby; do
  install -Dd -m 0755 %{_pkgdocdir}/${lang}
  install -pm 0644 contrib/${lang}/* %{_pkgdocdir}/${lang}
done
rm -f %{_pkgdocdir}/lua/.gitignore

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc %{_docdir}/%{name}/
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man5/%{name}*.5%{ext_man}

%changelog
