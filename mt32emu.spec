#
# spec file for package mt32emu
#
# Copyright (c) 2024 SUSE LLC
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


%define s_name  munt-lib%{name}_%{s_ver}
%define s_ver   2_7_1
%define sover   2
Name:           mt32emu
Version:        2.7.1
Release:        0
Summary:        An emulator of the Roland MT-32, CM-32L and LAPC-I synthesiser modules
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/munt/munt
Source0:        https://github.com/munt/munt/archive/lib%{name}_%{s_ver}.tar.gz#/%{s_name}.tar.gz
Patch0:         %{name}-2.6.3-name.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(portaudio-2.0)

%description
A multi-platform software synthesiser emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I.

%package qt
Summary:        The main Qt-frontend synthesiser application
Requires:       lib%{name}%{sover} = %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description qt
It facilitates both realtime synthesis and conversion of pre-recorded SMF files to WAVE making use of the mt32emu library.

%package -n lib%{name}%{sover}
Summary:        Shared library for %{name}

%description -n lib%{name}%{sover}
A multi-platform software synthesiser emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I.
This package provides the %{name} library.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{sover} = %{version}

%description -n lib%{name}-devel
A multi-platform software synthesiser emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I.
Development files for lib%{name}.

%prep
%autosetup -p1 -n %{s_name}

%build
%cmake -LA \
       -DCMAKE_SHARED_LINKER_FLAGS="-lm" \
       -DLIB_INSTALL_DIR:PATH="%{_lib}" \
       -Dlibmt32emu_PKGCONFIG_INSTALL_PREFIX="%{_libdir}"
%make_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/doc %{buildroot}%{_libdir}/cmake

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files qt
%license %{name}_qt/COPYING.txt
%doc %{name}_qt/AUTHORS.txt %{name}_qt/NEWS.txt %{name}_qt/README.md %{name}_qt/TODO.txt
%{_bindir}/%{name}-qt
%{_bindir}/%{name}-smf2wav
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files -n lib%{name}%{sover}
%license %{name}/COPYING.LESSER.txt
%doc %{name}/AUTHORS.txt %{name}/NEWS.txt %{name}/README.md %{name}/TODO.txt
%{_libdir}/lib%{name}*.so.%{sover}*

%files -n lib%{name}-devel
%{_libdir}/lib%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_includedir}/%{name}/*.h
%dir %{_includedir}/%{name}/c_interface
%{_includedir}/%{name}/c_interface/*.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
