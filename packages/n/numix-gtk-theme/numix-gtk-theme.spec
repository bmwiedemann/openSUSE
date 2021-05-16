#
# spec file for package numix-gtk-theme
#
# Copyright (c) 2021 SUSE LLC
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


%define _theme  Numix
%define _name   numix
Name:           numix-gtk-theme
Version:        2.6.7.1617863126.0d6b4c8
Release:        0
Summary:        Numix GTK+ theme for MATE, Cinnamon, GNOME, and Xfce
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://numixproject.org/
Source0:        %{name}-%{version}.tar.xz 
# PATCH-FIX-OPENSUSE numix-gtk-theme-light-menubars.patch sor.alexei@meowr.ru -- Make light menus (Gtk2), dark menus are buggy in Qt4 QGtk2Style.
Patch0:         %{name}-light-menubars.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildArch:      noarch
BuildRequires:  glib2-tools
BuildRequires:  libxml2-tools
BuildRequires:  sassc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

%description
Numix is a modern flat theme with a combination of light and dark
elements. It supports MATE, GNOME, Xfce, and Openbox.

%package -n metatheme-%{_name}-common
Summary:        Numix Common Theme Files
Group:          System/GUI/Other
Suggests:       gtk2-metatheme-%{_name} = %{version}
Suggests:       gtk3-metatheme-%{_name} = %{version}

%description -n metatheme-%{_name}-common
Numix is a modern flat theme with a combination of light and dark
elements. It supports MATE, GNOME, Xfce, and Openbox.
This package contains common files and themes for Marco, Openbox,
and Xfwm4.

%package -n gtk2-metatheme-%{_name}
Summary:        Numix GTK+2 Theme
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine >= 0.98.1.1
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk2)

%description -n gtk2-metatheme-%{_name}
Numix is a modern flat theme with a combination of light and dark
elements. It supports MATE, GNOME, Xfce, and Openbox.
This package contains the GTK+2 theme.

%package -n gtk3-metatheme-%{_name}
Summary:        Numix GTK+3 Theme
Group:          System/GUI/Other
Requires:       gtk3 >= 3.6.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk3)

%description -n gtk3-metatheme-%{_name}
Numix is a modern flat theme with a combination of light and dark
elements. It supports MATE, GNOME, Xfce, and Openbox.
This package contains the GTK+3 theme.

%prep
%setup -q
%patch0 -p1

%build
%make_build

%install
%make_install
# Changed to a symlink in numix-gtk-theme 2.6.4, breaks update from older versions.
ls -d %{buildroot}%{_datadir}/themes/Numix/gtk-3.*/assets | while read dir; do
    if [ -L "$dir" ]; then
        real_dir="$(readlink "$dir")"
        rm -f "$dir"
        pushd "$(dirname "$dir")"
        cp -a "$real_dir" "$dir"
        popd
    fi
done
chmod -R a-x+X %{buildroot}%{_datadir}/themes/%{_theme}/
%fdupes %{buildroot}%{_datadir}/

%files -n metatheme-%{_name}-common
%license LICENSE
%doc CHANGES CREDITS README.md
%{_datadir}/themes/%{_theme}/
%exclude %{_datadir}/themes/%{_theme}/gtk-2.*/
%exclude %{_datadir}/themes/%{_theme}/gtk-3.*/

%files -n gtk2-metatheme-%{_name}
%license LICENSE
%doc CHANGES CREDITS README.md
%{_datadir}/themes/%{_theme}/gtk-2.*/

%files -n gtk3-metatheme-%{_name}
%license LICENSE
%doc CHANGES CREDITS README.md
%{_datadir}/themes/%{_theme}/gtk-3.*/

%changelog
