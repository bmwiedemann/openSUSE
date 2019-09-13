#
# spec file for package fcitx-configtool
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define		pkgname fcitx-config-gtk3
Name:           fcitx-configtool
Version:        0.4.10
Release:        0
Summary:        GTK GUI config tool for FCITX
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-configtool
Source:         http://download.fcitx-im.org/fcitx-configtool/%{name}-%{version}.tar.xz
#PATCH-FIX-UPSTREAM for loop init declaration is only allowed in c99 mode
Patch:          fcitx-configtool-0.4.9-for-loop-init-declaration-c99.patch
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  libtool
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dbus-1-glib-devel

%description
fcitx-config Gtk based configure tool for fcitx.

KDE Version see fcitx-config-kde4 or kcm-fcitx.

%package -n %{pkgname}
Summary:        GTK GUI Config tool for FCITX
Group:          System/I18n/Chinese
Supplements:    packageand(fcitx:libgtk-3-0)
Provides:       fcitx-config-gtk = %{version}
Obsoletes:      fcitx-config-gtk < %{version}
Provides:       fcitx-config-gtk2 = %{version}
Obsoletes:      fcitx-config-gtk2 < %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Provides:       locale(libgnome:ko;zh_CN;zh_SG)
%{fcitx_requires}

%description -n %{pkgname}
fcitx-config GTK based configure tool for fcitx.

KDE Version see fcitx-config-kde4 or kcm-fcitx.

%prep
%setup -q
%patch -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{pkgname} -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_bindir}/fcitx-config-gtk3

%changelog
