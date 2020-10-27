#
# spec file for package mt32emu
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


%define sover   2
%define _version 2_4_1
Name:           mt32emu
Version:        2.4.1
Release:        0
Summary:        An emulator of the Roland MT-32, CM-32L and LAPC-I synthesiser modules
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/munt/munt
Source0:        https://github.com/munt/munt/archive/lib%{name}_%{_version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
BuildRequires:  alsa-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libpulse-devel
BuildRequires:  portaudio-devel
Requires:       lib%{name}%{sover} = %{version}

%description
A multi-platform software synthesiser emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I.

%package -n lib%{name}%{sover}
Summary:        Shared library for %{name}

%description -n lib%{name}%{sover}
A multi-platform software synthesiser emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I.
This package provides the %{name} library.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       alsa-devel
Requires:       glib2-devel
Requires:       libQt5Core-devel
Requires:       libQt5Gui-devel
Requires:       libQt5Widgets-devel
Requires:       libmt32emu%{sover} = %{version}
Requires:       libpulse-devel
Requires:       portaudio-devel

%description -n lib%{name}-devel
A multi-platform software synthesiser emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I.
Development files for lib%{name}.

%prep
%autosetup -p1 -n munt-lib%{name}_%{_version}

%build
%cmake -LA \
       -DCMAKE_SHARED_LINKER_FLAGS="-lm"
%make_build

%install
%cmake_install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
rm -r %{buildroot}%{_datadir}/doc

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license %{name}_qt/COPYING.txt
%doc %{name}_qt/AUTHORS.txt %{name}_qt/NEWS.txt %{name}_qt/README.txt %{name}_qt/TODO.txt
%{_bindir}/%{name}-qt
%{_bindir}/%{name}-smf2wav
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files -n lib%{name}%{sover}
%license %{name}/COPYING.LESSER.txt
%doc %{name}/AUTHORS.txt %{name}/NEWS.txt %{name}/README.txt %{name}/TODO.txt
%{_libdir}/lib%{name}*.so.%{sover}*

%files -n lib%{name}-devel
%{_libdir}/lib%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_includedir}/%{name}/c_interface
%{_includedir}/%{name}/c_interface/*.h

%changelog
