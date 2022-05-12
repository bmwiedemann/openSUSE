#
# spec file for package xyscan
#
# Copyright (c) 2022 SUSE LLC
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

%if 0%{?suse_version} >= 1550
%bcond_without  qt6
%else
# Leap still only provides qt5
%bcond_with     qt5
%endif
Name:           xyscan
Version:        4.64
Release:        0
Summary:        Data extractor for data points from graphical plots
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://rhig.physics.yale.edu/~ullrich/software/xyscan/
Source0:        https://rhig.physics.yale.edu/~ullrich/software/xyscan/Distributions/%{version}/xyscan-%{version}-src.tgz
# PATCH-FIX-UPSTREAM no-build-date.patch -- delete build date from source
Patch0:         no-build-date.patch
# PATCH-FEATURE-UPSTREAM allow-qt6-also-on-non-mac.patch -- Allow building with QT6 (already supported on Mac)
Patch1:         allow-qt6-also-on-non-mac.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if %{with qt6}
BuildRequires:  qt6-tools-linguist
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(poppler-qt6)
%else
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Core) >= 5.14
BuildRequires:  pkgconfig(Qt5Gui) >= 5.14
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(poppler-qt5)
%endif
Requires:       hicolor-icon-theme
Recommends:     %{name}-doc = %{version}

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
%autosetup -p1 -n %{name}

# Change hard-coded directories to proper macros
sed -i 's|/usr/local|%{_prefix}|' xyscan.pro
sed -i 's|/usr/lib|%{_libdir}|' xyscan.pro
sed -i 's|\$\$PREFIX/share/xyscan/docs|%{_docdir}/%{name}/html|' xyscan.pro
sed -i 's|/usr/share/doc/xyscan/docs|%{_docdir}/%{name}/html|' src/*.cpp

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' license.txt

%build
%if %{with qt6}
%qmake6
%else
%qmake5
%endif
%make_jobs

%install
%if %{with qt6}
%qmake6_install
%else
%qmake5_install
%endif

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
