#
# spec file for package gnuradio
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


%define sover  3_10_12
%bcond_without docs
Name:           gnuradio
Version:        3.10.12.0
Release:        0
Summary:        GNU software radio
License:        GPL-3.0-or-later
URL:            https://gnuradio.org
Source0:        https://github.com/gnuradio/gnuradio/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
Patch0:         boost.patch
# PATCH-FIX-UPSTREAM gnuradio-fix-fastnoise-unit-test.patch gh#gnuradio/gnuradio#8145
Patch1:         gnuradio-fix-fastnoise-unit-test.patch
# PATCH-FIX-UPSTREAM gnuradio-run-qtgui-tests-with-xvfb.patch gh#gnuradio/gnuradio#8170
Patch2:         gnuradio-run-qtgui-tests-with-xvfb.patch
BuildRequires:  alsa-devel
BuildRequires:  cmake >= 3.16.3
BuildRequires:  codec2-devel
BuildRequires:  cppunit-devel
BuildRequires:  cppzmq-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel
BuildRequires:  fish
BuildRequires:  gcc-c++ >= 9.3.0
BuildRequires:  gmp-devel
BuildRequires:  gobject-introspection
BuildRequires:  gsl-devel
BuildRequires:  libSDL-devel
BuildRequires:  libad9361-iio-devel
BuildRequires:  libboost_atomic-devel >= 1.69
BuildRequires:  libboost_filesystem-devel >= 1.69
BuildRequires:  libboost_regex-devel >= 1.69
BuildRequires:  libboost_test-devel >= 1.69
%if 0%{?suse_version} <= 1600
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  libgsm-devel
BuildRequires:  libiio-devel
BuildRequires:  libjack-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libthrift-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  libxml2-devel
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-click
BuildRequires:  python3-click-plugins
BuildRequires:  python3-devel >= 3.6.5
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-cairo
BuildRequires:  python3-jsonschema
BuildRequires:  python3-mako >= 1.0.7
BuildRequires:  python3-numpy-devel >= 1.17.4
BuildRequires:  python3-pyaml >= 3.11
BuildRequires:  python3-pybind11-devel >= 2.4.3
BuildRequires:  python3-pycairo
BuildRequires:  python3-pyzmq
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-thrift
BuildRequires:  qwt6-qt5-devel
BuildRequires:  soapy-sdr-devel
BuildRequires:  spdlog-devel
BuildRequires:  thrift
BuildRequires:  uhd-devel
BuildRequires:  volk-devel >= 2.4.1
BuildRequires:  xvfb-run
BuildRequires:  typelib(Gtk) = 3.0
BuildRequires:  typelib(PangoCairo) = 1.0
BuildRequires:  typelib(cairo) = 1.0
# gr_soapy dependencies
Requires:       python3-SoapySDR
# gnuradio-companion dependencies
Requires:       python3-cairo
Requires:       python3-QDarkStyle
Requires:       python3-QtPy
# gr_modtool dependencies
Requires:       python3-click
Requires:       python3-click-plugins
Requires:       python3-gobject-Gdk
Requires:       python3-jsonschema
Requires:       python3-mako >= 1.1.0
Requires:       python3-numpy >= 1.17.4
Requires:       python3-pyaml >= 3.11
Requires:       python3-pyqtgraph
# gr_network dependencies
Requires:       python3-pyzmq
Requires:       python3-qt5
# gr_filter dependencies
Requires:       python3-scipy
Requires:       typelib(Gtk) = 3.0
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  mathjax
%endif

%description
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

%package     -n libgnuradio-%{sover}
Summary:        Libraries for GNU Radio

%description -n libgnuradio-%{sover}
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains the libraries for GNU Radio.

%package        devel
Summary:        Deveopment files for GNU Radio
Requires:       %{name} = %{version}
Requires:       gmp-devel
Requires:       spdlog-devel

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
Requires:       %{name} = %{version}

%description    examples
GNU Radio is a collection of software that when combined with minimal
hardware, allows the construction of radios where the actual waveforms
transmitted and received are defined by software. What this means is
that it turns the digital modulation schemes used in today's high
performance wireless devices into software problems.

