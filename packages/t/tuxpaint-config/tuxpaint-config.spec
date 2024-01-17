#
# spec file for package tuxpaint-config
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


Name:           tuxpaint-config
Version:        0.0.22
Release:        0
Summary:        Configuration tool for Tux Paint
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://www.tuxpaint.org/
Source:         https://download.sourceforge.net/tuxpaint/tuxpaint-config/%{version}/%{name}-%{version}.tar.gz
Patch1:         tuxpaint-config-docpath.patch
Patch2:         tuxpaint-config-desktop.patch
Patch3:         tuxpaint-config-manpage.patch
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpaper-devel
BuildRequires:  libunibreak-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pangoft2)
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       %{name}-lang = %{version}
Recommends:     tuxpaint
%endif

%description
Tux Paint has a rich set of configuration options, controllable via
command-line options or configuration files. This configuration tool
provides a point-and-click interface for administrators to tailor
Tux Paint to suit the needs of their users.

%if 0%{?suse_version}
%{lang_package ca da el en_GB es fr it ja nl nn pt_BR pt_PT ru sk sl son sv uk zh_TW}
%endif

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}" PREFIX="%{_prefix}" X11_ICON_PREFIX=%{_includedir}/X11/pixmaps/

%install
mkdir -p %{buildroot}/%{_bindir}
make PREFIX="%{buildroot}/%{_prefix}" \
     X11_ICON_PREFIX="%{buildroot}/%{_includedir}/X11/pixmaps/" \
     DOC_PREFIX="%{buildroot}/%{_defaultdocdir}/%{name}" install
install -D -m644 src/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# desktop file
%if 0%{?suse_version}
%suse_update_desktop_file -n %{name}
%endif

# fix file permissions
find %{buildroot}%{_defaultdocdir}/%{name} -type f -exec chmod 644 {} \;
find %{buildroot}%{_mandir} -type f -exec chmod 644 {} \;

# reduce space
%if 0%{?suse_version}
%fdupes -s %{buildroot}
%endif

%find_lang %{name}

%files
%doc %{_defaultdocdir}/%{name}
%dir %{_includedir}/X11/pixmaps
%{_bindir}/tuxpaint-config
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/*.png
%{_datadir}/tuxpaint-config/
%{_includedir}/X11/pixmaps/tuxpaint-config.xpm
%{_mandir}/man1/*

%files lang -f %{name}.lang

%changelog
