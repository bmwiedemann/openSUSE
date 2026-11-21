#
# spec file for package cropgui
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Tristan Miller <psychonaut@nothingisreal.com>
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

Summary: Graphical front end for lossless cropping of JPEG images
Name: cropgui
Version: 0.9
Release: 0
License: GPL-2.0+
URL: https://codeberg.org/jepler/cropgui
Source0: https://codeberg.org/jepler/%{name}/archive/v%{version}.tar.gz
Patch1: desktop-copyedit.patch
Requires: ImageMagick
Requires: exiftool
Requires: python3-Pillow
Requires: python3-gobject
Requires: typelib-1_0-Gtk-3_0
Requires: typelib-1_0-GdkPixbuf-2_0
BuildRequires: python3
BuildRequires: sed
BuildArch: noarch

%description
cropgui is a graphical front end for lossless cropping of JPEG images
using jpegtran.

%prep
%autosetup -n %{name}

%build

%install
install -Dpm 0755 cropgtk.py %{buildroot}%{_bindir}/cropgui
%python3_fix_shebang
install -d %{buildroot}%{python3_sitelib}
sed -i -e '1d' filechooser.py # Remove extraneous shebang
install -pm 0644 cropgui_common.py filechooser.py cropgui.glade \
    stock-rotate-90-16.png stock-rotate-270-16.png \
    %{buildroot}%{python3_sitelib}/
install -Dpm 0644 cropgui.desktop \
    %{buildroot}%{_datadir}/applications/cropgui.desktop
install -Dpm 0644 cropgui.png \
    %{buildroot}%{_datadir}/pixmaps/cropgui.png
python3 -m compileall -s %{buildroot} -p / \
    %{buildroot}%{python3_sitelib}/cropgui_common.py \
    %{buildroot}%{python3_sitelib}/filechooser.py

%files
%license COPYING
%doc README.md
%{_bindir}/cropgui
%{python3_sitelib}/cropgui_common.py
%{python3_sitelib}/filechooser.py
%pycache_only %{python3_sitelib}/__pycache__/cropgui_common*.pyc
%pycache_only %{python3_sitelib}/__pycache__/filechooser*.pyc
%{python3_sitelib}/cropgui.glade
%{python3_sitelib}/stock-rotate-90-16.png
%{python3_sitelib}/stock-rotate-270-16.png
%{_datadir}/applications/cropgui.desktop
%{_datadir}/pixmaps/cropgui.png

%changelog
