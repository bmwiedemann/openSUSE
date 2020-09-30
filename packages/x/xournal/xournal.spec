#
# spec file for package xournal
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


Name:           xournal
Version:        0.4.8.2016
Release:        0
Summary:        An application for notetaking, sketching, and keeping a journal using a stylus
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            http://xournal.sourceforge.net/
Source:         http://download.sf.net/xournal/%{name}-%{version}.tar.gz
Patch0:         %{name}-implicit-funcs.patch
# PATCH-FIX-UPSTREAM xournal-Improve-window-title.patch -- https://sourceforge.net/p/xournal/patches/79/
Patch1:         %{name}-Improve-window-title.patch
# PATCH-FIX-UPSTREAM xournal-appdata.patch badshah400@gmail.com -- Add, translate and install appdata file
Patch2:         xournal-appdata.patch
# PATCH-FIX-UPSTREAM xournal-fix-strokes-on-Lenovo-active-pen.patch badshah400@gmail.com -- Fix strokes with Lenovo active pen 2; patches taken from upstream git
Patch3:         xournal-fix-strokes-on-Lenovo-active-pen.patch
BuildRequires:  automake >= 1.11.2
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  inkscape
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(libart-2.0)
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)

%description
Xournal is an application for notetaking, sketching, and keeping a journal
using a stylus. You can also use it to annotate PDF files with scribbles or
text. It works similarly to applications like Microsoft Windows Journal or
Jarnal.
It is free software (GNU GPL) and runs on Linux and other GTK+/Gnome platforms.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
intltoolize --force
%configure
%make_build

%install
%make_install
make DESTDIR=%{buildroot} desktop-install

%if 0%{?suse_version} > 1500
export EXPORT="--export-filename"
%else
export EXPORT="-e"
%endif
# GENERATE AND INSTALL HIRES ICONS IN HICOLOR ICON DIR
for i in 64 128 256
do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes
  inkscape -w ${i} -C pixmaps/%{name}.svg \
           $EXPORT %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
  inkscape -w ${i} -C pixmaps/xoj.svg \
           $EXPORT %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/application-x-xoj.png
done

%suse_update_desktop_file %{name}
%find_lang %{name}

install -D -m 0644 %{name}.xml %{buildroot}%{_datadir}/mime/application/x-xoj.xml
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 0644 -t %{buildroot}%{_docdir}/%{name} AUTHORS COPYING ChangeLog NEWS README

%fdupes %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files -f %{name}.lang
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/*xoj.*
%{_datadir}/mime/packages/xournal.xml
%dir %{_datadir}/mime/application
%{_datadir}/mime/application/x-xoj.xml
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_datadir}/mimelnk/application/x-xoj.desktop
%if 0%{?suse_version} < 1320
%dir %{_datadir}/appdata
%endif

%changelog
