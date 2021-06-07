#
# spec file for package matcha-gtk-theme
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


%define         _name               matcha
%define         _theme              Matcha
%define         gtk3_min_version    3.20.0
%define         gtk2_min_version    2.24.30
%define         _version            2021-06-02
Name:           matcha-gtk-theme
Version:        20210602
Release:        0
Summary:        Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/vinceliuice/Matcha-gtk-theme
Source:         %{url}/archive/%{_version}/Matcha-gtk-theme-%{_version}.tar.gz
# PATCH-FEATURE-UPSTREAM allow-setting-gnome-shell-version.patch -- Allow setting the gnome shell version, so no installed one is required
Patch0:         allow-setting-gnome-shell-version.patch
BuildRequires:  fdupes

%description
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

%package -n metatheme-%{_name}-common
Summary:        Matcha common theme files
Group:          System/GUI/Other
Requires:       google-roboto-fonts
Requires:       noto-sans-fonts
Suggests:       gtk2-metatheme-%{_name} = %{version}
Suggests:       gtk3-metatheme-%{_name} = %{version}
Provides:       matcha-gtk-theme
BuildArch:      noarch

%description -n metatheme-%{_name}-common
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains common files for all Matcha themes.

%package -n gtk2-metatheme-%{_name}
Summary:        Matcha GTK+2 themes
Group:          System/GUI/Other
Requires:       gtk2 >= %{gtk2_min_version}
Requires:       gtk2-engine-murrine >= 0.98.1
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk2)
BuildArch:      noarch

%description -n gtk2-metatheme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the GTK2+ themes.

%package -n gtk3-metatheme-%{_name}
Summary:        Matcha GTK+3 themes
Group:          System/GUI/Other
Requires:       gtk3 >= %{gtk3_min_version}
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk3)
BuildArch:      noarch

%description -n gtk3-metatheme-%{_name}
Matcha is a flat Design theme for GTK4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the GTK3+ themes.


%if 0%{?suse_version} > 1500
%package -n gtk4-metatheme-%{_name}
Summary:        Matcha GTK+4 themes
Group:          System/GUI/Other
Requires:       gtk4
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk4)
BuildArch:      noarch

%description -n gtk4-metatheme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the GTK+4 themes.
%endif

%package -n metacity-theme-%{_name}
Summary:        Matcha Metacity themes
Group:          System/GUI/Other
Requires:       metacity
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:metacity)
BuildArch:      noarch

%description -n metacity-theme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the metacity themes.

%package -n cinnamon-theme-%{_name}
Summary:        Matcha Cinnamon themes
Group:          System/GUI/Other
Requires:       cinnamon >= 3.2.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:cinnamon)
BuildArch:      noarch

%description -n cinnamon-theme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the cinnamon themes.

%package -n gnome-shell-theme-%{_name}
Summary:        Matcha GNOME Shell themes
Group:          System/GUI/Other
Requires:       gnome-shell >= 3.20.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gnome-shell)
BuildArch:      noarch

%description -n gnome-shell-theme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the GNOME Shell themes.

%package -n xfwm4-theme-%{_name}
Summary:        Matcha Xfwm4 themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       xfwm4
Supplements:    packageand(metatheme-%{_name}-common:xfwm4)
BuildArch:      noarch

%description -n xfwm4-theme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the Xfwm4 themes.

%package -n plank-theme-%{_name}
Summary:        Matcha Plank themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       plank
Supplements:    packageand(metatheme-%{_name}-common:plank)
BuildArch:      noarch

%description -n plank-theme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the Plank themes.

%package -n openbox-theme-%{_name}
Summary:        Matcha openbox themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       openbox >= 3.6.1
Supplements:    packageand(metatheme-%{_name}-common:openbox)
BuildArch:      noarch

%description -n openbox-theme-%{_name}
Matcha is a flat Design theme for GTK 4, GTK 3, GTK 2 and Gnome-Shell.

This package contains the openbox themes.

%prep
%setup -q -n Matcha-gtk-theme-%{_version}
%patch0 -p1

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh \
%if 0%{?sle_version} && 0%{?sle_version} <= 150300
	-s old \
%endif	
	-d "%{buildroot}%{_datadir}/themes"

# Remove unity and index.theme files
rm -rf  %{buildroot}%{_datadir}/themes/*/unity
rm -f   %{buildroot}%{_datadir}/themes/*/index.theme

