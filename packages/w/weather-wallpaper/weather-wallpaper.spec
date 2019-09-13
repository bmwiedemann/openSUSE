#
# spec file for package weather-wallpaper
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           weather-wallpaper
Version:        0.2.0
Release:        0
Summary:        Utility to create a wallpaper based on the current weather
License:        GPL-2.0
Group:          Amusements/Toys/Background
Url:            http://mundogeek.net/weather-wallpaper/
Source0:        http://launchpadlibrarian.net/17362202/weather-wallpaper_0.2.0-1.tar.gz
# PATCH-FIX-UPSTREAM weather-wallpaper-update-for-gnome3.patch lp#921375 malcolmlewis@opensuse.org -- Update python code to use gsettings as well as gconf.
Patch0:         weather-wallpaper-update-for-gnome3.patch
# PATCH-FIX-UPSTREAM weather-wallpaper-fix-desktop-file.patch lp#929642 malcolmlewis@opensuse.org -- Add trailing ; to desktop categories.
Patch1:         weather-wallpaper-fix-desktop-file.patch
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
Requires:       ImageMagick
Requires:       inkscape
Requires:       python-gtk
Requires:       python-pymetar
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%py_requires

%description
Weather wallpaper is a program which connects to NOAA each hour to get the
current weather at the specified location and creates and sets a wallpaper
with the data retrieved.

%lang_package
%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%install
%makeinstall
# Remove installed files as we'll package them as rpm docs
rm %{buildroot}%{_datadir}/%{name}/AUTHORS \
   %{buildroot}%{_datadir}/%{name}/COPYING \
   %{buildroot}%{_datadir}/%{name}/TRANSLATORS
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root,-)
%doc AUTHORS changelog COPYING TRANSLATORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
