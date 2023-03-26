#
# spec file for xfce4-docklike-plugin
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


%define panel_version 4.14.0
%define plugin docklike
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        0.4.1
Release:        0
Summary:        Docklike Taskbar
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-docklike-plugin/start
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/0.4/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo) >= 1.16.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.58.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.30.0
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.14.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.14.0
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
# uses exo-open
Requires:       exo-tools
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}

%description
Docklike Taskbar behaves similarly to many other desktop environments
and operating systems. Wherein all application windows are grouped
together as an icon and can be pinned to act as a launcher when the
application is not running. Commonly referred to as a dock.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
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

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libdocklike.la

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_datadir}/xfce4/panel/plugins/docklike.desktop
%{_libdir}/xfce4/panel/plugins/libdocklike.so

%files lang -f %{name}.lang

%changelog
