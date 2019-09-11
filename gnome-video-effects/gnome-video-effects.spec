#
# spec file for package gnome-video-effects
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


Name:           gnome-video-effects
Version:        0.5.0
Release:        0
Summary:        Collection of GStreamer effects
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://wiki.gnome.org/Projects/GnomeVideoEffects
Source0:        https://download.gnome.org/sources/gnome-video-effects/0.5/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-video-effects-meson-pkgconfig-fix.patch -- Various meson improvements and fixes
Patch0:         gnome-video-effects-meson-pkgconfig-fix.patch

BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
A collection of GStreamer effects to be used in different GNOME Modules.

%package devel
Summary:        Collection of GStreamer effects -- Development Files
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description devel
A collection of GStreamer effects to be used in different GNOME Modules.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/%{name}/

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
