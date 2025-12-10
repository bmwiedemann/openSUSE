#
# spec file for package evdi
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _dllibdir %{_libdir}/displaylink
%define lname   libevdi1

Name:           evdi
Release:        0
Version:        1.14.11
Summary:        Extensible Virtual Display Interface (EVDI) is a Linux Kernel Module
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          System/Kernel
URL:            https://github.com/DisplayLink/evdi
Source0:        evdi-%{version}.tar.gz
Source1:        evdi-kmp-preamble
Source2:        evdi-rpmlintrc
Patch0:         buildfix.patch
Patch1:         0001-Support-Linux-v6.18-No-need-to-lock-in-drm_gem_looku.patch
Patch2:         0002-Support-Linux-v6.18-Lock-on-dev-struct_mutex-unneces.patch
Patch3:         0003-Support-Linux-v6.18-Remove-lock-on-device-struct_mut.patch
Patch4:         0004-fix-README-Outdated-link-to-AUR-package.patch
Patch5:         0005-Fix-building-on-EL-10-kernels.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  pesign-obs-integration
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm)
# needssslcertforbuild
%kernel_module_package -p %{_sourcedir}/evdi-kmp-preamble

%description
The Extensible Virtual Display Interface (EVDI) is a Linux kernel module
that enables management of multiple screens, allowing user-space programs
to take control over what happens with the image. It is essentially
a virtual display you can add, remove and receive screen updates for, in
an application that uses the libevdi library.

%package -n %{lname}
Summary:        LibEVDI Library
Group:          System/Libraries
Requires:       evdi-kmp

%description -n %{lname}
The Extensible Virtual Display Interface (EVDI) is a Linux kernel module
that enables management of multiple screens, allowing user-space programs
to take control over what happens with the image. It is essentially
a virtual display you can add, remove and receive screen updates for, in
an application that uses the libevdi library.

%package devel
Summary:        Development files for libevdi Library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The Extensible Virtual Display Interface (EVDI) is a Linux kernel module
that enables management of multiple screens, allowing user-space programs
to take control over what happens with the image. It is essentially
a virtual display you can add, remove and receive screen updates for, in
an application that uses the libevdi library.

%prep
%autosetup -p 1

%build
pushd library
%make_build
mv LICENSE LICENSE.library
popd

pushd module
sed -i 's:/kernel/drivers/gpu/drm/evdi:/extra:' Makefile
mv LICENSE LICENSE.module
set -- *
mkdir source
mv "$@" source/
mkdir obj
for flavor in %flavors_to_build; do
       rm -rf obj/$flavor
       cp -r source obj/$flavor
       make %{?_smp_mflags} -C /usr/src/linux-obj/%_target_cpu/$flavor M=$PWD/obj/$flavor \
       modules
done

%install
export BRP_PESIGN_FILES="*.ko"
pushd library
%make_install PREFIX=%{_prefix} LIBDIR=%{_dllibdir}
install -m644 -D evdi_lib.h %{buildroot}%{_includedir}/%{name}/evdi_lib.h
popd

pushd module
for flavor in %flavors_to_build; do
       make -C  /usr/src/linux-obj/%_target_cpu/$flavor M=$PWD/obj/$flavor \
       INSTALL_MOD_PATH=%{buildroot} \
       INSTALL_MOD_DIR=/extra \
       modules_install
done

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license {library,module/source}/LICENSE.*
%doc README.md docs

%files -n %{lname}
%dir %{_dllibdir}
%{_dllibdir}/libevdi.so
%{_dllibdir}/libevdi.so.1*

%files devel
%{_includedir}/%{name}

%changelog
