#
# spec file for package gtk2-metatheme-equinox
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define _version 1.50
# Unfortunately, the tarballs are not properly versioned. The real
# version has to be found on the website...

Name:           gtk2-metatheme-equinox
Version:        1.50
Release:        0
Summary:        Equinox Metathemes for GTK+
License:        GPL-2.0+
Group:          System/GUI/GNOME
Url:            http://gnome-look.org/content/show.php/Equinox+GTK+Engine?content=121881
Source0:        http://gnome-look.org/CONTENT/content-files/121881-equinox-%{_version}.tar.gz
Source1:        http://gnome-look.org/CONTENT/content-files/140449-equinox-themes-%{_version}.tar.gz
# PATCH-FIX-UPSTREAM gtk2-metatheme-equinox-glib-2.31.patch dimstar@opensuse.org -- Fix build with glib 2.31. Sent upstream by mail (vuntz, 2011-01-05)
Patch1:         gtk2-metatheme-equinox-glib-2.31.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig(gtk+-2.0)
# Cursor theme specified in .theme files
Requires:       dmz-icon-theme-cursors
# Icon theme specified in .theme files
Requires:       faenza-icon-theme
Requires:       gtk2-engine-equinox
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a set of elegant GTK+ themes that use the Equinox
engine.

%package -n gtk2-engine-equinox
Summary:        Equinox GTK+ Theme Engine
Group:          System/GUI/GNOME
Recommends:     gtk2-metatheme-equinox

%description -n gtk2-engine-equinox
Equinox is a theme engine for GTK+. It is a heavily modified derivative
of the Aurora engine (version 1.40).

%prep
%setup -q -c %{name}-%{_version} -a1
pushd equinox-%{_version}
%patch1 -p1
for file in AUTHORS ChangeLog COPYING NEWS README; do
  chmod -x $file
done
popd

%build
pushd equinox-%{_version}
%configure --enable-animation
make %{?_smp_mflags}
popd

%install
pushd equinox-%{_version}
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
popd
install -d %{buildroot}%{_datadir}/themes
for file in "Equinox Evolution" "Equinox Evolution Dawn" "Equinox Evolution Dawn Squared" "Equinox Evolution Dusk" "Equinox Evolution Light" "Equinox Evolution Midnight" "Equinox Evolution Rounded" "Equinox Evolution Squared"; do
  cp -a "$file" "%{buildroot}%{_datadir}/themes/"
done
%fdupes -s %{buildroot}%{_datadir}/themes/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# We use wildcards because of spaces in filenames
%doc Equinox*Evolution.crx
%{_datadir}/themes/*

%files -n gtk2-engine-equinox
%defattr(-,root,root)
%doc equinox-%{_version}/AUTHORS equinox-%{_version}/ChangeLog equinox-%{_version}/COPYING equinox-%{_version}/NEWS equinox-%{_version}/README
%{_libdir}/gtk-2.*/2.*.*/engines/libequinox.so

%changelog
