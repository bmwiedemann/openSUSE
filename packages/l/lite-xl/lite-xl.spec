#
# spec file for package lite-xl
#
# Copyright (c) 2022 SUSE LLC
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


Name:           lite-xl
Version:        2.1.1+git20221230.4e272c3
Release:        0
Summary:        A lightweight text editor written in Lua
Group:          Productivity/Text/Editors
License:        MIT
URL:            https://github.com/lite-xl/lite-xl
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(lua) >= 5.4
BuildRequires:  pkgconfig(sdl2)
Suggests:       %{name}-colors
Suggests:       %{name}-plugins
Suggests:       %{name}-widgets

%description
Lite XL is derived from lite. It is a lightweight text editor written mostly in Lua — it aims to provide something practical, pretty, small and fast easy to modify and extend, or to use without doing either. The aim of Lite XL compared to lite is to be more user friendly, improve the quality of font rendering, and reduce CPU usage.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -D -m644 docs/README.md %{buildroot}%{_datadir}/doc/%{name}/README.md

%files
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/org.lite_xl.lite_xl.desktop
%{_datadir}/doc/%{name}/README.md
%{_datadir}/doc/%{name}/licenses.md
%{_datadir}/icons/hicolor/scalable/apps/lite-xl.svg
%{_datadir}/%{name}/*
%{_datadir}/metainfo/org.lite_xl.lite_xl.appdata.xml

%changelog
