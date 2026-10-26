#
# spec file for package stlink
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


%global modprobe_d_files stlink_v1.conf
%define         sover 1
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
Name:           stlink
Version:        1.9.0
Release:        0
Summary:        STM32 discovery line linux programmer
License:        BSD-3-Clause
URL:            https://github.com/stlink-org/stlink/
Source0:        https://github.com/stlink-org/stlink/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.21
# Keep the plain -devel form: its pkgconfig expansion is ten sub-libraries
# the GUI never names directly; the single BuildRequires is exact.
BuildRequires:  gtk3-devel >= 3.24.30
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.24
BuildRequires:  pkgconfig(udev)
# Runtime requirement on the udev package itself, not its devel files.
Requires:       udev

%description
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        gui
Summary:        GUI for STM32 discovery line linux programmer
Requires:       %{name} = %{version}

%description    gui
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package -n     libstlink%{sover}
Summary:        Shared library for stlink

%description -n libstlink%{sover}
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        devel
Summary:        Development files for stlink package
Requires:       libstlink%{sover} = %{version}

%description    devel
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%prep
%autosetup -p1

%build
%cmake -DSTLINK_UDEV_RULES_DIR="%{_udevrulesdir}" \
       -DSTLINK_MODPROBED_DIR="%{_modprobedir}" \
       -DCMAKE_EXE_LINKER_FLAGS="-pie"

%cmake_build

%install
%cmake_install

# remove static lib sdi
rm %{buildroot}%{_libdir}/*.a
# Upstream installs a second copy of the shared library into bindir via
# RUNTIME_DEPENDENCY_SET (meant for Windows DLL deployment); drop the
# duplicates, the libdir copies are the packaged ones.
rm %{buildroot}%{_bindir}/libstlink.so*

%suse_update_desktop_file -r stlink-gui Development Debugger

%pre
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" "%{_sysconfdir}/modprobe.d/${_f}.rpmsave.old" || :
done

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" "%{_sysconfdir}/modprobe.d/${_f}" || :
done

%post -n libstlink%{sover} -p /sbin/ldconfig
%postun -n libstlink%{sover} -p /sbin/ldconfig

%files
%doc README.md CHANGELOG.md doc/supported_devices.md doc/tutorial.md doc/flashloaders.md
%license LICENSE.md
%{_bindir}/st-*
%{_udevrulesdir}/49-stlink*
%dir %{_modprobedir}
%{_modprobedir}/stlink_v1.conf
%{_mandir}/man1/st-flash.1%{?ext_man}
%{_mandir}/man1/st-info.1%{?ext_man}
%{_mandir}/man1/st-server.1%{?ext_man}
%{_mandir}/man1/st-util.1%{?ext_man}

%files -n libstlink%{sover}
%{_libdir}/libstlink.so.1*

%files gui
%{_bindir}/stlink-gui
%{_datadir}/stlink/
%{_datadir}/applications/stlink-gui.desktop
%{_datadir}/icons/hicolor/scalable/apps/stlink-gui.svg

%files devel
%dir %{_includedir}/stlink
%{_includedir}/stlink/
%{_libdir}/libstlink.so

%changelog
