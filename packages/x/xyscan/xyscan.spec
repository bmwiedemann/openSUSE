#
# spec file for package xyscan
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


Name:           xyscan
Version:        4.50
Release:        0
Summary:        Data extractor for data points from graphical plots
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://rhig.physics.yale.edu/~ullrich/software/xyscan/
Source0:        http://rhig.physics.yale.edu/~ullrich/software/xyscan/Distributions/%{version}/xyscan-%{version}-src.tgz
# PATCH-FIX-UPSTREAM no-build-date.patch -- delete build date from source
Patch0:         no-build-date.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(poppler-qt5)
Requires:       hicolor-icon-theme

%description
xyscan is a tool for scientists in need of extracting data points,
i.e. numeric values, from a plot.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
xyscan is a tool for scientists in need of extracting data points,
i.e. numeric values, from a plot.

This package contains the documentation and help files for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1

# Change hard-coded directories to proper macros
sed -i 's|/usr/local|%{_prefix}|' xyscan.pro
sed -i 's|%{_prefix}/lib|%{_libdir}|' xyscan.pro
sed -i 's|\$\$PREFIX/share/xyscan/docs|%{_docdir}/%{name}/html|' xyscan.pro
sed -i 's|\$\$PREFIX/share/xyscan/docs|%{_docdir}/%{name}/html|' src/*.cpp

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' license.txt

%build
%qmake5
%make_jobs

%install
%qmake5_install

%suse_update_desktop_file -c %{name} %{name} "A visualization tool for 3D datasets" %{name} %{name} Science Math

# Install application icons
for px in 16 24 32 48 64 128 256 512 ; do
install -Dm 664 images/xyscanLogo${px}.png %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done
install -Dm 664 images/xyscanIcon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%license gpl.txt license.txt
%doc README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%exclude %{_docdir}/%{name}/html/

%files doc
%license gpl.txt license.txt
%{_docdir}/%{name}/html/

%changelog
