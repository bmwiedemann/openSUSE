#
# spec file for package gnuradio
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


%define sover  3_7_12-0_0_0
%define sover_volk  1_4
%define volk_version 1.4
Name:           gnuradio
Version:        3.7.13.5
Release:        0
Summary:        GNU software radio
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            http://gnuradio.org
Source0:        https://github.com/gnuradio/gnuradio/releases/download/v%{version}/gnuradio-%{version}.tar.xz
Source1:        https://github.com/gnuradio/gnuradio/releases/download/v%{version}/gnuradio-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        https://github.com/gnuradio/volk/archive/v%{volk_version}.tar.gz#/volk-%{volk_version}.tar.gz
# http://www.nathanwest.us/grc_to_37.sh
Source4:        grc_to_37.sh
Source99:       %{name}-rpmlintrc
Patch0:         missing_library.patch
# PATCH 100-120 Qt5 port patches
Patch100:       qt5-maint-0001-CMake-Update-required-minimum-version-to-2.8.12.patch
Patch101:       qt5-maint-0002-CMake-FindQwt-Find-the-Qt5-version-of-QWT-instead-of.patch
Patch102:       qt5-maint-0003-gr-qtgui-update-for-Qt5.patch
Patch103:       qt5-maint-0004-grc-Generate-Python-scripts-that-use-PyQt5.patch
Patch104:       qt5-maint-0005-gr-qtgui-Add-a-workaround-for-an-upstream-bug-of-uic.patch
Patch105:       qt5-maint-0006-qtgui-fixed-examples-for-Qt5-compatibility.patch
Patch106:       qt5-maint-0007-qtgui-Fixes-for-edit_box_msg-to-work-with-QT5.patch
Patch107:       qt5-maint-0008-gr-qtgui-Allow-build-with-Qt4-or-Qt5-default.patch
Patch108:       qt5-maint-0009-gr-qtgui-Fix-PyQt-4-5-include-in-XMLs-for-GRC.patch
Patch109:       qt5-maint-0010-gr-qtgui-Fix-range.py-to-work-with-both-Qt4-and-Qt5.patch
Patch110:       qt5-maint-0011-gr-qtgui-Re-introduce-some-Qt4-specific-code.patch
Patch111:       qt5-maint-0012-grc-Fix-generation-of-Python-code-for-Qt4-and-Qt5.patch
Patch112:       qt5-maint-0013-grc-replace-templated-xml-files-with-search-and-repl.patch
Patch113:       qt5-maint-0014-qtgui-replace-templated-xml-files-with-search-and-re.patch
Patch114:       qt5-maint-0017-qtgui-fix-stylesheet-for-qt5.patch
Patch115:       qt5-maint-0019-qtgui-fixed-apps-for-Qt5-compatibility.patch
Patch116:       qt5-maint-0021-gnuradio-runtime-ctrlport-qt5.patch
Patch117:       qt5-maint-0022-gr-uhd-qt5.patch
Patch118:       qt5-maint-0023-gr-qtgui-util.patch
Patch119:       qt5-maint-0024-gr-qtgui-restoreGeometry.patch
#PATCH-FIX-OPENSUSE 0001-Add-the-include-path-used-by-the-openSUSE-package.patch
Patch120:       0001-Add-the-include-path-used-by-the-openSUSE-package.patch
BuildRequires:  alsa-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  libSDL-devel
BuildRequires:  libgsm-devel
BuildRequires:  libjack-devel
BuildRequires:  libxslt-python
BuildRequires:  memory-constraints
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  python-Cheetah
BuildRequires:  python-Sphinx
BuildRequires:  python-gtk
BuildRequires:  python-lxml
BuildRequires:  python-mako
BuildRequires:  python-numpy
%if 0%{?suse_version} > 1500
BuildRequires:  python-qt5-devel
BuildRequires:  qwt6-qt5-devel
%else
BuildRequires:  python-qt4-devel
BuildRequires:  qwt6-devel
%endif
BuildRequires:  swig
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  uhd-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
# Workaround for openssl migration
#!BuildIgnore:  openssl-1_0_0
Requires:       python
Requires:       python-Cheetah
Requires:       python-gtk
Requires:       python-lxml
Requires:       python-numpy
%if 0%{?suse_version} > 1500
Requires:       python-qt5
%else
Requires:       python-qt4
%endif

