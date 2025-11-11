#
# spec file for package mate-utils
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define soname_dict libmatedict
%define sover_dict 6
%define d_applet   0
%define _version 1.28

Name:           mate-utils
Version:        1.28.0
Release:        0
Summary:        MATE Desktop utilities
License:        GFDL-1.1-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Patch0:         fix-save-issue.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  inkscape
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= %{_version}
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
%glib2_gsettings_schema_requires
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif

%description
This package provides all the tools bundled with MATE utilities:
 - mate-disk-image-mounter, a disc image mounter.
 - mate-disk-usage-analyzer, a disc usage analyser.
 - mate-dictionary, a program which can look up definitions of words.
 - mate-search-tool, with which one can find files by name or content.
 - mate-system-log, a log viewing application.
 - mate-screenshot, a tool to take desktop screenshots and save them.

%package common-lang
Summary:        Languages for MATE utilities
License:        GFDL-1.1-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System/X11/Utilities
Provides:       mate-dictionary-lang = %{version}
Provides:       mate-disk-image-mounter-lang = %{version}
Provides:       mate-disk-usage-analyzer-lang = %{version}
Provides:       mate-screenshot-lang = %{version}
Provides:       mate-search-tool-lang = %{version}
Provides:       mate-system-log-lang = %{version}
BuildArch:      noarch

%description common-lang
Provides common translations shared by Caja extensions

%package -n mate-search-tool
Summary:        MATE Search Tool
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Requires:       mate-desktop-gschemas >= %{_version}
Recommends:     %{name}-doc
Recommends:     mate-search-tool-lang

%description -n mate-search-tool
This is the MATE Seach Tool as shipped with the MATE utilities. It uses
command-line tools such as find and locate to get results.

%package -n mate-disk-image-mounter
Summary:        MATE disk image mounter
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Recommends:     %{name}-doc
Recommends:     mate-disk-image-mounter-lang

%description -n mate-disk-image-mounter
This is the MATE Disk Image Mounter as shipped with the MATE
utilities. mate-disk-image-mounter shows up in Caja for .ISO files
to be conviniently mounted.

%package -n mate-disk-usage-analyzer
Summary:        MATE disk usage analyser
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Recommends:     %{name}-doc
Recommends:     mate-disk-usage-analyzer-lang

%description -n mate-disk-usage-analyzer
This is the MATE Disk Usage Analyzer as shipped with the MATE utilities.
mate-disk-usage-analyzer is able to scan either specific directories or
the wholefilesystem, in order to give the user a graphical tree representation
including each directory size or percentage in the branch.
It also auto-detects in real-time any change made to your home
directory as far as any mounted/unmounted device.

%package -n mate-dictionary
Summary:        MATE dictionary
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Requires:       mate-desktop-gschemas >= %{_version}
Recommends:     %{name}-doc
Recommends:     mate-dictionary-lang

%description -n mate-dictionary
This is the MATE dictionary as shipped with the MATE utilities.
mate-dictionary is a program which can look up the definition of
words

%package -n mate-system-log
Summary:        MATE system log viewer
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/X11/Utilities
Requires:       mate-desktop-gschemas >= %{_version}
Recommends:     %{name}-doc
Recommends:     mate-system-log-lang

%description -n mate-system-log
This is the MATE system log viewer as shipped with the MATE utilities.
mate-system-log is a program which can view logs generated by the
operating system.

%package -n mate-screenshot
Summary:        MATE screenshot maker
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Recommends:     %{name}-doc
Recommends:     mate-screenshot-lang

%description -n mate-screenshot
This is the MATE screenshot maker as shipped with the MATE utilities.
mate-screenshot is a program which cantake desktop screenshots and
save them.

%package -n %{soname_dict}%{sover_dict}
Summary:        Library to look up words in dictionary sources
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{soname_dict}%{sover_dict}
The matedict library is an engine to look up words in dictionary sources.

%package -n %{soname_dict}-devel
Summary:        Header files for MATE's dictionary library
License:        GPL-2.0-or-later
Group:          Development/Libraries/X11
Requires:       %{soname_dict}%{sover_dict} = %{version}

%description -n %{soname_dict}-devel
The matedict library is an engine to look up words in dictionary sources.
This package contains development files for libmatedict.

%package doc
Summary:        Documentation how to mate-utils
License:        GFDL-1.1-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the documentation for mate-utils

%prep
%autosetup -p1

