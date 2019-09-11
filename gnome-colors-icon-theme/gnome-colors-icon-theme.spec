#
# spec file for package gnome-colors-icon-theme
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           gnome-colors-icon-theme
Version:        5.5.1
Release:        2
License:        GPL-2.0+
Summary:        A complete, multi-colored suite of icons for Linux
Url:            http://code.google.com/p/gnome-colors
Group:          System/X11/Icons
Source:         http://gnome-colors.googlecode.com/files/gnome-colors-%{version}.tar.gz
Source1:        http://gnome-colors.googlecode.com/files/gnome-colors-extras-%{version}.tar.gz
BuildRequires:  fdupes
# For all the icon themes macros
BuildRequires:  hicolor-icon-theme
Requires:       gnome-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The GNOME-Colors is a project that aims to make the GNOME desktop as
elegant, consistent and colorful as possible.

The current goal is to allow full color customization of themes, icons,
GDM logins and splash screens. There are already five full
color-schemes available; Brave (Blue), Human (Orange), Wine (Red),
Noble (Purple) and Wise (Green).

GNOME-Colors is mostly inspired/based on Tango, GNOME, Elementary,
Tango-Generator and many other open-source projects.

%prep
%setup -q -c %{name}-%{version} -a 1

%build

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -a gnome-* %{buildroot}%{_datadir}/icons
%fdupes %{buildroot}%{_datadir}
%if 0%{?suse_version} > 1130
%icon_theme_cache_create_ghost gnome-brave
%icon_theme_cache_create_ghost gnome-carbonite
%icon_theme_cache_create_ghost gnome-colors-common
%icon_theme_cache_create_ghost gnome-dust
%icon_theme_cache_create_ghost gnome-human
%icon_theme_cache_create_ghost gnome-illustrious
%icon_theme_cache_create_ghost gnome-noble
%icon_theme_cache_create_ghost gnome-tribute
%icon_theme_cache_create_ghost gnome-wine
%icon_theme_cache_create_ghost gnome-wise
%endif

%clean
rm -rf %{buildroot}

%if 0%{?suse_version} > 1130

%post
%icon_theme_cache_post gnome-brave
%icon_theme_cache_post gnome-carbonite
%icon_theme_cache_post gnome-colors-common
%icon_theme_cache_post gnome-dust
%icon_theme_cache_post gnome-human
%icon_theme_cache_post gnome-illustrious
%icon_theme_cache_post gnome-noble
%icon_theme_cache_post gnome-tribute
%icon_theme_cache_post gnome-wine
%icon_theme_cache_post gnome-wise
%endif

# No need for %%icon_theme_cache_postun in %postun since the themes won't exist anymore

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README Palette.svg
%if 0%{?suse_version} > 1130
%ghost %{_datadir}/icons/*/icon-theme.cache
%endif
%{_datadir}/icons/gnome-brave/
%{_datadir}/icons/gnome-carbonite/
%{_datadir}/icons/gnome-colors-common/
%{_datadir}/icons/gnome-dust/
%{_datadir}/icons/gnome-human/
%{_datadir}/icons/gnome-illustrious/
%{_datadir}/icons/gnome-noble/
%{_datadir}/icons/gnome-tribute/
%{_datadir}/icons/gnome-wine/
%{_datadir}/icons/gnome-wise/

%changelog
