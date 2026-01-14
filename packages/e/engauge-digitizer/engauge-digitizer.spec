#
# spec file for package engauge-digitizer
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        12.9.1
Release:        0
Summary:        Ditigizer software that converts old graphs into numbers again
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://markummitchell.github.io/engauge-digitizer/
Source0:        https://github.com/akhuettel/engauge-digitizer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  icns-utils
BuildRequires:  optipng
BuildRequires:  qt6-tools-helpgenerators
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Help)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(log4cpp)
BuildRequires:  pkgconfig(poppler-qt6)
Suggests:       %{name}-doc

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

# Remove any RUNPATH, we don't use the wrapper script or private libraries
sed -i -e '/QMAKE_LFLAGS.*ORIGIN/ d' engauge.pro

%build
# ADD JPEG2000 SUPPORT
export OPENJPEG_INCLUDE=$(pkg-config --cflags-only-I libopenjp2 | sed -e 's@-I\(\S\+\).*@\1@g')
export OPENJPEG_LIB=%{_libdir}
export POPPLER_INCLUDE=%{_includedir}/poppler/qt6
export POPPLER_LIB=%{_libdir}

qmake6 engauge.pro \
  "DEFINES+=HELPDIR=%{_docdir}/%{name}/" \
  QMAKE_CFLAGS="%optflags -fno-strict-aliasing" \
  QMAKE_CXXFLAGS="%optflags -fno-strict-aliasing" \
  CONFIG+="pdf jpeg2000"
%make_build

# HELP files
pushd help
# CRLF -> LF
sed -i 's/\r$//' engauge.qhcp dateformats.css dateformats.html
optipng -o2 *png
%{_libexecdir}/qt6/qhelpgenerator engauge.qhcp -o engauge.qhc
mv engauge.qch engauge.qhc ../
rm engauge.qhcp .gitignore build.bash build.windows
popd

# Generate source code documentation in HTML format
pushd src
sed -i 's/\(GENERATE_LATEX.*\)=.*/\1 = NO/' Doxyfile
doxygen
popd

%install
install -Dm 755 bin/Engauge %{buildroot}%{_bindir}/engauge

# INSTALL HI-RES ICONS
pushd src/img
icns2png -x digitizer.icns
for sz in 16 32 128 256 512; do
  install -Dm 0644 digitizer_${sz}x${sz}x32.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/%{name}.png
done
popd

# Install appdata and desktop file
install -Dm 0644 dev/gnome/engauge-digitizer.appdata.xml \
            %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
install -Dm 0644 dev/engauge-digitizer.desktop \
            %{buildroot}%{_datadir}/applications/%{name}.desktop

%fdupes -s doc/doxygen/html

%files
%doc README.md engauge.qhc engauge.qch
%license LICENSE
%{_bindir}/engauge
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

%files doc
%doc help

%files devel-doc
%doc doc/doxygen/html

%changelog
