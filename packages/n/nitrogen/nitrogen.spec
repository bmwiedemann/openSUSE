#
# spec file for package nitrogen
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nitrogen
Version:        1.6.1
Release:        0
Summary:        A background browser and setter for X windows
License:        GPL-2.0-only AND CC-BY-SA-3.0
Group:          System/X11/Utilities
Url:            http://projects.l3ib.org/nitrogen/
Source0:        http://projects.l3ib.org/nitrogen/files/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtkmm2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(xinerama)
Requires:       hicolor-icon-theme
Recommends:     %{name}-lang
%lang_package

%description

Nitrogen is a background browser and setter for X windows. It is written
in C++ using the gtkmm toolkit. It can be used in two modes: browser and
recall. Some of the features are:

* Multihead and Xinerama aware.
* Recall mode to used via startup script.
* Uses freedesktop.org standard for thumbnails.
* Can set GNOME background.
* Command line set modes for script use.
* Inotify monitoring of browse directory.
* Lazy loading of thumbnails - conserves memory .
* "Automatic" set mode - determines best mode to set an image based on
  its size.
* Display preview images in a tiled icon layout

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
install -D -m 644 data/icons/%{name}-48.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file %{name} Settings DesktopSettings

%fdupes  %{buildroot}/

%find_lang %{name}

%files lang -f %{name}.lang
%{_datadir}/locale/*/LC_MESSAGES/nitrogen.mo

%files
%license COPYING
%doc AUTHORS README ChangeLog NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/appdata/nitrogen.appdata.xml

%changelog
