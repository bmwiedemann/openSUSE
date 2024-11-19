#
# spec file for package pantheon-code
#
# Copyright (c) 2024 SUSE LLC
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
%define         appid io.elementary.code
Name:           pantheon-code
Version:        7.4.0
Release:        0
Summary:        Extensible Text Editor for the Pantheon Desktop
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/code
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libvala-0.56)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkitgtk-6.0)
Provides:       elementary-code = %{version}
Obsoletes:      elementary-code < %{version}

%description
pantheon-code is a Granite-based text editor. It
auto-saves files, and can remembers tabs and cursor positions. You
can install extensions to turn elementary-code into a full-blown IDE, as
well as tweak the behaviour and interface to your liking. It has
highlighting for many programming, scripting and markup languages.

%package -n     libcodecore%{sover}
Summary:        Library files for %{name}

%description -n libcodecore%{sover}
Extensible Text Editor for the Pantheon Desktop.

This package contains the shared library.

%package        plugins
Summary:        A collection of plugins for %{name}
Requires:       %{name} = %{version}

%description    plugins
Extensible Text Editor for the Pantheon Desktop.

This package contains a collection of plugins: Contractor, Folder-Manager,
Outline, Pastebin and etc.

%package        devel
Summary:        Development Files for %{name}
Requires:       libcodecore%{sover} = %{version}

%description    devel
Extensible Text Editor for the Pantheon Desktop.

This package contains development files needed to develop plugins for
for %{name}.

%lang_package

%prep
%autosetup -n code-%{version}

%build
%meson \
  -Dhave_pkexec=false
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%ldconfig_scriptlets -n libcodecore%{sover}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.{,plugins.spell.}gschema.xml
%{_datadir}/gtksourceview-4/styles/elementary-{dark,light}.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/%{appid}
%{_mandir}/man?/%{appid}.?%{?ext_man}
%{_datadir}/vala/vapi/codecore.{deps,vapi}
%{_datadir}/metainfo/%{appid}.metainfo.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files plugins
%{_libdir}/%{appid}

%files -n libcodecore%{sover}
%{_libdir}/libcodecore.so.*

%files devel
%{_includedir}/codecore.h
%{_libdir}/libcodecore.so
%{_libdir}/pkgconfig/codecore.pc

%files lang -f %{appid}.lang

%changelog
