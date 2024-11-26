#
# spec file for package profanity
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


Name:           profanity
Version:        0.14.0
Release:        0
Summary:        Console-based XMPP client
License:        SUSE-GPL-3.0+-with-openssl-exception
Group:          Productivity/Networking/Instant Messenger
URL:            https://profanity-im.github.io
Source:         https://github.com/profanity-im/profanity/releases/download/%{version}/profanity-%{version}.tar.gz
Source1:        profanity-rpmlintrc
# all 4 patches taken from upstream repo
Patch0:         profanity-0.14.0-ox-carbons.patch
Patch1:         profanity-0.14.0-typos.patch
Patch2:         profanity-0.14.0-xscreensaver.patch
Patch3:         profanity-0.14.0-plugins-install.patch
BuildRequires:  glib2-devel >= 2.62
BuildRequires:  gtk2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libgcrypt-devel >= 1.7.0
BuildRequires:  libgpgme-devel
BuildRequires:  libnotify-devel
BuildRequires:  libotr-devel
BuildRequires:  libsignal-protocol-c-devel >= 2.3.2
BuildRequires:  libstrophe-devel >= 0.12.2
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite3-devel >= 3.22.0
Requires:       libstrophe0 >= 0.12.3
Requires:       profanity-binary = %{version}
Suggests:       profanity-standard

%description
Profanity is a console-based XMPP client written in C using ncurses,
and inspired by Irssi.

%package mini
Summary:        Console-based XMPP client
Group:          Productivity/Networking/Instant Messenger
Requires:       profanity = %{version}
Provides:       profanity-binary = %{version}-%{release}
Conflicts:      profanity-binary
Removepathpostfixes: .mini

%description mini
Profanity is a console-based XMPP client written in C using ncurses,
and inspired by Irssi.
This package holds a minimal version, with most options not compiled
in to have fewer dependencies. It is thus well suited for headless
servers.

%package standard
Summary:        Console-based XMPP client
Group:          Productivity/Networking/Instant Messenger
Requires:       profanity = %{version}
Provides:       profanity-binary = %{version}-%{release}
Conflicts:      profanity-binary
Removepathpostfixes: .standard

%description standard
Profanity is a-console based XMPP client written in C using ncurses,
and inspired by Irssi.

This package holds the standard version.
Including:
 * Desktop notifications (OSD)
 * Tray icon

%prep
%autosetup -p1
sed -i -e "s/python-config/python3-config/g" configure

%build
%configure PYTHON_VERSION=3 \
	--enable-notifications \
	--with-themes \
	--enable-otr \
	--enable-pgp \
	--enable-omemo \
	--enable-python-plugins \
	--enable-c-plugins \
	--enable-plugins \
	--enable-icons-and-clipboard

export CFLAGS="%{optflags} -fcommon"
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libprofanity.la

mv %{buildroot}%{_bindir}/profanity %{buildroot}%{_bindir}/profanity.standard

make clean

%configure PYTHON_VERSION=3 \
	--disable-notifications \
	--with-themes \
	--enable-otr \
	--enable-pgp \
	--enable-omemo \
	--enable-python-plugins \
	--enable-c-plugins \
	--enable-plugins \
    --disable-icons-and-clipboard

export CFLAGS="%{optflags} -fcommon"
make %{?_smp_mflags}
%make_install
rm %{buildroot}%{_libdir}/libprofanity.la

mv %{buildroot}%{_bindir}/profanity %{buildroot}%{_bindir}/profanity.mini

%files
%{_mandir}/man1/profanity.1%{?ext_man}
%{_mandir}/man1/profanity-*.1%{?ext_man}
%dir %{_datadir}/profanity/
%dir %{_datadir}/profanity/themes/
%dir %{_datadir}/profanity/icons/
%{_datadir}/profanity/themes/*
%{_datadir}/profanity/icons/*
# for now we will have them here
%{_libdir}/libprofanity.so*

%{_includedir}/profapi.h

%files mini
%{_bindir}/profanity.mini

%files standard
%{_bindir}/profanity.standard

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
