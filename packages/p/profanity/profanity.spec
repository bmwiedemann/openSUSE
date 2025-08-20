#
# spec file for package profanity
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global flavor @BUILD_FLAVOR@%{nil}
%global sname profanity
%if "%{flavor}" == ""
%global pname %{sname}
%else
%global pname %{sname}-%{flavor}
%endif
%define sover 0
# standard flavor
%if "%{flavor}" == ""
%bcond_without notifications
%bcond_without xscreensaver
%bcond_without icons
%bcond_without scaled_avatars
%bcond_without tests
%else
# -mini
%bcond_with notifications
%bcond_with xscreensaver
%bcond_with icons
%bcond_with scaled_avatars
%bcond_with tests
%endif
# common to both
%bcond_without python
%bcond_without otr
%bcond_without gpg
%bcond_without omemo
%bcond_without omemo_qrcode
#
Name:           %{pname}
Version:        0.15.0
Release:        0
Summary:        Console-based XMPP client
License:        SUSE-GPL-3.0+-with-openssl-exception
Group:          Productivity/Networking/Instant Messenger
URL:            https://profanity-im.github.io
Source:         https://github.com/profanity-im/profanity/releases/download/%{version}/profanity-%{version}.tar.gz
# bsc#1246850: Fix build with gpgme >= 2.0.0. See gh/profanity#2048
Patch0:         profanity-0.15.0-gpgme.patch
# fixes tests build with ggc15. See gh/profanity#2055
Patch1:         profanity-0.15.0-Fix-tests-with-gcc15-uintptr_t.patch
BuildRequires:  pkgconfig
# mandatory requirements
BuildRequires:  pkgconfig(glib-2.0) >= 2.62
BuildRequires:  pkgconfig(libcurl) >= 7.62.0
BuildRequires:  pkgconfig(libstrophe) >= 0.12.3
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sqlite3) >= 3.22.0
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(readline)
%endif
Conflicts:      profanity-binary
Provides:       profanity-binary = %{version}
# optional requirements
%if %{with notifications}
BuildRequires:  pkgconfig(libnotify)
%endif
%if %{with python}
BuildRequires:  python3-devel
%endif
%if %{with otr}
BuildRequires:  pkgconfig(libotr) >= 4.0
%endif
%if %{with gpg}
BuildRequires:  pkgconfig(gpgme)
%endif
%if %{with omemo}
BuildRequires:  pkgconfig(libgcrypt) >= 1.7.0
BuildRequires:  pkgconfig(libsignal-protocol-c) >= 2.3.2
%endif
%if %{with xscreensaver}
BuildRequires:  pkgconfig(xscrnsaver)
%endif
%if %{with icons}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
%endif
%if %{with scaled_avatars}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
%endif
%if %{with omemo_qrcode}
BuildRequires:  pkgconfig(libqrencode)
%endif
# tests requirements
%if %{with tests}
BuildRequires:  expect
BuildRequires:  pkgconfig(cmocka)
%endif
%if "%{flavor}" == ""
Obsoletes:      profanity-standard
%endif

%description
Profanity is a console-based XMPP client written in C using ncurses, and
inspired by Irssi.
%if "%{flavor}" == "mini"
This package holds a minimal version, with most options not compiled
in to have fewer dependencies. It is thus well suited for headless
servers.
%endif

# only standard flavor builds the plugin library
%if "%{flavor}" == ""
%package -n libprofanity%{sover}
Summary:        Shared library for the %{name} console-based XMPP client

%description -n libprofanity%{sover}
Profanity is a console-based XMPP client written in C using ncurses, and
inspired by Irssi.

This package contains the shared library used by the profanity client and
plug-ins.

%package devel
Summary:        Development files for the libprofanity XMPP client library
Requires:       libprofanity%{sover} = %{version}

%description devel
Profanity is a console-based XMPP client written in C using ncurses, and
inspired by Irssi.

This package contains the files needed to build with libprofanity.
%endif

%prep
%autosetup -p1 -n %{sname}-%{version}
sed -i -e "s/python-config/python3-config/g" configure

%build
%configure \
%if %{with notifications}
	--enable-notifications \
%endif
%if %{with python}
	PYTHON_VERSION=3 \
	--enable-python-plugins \
%endif
	--enable-c-plugins \
	--enable-plugins \
%if %{with otr}
	--enable-otr \
%endif
%if %{with gpg}
	--enable-pgp \
%endif
%if %{with omemo}
	--enable-omemo \
%endif
%if %{with xscreensaver}
	--with-xscreensaver \
%endif
	--with-themes \
%if %{with icons}
	--enable-icons-and-clipboard \
%endif
%if %{with scaled_avatars}
	--enable-gdk-pixbuf \
%endif
%if %{with omemo_qrcode}
	--enable-omemo-qrcode \
%endif
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if "%{flavor}" == "mini"
rm %{buildroot}%{_includedir}/profapi.h
rm %{buildroot}%{_libdir}/libprofanity.so*
%endif

%check
%if %{with tests}
%make_build check
%endif

# only standard flavor builds the plugin library
%if "%{flavor}" == ""
%ldconfig_scriptlets -n libprofanity%{sover}
%endif

%files
%license COPYING LICENSE.txt
%{_bindir}/profanity
%{_mandir}/man1/*1%{?ext_man}
%{_datadir}/profanity/

# only standard flavor builds the plugin library
%if "%{flavor}" == ""
%files -n libprofanity%{sover}
%license COPYING LICENSE.txt
%{_libdir}/libprofanity.so.%{sover}{,.*}

%files devel
%license COPYING LICENSE.txt
%{_includedir}/profapi.h
%{_libdir}/libprofanity.so
%endif

%changelog