%if 0%{?suse_version} > 1320
BuildRequires:  python-wxWidgets-3_0
%else
BuildRequires:  python-wxWidgets
%endif

%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

%package        wxgui
Summary:        Libraries for GNU Radio
Group:          System/Libraries
%if 0%{?suse_version} > 1320
Requires:       python-wxWidgets-3_0
%else
Requires:       python-wxWidgets
%endif

%description    wxgui
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains the wxgui blocks

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

%package     -n libvolk%{sover_volk}
Summary:        Libraries for GNU Radio
Group:          System/Libraries
Conflicts:      libgnuradio0
Obsoletes:      libvolk0_0_0

%description -n libvolk%{sover_volk}
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains the Vector-Optimized Library of Kernels (VOLK)

%package        devel
Summary:        Deveopment files for GNU Radio
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

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

%package        examples-wxgui
Summary:        GNU Radio wxgui examples
Group:          Productivity/Hamradio/Other
Requires:       %{name}-wxgui = %{version}

%description    examples-wxgui
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains the examples of using GNU Radio depending on wxWidgets.

%prep
%setup -q
tar xzf %{SOURCE3} -C volk/ --strip-components=1
%patch0 -p1
%if 0%{?suse_version} > 1500
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%endif

# remove buildtime from documentation
sed -i 's|^HTML_TIMESTAMP         = YES|HTML_TIMESTAMP         = NO|' docs/doxygen/Doxyfile.in
sed -i 's|^HTML_TIMESTAMP         = YES|HTML_TIMESTAMP         = NO|' docs/doxygen/Doxyfile.swig_doc.in

%build
%limit_build -m 2000
%ifnarch armv6l armv6hl
  %cmake
%else
  %cmake -Dhave_mfpu_neon=0
%endif
%make_jobs

%install
%cmake_install

