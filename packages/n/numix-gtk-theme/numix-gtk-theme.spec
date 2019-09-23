#
# spec file for package numix-gtk-theme
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _theme  Numix
%define _name   numix
Name:           numix-gtk-theme
Version:        2.6.7
Release:        0
Summary:        Numix GTK+ theme for MATE, Cinnamon, GNOME, and Xfce
License:        GPL-3.0+
Group:          System/GUI/Other
Url:            https://numixproject.org/
Source0:        https://github.com/numixproject/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/numixproject/%{name}/archive/v2.5.1.tar.gz#/%{name}-2.5.1.tar.gz
# PATCH-FIX-OPENSUSE numix-gtk-theme-light-menubars.patch sor.alexei@meowr.ru -- Make light menus (Gtk2), dark menus are buggy in Qt4 QGtk2Style.
Patch0:         %{name}-light-menubars.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildArch:      noarch
%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse}) || 0%{?sle_version} >= 120200
BuildRequires:  glib2-tools
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  rubygem(sass)
%endif

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
Supplements:    packageand(metatheme-%{_name}-common:gtk2)

%description -n gtk2-metatheme-%{_name}
Numix is a modern flat theme with a combination of light and dark
elements. It supports MATE, GNOME, Xfce, and Openbox.
This package contains the GTK+2 theme.

%package -n gtk3-metatheme-%{_name}
Summary:        Numix GTK+3 Theme
Group:          System/GUI/Other
Requires:       gtk3 >= 3.6.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk3)

%description -n gtk3-metatheme-%{_name}
Numix is a modern flat theme with a combination of light and dark
elements. It supports MATE, GNOME, Xfce, and Openbox.
This package contains the GTK+3 theme.

%prep
%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse}) || 0%{?sle_version} >= 120200
%setup -q
%else
%setup -q -T -n %{name}-2.5.1 -b1
ln -s . src
%endif
%patch0 -p1

%build
%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse}) || 0%{?sle_version} >= 120200
make %{?_smp_mflags} V=1
%endif

%install
%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse}) || 0%{?sle_version} >= 120200
%make_install
%else
install -Dpm 0644 index.theme %{buildroot}%{_datadir}/themes/%{_theme}/index.theme
mkdir -p %{buildroot}%{_datadir}/themes/%{_theme}/
ls -d */ | while read dir; do
    cp -a "$dir" "%{buildroot}%{_datadir}/themes/%{_theme}/$dir"
done
find %{buildroot} -type f -name "*.orig" -delete -print
%endif
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
%doc CHANGES CREDITS LICENSE README.md
%{_datadir}/themes/%{_theme}/
%exclude %{_datadir}/themes/%{_theme}/gtk-2.*/
%exclude %{_datadir}/themes/%{_theme}/gtk-3.*/

%files -n gtk2-metatheme-%{_name}
%doc CHANGES CREDITS LICENSE README.md
%{_datadir}/themes/%{_theme}/gtk-2.*/

%files -n gtk3-metatheme-%{_name}
%doc CHANGES CREDITS LICENSE README.md
%{_datadir}/themes/%{_theme}/gtk-3.*/

%changelog
