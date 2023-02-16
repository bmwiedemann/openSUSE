#
# spec file for package gnome-backgrounds
#
# Copyright (c) 2023 SUSE LLC
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
Version:        43.1
Release:        0
Summary:        GNOME Backgrounds
License:        CC-BY-SA-3.0
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-backgrounds
Source0:        https://download.gnome.org/sources/gnome-backgrounds/43/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
# svg pixbuf loader
Requires:       gdk-pixbuf-loader-rsvg
# webp pixbuf loader
Requires:       webp-pixbuf-loader
BuildArch:      noarch
Obsoletes:      %{name}-lang < %{version}

%description
Background images from the GNOME project.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_datadir}/gnome-background-properties/
%{_datadir}/backgrounds/

%changelog