# Do not build the pt lingua for the search tool help to solve build issues.
sed -i 's/^\(IGNORE_HELP_LINGUAS =\)/\1 pt/' gsearchtool/help/Makefile.am

%build
NOCONFIGURE=1 mate-autogen
%configure  --disable-static \
            --libexecdir=%{_libexecdir}/%{name} \
            --with-x \
            --enable-ipv6=yes \
            --enable-debug=yes \
            --enable-wayland \
            --enable-in-process \
            --enable-gtk-doc \
            --enable-gtk-doc-html \
            --enable-gtk-doc-pdf
%make_build

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}

%suse_update_desktop_file mate-disk-usage-analyzer
%suse_update_desktop_file mate-dictionary
%suse_update_desktop_file mate-search-tool
%suse_update_desktop_file mate-system-log
%suse_update_desktop_file mate-screenshot

%post -n %{soname_dict}%{sover_dict} -p /sbin/ldconfig
%postun -n %{soname_dict}%{sover_dict} -p /sbin/ldconfig

%files -n mate-disk-image-mounter
%license COPYING*
%doc AUTHORS NEWS README.md ChangeLog
%{_bindir}/mate-disk-image-mounter
%{_datadir}/applications/mate-disk-image-mounter.desktop

%files -n mate-disk-usage-analyzer
%license COPYING*
%doc AUTHORS NEWS README.md ChangeLog
%exclude %{_datadir}/help/C/mate-disk-usage-analyzer/
%{_bindir}/mate-disk-usage-analyzer
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/applications/mate-disk-usage-analyzer.desktop
%{_datadir}/icons/hicolor/*/apps/mate-disk-usage-analyzer.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/mate-disk-usage-analyzer.appdata.xml
%{_mandir}/man?/mate-disk-usage-analyzer.?%{?ext_man}

%files -n mate-dictionary
%license COPYING*
%doc AUTHORS NEWS README.md ChangeLog
%exclude %{_datadir}/help/C/mate-dictionary/
%{_bindir}/mate-dictionary
#%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/mate-dictionary/
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
#%dir %{_libexecdir}/mate-utils/
#%{_libexecdir}/mate-utils/mate-dictionary-applet
%{_datadir}/applications/mate-dictionary.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/mate-dictionary.appdata.xml
%{_mandir}/man?/mate-dictionary.?%{?ext_man}
%dir %{_libdir}/mate-utils
%{_libdir}/mate-utils/libmate-dictionary-applet.so.*

%files -n mate-screenshot
%license COPYING*
%doc AUTHORS NEWS README.md ChangeLog
%{_bindir}/mate-panel-screenshot
%{_bindir}/mate-screenshot
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml
%{_datadir}/applications/mate-screenshot.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/mate-screenshot.appdata.xml
%{_mandir}/man?/mate-panel-screenshot.?%{?ext_man}
%{_mandir}/man?/mate-screenshot.?%{?ext_man}

%files -n mate-search-tool
%license COPYING*
%doc AUTHORS NEWS README.md ChangeLog
%exclude %{_datadir}/help/C/mate-search-tool/
%{_bindir}/mate-search-tool
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/applications/mate-search-tool.desktop
%{_datadir}/pixmaps/mate-search-tool/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/mate-search-tool.appdata.xml
%{_mandir}/man?/mate-search-tool.?%{?ext_man}

%files -n mate-system-log
%license COPYING*
%doc AUTHORS NEWS README.md ChangeLog
%exclude %{_datadir}/help/C/mate-system-log/
%{_bindir}/mate-system-log
%{_datadir}/applications/mate-system-log.desktop
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/icons/hicolor/*/apps/mate-system-log*
%{_mandir}/man?/mate-system-log.?%{?ext_man}

%files -n %{soname_dict}%{sover_dict}
%{_libdir}/%{soname_dict}.so.%{sover_dict}*

%files -n %{soname_dict}-devel
%doc %{_datadir}/gtk-doc/html/mate-dict/
%{_includedir}/mate-dict/
%{_datadir}/mate-dict/
%{_libdir}/%{soname_dict}.so
%{_libdir}/mate-utils/libmate-dictionary-applet.so
%{_libdir}/pkgconfig/mate-dict.pc

%files common-lang -f %{name}.lang
%exclude %{_datadir}/help/*

%files doc
%doc %{_datadir}/help/C/*/

%changelog
