#
# spec file for package w3m
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


Name:           w3m
URL:            http://w3m.sourceforge.net/
Version:        0.5.3+git20180125
Release:        0
Summary:        A text-based WWW browser
License:        ISC
Group:          Productivity/Networking/Web/Browsers

Source0:        w3m-%{version}.tar.xz
Patch0:         0001-allow-to-configure-the-accept-option-for-bad-cookies.patch
Patch1:         0001-implements-simple-session-management.patch
Patch2:         0001-handle-EXDEV-during-history-file-rename.patch
Patch3:         0001-w3mman-don-t-show-invalid-characters-bsc-950800.patch
Patch4:         0001-Fix-warning-for-unused-variable-without-USE_M17N.patch
Patch5:         0002-Fix-m17n-backspace-handling-causes-out-of-bounds-wri.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
BuildRequires:  gpm
BuildRequires:  imlib2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
Provides:       w3m_ssl = %version
Provides:       web_browser
Obsoletes:      w3m_ssl < %version

%package inline-image
Summary:        An inline image extension for w3m
Group:          Productivity/Networking/Web/Browsers
Requires:       imlib2-loaders
Requires:       w3m
Provides:       w3m:/usr/%_lib/w3m/w3mimgdisplay

%description
W3m is a pager and text-based WWW browser. It has a number of useful
features:

* w3m can render tables

* w3m can render frames (it converts the frames into a table)

* SSL support

* w3m can easily display documents from standard input

* w3m can handle cookies

* w3m is small

* w3m has mouse support

If w3m-inline-image is installed it can display graphics inside
terminals, even on the console on some platforms.

%description inline-image
Inline image extension for w3m, the text-based WWW browser.

When this package is installed w3m can display images inline in an X
terminal (if it runs in a graphical X Window System environment).

%prep
%setup -q -n w3m-%{version}
find -name CVS -exec rm -Rf "{}" "+"
%autopatch -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -DUSE_BUFINFO -DOPENSSL_NO_SSL_INTERN -D_GNU_SOURCE $(getconf LFS_CFLAGS) -fno-strict-aliasing `ncursesw6-config --cflags` -fPIE"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="`ncursesw6-config --libs` -pie"
./configure	--bindir=/usr/bin \
        --with-termlib=ncursesw \
		--mandir=%_mandir \
		--libdir=%_libdir \
		--libexecdir=%_libdir \
		--prefix=/usr \
		--sysconfdir=/etc \
		--enable-ipv6 \
		--enable-alarm \
		--enable-ansi-color \
		--enable-digest-auth \
		--enable-external-uri-loader \
		--enable-gopher \
		--enable-history \
		--enable-image=x11,fb \
		--enable-keymap=lynx \
		--enable-m17n \
		--enable-mouse \
		--enable-nls \
		--enable-nntp \
		--enable-sslverify \
		--enable-unicode \
		--disable-w3mmailer
make %{?_smp_mflags}

%install
make install install-helpfile DESTDIR=$RPM_BUILD_ROOT
install -m 755 Bonus/*.cgi $RPM_BUILD_ROOT/usr/%_lib/w3m/cgi-bin
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
/usr/bin/w3m
/usr/bin/w3mman
%doc doc/*
%doc ChangeLog
%_mandir/de/man1/w3m*
%_libdir/w3m
%exclude %_libdir/w3m/w3mimgdisplay
%lang(ja)%doc %_mandir/ja
%doc %_mandir/man*/*
%_datadir/%name

%files inline-image
%defattr(-,root,root)
%dir %_libdir/w3m
/usr/%_lib/w3m/w3mimgdisplay

%changelog
