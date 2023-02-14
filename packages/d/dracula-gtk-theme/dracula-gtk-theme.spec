#
# spec file for package dracula-gtk-theme
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


%define         _name               dracula
%define         _kf5_plasmadir      /usr/share/plasma

Name:           dracula-gtk-theme
Version:        3.0+git94.9840b6b
Release:        0
Summary:        A dark theme for GTK
License:        GPL-3.0-only
URL:            https://github.com/dracula/gtk
Source:         gtk-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch

%description
This is a dark theme for GTK-3 and GTK-2 based desktop environments like
Gnome, XFCE, Mate, Cinnamon, etc. Also provides support for KDE plasma.

%package -n metatheme-%{_name}-common
Summary:        Common files for the Dracula theme
Suggests:       gtk2-metatheme-%{_name}
Suggests:       gtk3-metatheme-%{_name}
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n metatheme-dracula-common
This is a dark theme for GTK-3 and GTK-2 based desktop environments like
Gnome, XFCE, Mate, Cinnamon, etc. Also provides support for KDE plasma.

This package provides the files common to the GTK+ themes and the window
manager themes.

%package -n gtk2-metatheme-%{_name}
Summary:        GTK+ 2 support for the Dracula theme
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk2)
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n gtk2-metatheme-%{_name}
This package provides the GTK+ 2 support for Dracula theme.

%package -n gtk3-metatheme-%{_name}
Summary:        GTK+ 3 support for the Dracula theme
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk3)
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n gtk3-metatheme-%{_name}
This is a dark theme for GTK-3 and GTK-2 based desktop environments like
Gnome, XFCE, Mate, Cinnamon, etc. Also provides support for KDE plasma.

This package provides the GTK+ 3 support for Dracula theme.

%package -n gtk4-metatheme-%{_name}
Summary:        GTK+ 4 support for the Dracula theme
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk4)
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n gtk4-metatheme-%{_name}
This is a dark theme for GTK-3 and GTK-2 based desktop environments like
Gnome, XFCE, Mate, Cinnamon, etc. Also provides support for KDE plasma.

This package provides the GTK+ 4 support for Dracula theme.

%package -n kde-theme-%{_name}
Summary:        KDE support for the Dracula theme
Requires:       metatheme-%{_name}-common = %{version}
Requires:       plasma5-desktop
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n kde-theme-%{_name}
This package provides the KDE support for Dracula theme.

%package -n metacity-theme-%{_name}
Summary:        Dracula Metacity themes
Requires:       metacity
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and metacity)
BuildArch:      noarch
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n metacity-theme-%{_name}
This package contains the metacity themes.

%package -n cinnamon-theme-%{_name}
Summary:        Dracula Cinnamon themes
Requires:       cinnamon >= 3.2.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and cinnamon)
BuildArch:      noarch
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n cinnamon-theme-%{_name}
This package contains the cinnamon themes for Dracula theme.

%package -n gnome-shell-theme-%{_name}
Summary:        Dracula GNOME Shell themes
Requires:       gnome-shell >= 3.20.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gnome-shell)
BuildArch:      noarch
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n gnome-shell-theme-%{_name}
This package contains the GNOME Shell support for Dracula theme.

%package -n xfwm4-theme-%{_name}
Summary:        Dracula Xfwm4 themes
Requires:       metatheme-%{_name}-common = %{version}
Requires:       xfwm4
Supplements:    (metatheme-%{_name}-common and xfwm4)
BuildArch:      noarch
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description -n xfwm4-theme-%{_name}
This package contains the Xfwm4 support for for Dracula theme.

%prep
%setup -q -n gtk-%{version}

# Remove useless stuff
rm -rf \
    ./unity                             \
    ./.github                           \
    ./kde/aurorae/Dracula/.shade.svg    \
    ./kde/sddm/Dracula/faces/.face.icon \
    ./kde/cursors/build.sh		\
    ./Art                               \
    ./gtk-2.0/render-assets.sh          \
    ./gtk-3.20/assets/render-gtk3-assets-hidpi.py    \
    ./gtk-3.20/assets/render-gtk3-assets.py          \
    ./gtk-4.0/assets/render-gtk3-assets.py 	     \
    ./gtk-4.0/assets/render-gtk3-assets-hidpi.py     \
    ./src                               \
    ./.gitignore

