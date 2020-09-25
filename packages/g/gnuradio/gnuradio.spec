#
# spec file for package gnuradio
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


%bcond_without docs

%define sover  3_8_2
Name:           gnuradio
Version:        3.8.2.0
Release:        0
Summary:        GNU software radio
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://gnuradio.org
Source0:        https://github.com/gnuradio/gnuradio/releases/download/v%{version}/gnuradio-%{version}.tar.xz
# http://www.nathanwest.us/grc_to_37.sh
Source4:        grc_to_37.sh
Source99:       %{name}-rpmlintrc
Patch0:         missing_library.patch
Patch1:         revert-23cece0d0.patch
Patch2:         0001-gr-digital-glfsr.h-drop-boost-cstdint.hpp-and-use-cs.patch
Patch3:         0002-boost_qualify_placeholders_with_their_full_namespace.patch
BuildRequires:  alsa-devel
BuildRequires:  cmake >= 3.8
BuildRequires:  cppunit-devel
BuildRequires:  cppzmq-devel
%if %{with docs}
BuildRequires:  doxygen
# TeX is required for formula rendering
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  tex(newunicodechar.sty)
%endif
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  libSDL-devel
BuildRequires:  libboost_atomic-devel >= 1.53
BuildRequires:  libboost_filesystem-devel >= 1.53
BuildRequires:  libboost_system-devel
BuildRequires:  libgsm-devel
BuildRequires:  libjack-devel
BuildRequires:  libmpir-devel
BuildRequires:  log4cpp-devel
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-click
BuildRequires:  python3-click-plugins
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-cairo
BuildRequires:  python3-mako >= 0.9.1
BuildRequires:  python3-numpy
BuildRequires:  python3-pyaml >= 3.11
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-six
BuildRequires:  qwt6-qt5-devel
BuildRequires:  swig >= 3.0.8
BuildRequires:  uhd-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  pkgconfig(volk) >= 2.0
BuildRequires:  typelib(Gtk) = 3.0
BuildRequires:  typelib(PangoCairo) = 1.0
BuildRequires:  typelib(cairo) = 1.0
Requires:       python3-numpy
Requires:       python3-pyaml >= 3.11
Requires:       python3-qt5
# gr_modtool dependencies
Requires:       python3-click
Requires:       python3-click-plugins
Requires:       python3-mako

%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

%package     -n libgnuradio-%{sover}
Summary:        Libraries for GNU Radio
Group:          System/Libraries
Obsoletes:      libgnuradio0

%description -n libgnuradio-%{sover}
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains the libraries for GNU Radio.

%package        devel
Summary:        Deveopment files for GNU Radio
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gmp-devel
Requires:       log4cpp-devel

%description    devel
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains libraries and header files for developing
applications that use GNU Radio.

%package        doc
Summary:        GNU Radio documentation
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    doc
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains documentation for GNU Radio.

%package        examples
Summary:        GNU Radio examples
Group:          Productivity/Hamradio/Other
Requires:       %{name} = %{version}

%description    examples
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains some examples of using GNU Radio.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# remove buildtime from documentation
sed -i 's|^HTML_TIMESTAMP         = YES|HTML_TIMESTAMP         = NO|' docs/doxygen/Doxyfile.in
sed -i 's|^HTML_TIMESTAMP         = YES|HTML_TIMESTAMP         = NO|' docs/doxygen/Doxyfile.swig_doc.in

# protect the template files from %%cmake macro magic / mangling
find  gr-utils/python/modtool/templates/gr-newmod -name CMakeLists.txt -exec mv '{}' '{}.tmpl' \;

%build
%cmake \
%ifarch armv6l armv6hl
  -Dhave_mfpu_neon=0 \
%endif
  -DGR_PYTHON_DIR=%{python3_sitearch} \
  -DENABLE_INTERNAL_VOLK:BOOL=OFF
%cmake_build

%install
# move the template files back
find  gr-utils/python/modtool/templates/gr-newmod -name CMakeLists.txt.tmpl -execdir mv '{}' 'CMakeLists.txt' \;

%cmake_install

install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/%{_datadir}/doc/%{name}-*/* %{buildroot}%{_docdir}/%{name}/

%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/gnuradio-grc.desktop Network HamRadio

install -Dpm 0755 %{SOURCE4} %{buildroot}/%{_bindir}

# Compiled examples are installed as "data", but are arch dependent
install -dm 0755 %{buildroot}%{_libdir}/gnuradio
mv %{buildroot}%{_datadir}/gnuradio/examples %{buildroot}%{_libdir}/gnuradio/

# remove duplicate icons (just keep hicolor)
rm -rf %{buildroot}%{_datadir}/%{name}/grc/freedesktop
rm -rf %{buildroot}%{_datadir}/icons/gnome

%fdupes %{buildroot}%{_docdir}
%fdupes %{buildroot}%{_includedir}
%fdupes %{buildroot}%{_libdir}

%post -n libgnuradio-%{sover} -p /sbin/ldconfig
%postun -n libgnuradio-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/*
%dir %{_datadir}/gnuradio
%{_datadir}/gnuradio/grc/
%{_datadir}/gnuradio/modtool/
%{_datadir}/gnuradio/themes/
%{_datadir}/gnuradio/fec/
%{_datadir}/icons/hicolor/*/apps/gnuradio-grc.png
%{_datadir}/applications/gnuradio-grc.desktop
%{_datadir}/mime/packages/gnuradio-grc.xml
%{python3_sitearch}/*
%dir %{_sysconfdir}/gnuradio
%dir %{_sysconfdir}/gnuradio/conf.d
%config(noreplace) %{_sysconfdir}/gnuradio/conf.d/*.conf
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/README*
%{_docdir}/%{name}/CHANGELOG*
# doc package
%exclude %{_docdir}/%{name}/html/
%exclude %{_docdir}/%{name}/xml/
%exclude %{_docdir}/%{name}/*.py
%exclude %{_docdir}/%{name}/*.grc

%files -n libgnuradio-%{sover}
%{_libdir}/libgnuradio*.so.*

%files devel
%{_includedir}/%{name}/
%{_includedir}/pmt/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/gnuradio/

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/xml/
%{_docdir}/%{name}/*.py
%{_docdir}/%{name}/*.grc

%files examples
%dir %{_libdir}/gnuradio
%{_libdir}/gnuradio/examples/

%changelog
