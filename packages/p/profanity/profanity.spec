#
# spec file for package profanity
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.9.2
Release:        0
Summary:        Console-based XMPP client
License:        SUSE-GPL-3.0+-with-openssl-exception
Group:          Productivity/Networking/Instant Messenger
URL:            https://profanity-im.github.io
Source:         https://github.com/profanity-im/profanity/releases/download/%{version}/profanity-%{version}.tar.gz
Source1:        profanity-rpmlintrc
BuildRequires:  glib2-devel >= 2.56
BuildRequires:  gtk2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libgcrypt-devel >= 1.7.0
BuildRequires:  libgpgme-devel
BuildRequires:  libmesode-devel >= 0.9.3
BuildRequires:  libnotify-devel
BuildRequires:  libotr-devel
BuildRequires:  libsignal-protocol-c-devel >= 2.3.1
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite3-devel >= 3.22.0
Requires:       libmesode0 >= 0.9.3
Requires:       profanity-binary = %{version}

%description
Profanity is a console-based XMPP client written in C using ncurses,
and inspired by Irssi.

%package mini
Summary:        Console-based XMPP client
Group:          Productivity/Networking/Instant Messenger
Requires:       profanity = %{version}
Requires(post): update-alternatives
Requires(preun): update-alternatives
Provides:       profanity-binary = %{version}-%{release}

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
Requires(post): update-alternatives
Requires(preun): update-alternatives
Provides:       profanity-binary = %{version}-%{release}

%description standard
Profanity is a-console based XMPP client written in C using ncurses,
and inspired by Irssi.

This package holds the standard version.
Including:
 * Desktop notifications (OSD)
 * Tray icon

%prep
%setup -q
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
	--enable-icons

export CFLAGS="%{optflags} -fcommon"
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libprofanity.la

mv %{buildroot}%{_bindir}/profanity{,-standard}

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
	--disable-icons

export CFLAGS="%{optflags} -fcommon"
make %{?_smp_mflags}
%make_install
rm %{buildroot}%{_libdir}/libprofanity.la

mv %{buildroot}%{_bindir}/profanity{,-mini}

# u-a handling
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -s profanity %{buildroot}%{_sysconfdir}/alternatives/profanity
ln -s profanity %{buildroot}%{_bindir}/profanity

%files
%{_mandir}/man1/profanity.1%{?ext_man}
%dir %{_datadir}/profanity/
%dir %{_datadir}/profanity/themes/
%dir %{_datadir}/profanity/icons/
%{_datadir}/profanity/themes/*
%{_datadir}/profanity/icons/*
# for now we will have them here
%{_libdir}/libprofanity.so*

%{_includedir}/profapi.h

%files mini
%ghost %{_sysconfdir}/alternatives/profanity
%ghost %{_bindir}/profanity
%{_bindir}/profanity-mini

%files standard
%ghost %{_sysconfdir}/alternatives/profanity
%ghost %{_bindir}/profanity
%{_bindir}/profanity-standard

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post mini
%{_sbindir}/update-alternatives --install \
    %{_bindir}/profanity profanity %{_bindir}/profanity-mini 10

%preun mini
if [ "$1" = 0 ] ; then
  %{_sbindir}/update-alternatives --remove profanity %{_bindir}/profanity-mini
fi

%post standard
%{_sbindir}/update-alternatives --install \
    %{_bindir}/profanity profanity %{_bindir}/profanity-standard 20
/sbin/ldconfig

%preun standard
if [ "$1" = 0 ] ; then
  %{_sbindir}/update-alternatives --remove profanity %{_bindir}/profanity-standard
fi

%changelog