This package contains some examples of using GNU Radio.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%setup -q
%if 0%{?suse_version} > 1600
%patch -P 0 -p1
%endif
%patch -P 1 -p1
%patch -P 2 -p1

# protect the template files from %%cmake macro magic / mangling
find  gr-utils/modtool/templates/gr-newmod -name CMakeLists.txt -ls -exec mv '{}' '{}.tmpl' \;

%build
%limit_build -m 1500

%define __builder ninja
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DENABLE_DEFAULT:BOOL=OFF \
  -DENABLE_TESTING:BOOL=ON \
  -DENABLE_PYTHON:BOOL=ON \
  -DENABLE_GRC:BOOL=ON \
  -DENABLE_JSONYAML_BLOCKS:BOOL=ON \
  -DENABLE_GNURADIO_RUNTIME:BOOL=ON \
  -DENABLE_COMMON_PCH:BOOL=ON \
  -DENABLE_GR_CTRLPORT:BOOL=ON \
  -DENABLE_CTRLPORT_THRIFT:BOOL=ON \
  -DENABLE_GR_BLOCKS:BOOL=ON \
  -DENABLE_GR_FEC:BOOL=ON \
  -DENABLE_GR_FFT:BOOL=ON \
  -DENABLE_GR_FILTER:BOOL=ON \
  -DENABLE_GR_ANALOG:BOOL=ON \
  -DENABLE_GR_DIGITAL:BOOL=ON \
  -DENABLE_GR_DTV:BOOL=ON \
  -DENABLE_GR_AUDIO:BOOL=ON \
  -DENABLE_GR_CHANNELS:BOOL=ON \
  -DENABLE_GR_PDU:BOOL=ON \
  -DENABLE_GR_IIO:BOOL=ON \
  -DENABLE_GR_QTGUI:BOOL=ON \
  -DENABLE_GR_TRELLIS:BOOL=ON \
  -DENABLE_GR_UHD:BOOL=ON \
  -DENABLE_UHD_RFNOC:BOOL=ON \
  -DENABLE_GR_UTILS:BOOL=ON \
  -DENABLE_GR_MODTOOL:BOOL=ON \
  -DENABLE_GR_BLOCKTOOL:BOOL=ON \
  -DENABLE_GR_VIDEO_SDL:BOOL=ON \
  -DENABLE_GR_VOCODER:BOOL=ON \
  -DENABLE_GR_WAVELET:BOOL=ON \
  -DENABLE_GR_ZEROMQ:BOOL=ON \
  -DENABLE_GR_NETWORK:BOOL=ON \
  -DENABLE_GR_SOAPY:BOOL=ON \
  -DENABLE_DOXYGEN:BOOL=%{with docs} \
  -DENABLE_MANPAGES:BOOL=ON \
  -DENABLE_EXAMPLES:BOOL=ON \
  -DENABLE_PERFORMANCE_COUNTERS:BOOL=ON \
  -DENABLE_BASH_COMPLETIONS:BOOL=ON \
  -DENABLE_FISH_COMPLETIONS:BOOL=ON \
  -DENABLE_ZSH_COMPLETIONS:BOOL=ON \
  -DTRY_SHM_VMCIRCBUF:BOOL=ON \
  -DENABLE_POSTINSTALL:BOOL=OFF \
  -DENABLE_NATIVE:BOOL=OFF \
  -DENABLE_BAD_BOOST:BOOL=OFF \
%ifarch armv6l armv6hl
  -Dhave_mfpu_neon=0 \
%endif
  -DGR_PYTHON_DIR=%{python3_sitearch} \
  -DENABLE_INTERNAL_VOLK:BOOL=OFF
%cmake_build

%check
%ifarch ppc64le
# The ZeroMQ message source tests segfault during teardown on ppc64le.
%ctest --exclude-regex '^qa_zeromq_(pull|req|sub)_msg_source$'
%else
%ctest
%endif

%install
# move the template files back
find  gr-utils/modtool/templates/gr-newmod -name CMakeLists.txt.tmpl -execdir mv '{}' 'CMakeLists.txt' \;

%cmake_install

