#
# spec file for package lugaru
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Neal Gompa <ngompa13@gmail.com>.
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


Name:           lugaru
Version:        1.2
Release:        0
Summary:        Third-person ninja rabbit fighting game
License:        GPL-2.0+
Group:          Amusements/Games/Action/Other
Url:            https://osslugaru.gitlab.io/
Source:         https://bitbucket.org/osslugaru/lugaru/downloads/%{name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM 0001-CMake-Define-build-type-before-configuring-version-h.patch rverschelde@gmail.com -- Define build type before configuring version header
Patch0001:      0001-CMake-Define-build-type-before-configuring-version-h.patch
# PATCH-FIX-UPSTREAM 0002-ImageIO-fix-invalid-conversion.patch romain.naour@gmail.com -- ImageIO: fix invalid conversion
Patch0002:      0002-ImageIO-fix-invalid-conversion.patch
# PATCH-FIX-UPSTREAM 0003-Dist-Linux-Add-content-ratings-to-AppStream-appdata-.patch ngompa13@gmail.com -- Add content ratings to AppStream data
Patch0003:      0003-Dist-Linux-Add-content-ratings-to-AppStream-appdata-.patch

# PATCH-FIX-OPENSUSE lugaru-1.1-do-not-install-documentation.patch ngompa13@gmail.com -- Don't try to install docs, as we're doing it ourselves
Patch1000:      lugaru-1.1-do-not-install-documentation.patch

# For autosetup
BuildRequires:  git-core

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# Icon is installed into hicolor-icon-theme path
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
# Require Lugaru game content
Requires:       %{name}-data = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
# Ensure cache is updated
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme
%endif

%description
Lugaru is the predecessor to Overgrowth (http://www.wolfire.com/overgrowth).
It is a third-person action game. The main character, Turner, is an anthropomorphic
rebel bunny rabbit with impressive combat skills. In his quest to find those responsible
for slaughtering his village, he uncovers a far-reaching conspiracy involving the corrupt
leaders of the rabbit republic and the starving wolves from a nearby den. Turner takes it
upon himself to fight against their plot and save his fellow rabbits from slavery.

%package data
Summary:        Arch-independent data files for the Lugaru game
License:        CC-BY-SA-3.0 and CC-BY-SA-4.0
Group:          Amusements/Games/Action/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
This package contains arch-independent data files for the game Lugaru.

%prep
%autosetup -S git

%build
# Ensure that it looks in the right place for the game data
%cmake -DSYSTEM_INSTALL=ON \
       -DCMAKE_INSTALL_DATADIR=%{_datadir}

%make_jobs

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version}
%suse_update_desktop_file %{name}

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc COPYING.txt AUTHORS RELEASE-NOTES.md Docs/*
%{_bindir}/%{name}
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%files data
%defattr(-,root,root)
%doc CONTENT-LICENSE.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
