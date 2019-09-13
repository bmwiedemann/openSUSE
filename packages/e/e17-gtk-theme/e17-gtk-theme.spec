#
# spec file for package e17-gtk-theme
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


Name:           e17-gtk-theme
Version:        3.22.2
Release:        0
Summary:        The Enlightenment GTK theme
License:        GPL-3.0
Group:          System/GUI/Other
URL:            https://github.com/tsujan
Source:         https://github.com/tsujan/E17gtk/archive/V%{version}.tar.gz#/E17gtk-%{version}.tar.gz
BuildArch:      noarch

%description
The dark GTK2/GTK3 theme with sharp corners, which is designed for use in
Enlightenment and gives the elegant look of Enlightenment to GTK widgets.

%package -n     metatheme-e17gtk-common
Summary:        The Enlightenment GTK theme -- Common Files
Group:          System/GUI/Other
Recommends:     adwaita-icon-theme
Suggests:       gtk2-metatheme-e17gtk
Suggests:       gtk3-metatheme-e17gtk

%description -n metatheme-e17gtk-common
The dark GTK2/GTK3 theme with sharp corners, which is designed for use in
Enlightenment and gives the elegant look of Enlightenment to GTK widgets.

This package provides the common files to the GTK+ themes.

%package -n     gtk2-metatheme-e17gtk
Summary:        The Enlightenment GTK theme -- GTK+ 2 Support
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine
Requires:       metatheme-e17gtk-common = %{version}
Supplements:    packageand(metatheme-e17gtk-common:gtk2)

%description -n gtk2-metatheme-e17gtk
The dark GTK2/GTK3 theme with sharp corners, which is designed for use in
Enlightenment and gives the elegant look of Enlightenment to GTK widgets.

This package contains the GTK+2 theme.

%package -n     gtk3-metatheme-e17gtk
Summary:        The Enlightenment GTK theme -- GTK+ 3 Support
Group:          System/GUI/Other
Requires:       gtk3 >= 3.20.0
Requires:       metatheme-e17gtk-common = %{version}
Supplements:    packageand(metatheme-e17gtk-common:gtk3)

%description -n gtk3-metatheme-e17gtk
The dark GTK2/GTK3 theme with sharp corners, which is designed for use in
Enlightenment and gives the elegant look of Enlightenment to GTK widgets.

This package contains the GTK+3 theme.

%prep
%setup -q -n E17gtk-%{version}

sed -i '/^IconTheme/s/[^=]*$/Adwaita/' $(grep -rwl '^IconTheme')

%build
# There is nothing to build.

%install
install -dm 0755 %{buildroot}%{_datadir}/themes/E17gtk
for _source in $(ls -1F | grep \/) index.theme; do
  cp -a $_source %{buildroot}%{_datadir}/themes/E17gtk
done

%files -n metatheme-e17gtk-common
%doc COPYING NEWS README.md WORKAROUNDS
%dir %{_datadir}/themes/E17gtk/
%{_datadir}/themes/E17gtk/metacity-1/
%{_datadir}/themes/E17gtk/index.theme

%files -n gtk2-metatheme-e17gtk
%{_datadir}/themes/E17gtk/gtk-2.0/

%files -n gtk3-metatheme-e17gtk
%{_datadir}/themes/E17gtk/gtk-3.0/

%changelog
