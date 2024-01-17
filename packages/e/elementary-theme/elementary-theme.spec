#
# spec file for package elementary-theme
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           elementary-theme
Version:        5.3.0
Release:        0
Summary:        The Elementary GTK theme
License:        GPL-3.0-only
Group:          System/GUI/GNOME
URL:            https://elementary.io/
Source:         https://github.com/elementary/stylesheet/archive/%{version}.tar.gz#/stylesheet-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildArch:      noarch

%description
The official elementary GTK theme designed to be smooth, attractive, fast,
and usable.

%package -n     metatheme-elementary-common
Summary:        Common files for the Elementary GTK theme
Group:          System/GUI/GNOME
Suggests:       gtk2-metatheme-elementary
Suggests:       gtk3-metatheme-elementary

%description -n metatheme-elementary-common
The official elementary GTK theme designed to be smooth, attractive, fast,
and usable.

This package provides the files common to the GTK+ themes and the window
manager themes as well as background images.

%package -n     gtk2-metatheme-elementary
Summary:        GTK+ 2 support for the Elementary GTK theme
Group:          System/GUI/GNOME
Requires:       gtk2-engine-murrine
Requires:       metatheme-elementary-common = %{version}
Supplements:    packageand(metatheme-elementary-common:gtk2)

%description -n gtk2-metatheme-elementary
The official elementary GTK theme designed to be smooth, attractive, fast,
and usable.

This package provides the GTK+ 2 support of Elementary.

%package -n     gtk3-metatheme-elementary
Summary:        GTK+ 3 support for the Elementary GTK theme
Group:          System/GUI/GNOME
Requires:       metatheme-elementary-common = %{version}
Supplements:    packageand(metatheme-elementary-common:gtk3)

%description -n gtk3-metatheme-elementary
The official elementary GTK theme designed to be smooth, attractive, fast,
and usable.

This package provides the GTK+ 3 support of Elementary.

%package -n     plank-theme-elementary
Summary:        The Elementary Plank theme
Group:          System/GUI/GNOME
Requires:       plank

%description -n plank-theme-elementary
The official elementary plank theme.

%package -n     plank-metatheme-elementary
Summary:        GTK+ support for the Elementary Plank theme
Group:          System/GUI/GNOME
Requires:       metatheme-elementary-common = %{version}
Requires:       plank-theme-elementary

%description -n plank-metatheme-elementary
This package provides the elementary GTK+ theme for Plank.

%prep
%setup -q -n stylesheet-%{version}

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_datadir}/plank/themes/elementary
mv \
	%{buildroot}%{_datadir}/themes/elementary/plank/dock.theme \
	%{buildroot}%{_datadir}/plank/themes/elementary/dock.theme
ln -s \
	../../../plank/themes/elementary/dock.theme \
    %{buildroot}%{_datadir}/themes/elementary/plank/dock.theme

%fdupes %{buildroot}%{_datadir}/themes/elementary

%files -n metatheme-elementary-common
%license COPYING
%doc AUTHORS CONTRIBUTORS
%dir %{_datadir}/themes/elementary/
%{_datadir}/themes/elementary/index.theme
%{_datadir}/metainfo/io.elementary.stylesheet.appdata.xml

%files -n gtk2-metatheme-elementary
%{_datadir}/themes/elementary/gtk-2.0/

%files -n gtk3-metatheme-elementary
%{_datadir}/themes/elementary/gtk-3.0/

%files -n plank-theme-elementary
%license COPYING
%dir %{_datadir}/plank
%dir %{_datadir}/plank/themes
%dir %{_datadir}/plank/themes/elementary
%dir %{_datadir}/plank/themes/elementary-dark
%{_datadir}/plank/themes/elementary/dock.theme
%{_datadir}/plank/themes/elementary-dark/dock.theme

%files -n plank-metatheme-elementary
%dir %{_datadir}/themes/elementary/plank
%{_datadir}/themes/elementary/plank/dock.theme
%{_datadir}/themes/elementary/plank/dock-dark.theme

%changelog
