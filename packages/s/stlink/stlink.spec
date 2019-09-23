#
# spec file for package stlink
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           stlink
Version:        1.5.0
Release:        0
Summary:        STM32 discovery line linux programmer
License:        BSD-3-Clause
Group:          Development/Tools/Debuggers
Url:            https://github.com/texane/stlink
Source0:        https://github.com/texane/stlink/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-deprecated-libusb-function.patch
Patch0:         https://github.com/texane/stlink/commit/aaf8e9207581.patch#/fix-deprecated-libusb-function.patch
BuildRequires:  cmake
BuildRequires:  gtk3-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  udev
BuildRequires:  pkgconfig(libusb-1.0)
Requires:       udev
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        gui
Summary:        GUI for STM32 discovery line linux programmer
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}

%description    gui
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package -n     libstlink-shared1
Summary:        Shared library for stlink
Group:          Development/Tools/Debuggers

%description -n libstlink-shared1
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        devel
Summary:        Development files for stlink package
#Requires:      %%{name} = %%{version}
Group:          Development/Tools/Debuggers
Requires:       libstlink-shared1 = %{version}

%description    devel
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%prep
%setup -q
%patch0 -p1

%build
%cmake -DSTLINK_UDEV_RULES_DIR="%_udevrulesdir" \
       -DCMAKE_EXE_LINKER_FLAGS="-pie"

make %{?_smp_mflags}

%install
%cmake_install
# remove static lib sdi
rm -f %{buildroot}%{_libdir}/*.a
install -d %{buildroot}/%{_udevrulesdir}/
install -D -m 0644 etc/udev/rules.d/49-stlink*.rules %{buildroot}/%{_udevrulesdir}/

%post -n libstlink-shared1 -p /sbin/ldconfig

%postun -n libstlink-shared1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE README.md doc/app-example doc/tested-boards.md doc/tutorial.md
%{_bindir}/st-*
%{_udevrulesdir}/49-stlink*
%config %{_sysconfdir}/modprobe.d/stlink_v1.conf
%{_mandir}/man1/st-flash.1*
%{_mandir}/man1/st-info.1*
%{_mandir}/man1/st-util.1*

%files -n libstlink-shared1
%{_libdir}/libstlink-shared.so.1*

%files gui
%defattr(-,root,root)
%{_bindir}/stlink-gui
%{_datadir}/stlink/

%files devel
%dir %{_includedir}/stlink
%{_includedir}/stlink.h
%{_includedir}/stlink/backend.h
%{_includedir}/stlink/chipid.h
%{_includedir}/stlink/commands.h
%{_includedir}/stlink/flash_loader.h
%{_includedir}/stlink/logging.h
%{_includedir}/stlink/mmap.h
%{_includedir}/stlink/reg.h
%{_includedir}/stlink/sg.h
%{_includedir}/stlink/usb.h
%{_includedir}/stlink/version.h
%{_libdir}/libstlink-shared.so
%{_libdir}/pkgconfig/stlink.pc

%changelog