# Python modules are imported, not executed directly.
find %{buildroot}%{python3_sitearch}/gnuradio \
  %{buildroot}%{_datadir}/gnuradio/modtool/templates \
  -type f ! -perm /111 -exec sed -i '1{/^#!.*\(python\|bash\)/d}' '{}' +
rm %{buildroot}%{_datadir}/gnuradio/modtool/templates/gr-newmod/python/howto/bindings/README.md

install -Dpm 0644 grc/scripts/freedesktop/gnuradio-grc.desktop %{buildroot}%{_datadir}/applications/gnuradio-grc.desktop
install -Dpm 0644 grc/scripts/freedesktop/gnuradio-grc.xml %{buildroot}%{_datadir}/mime/packages/gnuradio-grc.xml
install -Dpm 0644 grc/scripts/freedesktop/org.gnuradio.grc.metainfo.xml %{buildroot}%{_datadir}/metainfo/org.gnuradio.grc.metainfo.xml
for size in 16 24 32 48 64 128 256; do
  install -Dpm 0644 grc/scripts/freedesktop/grc-icon-${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/gnuradio-grc.png
done

install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/%{_datadir}/doc/%{name}-*/* %{buildroot}%{_docdir}/%{name}/

# Compiled examples are installed as "data", but are arch dependent
install -dm 0755 %{buildroot}%{_libdir}/gnuradio
mv %{buildroot}%{_datadir}/gnuradio/examples %{buildroot}%{_libdir}/gnuradio/

%fdupes %{buildroot}%{_docdir}
%fdupes %{buildroot}%{_includedir}
%fdupes %{buildroot}%{_libdir}

%post -n libgnuradio-%{sover} -p /sbin/ldconfig
%postun -n libgnuradio-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/gnuradio-companion
%{_bindir}/gnuradio-config-info
%{_bindir}/gr-ctrlport-monitor
%{_bindir}/gr-perf-monitorx
%{_bindir}/gr_filter_design
%{_bindir}/gr_modtool
%{_bindir}/gr_plot
%{_bindir}/gr_plot_const
%{_bindir}/gr_plot_fft
%{_bindir}/gr_plot_iq
%{_bindir}/gr_plot_psd
%{_bindir}/gr_plot_qt
%{_bindir}/gr_read_file_metadata
%{_bindir}/grcc
%{_bindir}/polar_channel_construction
%{_bindir}/uhd_fft
%{_bindir}/uhd_rx_cfile
%{_bindir}/uhd_rx_nogui
%{_bindir}/uhd_siggen
%{_bindir}/uhd_siggen_gui
%dir %{_datadir}/gnuradio
%{_datadir}/gnuradio/grc/
%{_datadir}/gnuradio/modtool/
%{_datadir}/gnuradio/themes/
%{_datadir}/gnuradio/fec/
%{_datadir}/gnuradio/clang-format.conf
%{_datadir}/gnuradio/.cmake-format.py
%{_datadir}/icons/hicolor/*/apps/gnuradio-grc.png
%{_datadir}/applications/gnuradio-grc.desktop
%{_datadir}/mime/packages/gnuradio-grc.xml
%{_datadir}/metainfo/org.gnuradio.grc.metainfo.xml
%{python3_sitearch}/*
%dir %{_sysconfdir}/gnuradio
%dir %{_sysconfdir}/gnuradio/conf.d
%config(noreplace) %{_sysconfdir}/gnuradio/conf.d/*.conf
%{_mandir}/man1/*.1%{?ext_man}
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/README*
%{_docdir}/%{name}/CHANGELOG*
%{_docdir}/%{name}/CONTRIBUTING.md
%dir %{_docdir}/%{name}/config/
%{_docdir}/%{name}/config/*
# doc package
%exclude %{_docdir}/%{name}/html/
%exclude %{_docdir}/%{name}/xml/

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

%files examples
%dir %{_libdir}/gnuradio
%{_libdir}/gnuradio/examples/

%files -n %{name}-bash-completion
%{_datadir}/bash-completion/completions/gr_modtool

%files -n %{name}-fish-completion
%{_datadir}/fish/vendor_completions.d/gr_modtool.fish

%files -n %{name}-zsh-completion
%{_datadir}/zsh/site-functions/_gr_modtool

%changelog