%if 0%{?suse_version} <= 1500
rm -rf %{buildroot}%{_datadir}/themes/*/gtk-4.0
%endif

%fdupes %{buildroot}/%{_datadir}/themes

%files -n metatheme-%{_name}-common
%license LICENSE
%doc README.md
%dir %{_datadir}/themes/%{_theme}-aliz/
%dir %{_datadir}/themes/%{_theme}-azul/
%dir %{_datadir}/themes/%{_theme}-sea/
%dir %{_datadir}/themes/%{_theme}-dark-aliz/
%dir %{_datadir}/themes/%{_theme}-dark-azul/
%dir %{_datadir}/themes/%{_theme}-dark-sea/
%dir %{_datadir}/themes/%{_theme}-light-aliz/
%dir %{_datadir}/themes/%{_theme}-light-azul/
%dir %{_datadir}/themes/%{_theme}-light-sea/

%files -n gtk2-metatheme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/gtk-2.0/
%{_datadir}/themes/%{_theme}-azul/gtk-2.0/
%{_datadir}/themes/%{_theme}-sea/gtk-2.0/
%{_datadir}/themes/%{_theme}-light-aliz/gtk-2.0/
%{_datadir}/themes/%{_theme}-light-azul/gtk-2.0/
%{_datadir}/themes/%{_theme}-light-sea/gtk-2.0/
%{_datadir}/themes/%{_theme}-dark-aliz/gtk-2.0/
%{_datadir}/themes/%{_theme}-dark-azul/gtk-2.0/
%{_datadir}/themes/%{_theme}-dark-sea/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/gtk-3.0/
%{_datadir}/themes/%{_theme}-azul/gtk-3.0/
%{_datadir}/themes/%{_theme}-sea/gtk-3.0/
%{_datadir}/themes/%{_theme}-light-aliz/gtk-3.0/
%{_datadir}/themes/%{_theme}-light-azul/gtk-3.0/
%{_datadir}/themes/%{_theme}-light-sea/gtk-3.0/
%{_datadir}/themes/%{_theme}-dark-aliz/gtk-3.0/
%{_datadir}/themes/%{_theme}-dark-azul/gtk-3.0/
%{_datadir}/themes/%{_theme}-dark-sea/gtk-3.0/

%if 0%{?suse_version} > 1500
%files -n gtk4-metatheme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/gtk-4.0/
%{_datadir}/themes/%{_theme}-azul/gtk-4.0/
%{_datadir}/themes/%{_theme}-sea/gtk-4.0/
%{_datadir}/themes/%{_theme}-light-aliz/gtk-4.0/
%{_datadir}/themes/%{_theme}-light-azul/gtk-4.0/
%{_datadir}/themes/%{_theme}-light-sea/gtk-4.0/
%{_datadir}/themes/%{_theme}-dark-aliz/gtk-4.0/
%{_datadir}/themes/%{_theme}-dark-azul/gtk-4.0/
%{_datadir}/themes/%{_theme}-dark-sea/gtk-4.0/
%endif

%files -n gnome-shell-theme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/gnome-shell/
%{_datadir}/themes/%{_theme}-azul/gnome-shell/
%{_datadir}/themes/%{_theme}-sea/gnome-shell/
%{_datadir}/themes/%{_theme}-light-aliz/gnome-shell/
%{_datadir}/themes/%{_theme}-light-azul/gnome-shell/
%{_datadir}/themes/%{_theme}-light-sea/gnome-shell/
%{_datadir}/themes/%{_theme}-dark-aliz/gnome-shell/
%{_datadir}/themes/%{_theme}-dark-azul/gnome-shell/
%{_datadir}/themes/%{_theme}-dark-sea/gnome-shell/

%files -n metacity-theme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/metacity-1/
%{_datadir}/themes/%{_theme}-azul/metacity-1/
%{_datadir}/themes/%{_theme}-sea/metacity-1/
%{_datadir}/themes/%{_theme}-light-aliz/metacity-1/
%{_datadir}/themes/%{_theme}-light-azul/metacity-1/
%{_datadir}/themes/%{_theme}-light-sea/metacity-1/
%{_datadir}/themes/%{_theme}-dark-aliz/metacity-1/
%{_datadir}/themes/%{_theme}-dark-azul/metacity-1/
%{_datadir}/themes/%{_theme}-dark-sea/metacity-1/

%files -n cinnamon-theme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/cinnamon/
%{_datadir}/themes/%{_theme}-azul/cinnamon/
%{_datadir}/themes/%{_theme}-sea/cinnamon/
%{_datadir}/themes/%{_theme}-light-aliz/cinnamon/
%{_datadir}/themes/%{_theme}-light-azul/cinnamon/
%{_datadir}/themes/%{_theme}-light-sea/cinnamon/
%{_datadir}/themes/%{_theme}-dark-aliz/cinnamon/
%{_datadir}/themes/%{_theme}-dark-azul/cinnamon/
%{_datadir}/themes/%{_theme}-dark-sea/cinnamon/

%files -n xfwm4-theme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/xfwm4/
%{_datadir}/themes/%{_theme}-azul/xfwm4/
%{_datadir}/themes/%{_theme}-sea/xfwm4/
%{_datadir}/themes/%{_theme}-light-aliz/xfwm4/
%{_datadir}/themes/%{_theme}-light-azul/xfwm4/
%{_datadir}/themes/%{_theme}-light-sea/xfwm4/
%{_datadir}/themes/%{_theme}-dark-aliz/xfwm4/
%{_datadir}/themes/%{_theme}-dark-azul/xfwm4/
%{_datadir}/themes/%{_theme}-dark-sea/xfwm4/

%files -n plank-theme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/plank/
%{_datadir}/themes/%{_theme}-azul/plank/
%{_datadir}/themes/%{_theme}-sea/plank/
%{_datadir}/themes/%{_theme}-light-aliz/plank/
%{_datadir}/themes/%{_theme}-light-azul/plank/
%{_datadir}/themes/%{_theme}-light-sea/plank/
%{_datadir}/themes/%{_theme}-dark-aliz/plank/
%{_datadir}/themes/%{_theme}-dark-azul/plank/
%{_datadir}/themes/%{_theme}-dark-sea/plank/

%files -n openbox-theme-%{_name}
%{_datadir}/themes/%{_theme}-aliz/openbox-3/
%{_datadir}/themes/%{_theme}-azul/openbox-3/
%{_datadir}/themes/%{_theme}-sea/openbox-3/
%{_datadir}/themes/%{_theme}-light-aliz/openbox-3/
%{_datadir}/themes/%{_theme}-light-azul/openbox-3/
%{_datadir}/themes/%{_theme}-light-sea/openbox-3/
%{_datadir}/themes/%{_theme}-dark-aliz/openbox-3/
%{_datadir}/themes/%{_theme}-dark-azul/openbox-3/
%{_datadir}/themes/%{_theme}-dark-sea/openbox-3/

%changelog
