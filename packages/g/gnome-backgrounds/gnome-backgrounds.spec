#
# spec file for package gnome-backgrounds
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


Name:           gnome-backgrounds
Version:        3.34.0
Release:        0
Summary:        GNOME Backgrounds
License:        GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-backgrounds
Source0:        https://download.gnome.org/sources/gnome-backgrounds/3.34/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
Background images from the GNOME project.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING COPYING_CCBY2 COPYING_CCBYSA2 COPYING_CCBYSA3
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-background-properties/
%{_datadir}/backgrounds/

%files lang -f %{name}.lang

%changelog
