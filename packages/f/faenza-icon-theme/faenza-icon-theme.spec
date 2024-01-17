# vim: set ts=4 sw=4 et:
#
# spec file for package faenza-icon-theme
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2011 PAscal Bleser
# Copyright (c) 2010 Nelson Marques
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


Name:           faenza-icon-theme
Version:        1.3.1
Release:        0
Summary:        Faenza Icon Theme
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:        http://ppa.launchpad.net/tiheum/equinox/ubuntu/pool/main/f/%{name}/%{name}_%{version}.tar.gz
Source1:        http://gnome-look.org/CONTENT/content-files/132681-Faenza-Mint.tar.gz
# script to rebrand and install stuff...
Source2:        faenza-install
BuildRequires:  fdupes
BuildRequires:  python3-base
# For all the icon themes macros
BuildRequires:  hicolor-icon-theme
# Inherits from GNOME icon theme
Requires:       gnome-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and GNOME menu items.

%package ambiance
Summary:        Faenza-Ambiance Icon Theme
Group:          System/GUI/GNOME
Requires:       %{name}-darkest = %{version}

%description ambiance
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and GNOME menu items.

Faenza-Ambiance is suitable with dark panel and toolbars.

%package dark
Summary:        Faenza-Dark Icon Theme
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}

%description dark
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and GNOME menu items.

%package darker
Summary:        Faenza-Dark Icon Theme
Group:          System/GUI/GNOME
Requires:       %{name}-darkest = %{version}

%description darker
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and GNOME menu items.

%package darkest
Summary:        Faenza-Dark Icon Theme
Group:          System/GUI/GNOME
Requires:       %{name}-dark = %{version}

%description darkest
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and GNOME menu items.

%package radiance
Summary:        Faenza-Radiance Icon Theme
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}

%description radiance
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and GNOME menu items.

Faenza-Radiance is suitable with light panel and controls.

%package mint
Summary:        Faenza-Mint Icon Theme
Group:          System/GUI/GNOME
Requires:       %{name}-dark = %{version}

%description mint
This icon theme for GNOME provides monochromatic icons for panels,
toolbars and buttons and colourful squared icons for devices,
applications, folder, files and GNOME menu items.

%prep
%setup -q -n %{name}-1.3 -a 1

%build

%install
python3 %{S:2} --install %{buildroot}%{_datadir}/icons/
%fdupes %{buildroot}%{_datadir}/icons
find %{buildroot}%{_datadir}/icons -type f -exec chmod 0644 {} \;

%icon_theme_cache_create_ghost Faenza
%icon_theme_cache_create_ghost Faenza-Ambiance
%icon_theme_cache_create_ghost Faenza-Dark
%icon_theme_cache_create_ghost Faenza-Darker
%icon_theme_cache_create_ghost Faenza-Darkest
%icon_theme_cache_create_ghost Faenza-Radiance
%icon_theme_cache_create_ghost Faenza-Mint

# No need for %%icon_theme_cache_postun in %%postun since the themes won't exist anymore
%post
%icon_theme_cache_post Faenza

%post ambiance
%icon_theme_cache_post Faenza-Ambiance

%post dark
%icon_theme_cache_post Faenza-Dark

%post darker
%icon_theme_cache_post Faenza-Darker

%post darkest
%icon_theme_cache_post Faenza-Darkest

%post radiance
%icon_theme_cache_post Faenza-Radiance

%post mint
%icon_theme_cache_post Faenza-Mint

%files
%defattr(-,root,root)
%doc debian/changelog debian/copyright
%{_datadir}/icons/Faenza
%ghost %{_datadir}/icons/Faenza/icon-theme.cache

%files ambiance
%defattr(-,root,root)
%{_datadir}/icons/Faenza-Ambiance
%ghost %{_datadir}/icons/Faenza-Ambiance/icon-theme.cache

%files dark
%defattr(-,root,root)
%{_datadir}/icons/Faenza-Dark
%ghost %{_datadir}/icons/Faenza-Dark/icon-theme.cache

%files darker
%defattr(-,root,root)
%{_datadir}/icons/Faenza-Darker
%ghost %{_datadir}/icons/Faenza-Darker/icon-theme.cache

%files darkest
%defattr(-,root,root)
%{_datadir}/icons/Faenza-Darkest
%ghost %{_datadir}/icons/Faenza-Darkest/icon-theme.cache

%files radiance
%defattr(-,root,root)
%{_datadir}/icons/Faenza-Radiance
%ghost %{_datadir}/icons/Faenza-Radiance/icon-theme.cache

%files mint
%defattr(-,root,root)
%{_datadir}/icons/Faenza-Mint
%ghost %{_datadir}/icons/Faenza-Mint/icon-theme.cache

%changelog
