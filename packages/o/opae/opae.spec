#
# spec file for package opae
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


%define git_ver .0.c83632afa605
%define lib_opae_major 0
%define lib_hssi_major 0

Name:           opae
Version:        0.13.0
Release:        0
Summary:        Open Programmable Acceleration Engine
License:        Intel OR MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/OPAE/opae-sdk
Source0:        %{name}-%{version}%{git_ver}.tar.bz2
Patch0:         opae-add-missing-lpthread.patch
Patch1:         opae-fix-cmake-paths.patch
Patch2:         opae-missing-shebang.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libjson-c-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
#Currently *only* builds on x86_64
ExclusiveArch:  x86_64
Requires:       libhssi-io%{lib_hssi_major} = %{version}
Requires:       libopae-c%{lib_opae_major} = %{version}

%description
OPAE is the Open Programmable Acceleration Engine, a software framework for
managing and accessing programmable accelerators (FPGAs).

The OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.

%package        devel
Summary:        Development files for OPAE SDK
Group:          Development/Libraries/C and C++
Requires:       opae = %{version}

%description    devel
OPAE is the Open Programmable Acceleration Engine, a software framework for
managing and accessing programmable accelerators (FPGAs).

The OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.
This package contains the development files.

%package -n libopae-c%{lib_opae_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libopae-c%{lib_opae_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.


%package -n libhssi-io%{lib_hssi_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libhssi-io%{lib_hssi_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%prep
%setup -q -n %{name}-%{version}%{git_ver}
%patch0
%patch1
%patch2

%build
export RPM_OPT_FLAGS
%cmake	 -DCMAKE_BUILD_TYPE=Release

make VERBOSE=1 all %{?_smp_mflags}

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libsafestr.a
rm -Rf %{buildroot}%{_includedir}/safe_string

%post   -n libopae-c%{lib_opae_major} -p /sbin/ldconfig
%postun -n libopae-c%{lib_opae_major} -p /sbin/ldconfig
%post   -n libhssi-io%{lib_hssi_major} -p /sbin/ldconfig
%postun -n libhssi-io%{lib_hssi_major} -p /sbin/ldconfig

%files
%{_bindir}/*
%license COPYING RELEASE_NOTES

%files devel
%{_includedir}/opae
%{_libdir}/*.so
%dir %{_datarootdir}/opae
%{_datarootdir}/opae/hello_fpga.c
%{_datarootdir}/opae/hello_events.c
%{_datarootdir}/opae/platform

%files -n libopae-c%{lib_opae_major}
%{_libdir}/libopae-c*.so.%{lib_opae_major}
%{_libdir}/libopae-c*.so.%{lib_opae_major}.*

%files -n libhssi-io%{lib_hssi_major}
%{_libdir}/libhssi-io*.so.%{lib_hssi_major}
%{_libdir}/libhssi-io*.so.%{lib_hssi_major}.*

%changelog
