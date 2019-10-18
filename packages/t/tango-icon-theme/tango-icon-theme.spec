#
# spec file for package tango-icon-theme
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


Name:           tango-icon-theme
Version:        0.8.90
Release:        0
Summary:        Tango Icon Theme
License:        CC-BY-SA-2.5
Group:          System/GUI/GNOME
URL:            http://tango.freedesktop.org/
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-extras-0.1.1.tar.bz2
# PATCH-FIX-UPSTREAM tango-icon-theme-rsvg-2_35_2.patch fdo#45803 dimstar@opensuse.org -- Fix build with librsvg 2.35.2: /usr/bin/rsvg was a deprecated wrapper.
Patch0:         tango-icon-theme-rsvg-2_35_2.patch
# PATCH-FIX-UPSTREAM tango-icon-theme-extras-rsvg-2_35_2.patch fdo#45803 dimstar@opensuse.org -- Fix build with librsvg 2.35.2: /usr/bin/rsvg was a deprecated wrapper.
Patch1:         tango-icon-theme-extras-rsvg-2_35_2.patch
# PATCH-FIX-UPSTREAM tango-icon-theme-reproducible.patch fdo#94510 bwiedemann@suse.com -- Drop png timestamps.
Patch2:         tango-icon-theme-reproducible.patch
BuildRequires:  ImageMagick-devel
BuildRequires:  fdupes
BuildRequires:  icon-naming-utils
BuildRequires:  intltool
BuildRequires:  librsvg-devel
# Needed by patch0, patch1 and patch2
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  rsvg-convert
Recommends:     gnome-icon-theme >= 2.12.0
BuildArch:      noarch

%description
This is the Tango base theme. On top of that, the package includes
some specific icons from the legacy tango-icon-theme-extras package.

%prep
%setup -q -b 1
%patch0 -p1
%patch2 -p1
cd ../%{name}-extras-0.1.1
%patch1 -p1
%patch2 -p1

%build
# Needed by patch0, patch1 and patch2.
autoreconf -fi
%configure --enable-png-creation
make %{?_smp_mflags}
cd ../%{name}-extras-0.1.1
# Needed by patch1
autoreconf -fi
%configure --enable-png-creation
%make_build

%install
%make_install
cd ../%{name}-extras-0.1.1
%make_install
%{icon_theme_cache_create_ghost Tango}
%fdupes %{buildroot}

%post
%icon_theme_cache_post Tango

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore

%files
%license COPYING
%doc AUTHORS ChangeLog README
%ghost %{_datadir}/icons/Tango/icon-theme.cache
%{_datadir}/icons/Tango/

%changelog
