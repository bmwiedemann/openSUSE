#
# spec file for package vertex-gtk-theme
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _theme  Vertex
%define _name   vertex
Name:           vertex-gtk-theme
Version:        20170128
Release:        0
Summary:        Vertex GTK+ theme
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/horst3180/Vertex-theme
Source:         https://github.com/horst3180/%{_name}-theme/archive/%{version}.tar.gz#/%{_name}-theme-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildArch:      noarch

%description
Vertex is a modern theme that comes with three variants to choose
from. The default variant with dark header-bars, a light variant,
and a dark variant. It supports MATE, Xfce, and Cinnamon.

%package -n metatheme-%{_name}-common
Summary:        Vertex Common Theme Files
Group:          System/GUI/Other
Recommends:     adwaita-icon-theme
Suggests:       gtk2-metatheme-%{_name} = %{version}
Suggests:       gtk3-metatheme-%{_name} = %{version}

%description -n metatheme-%{_name}-common
Vertex is a modern theme that comes with three variants to choose
from. The default variant with dark header-bars, a light variant,
and a dark variant. It supports MATE, Xfce, and Cinnamon.

This package contains common files and themes for Marco, Xfwm4, and
Cinnamon.

%package -n gtk2-metatheme-%{_name}
Summary:        Vertex GTK+2 Theme
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk2)

%description -n gtk2-metatheme-%{_name}
Vertex is a modern theme that comes with three variants to choose
from. The default variant with dark header-bars, a light variant,
and a dark variant. It supports MATE, Xfce, and Cinnamon.

This package contains the GTK+2 theme.

%package -n gtk3-metatheme-%{_name}
Summary:        Vertex GTK+3 Theme
Group:          System/GUI/Other
Requires:       gtk3 >= 3.10
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk3)

%description -n gtk3-metatheme-%{_name}
Vertex is a modern theme that comes with three variants to choose
from. The default variant with dark header-bars, a light variant,
and a dark variant. It supports MATE, Xfce, and Cinnamon.

This package contains the GTK+3 theme.

%prep
%setup -q -n %{_name}-theme-%{version}
sed -i '/configure/d' autogen.sh
sed -i 's/^\(IconTheme=\).*$/\1Adwaita/' common/index.theme*

[ ! -f common/gtk-3.0/3.24 ]
ln -s 3.20 common/gtk-3.0/3.24

%build
./autogen.sh
%configure \
%if 0%{?suse_version} > 1500
  --disable-gnome-shell
%else
  --enable-gnome-shell
%endif
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot}%{_datadir} -type f -name '*.sh' -delete
%fdupes %{buildroot}%{_datadir}/

%files -n metatheme-%{_name}-common
%license COPYING
%doc AUTHORS
%dir %{_datadir}/themes/%{_theme}*/
%exclude %{_datadir}/themes/%{_theme}*/gtk-2.*/
%exclude %{_datadir}/themes/%{_theme}*/gtk-3.*/
%{_datadir}/themes/%{_theme}*/*

%files -n gtk2-metatheme-%{_name}
%license COPYING
%doc AUTHORS
%{_datadir}/themes/%{_theme}*/gtk-2.*/

%files -n gtk3-metatheme-%{_name}
%license COPYING
%doc AUTHORS
%{_datadir}/themes/%{_theme}*/gtk-3.*/

%changelog
