#
# spec file for package engauge-digitizer
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


Name:           engauge-digitizer
Version:        11.3
Release:        0
Summary:        Ditigizer software that converts old graphs into numbers again
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
Url:            http://markummitchell.github.io/engauge-digitizer/
Source0:        https://github.com/markummitchell/%{name}/archive/v%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  icns-utils
BuildRequires:  optipng
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(log4cpp)
BuildRequires:  pkgconfig(poppler-qt5)
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Suggests:       %{name}-doc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This digitizing software converts an image file, showing a graph or
map, into numbers. The image file can come from a scanner, digital
camera or screenshot. The numbers can be read on the screen, and
written or copied to a spreadsheet.

%package doc
Summary:        Documentation for Engauge Digitizer
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
This package contains the documentation for Engauge Digitizer.

%package devel-doc
Summary:        Development documentation for Engauge Digitizer
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel-doc
This package contains the development documentation for Engauge Digitizer.

%prep
%autosetup -p1

# UNNECESSARY EXEC PERM
chmod -x help/build_qt5_12_0.bash

%build
# ADD JPEG2000 SUPPORT
export OPENJPEG_INCLUDE=$(pkg-config --cflags-only-I libopenjp2 | sed -e 's@-I\(\S\+\).*@\1@g')
export OPENJPEG_LIB=%{_libdir}
export POPPLER_INCLUDE=%{_includedir}/poppler/qt5
export POPPLER_LIB=%{_libdir}

qmake-qt5 engauge.pro \
  "DEFINES+=HELPDIR=%{_docdir}/%{name}/" \
  QMAKE_CFLAGS="%optflags -fno-strict-aliasing" \
  QMAKE_CXXFLAGS="%optflags -fno-strict-aliasing" \
  CONFIG+="pdf jpeg2000"
make %{?_smp_mflags}

# HELP files
pushd help
# CRLF -> LF
sed -i 's/\r$//' engauge.qhcp dateformats.css dateformats.html
optipng -o2 *png
%if 0%{?suse_version} > 1500
qhelpgenerator-qt5 engauge.qhcp -o engauge.qhc
%else
qcollectiongenerator-qt5 engauge.qhcp -o engauge.qhc
%endif
mv engauge.qch engauge.qhc ../
rm engauge.qhcp .gitignore build.bash
popd

# Generate source code documentation in HTML format
pushd src
sed -i 's/\(GENERATE_LATEX.*\)=.*/\1 = NO/' Doxyfile
doxygen
popd

%install
install -Dm 755 bin/engauge %{buildroot}%{_bindir}/engauge

# INSTALL HI-RES ICONS
pushd src/img
icns2png -x digitizer.icns
for sz in 16 32 128 256 512; do
  install -Dm 0644 digitizer_${sz}x${sz}x32.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/%{name}.png
done
popd

%suse_update_desktop_file -i %{name}

# INSTALL APPDATA
install -Dm 0644 dev/gnome/engauge-digitizer.appdata.xml \
            %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# REMOVE UNNECESSARY windows BUILD FILE
find ./ -name build.windows -delete -print

%fdupes -s doc/doxygen/html

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc README.md engauge.qhc engauge.qch
%license LICENSE
%{_bindir}/engauge
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%files doc
%doc help

%files devel-doc
%doc doc/doxygen/html

%changelog
