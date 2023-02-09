#
# spec file for package kernelshark
#
# Copyright (c) 2023 SUSE LLC
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


Name:           kernelshark
Version:        2.2.0
Release:        0
Summary:        Visualisation tool for trace-cmd data
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Tools/Debuggers
URL:            https://git.kernel.org/pub/scm/utils/trace-cmd/kernel-shark.git
Source0:        kernelshark-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  freeglut-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libtracecmd-devel
BuildRequires:  libtraceevent-devel
BuildRequires:  libtracefs-devel
BuildRequires:  trace-cmd >= 3.1.0
Recommends:     trace-cmd

%description
trace-cmd reporting can be extremely verbose making it difficult to
analyse. kernelshark visualises the data so that it can be filtered
or trimmed.

%package devel
Summary:        Development files for kernelshark
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for kernelshark

%prep
%autosetup -p1

%build
# We would like to use _ttfontsdir macro but somehow the expension
# doesn't seem to work
%define fontname %{_datadir}/fonts/truetype/FreeSans.ttf

# The upstream project decided it is a good idea to have a directory
# called build with build script. The cmake macro expects to be able
# to create and use a directory called build. This leads to complete
# broken configuration. For the time being let's expand the relavent
# parts of the cmake macro by hand until it is fixed in upstream.
cmake \
    -DTT_FONT_FILE:PATH=%{fontname} \
    -D_INSTALL_PREFIX:PATH=%{_prefix} \
    -D_LIBDIR:PATH=%{_libdir} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_C_FLAGS="${CFLAGS:-%optflags}" \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags}" \
    -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now" \
%if "%{?_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
%if %suse_version <= 1500
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
%endif
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DPKG_CONGIG_DIR=%{_libdir}/pkgconfig

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{_datadir}/polkit-1
sed -i -e 's/^Categories=.*/Categories=Development;Profiling/' %{buildroot}/%{_datadir}/applications/kernelshark.desktop
sed -i -e 's/^Version=1.5/Version=1.0/' %{buildroot}/%{_datadir}/applications/kernelshark.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/kernelshark
%{_bindir}/kshark-*
%{_libdir}/kernelshark
%{_libdir}/libkshark*.so.*
%{_datadir}/applications/kernelshark.desktop
%{_datadir}/icons/kernelshark
%license LICENSES/GPL-2.0
%license LICENSES/LGPL-2.1
%doc README

%files devel
%{_libdir}/libkshark*.so
%{_includedir}/kernelshark
%{_libdir}/pkgconfig/*.pc

%changelog
