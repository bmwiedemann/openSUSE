#
# spec file for package encfs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Perl-Test-More >= 0.31 is requires by checks but yet not present in SuSE repos
%define do_checks 0

# The cmake macro for distros with cmake 3.3 cannot build encfs
%define use_cmake_macro 1
%if 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100
# Leap 42.1
%define use_cmake_macro 0
%endif
%if 0%{?suse_version} > 1320
%ifarch ppc
%define use_cmake_macro 0
%endif
%endif

# Leap 42.2 and Tumbleweed have tinyxml2-3. For other distribution use the
# tinyxml2-3 that is shipped with encfs.
%define os_has_tinyxml2 0
%if 0%{?leap_version} >= 420200
%ifarch x86_64
%define os_has_tinyxml2 1
%endif
%endif
%if 0%{?suse_version} > 1320
%ifnarch ppc
%define os_has_tinyxml2 1
%endif
%endif

Name:           encfs
Version:        1.9.2
Release:        0
Summary:        Userspace Encrypted File System
License:        GPL-2.0+ and GPL-3.0+
Group:          System/Filesystems
Url:            https://vgough.github.io/encfs/
Source:         https://github.com/vgough/encfs/releases/download/v%{version}/encfs-%{version}.tar.gz
BuildRequires:  cmake >= 3.0.2
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if %{os_has_tinyxml2}
BuildRequires:  tinyxml2-devel
%endif
Requires:       fuse
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     %{name}-lang = %{version}

# requirements for check
%if %{do_checks}
BuildRequires:  fuse
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) => 31
BuildRequires:  perl(Time::HiRes)
%if %{os_has_tinyxml2}
BuildRequires:  libtinyxml2-3
%endif
BuildRequires:  expect
BuildRequires:  openssl
BuildRequires:  zlib
%endif

%description
EncFS provides an encrypted file system, layered on top of a normal
directory tree and encrypts individual files which are stored in the
hosting directory tree.

This has several advantages over the loopback encryption which
provided by the Linux kernel: 
- No space is and has to be reserved, encrypted files only 
  take the space that they really occupy
- Backups: encrypted files can be individually backed-up on the host
  filesystem
- Layering: Since it's hosted on a normal filesystem, encfs can be
  used on filesystems which normally have no support encryption,
  like NFS or other userspace filesystems.

EncFS is implemented as a userspace filesystem in an unprivileged
application using fuse (FUSE (Filesystem in USErspace)).


%lang_package

%prep
%setup 

%build
%if %{use_cmake_macro}
%cmake \
%if %{os_has_tinyxml2}
 -DUSE_INTERNAL_TINYXML:BOOL=OFF
%else
 -DUSE_INTERNAL_TINYXML:BOOL=ON
%endif
%else
mkdir build
cd build
/usr/bin/cmake .. -G"Unix Makefiles" \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
 -DLIB_INSTALL_DIR:PATH=%{_libdir} \
 -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
 -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DCMAKE_C_FLAGS="${CFLAGS:-%optflags} -DNDEBUG" \
 -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags} -DNDEBUG" \
 -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
 -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now" \
 -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now" \
%if "%{?_lib}" == "lib64" 
 -DLIB_SUFFIX=64 \
%endif  
 -DCMAKE_SKIP_RPATH:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DBUILD_SHARED_LIBS:BOOL=ON \
 -DBUILD_STATIC_LIBS:BOOL=OFF \
 -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
 -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
 -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules \
%if %{os_has_tinyxml2}
 -DUSE_INTERNAL_TINYXML:BOOL=OFF
%else
 -DUSE_INTERNAL_TINYXML:BOOL=ON
%endif
%endif

make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install
%__install -d -D -m 0755 %{buildroot}%{_libdir}
cp -a build/libencfs.so.* %{buildroot}%{_libdir}
%if %{os_has_tinyxml2}==0
cp -a build/internal/tinyxml2-3.0.0/libtinyxml2.so.* %{buildroot}%{_libdir}
%endif 
chmod 755 "%{buildroot}%{_bindir}/encfssh"

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
%if %{do_checks} 
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/build:
./test.sh
%endif

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog DESIGN.md PERFORMANCE.md README*
%{_mandir}/man?/*
%{_bindir}/encfs*
%{_libdir}/libencfs.so.*
%if %{os_has_tinyxml2}==0
%{_libdir}/libtinyxml2.so.*
%endif

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
