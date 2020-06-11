#
# spec file for package elementary-xfce-icon-theme
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


%define _name elementary-xfce
Name:           elementary-xfce-icon-theme
Version:        0.15+git8.ae895abc
Release:        0
Summary:        Icon theme inspired by Tango and Elementary
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://github.com/shimmerproject/elementary-xfce
Source:         %{_name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  hicolor-icon-theme
BuildRequires:  optipng
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       adwaita-icon-theme
Requires:       gtk3-tools
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
This is an icon-theme maintained with Xfce in mind,
but it supports other desktops like Gnome3 as well.
It's a fork of the upstream elementary-project,
which took place because the team decided to
drop a lot of desktop-specific symlinks.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure
%make_build

%install
%make_install

# Cleanup unused docs
rm %{buildroot}%{_datadir}/icons/%{_name}{,-dark,-darker}/{CONTRIBUTORS,AUTHORS,README.md,LICENSE}

# We don't want to install Darkest as it's not very useful
rm -rf %{buildroot}%{_datadir}/icons/%{_name}-darkest/

# fix duplicate files
%fdupes -s %{buildroot}%{_datadir}/icons/

%files
%doc AUTHORS CONTRIBUTORS README.md
%license LICENSE
%{_datadir}/icons/elementary-xfce/
%{_datadir}/icons/elementary-xfce-dark/
%{_datadir}/icons/elementary-xfce-darker/

%changelog
