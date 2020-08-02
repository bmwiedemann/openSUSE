#
# spec file for package lynx
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


%define tarbase 2.8.9rel.1
Name:           lynx
Version:        2.8.9rel.1
Release:        0
Summary:        A Text-Based WWW Browser
License:        GPL-2.0-only
Group:          Productivity/Networking/Web/Browsers
Url:            http://lynx.invisible-island.net/
Source:         http://invisible-mirror.net/archives/%{name}/tarballs/%{name}%{tarbase}.tar.bz2
# changing default configuration
Patch0:         lynx-charset.patch
Patch1:         lynx-enable_xli.patch
# bugs
Patch3:         lynx-proxy-empty-string.patch
BuildRequires:  libbz2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  postfix
BuildRequires:  zlib-devel
Requires:       xli
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         /bin/cp
Provides:       web_browser
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Lynx is an easy-to-use browser for HTML documents and other Internet
services like FTP, telnet, and news.  Lynx is fast.  It is purely text
based and therefore makes it possible to use WWW resources on text
terminals.

%prep
%setup -q -n %{name}%{tarbase}
%patch0 -p1
%patch1 -p1
%patch3 -p1

%build
%configure --enable-debug --with-build-cflags="%{optflags} -DNO_BUILDSTAMP" \
	--with-ssl \
	--with-zlib \
	--with-bzlib \
	--enable-nls \
	--disable-default-colors \
	--disable-color-style \
	--with-screen=ncursesw \
	--enable-ipv6
make %{?_smp_mflags}
mv lynx lynx-bw
make %{?_smp_mflags} distclean
%configure --enable-debug --with-build-cflags="%{optflags}" \
	--with-ssl \
	--with-bzlib \
	--enable-nls \
	--enable-default-colors \
	--with-screen=ncursesw \
	--enable-ipv6
make %{?_smp_mflags}

%install
%make_install
make clean
mkdir -p %{buildroot}
mv %{buildroot}%{_bindir}/lynx %{buildroot}%{_bindir}/lynx-color
install lynx-bw %{buildroot}%{_bindir}/lynx

chmod ogu-x scripts/conf.mingw.sh scripts/config.djgpp.sh

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/lynx
%{_bindir}/lynx-color
%config %{_sysconfdir}/lynx.cfg
%config %{_sysconfdir}/lynx.lss
%{_mandir}/man1/lynx.1%{ext_man}
%doc AUTHORS CHANGES README COPYING README PROBLEMS
%doc lynx_help samples scripts

%changelog