install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/%{_datadir}/doc/%{name}-*/* %{buildroot}%{_docdir}/%{name}/

# recompile python modules to avoid timestamp problems
%py_compile %{buildroot}%{python_sitearch}
%py_compile -O %{buildroot}%{python_sitearch}

# install icons and desktop file
install -Dpm 0644 %{buildroot}%{_datadir}/gnuradio/grc/freedesktop/grc-icon-32.png \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gnuradio-grc.png
install -Dpm 0644  %{buildroot}%{_datadir}/gnuradio/grc/freedesktop/grc-icon-48.png \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gnuradio-grc.png
install -Dpm 0644 %{buildroot}%{_datadir}/gnuradio/grc/freedesktop/grc-icon-64.png \
	%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gnuradio-grc.png
install -Dpm 0644 %{buildroot}%{_datadir}/gnuradio/grc/freedesktop/grc-icon-128.png \
	%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/gnuradio-grc.png
install -Dpm 0644 %{buildroot}%{_datadir}/gnuradio/grc/freedesktop/grc-icon-256.png \
	%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/gnuradio-grc.png

install -Dpm 0644 %{buildroot}%{_datadir}/gnuradio/grc/freedesktop/gnuradio-grc.desktop \
	%{buildroot}%{_datadir}/applications/gnuradio-grc.desktop
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/gnuradio-grc.desktop Network HamRadio

install -Dpm 0755 %{SOURCE4} %{buildroot}/%{_bindir}

#remove unneeded stuff
rm -rf %{buildroot}%{_datadir}/%{name}/grc/freedesktop
rm -rf %{buildroot}%{_prefix}/libexec

%fdupes -s %{buildroot}%{_docdir}
%fdupes -s %{buildroot}%{_includedir}
%fdupes -s %{buildroot}%{_libdir}

%post -n libgnuradio-%{sover} -p /sbin/ldconfig
%post -n libvolk%{sover_volk} -p /sbin/ldconfig
%postun -n libgnuradio-%{sover} -p /sbin/ldconfig
%postun -n libvolk%{sover_volk} -p /sbin/ldconfig

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
%{python_sitearch}/*
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
# wxgui package
%exclude %{python_sitearch}/gnuradio/wxgui/
%exclude %{_datadir}/gnuradio/grc/blocks/wxgui*.xml
%exclude %{_datadir}/gnuradio/grc/blocks/notebook.xml
%exclude %{_datadir}/gnuradio/grc/blocks/variable_check_box.xml
%exclude %{_datadir}/gnuradio/grc/blocks/variable_chooser.xml
%exclude %{_datadir}/gnuradio/grc/blocks/variable_slider.xml
%exclude %{_datadir}/gnuradio/grc/blocks/variable_static_text.xml
%exclude %{_datadir}/gnuradio/grc/blocks/variable_text_box.xml

%files wxgui
%{python_sitearch}/gnuradio/wxgui/
%{_datadir}/gnuradio/grc/blocks/wxgui*.xml
%{_datadir}/gnuradio/grc/blocks/notebook.xml
%{_datadir}/gnuradio/grc/blocks/variable_check_box.xml
%{_datadir}/gnuradio/grc/blocks/variable_chooser.xml
%{_datadir}/gnuradio/grc/blocks/variable_slider.xml
%{_datadir}/gnuradio/grc/blocks/variable_static_text.xml
%{_datadir}/gnuradio/grc/blocks/variable_text_box.xml

%files -n libgnuradio-%{sover}
%{_libdir}/libgnuradio*.so.*

%files -n libvolk%{sover_volk}
%{_libdir}/libvolk*.so.*

%files devel
%{_includedir}/%{name}/
%{_includedir}/pmt/
%{_includedir}/volk/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/gnuradio/
%{_libdir}/cmake/volk/

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/xml/
%{_docdir}/%{name}/*.py
%{_docdir}/%{name}/*.grc

%files examples
%{_datadir}/gnuradio/examples/
%exclude %{_datadir}/gnuradio/examples/audio/audio_fft.py
%exclude %{_datadir}/gnuradio/examples/hf_explorer/
%exclude %{_datadir}/gnuradio/examples/hf_radio/
%exclude %{_datadir}/gnuradio/examples/noaa/usrp_rx_hrpt.grc
%exclude %{_datadir}/gnuradio/examples/uhd/fm_tx4.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_am_mw_rcv.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_nbfm_ptt.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_nbfm_rcv.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_tv_rcv.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv_fmdet.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv_pll.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv_sca.py
%exclude %{_datadir}/gnuradio/examples/uhd/usrp_wxapt_rcv.py

%files examples-wxgui
%{_datadir}/gnuradio/examples/audio/audio_fft.py
%{_datadir}/gnuradio/examples/hf_explorer/
%{_datadir}/gnuradio/examples/hf_radio/
%{_datadir}/gnuradio/examples/noaa/usrp_rx_hrpt.grc
%{_datadir}/gnuradio/examples/uhd/fm_tx4.py
%{_datadir}/gnuradio/examples/uhd/usrp_am_mw_rcv.py
%{_datadir}/gnuradio/examples/uhd/usrp_nbfm_ptt.py
%{_datadir}/gnuradio/examples/uhd/usrp_nbfm_rcv.py
%{_datadir}/gnuradio/examples/uhd/usrp_tv_rcv.py
%{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv_fmdet.py
%{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv_pll.py
%{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv.py
%{_datadir}/gnuradio/examples/uhd/usrp_wfm_rcv_sca.py
%{_datadir}/gnuradio/examples/uhd/usrp_wxapt_rcv.py

%changelog
