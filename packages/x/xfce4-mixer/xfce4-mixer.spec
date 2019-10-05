#
# spec file for package xfce4-mixer
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define panel_version 4.10.0
%define plugin mixer
%bcond_with git
Name:           xfce4-mixer
Version:        4.11.0
Release:        0
Summary:        Volume Control Application for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://www.xfce.org/
Source0:        https://archive.xfce.org/src/apps/xfce4-mixer/4.11/xfce4-mixer-%{version}.tar.bz2
Source100:      %{name}-rpmlintrc
%if %{with git}
Patch1:         xfce4-mixer-alsa-git.patch
Patch2:         no-full-debug-default-for-git.patch
%else
Patch3:         xfce4-mixer-alsa.patch
Patch4:         xfce4-mixer-find-dbus.patch
Patch5:         xfce4-mixer-libunique.patch
%endif
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(keybinder)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4panel-1.0)
BuildRequires:  pkgconfig(libxfce4ui-1)
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxfconf-0)
Recommends:     %{name}-lang = %{version}
Suggests:       xfce4-panel-plugin-mixer

%description
xfce4-mixer is a volume control application for the Xfce desktop
environment.

%package -n xfce4-%{plugin}-plugin
Summary:        Volume Control Plugin for the Xfce Panel
Group:          Productivity/Multimedia/Sound/Mixers
Requires:       %{name} = %{version}
Requires:       xfce4-panel >= %{panel_version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}

%description -n xfce4-%{plugin}-plugin
This package contains the xfce4-mixer Xfce panel plugin.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 xdt-autogen
%if %{with git}
%configure \
    --enable-maintainer-mode \
    --disable-static
%else
%configure --disable-static
%endif
%make_build

%install
%make_install

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libmixer.la

%find_lang %{name} %{?no_lang_C}

%suse_update_desktop_file -i xfce4-mixer Settings DesktopSettings

%files
%license COPYING
%doc AUTHORS README
%{!?with_git:%doc NEWS}
%{_bindir}/xfce4-mixer
%{_datadir}/applications/*.desktop
%if %{with git}
%dir %{_datadir}/xfce4
%dir %{_datadir}/xfce4/mixer
%{_datadir}/xfce4/mixer/icons
%else
%{_datadir}/xfce4-mixer
%endif
%{_datadir}/pixmaps/xfce4-mixer/
%{_mandir}/man1/xfce4-mixer.1*

%files -n xfce4-mixer-plugin
%{_libdir}/xfce4/panel/plugins/libmixer.so
%{_datadir}/xfce4/panel/plugins/mixer.desktop

%files lang -f %{name}.lang

%changelog
