#
# spec file for package mate-backgrounds
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


%define _version 1.26
Name:           mate-backgrounds
Version:        1.26.0
Release:        0
Summary:        A set of backgrounds packaged with the MATE desktop
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM mesonfix-061.patch bjorn.lie@gamil.com -- Fix build with meson 0.61 and newer
Patch:          mesonfix-061.patch

BuildRequires:  mate-common >= %{_version}
BuildRequires:  meson
BuildArch:      noarch

%description
This is a collection of desktop wallpapers created with MATE users
in mind.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS
%{_datadir}/backgrounds/
%{_datadir}/mate-background-properties/

%files lang -f %{name}.lang

%changelog