# Fix executable permissions. We don't need this.
chmod -R -x+X .

%build
# Nothing to build

%install
mkdir -p  %{buildroot}%{_datadir}/themes/%{name}
cp -a ./ %{buildroot}%{_datadir}/themes/%{name}/
chmod 0644  %{buildroot}%{_datadir}/themes/%{name}/index.theme

# Move KDE files to the right folders
mkdir -p %{buildroot}%{_kf5_plasmadir}/desktoptheme
mv %{buildroot}%{_datadir}/themes/%{name}/kde/plasma/desktoptheme/* %{buildroot}%{_kf5_plasmadir}/desktoptheme

mkdir -p %{buildroot}%{_kf5_plasmadir}/look-and-feel
mv %{buildroot}%{_datadir}/themes/%{name}/kde/plasma/look-and-feel/* %{buildroot}%{_kf5_plasmadir}/look-and-feel

mkdir -p %{buildroot}%{_datadir}/color-schemes
mv %{buildroot}%{_datadir}/themes/%{name}/kde/color-schemes/* %{buildroot}%{_datadir}/color-schemes

mkdir -p %{buildroot}%{_datadir}/icons/Dracula-cursors
mv %{buildroot}%{_datadir}/themes/%{name}/kde/cursors/Dracula-cursors/* %{buildroot}%{_datadir}/icons/Dracula-cursors

mkdir -p %{buildroot}%{_datadir}/sddm/themes/Dracula
mv %{buildroot}%{_datadir}/themes/%{name}/kde/sddm/Dracula/* %{buildroot}%{_datadir}/sddm/themes/Dracula

mkdir -p %{buildroot}%{_datadir}/aurorae/themes/Dracula
mv %{buildroot}%{_datadir}/themes/%{name}/kde/aurorae/Dracula/* %{buildroot}%{_datadir}/aurorae/themes/Dracula

# Cleanup unused KDE files
rm -rf %{buildroot}%{_datadir}/themes/%{name}/kde

# fix duplicate files
%fdupes -s %{buildroot}/%{_datadir}/themes/

# Remove duplicate documents
rm %{buildroot}%{_datadir}/themes/%{name}/README.md
rm %{buildroot}%{_datadir}/themes/%{name}/LICENSE

# Remove useless files
rm %{buildroot}%{_datadir}/themes/%{name}/Gulpfile.js
rm %{buildroot}%{_datadir}/themes/%{name}/INSTALL.md
rm %{buildroot}%{_datadir}/themes/%{name}/package-lock.json
rm %{buildroot}%{_datadir}/themes/%{name}/package.json
rm %{buildroot}%{_datadir}/themes/%{name}/screenshot.png

%files -n metatheme-%{_name}-common
%license LICENSE
%doc README.md
%dir %{_datadir}/themes/%{name}/
%{_datadir}/themes/%{name}/index.theme
%{_datadir}/themes/%{name}/assets

%files -n gtk2-metatheme-%{_name}
%{_datadir}/themes/%{name}/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%{_datadir}/themes/%{name}/gtk-3.*/

%files -n gtk4-metatheme-%{_name}
%{_datadir}/themes/%{name}/gtk-4.*/

%files -n gnome-shell-theme-%{_name}
%{_datadir}/themes/%{name}/gnome-shell/

%files -n kde-theme-%{_name}
%dir %{_datadir}/aurorae
%dir %{_datadir}/aurorae/themes
%dir %{_datadir}/sddm/
%dir %{_datadir}/sddm/themes/
%{_kf5_plasmadir}/
%{_datadir}/color-schemes/
%{_datadir}/icons/Dracula-cursors
%{_datadir}/sddm/themes/Dracula
%{_datadir}/aurorae/themes/Dracula

%files -n metacity-theme-%{_name}
%{_datadir}/themes/%{name}/metacity-1/

%files -n cinnamon-theme-%{_name}
%{_datadir}/themes/%{name}/cinnamon/

%files -n xfwm4-theme-%{_name}
%{_datadir}/themes/%{name}/xfwm4/

%changelog
