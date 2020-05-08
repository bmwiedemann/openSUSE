#
# spec file for package arc-gtk-theme
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


%define _theme  Arc
%define _name   arc
Name:           arc-gtk-theme
Version:        20200502
Release:        0
Summary:        Arc GTK theme
License:        GPL-3.0-or-later
URL:            https://github.com/jnsh/arc-theme
Source:         %{_name}-theme-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cinnamon
BuildRequires:  fdupes
BuildRequires:  gnome-shell
BuildRequires:  inkscape
BuildRequires:  optipng
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  pkgconfig(gtk+-3.0)
BuildArch:      noarch

%description
Arc is a flat theme with transparent elements.
It supports MATE, GNOME, Budgie, Xfce, and Cinnamon.

%package -n metatheme-%{_name}-common
Summary:        Arc Common Theme Files
Recommends:     adwaita-icon-theme
Suggests:       gtk2-metatheme-%{_name} = %{version}
Suggests:       gtk3-metatheme-%{_name} = %{version}

%description -n metatheme-%{_name}-common
Arc is a flat theme with transparent elements.
It supports MATE, GNOME, Budgie, Xfce, and Cinnamon.

This package contains common files and themes for GNOME Shell,
Marco, Xfwm4, and Cinnamon.

%package -n gtk2-metatheme-%{_name}
Summary:        Arc GTK 2 Theme
Requires:       gtk2-engine-murrine
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk2)

%description -n gtk2-metatheme-%{_name}
Arc is a flat theme with transparent elements.
It supports MATE, GNOME, Budgie, Xfce, and Cinnamon.

This package contains the GTK 2 theme.

%package -n gtk3-metatheme-%{_name}
Summary:        Arc GTK 3 Theme
Requires:       gtk3
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk3)

%description -n gtk3-metatheme-%{_name}
Arc is a flat theme with transparent elements.
It supports MATE, GNOME, Budgie, Xfce, and Cinnamon.

This package contains the GTK 3 theme.

%prep
%setup -q -n %{_name}-theme-%{version}
sed -i '/configure/d' autogen.sh
sed -i 's/^\(IconTheme=\).*$/\1Adwaita/' common/index/*/index.theme

%build
./autogen.sh
%configure
%make_build

%install
%make_install
find %{buildroot}%{_datadir}/ -type f -name '*.sh' -delete
%fdupes %{buildroot}%{_datadir}/

%files -n metatheme-%{_name}-common
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/themes/%{_theme}*/
%exclude %{_datadir}/themes/%{_theme}*/gtk-?.0/
%{_datadir}/themes/%{_theme}*/*

%files -n gtk2-metatheme-%{_name}
%license COPYING
%doc AUTHORS README.md
%{_datadir}/themes/%{_theme}*/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%license COPYING
%doc AUTHORS README.md
%{_datadir}/themes/%{_theme}*/gtk-3.0/

%changelog
