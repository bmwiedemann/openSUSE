#
# spec file for package stellarium
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


Name:           stellarium
Version:        0.20.3
Release:        0
Summary:        Astronomical Sky Simulator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            http://stellarium.org/
Source0:        https://github.com/Stellarium/stellarium/releases/download/v%{version}/stellarium-%{version}.tar.gz
Source1:        https://github.com/Stellarium/stellarium/releases/download/v%{version}/stellarium-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 2.8.11
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.7.0
BuildRequires:  pkgconfig(Qt5MultimediaWidgets) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.7.0
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Positioning) >= 5.7.0
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script) >= 5.7.0
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Test) >= 5.7.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.7.0
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(zlib)
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libgps)
%endif

%description
Stellarium is a software to render 3D photo-realistic skies in real
time, similar to what can be observed with human eyes through
binoculars or a small telescope.

%prep
%setup -q

%build
export QT_HASH_SEED=0
%cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_POLICY_DEFAULT_CMP0063=NEW \
       -DCMAKE_CXX_VISIBILITY_PRESET=hidden -DCMAKE_VISIBILITY_INLINES_HIDDEN=1
%if 0%{?suse_version} >= 1550
%make_jobs -j1
%else
%make_jobs
%endif

%install
%cmake_install

# Remove .xpm icon from /usr/share/pixmaps as we already
# install appropriate icons in the hicolor directory
rm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

%suse_update_desktop_file -c stellarium Stellarium "Planetarium in your computer" stellarium stellarium Science Astronomy
mkdir -p %{buildroot}%{_datadir}/%{name}/data/script_internet_update
%fdupes %{buildroot}%{_datadir}/%{name}

#%%find_lang %%{name}
#%%find_lang %%{name}-skycultures
#cat %%{name}-skycultures.lang >> %%{name}.lang

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root,755)
%license COPYING
%doc CREDITS.md ChangeLog README.md
%dir %{_datadir}/icons/hicolor/512x512/
%dir %{_datadir}/icons/hicolor/512x512/apps/
%{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/stellarium.appdata.xml
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
