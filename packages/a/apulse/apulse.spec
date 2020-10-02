#
# spec file for package apulse
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


# integer of major pulse version
%define pulse_major %(sed -n '/^#define.*PA_MAJOR/{s/^.* //;p}' %{_includedir}/pulse/version.h)
%define __provides_exclude_from ^%{_libdir}/apulse/.*.so.*$
Name:           apulse
Version:        0.1.13
Release:        0
Summary:        PulseAudio emulation for ALSA
License:        MIT
URL:            https://github.com/i-rinat/apulse
Source0:        https://github.com/i-rinat/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        %{name}.py
Source3:        %{name}.conf
%if %{pulse_major} > 12
# PATCH-FIX-OPENSUSE apulse-fix-pulse-13.patch seife+obs@b1-systems.com -- Fix PulseAudio 13+ compatibility.
Patch0:         apulse-fix-pulse-13.patch
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse) >= 5.0
%if %{?_lib} == lib64
Recommends:     %{name}-32bit = %{version}
%endif

%description
PulseAudio emulation intended to be used with Firefox and Skype.

%prep
%autosetup -p1

%build
%cmake \
  -DUSE_BUNDLED_PULSEAUDIO_HEADERS=OFF \
  -DAPULSEPATH=%{_libdir}/%{name}      \
  -DCMAKE_SHARED_LINKER_FLAGS="" -LA
%make_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/%{name}/libpulse*.so
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE.MIT
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/libpulse*.so.*
%{_mandir}/man1/apulse.1%{?ext_man}

%changelog
