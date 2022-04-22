#
# spec file for package viewnior
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


Name:           viewnior
Version:        1.8
Release:        0
Summary:        An Image Viewer
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://siyanpanayotov.com/project/viewnior/
Source0:        https://github.com/hellosiyan/Viewnior/archive/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.43.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gtk+-2.0)
Recommends:     %{name}-lang

%description
Viewnior is an image viewer program with a minimal interface.
Its features are:

* Fullscreen & Slideshow
* Rotate, flip, save, delete images
* Animation support
* Browse only selected images
* Navigation window
* Simple interface
* Configurable mouse actions

%lang_package

%prep
%setup -q -n Viewnior-%{name}-%{version}
# fix spurious executable perms
chmod 0644 AUTHORS COPYING NEWS src/* data/icons/scalable/apps/viewnior.svg

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file -r -G "Elegant Image Viewer" %{name} Graphics Viewer GTK

%if 0%{?suse_version} && 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS README.md TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man*/%{name}.*

%files lang -f %{name}.lang

%changelog
