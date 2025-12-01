#
# spec file for package planify
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


%define         sover 0
%define         appid io.github.alainm23.planify
Name:           planify
Version:        4.16.1
Release:        0
Summary:        Task and project manager
License:        GPL-3.0-or-later
URL:            https://github.com/alainm23/planify
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson >= 0.56
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.48.0
BuildRequires:  pkgconfig(gee-0.8) >= 0.20.6
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.14.4
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.12.1
BuildRequires:  pkgconfig(gxml-0.20)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.8.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.7.0
BuildRequires:  pkgconfig(libecal-2.0) >= 3.52.4
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libportal) >= 0.7.1
BuildRequires:  pkgconfig(libportal-gtk4) >= 0.7.1
BuildRequires:  pkgconfig(libsecret-1) >= 0.21.4
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.4.4
BuildRequires:  pkgconfig(sqlite3) >= 3.45.1
BuildRequires:  pkgconfig(webkitgtk-6.0) >= 2.44.3
Provides:       elementary-planner = %{version}
Provides:       pantheon-planner = %{version}
Obsoletes:      elementary-planner < %{version}
Obsoletes:      pantheon-planner < %{version}

%description
Planify is here...

    🚀️ Neat visual style.
    🤚️ Drag and Order: Sort your tasks wherever you want.
    💯️ Progress indicator for each project.
    💪️ Be more productive and organize your tasks by 'Sections'.
    📅️ Visualize your events and plan your day better.
    ⏲️ Reminder system, you can create one or more reminders, you decide.
    🌙️ Better integration with the dark theme.
    🎉️ and much more.

☁️ Support for Todoist & Nextcloud:

    Synchronize your Projects, Tasks and Sections.
    Support for Todoist offline: Work without an internet connection; when everything is reconnected, it will be synchronized.
    Planify is not created by, affiliated with, or supported by Doist

💎️ Other features:

    ⏲️ Reminders notifications.
    🔍️ Quick Find.
    🌙️ Night mode.
    🔁️ Recurring due dates.

%package devel
Summary:        Development files for %{name}

%description devel
%{summary}.

This package ships the development files for %{name}

%package -n lib%{name}-%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}-%{sover}
%{summary}.

%lang_package

%prep
%autosetup

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson \
  -Devolution=true \
  -Dportal=true \
  -Dprofile=default \
  -Dtracing=true \
  -Dwebkit=true \
  %{nil}
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%ldconfig_scriptlets -n lib%{name}-%{sover}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{appid}{,.quick-add}
%{_datadir}/appdata/%{appid}.appdata.xml
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}{,.Devel}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg

%files devel
%{_datadir}/vala/vapi/%{name}.{deps,vapi}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}-%{sover}
%{_libdir}/lib%{name}.so.*

%files lang -f %{appid}.lang

%changelog
