#
# spec file for package kurso-de-esperanto
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 4
%define _name   kurso
Name:           kurso-de-esperanto
Version:        4.1.2
Release:        0
Summary:        Multimedia application for teaching oneself Esperanto
License:        GPL-3.0-only
Group:          Amusements/Teaching/Language
URL:            http://kurso.com.br/
Source:         http://kurso.com.br/%{_name}%{_version}_source.tar.gz#/%{name}-%{version}.tar.gz
Source1:        http://kurso.com.br/%{_name}.amd64.tar.gz#/%{name}-media.tar.gz
Source2:        br.com.kurso.%{_name}.desktop
Source3:        br.com.kurso.%{_name}.appdata.xml
# PATCH-FEATURE-OPENSUSE kurso-de-esperanto-qt5.patch sor.alexei@meowr.ru -- Port to Qt5.
Patch0:         kurso-de-esperanto-qt5.patch
BuildRequires:  ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
Kurso de Esperanto is a multimedia computer application for
teaching oneself Esperanto. Here are several of its features:
 * Just 12 lessons.
 * Pronunciation and listening exercises.
 * Audio songs – learn while you sing!
 * A wide variety of exercises, to reinforce the learning points.

%prep
%setup -qn %{_name}%{_version} -a1
%patch0 -p1
tail -n +2 kurso.cpp | head -n 16 > COPYRIGHT
# Use the data directory for media stuff.
sed -i 's|\(Loko = \).*$|\1"%{_datadir}/%{name}/";|' main.cpp

cp %{SOURCE2} br.com.kurso.%{_name}.desktop
cp %{SOURCE3} br.com.kurso.%{_name}.appdata.xml

%build
%qmake5
make %{?_smp_mflags} V=1

%install
install -Dpm 0755 %{_name}%{_version} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/
for dir in sonoj video tradukoj; do
    cp -a %{name}-%{_version}/$dir %{buildroot}%{_datadir}/%{name}/$dir
done
install -Dpm 0644 br.com.kurso.%{_name}.desktop %{buildroot}%{_datadir}/applications/br.com.kurso.%{_name}.desktop
install -Dpm 0644 br.com.kurso.%{_name}.appdata.xml %{buildroot}%{_datadir}/metainfo/br.com.kurso.%{_name}.appdata.xml

convert -strip ico:%{_name}%{_version}.ico png:%{name}-icon.png
for i in %{name}-icon*.png; do
    size=$(identify -ping -format '%%[w]x%%[h]\n' "$i")
    mkdir -p "%{buildroot}%{_datadir}/icons/hicolor/$size/apps/"
    mv "$i" "%{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{name}.png"
done
%suse_update_desktop_file br.com.kurso.%{_name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYRIGHT
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/br.com.kurso.%{_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/br.com.kurso.%{_name}.appdata.xml

%changelog
