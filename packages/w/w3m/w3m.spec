#
# spec file for package w3m
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           w3m
Version:        0.5.6
Release:        0
Summary:        A text-based WWW browser
License:        ISC
Group:          Productivity/Networking/Web/Browsers
URL:            https://git.sr.ht/~rkta/w3m
Source0:        https://git.sr.ht/~rkta/w3m/archive/v%{version}.tar.gz
Patch:          po-install.patch
BuildRequires:  compface
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gpm
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
Provides:       w3m_ssl = %{version}
Provides:       web_browser
Obsoletes:      w3m_ssl < %{version}

%package inline-image
Summary:        An inline image extension for w3m
Group:          Productivity/Networking/Web/Browsers
BuildRequires:  imlib2-devel
Requires:       imlib2-loaders
Requires:       w3m
Provides:       w3m:%{_libdir}/w3m/w3mimgdisplay

%description
W3m is a pager and text-based WWW browser. It has a number of useful features:

* w3m can render tables
* w3m can render frames (it converts the frames into a table)
* SSL support
* w3m can easily display documents from standard input
* w3m can handle cookies
* w3m is small
* w3m has mouse support

If w3m-inline-image is installed it can display graphics inside terminals, even
on the console on some platforms.

%description inline-image
Inline image extension for w3m, the text-based WWW browser.

When this package is installed w3m can display images inline in an X terminal
(if it runs in a graphical X Window System environment).

%prep
%autosetup -p1 -n w3m-v%{version}

%build
export CFLAGS="%{optflags} -DUSE_BUFINFO -DOPENSSL_NO_SSL_INTERN -D_GNU_SOURCE $(getconf LFS_CFLAGS) -fno-strict-aliasing `ncursesw6-config --cflags` -fPIE -std=gnu11"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="`ncursesw6-config --libs` -pie"
%configure --with-termlib=ncursesw \
        --enable-ipv6 \
        --enable-alarm \
	--enable-ansi-color \
	--enable-digest-auth \
	--enable-external-uri-loader \
	--enable-gopher \
	--enable-history \
        --with-imagelib=imlib2 \
	--enable-keymap=lynx \
	--enable-m17n \
	--enable-mouse \
        --enable-nls \
	--enable-nntp \
	--enable-sslverify \
	--enable-unicode \
	--disable-w3mmailer
%make_build

%install
make install install-helpfile DESTDIR=%{buildroot}
install -d -m 0755 %{buildroot}%{_libdir}/w3m/cgi-bin
install -m 755 Bonus/*.cgi %{buildroot}%{_libdir}/w3m/cgi-bin
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/w3m
%{_bindir}/w3mman
%doc doc/*
%doc ChangeLog
%{_mandir}/de/man1/w3m*
%{_libdir}/w3m
%{_libexecdir}/w3m
%exclude %{_libexecdir}/w3m/w3mimgdisplay
%lang(ja)%{_mandir}/ja
%{_mandir}/man*/*
%{_datadir}/%{name}

%files inline-image
%dir %{_libexecdir}/w3m
%{_libexecdir}/w3m/w3mimgdisplay

%changelog
