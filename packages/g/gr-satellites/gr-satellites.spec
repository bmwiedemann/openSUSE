#
# spec file for package gr-satellites
#
# Copyright (c) 2026 SUSE LLC
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


%define soname  %(echo %{version} | tr . _)
%define libname libgnuradio-satellites%{soname}
Name:           gr-satellites
Version:        5.9.0
Release:        0
Summary:        Collection of telemetry decoders for GNU Radio
# Legal-Review-Notice: everything below is linked into libgnuradio-satellites.
# GPL-3.0-or-later: upstream (458 SPDX headers). MIT: lib/randomizer.c.
# Apache-2.0: lib/viterbi/ (vendored from github.com/xukmin/viterbi).
# OPEN QUESTION for legal review: lib/viterbi.c and 7 of the 9 lib/libfec/*.c
# carry Karn's bare "may be used under the terms of the LGPL" with NO version
# (ccsds.c and taltab.c are bare data tables with no header at all). Tagged
# -or-later here because -only would be GPL-3-incompatible inside this very
# .so; Debian reads the same headers as LGPL-2.1. Not settled downstream.
License:        Apache-2.0 AND GPL-3.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://github.com/daniestevez/gr-satellites
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
BuildRequires:  bzip2
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# gnuradio's GnuradioConfig.cmake find_dependency()s these; not pulled in by
# the pkgconfig() deps below, and unit_test_framework comes from ENABLE_TESTING
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
# spec-cleaner turns this into stale pkgconfig(python-3.6); keep the package name
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-pybind11-devel
# floors per CMakeLists find_package(Gnuradio "3.10" COMPONENTS ...); spec-cleaner
# over-expands gnuradio-devel to all 16 .pc, trimmed to the components actually used
BuildRequires:  pkgconfig(gnuradio-analog) >= 3.10
BuildRequires:  pkgconfig(gnuradio-blocks) >= 3.10
BuildRequires:  pkgconfig(gnuradio-digital) >= 3.10
BuildRequires:  pkgconfig(gnuradio-fft) >= 3.10
BuildRequires:  pkgconfig(gnuradio-filter) >= 3.10
BuildRequires:  pkgconfig(gnuradio-runtime) >= 3.10
BuildRequires:  pkgconfig(volk)
Requires:       gnuradio
Requires:       python3-PyYAML
# satellites/__init__.py imports the submitter and csp_zmq modules
# unconditionally, so requests/websocket/zmq are hard deps, not extras
Requires:       python3-construct >= 2.9
Requires:       python3-matplotlib
Requires:       python3-numpy
Requires:       python3-pyzmq
Requires:       python3-requests
Requires:       python3-websocket-client
# only the realtime image decoders shell out to it
Recommends:     feh

%description
%{name} is a GNU Radio out-of-tree module encompassing a collection of
telemetry decoders that supports many different Amateur satellites.

%package -n %{libname}
Summary:        Library for %{name}

%description -n %{libname}
Library files for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}-%{release}
# the installed headers include <gnuradio/...> and satellitesTarget.cmake
# find_dependency()s the gnuradio targets; spec-cleaner over-expands this to
# all 16 pkgconfig(gnuradio-*), keep the package name
Requires:       gnuradio-devel

%description devel
Development files for %{name} module for GNU Radio.

%package devel-doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description devel-doc
Documentation for %{name} module for GNU Radio.

%prep
%autosetup
# upstream ships exactly these two with CRLF
dos2unix python/telemetry/aepex_70cm.py python/satyaml/EIRSAT-1.yml
# so it is not just another bare LICENSE.md under %%{_licensedir}
cp lib/viterbi/LICENSE.md LICENSE.viterbi-Apache-2.0

%build
%cmake
%cmake_build

# No %%check: upstream defines no C++ tests, and its 29 python QA tests set
# GR_TEST_PYTHON_DIRS to the build tree + a 3.8-era swig dir, neither of which
# holds an importable satellites package. Aimed at the installed tree instead
# they die in pybind11 ("type ax100_decode is already registered"). Upstream CI
# does not run them either; Debian runs them with failures ignored.
%install
%cmake_install

# doxygen output lands in %%{_datadir}/doc, not the openSUSE %%{_docdir}
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/%{name}/html %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/%{name}/xml %{buildroot}%{_docdir}/%{name}
rmdir %{buildroot}%{_datadir}/doc/%{name}

# these are importable modules, not scripts; the shebangs are dead weight
find %{buildroot}%{python3_sitearch} -name '*.py' -not -perm -u+x \
    -exec sed -i '1{/^#!/d}' {} +

# upstream's cmake installs no bytecode and there is no brp step for it;
# must follow the shebang strip above or the .pyc go stale
%{python_compileall}
# %%python_compileall writes identical .pyc and .opt-1.pyc
%fdupes %{buildroot}%{python3_sitearch}

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSE LICENSE.viterbi-Apache-2.0
%doc README.md
%{_bindir}/gr_satellites
%{_bindir}/gr_satellites_ssdv
%{_bindir}/smog_p_spectrum
%{_mandir}/man1/gr_satellites.1%{?ext_man}
%{_mandir}/man1/gr_satellites_ssdv.1%{?ext_man}
%{_mandir}/man1/smog_p_spectrum.1%{?ext_man}
%{_datadir}/gnuradio/grc/blocks/satellites_*.yml
%{_datadir}/gnuradio/grc/blocks/variable_time_format_parameters.block.yml
%{python3_sitearch}/satellites/

%files -n %{libname}
%{_libdir}/libgnuradio-satellites.so.%{version}*

%files devel
%{_includedir}/satellites/
%{_libdir}/libgnuradio-satellites.so
%{_libdir}/cmake/satellites/

%files devel-doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html
%{_docdir}/%{name}/xml

%changelog
