#
# spec file for package xfce4-notes-plugin
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


%define panel_version 4.12.0
%define plugin notes
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        1.10.0
Release:        0
Summary:        Note-taking Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-notes-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/1.10/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= 4.14.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.14.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.14.0
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(xfce4-vala)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
# uses exo-open
Requires:       exo-tools
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The Notes plugin provides the equivalent to post-it notes on the Xfce desktop
and allows to quickly take and store small notes.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
# package was renamed in 2019 after Leap 15.1
Obsoletes:      xfce4-panel-plugin-%{plugin}-lang < %{version}-%{release}
Provides:       xfce4-panel-plugin-%{plugin}-lang = %{version}-%{release}
BuildArch:      noarch

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-maintainer-mode \
  --disable-static
%else
%configure --disable-static
%endif
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libnotes.la

%suse_update_desktop_file xfce4-notes
%suse_update_desktop_file xfce4-notes-autostart

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/xfce4-notes
%{_bindir}/xfce4-notes-settings
%{_bindir}/xfce4-popup-notes
%{_datadir}/xfce4-notes-plugin
%{_datadir}/icons/hicolor/*/apps/xfce4-notes-plugin.*
%{_datadir}/xfce4/panel/plugins/xfce4-notes-plugin.desktop
%{_datadir}/applications/xfce4-notes.desktop
%{_libdir}/xfce4/panel/plugins/libnotes.so
%{_sysconfdir}/xdg/autostart/xfce4-notes-autostart.desktop

%files lang -f %{name}.lang

%changelog
