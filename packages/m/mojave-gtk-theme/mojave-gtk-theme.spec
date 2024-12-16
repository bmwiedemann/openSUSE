#
# spec file for package mojave-gtk-theme
#
# Copyright (c) 2024 SUSE LLC
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


%define         _name Mojave-gtk-theme
%define         _version 2024-11-15
Name:           mojave-gtk-theme
Version:        20241115
Release:        0
Summary:        MacOS Mojave like theme for GTK 3, Gnome-Shell and others
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/vinceliuice/Mojave-gtk-theme
Source:         https://github.com/vinceliuice/Mojave-gtk-theme/archive/%{_version}.tar.gz
Source1:        mojave-gtk-theme-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  inkscape
BuildRequires:  optipng
BuildRequires:  sassc
# FOR glib-compile-resources
BuildRequires:  glib2-devel
# for gtk2 only
Recommends:     gtk2-engine-murrine
BuildArch:      noarch

%description
MacOS Mojave like theme for GTK 3, GTK 2 and Gnome-Shell which supports GTK 3
and GTK 2 based desktop environments like Gnome, Pantheon, XFCE, Mate, etc.

%prep
%setup -q -n %{_name}-%{_version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -d %{buildroot}%{_datadir}/themes
%fdupes %{buildroot}%{_datadir}/themes

%files
%license COPYING
%doc README.md
%{_datadir}/themes/*

%changelog
