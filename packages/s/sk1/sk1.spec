#
# spec file for package sk1
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           sk1
Version:        2.0~rc2
Release:        0
Summary:        Python-Based Vector Drawing Program
License:        GPL-2.0-only AND LGPL-2.0-or-later
Group:          Productivity/Graphics/Vector Editors
URL:            http://sk1project.net/
Source:         http://sk1project.net/dc3.php?version=2.0rc2&target=sk1-2.0rc2.tar.gz#/%{name}-2.0rc2.tar.gz
# should go upstream, but
# (1) it is not complete. Source file
#     includes wand/MagickWand.h but it should include
#     MagickWand/MagickWand.h instead for ImageMagick 7
# (2) it is ok to change *Matte* to *Alpha* in magickwand.py
#     unconditionally?
Patch0:         sk1-ImageMagick7.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(MagickWand)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  pkgconfig(pycairo)
BuildRequires:  pkgconfig(python-2.7)
Requires:       python-wxGTK
Requires:       python2-Pillow
Requires:       python2-cairo
Requires:       python2-pycups
Requires:       python2-reportlab
Provides:       skencil = %{version}
Obsoletes:      skencil < %{version}
Provides:       sketch = %{version}
Obsoletes:      sketch < %{version}

%description
The program sK1 is an open source vector graphics editor similar to
CorelDRAW, Adobe Illustrator, or Freehand. First of all sK1 is oriented
for PostScript processing. It features CMYK colorspace support, CMYK
support in Postscript, a Cairo-based engine, color managment, universal
CDR importer (7-X3 versions), and a modern Ttk based (former Tile
widgets) user interface.

%prep
%setup -q -n %{name}-2.0rc2
%patch0 -p1

# Use the path defined by %%python_sitearch
sed -i '/install_path/s|\/.*\(\/\)|%{python_sitearch}\1|' setup-sk1.py

%build
export CFLAGS="%{optflags}"
python setup-sk1.py build

%install
python setup-sk1.py install --root=%{buildroot}
%suse_update_desktop_file -r %{name} Graphics VectorGraphics
%fdupes -s %{buildroot}%{python_sitearch}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license LICENSE
%{_bindir}/%{name}
%{python_sitearch}/%{name}-wx-2.0rc2/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.???

%changelog
