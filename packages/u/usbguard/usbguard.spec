#
# spec file for package usbguard
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global _hardened_build 1
%define lname libusbguard0
Name:           usbguard
Version:        0.7.4
Release:        0
Summary:        A tool for implementing USB device usage policy
## Not installed
# src/ThirdParty/Catch: Boost Software License - Version 1.0
License:        GPL-2.0-or-later
Group:          System/Daemons
Url:            https://usbguard.github.io
Source0:        https://github.com/USBGuard/usbguard/releases/download/usbguard-%{version}/usbguard-%{version}.tar.gz
Source1:        https://github.com/USBGuard/usbguard/releases/download/usbguard-%{version}/usbguard-%{version}.tar.gz.sig
Source2:        usbguard.keyring
Source3:        usbguard-daemon.conf
Source4:        usbguard-rpmlintrc
Patch0:         usbguard-applet-qt_desktop_menu_categories.patch
Patch1:         usbguard-pthread.patch
BuildRequires:  asciidoc
BuildRequires:  aspell
BuildRequires:  audit-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash-completion-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libqb-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  pegtl-devel
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
#BuildRequires:  spdlog-static
BuildRequires:  protobuf-devel
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

%description
The USBGuard software framework helps to protect your computer against rogue USB
devices by implementing basic whitelisting/blacklisting capabilities based on
USB device attributes.

%package -n %{lname}
Summary:        Library for implementing USB device usage policy
Group:          System/Libraries

%description -n %{lname}
The USBGuard software framework helps to protect your computer against rogue USB
devices by implementing basic whitelisting/blacklisting capabilities based on
USB device attributes.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        USBGuard Tools
Group:          System/Management
Requires:       %{name} = %{version}-%{release}

%description    tools
The %{name}-tools package contains optional tools from the USBGuard
software framework.

%package        applet-qt
Summary:        USBGuard Qt 5.x Applet
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Obsoletes:      usbguard-applet-qt <= 0.3

%description    applet-qt
The %{name}-applet-qt package contains an optional Qt 5.x desktop applet
for interacting with the USBGuard daemon component.

%prep
%setup -q -n usbguard-%{version}
%patch0 -p1
%patch1 -p1

%build
mkdir -p ./m4
autoreconf -i -s --no-recursive ./

%configure \
    --disable-silent-rules \
    --with-bundled-catch \
    --with-bundled-pegtl \
    --enable-systemd \
    --with-gui-qt=qt5 \
    --without-dbus \
    --disable-static

make %{?_smp_mflags}

%check
# while we specify --with-bundled-catch, it is not there :(
# make check

%install
%make_install INSTALL="install -p"
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rcusbguard

# Install configuration
mkdir -p %{buildroot}%{_sysconfdir}/usbguard
install -p -m 600 %{SOURCE3} %{buildroot}%{_sysconfdir}/usbguard/usbguard-daemon.conf

# zsh completion, currently needs manual intervention
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -p -m 644 scripts/usbguard-zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_usbguard

# Cleanup
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -delete

%preun
%service_del_preun usbguard.service

%post
%service_add_post usbguard.service

%postun
%service_del_postun usbguard.service

%pre
%service_add_pre usbguard.service

%post -n libusbguard0 -p /sbin/ldconfig
%postun -n libusbguard0 -p /sbin/ldconfig

%files
%doc README.adoc CHANGELOG.md
%license LICENSE
%{_sbindir}/usbguard-daemon
%dir %{_localstatedir}/log/usbguard
%dir %{_sysconfdir}/usbguard
%{_sbindir}/rcusbguard
%dir %{_sysconfdir}/usbguard/IPCAccessControl.d
%config(noreplace) %attr(0600,-,-) %{_sysconfdir}/usbguard/usbguard-daemon.conf
%config(noreplace) %attr(0600,-,-) %{_sysconfdir}/usbguard/rules.conf
%{_unitdir}/usbguard.service
%{_mandir}/man8/usbguard-daemon.8%{?ext_man}
%{_mandir}/man5/usbguard-daemon.conf.5%{?ext_man}
%{_mandir}/man5/usbguard-rules.conf.5%{?ext_man}
%{_datadir}/bash-completion/completions/usbguard
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_usbguard

%files -n %{lname}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%{_bindir}/usbguard
%{_bindir}/usbguard-rule-parser
%{_mandir}/man1/usbguard.1%{?ext_man}

%files applet-qt
%{_bindir}/usbguard-applet-qt
%{_mandir}/man1/usbguard-applet-qt.1%{?ext_man}
%{_datadir}/applications/usbguard-applet-qt.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/usbguard-icon.svg

%changelog
