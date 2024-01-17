#
# spec file for package physfs
#
# Copyright (c) 2022 SUSE LLC
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


%define so_nr 1
Name:           physfs
Version:        3.2.0
Release:        0
Summary:        PhysicsFS file abstraction layer for games
License:        (CPL-1.0 OR LGPL-2.1-or-later) AND Zlib
Group:          System/Libraries
URL:            https://www.icculus.org/physfs/
Source:         https://github.com/icculus/physfs/archive/refs/tags/release-%{version}.tar.gz
BuildRequires:  cmake >= 3.0.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
PhysicsFS is a library to provide abstract access to various archives.
It is intended for use in video games, and the design was somewhat
inspired by Quake 3's file subsystem. The programmer defines a "write
directory" on the physical filesystem. No file writing done through the
PhysicsFS API can leave that write directory, for security. For
example, an embedded scripting language cannot write outside of this
path if it uses PhysFS for all of its I/O, which means that untrusted
scripts can run more safely. Symbolic links can be disabled as well,
for added safety. For file reading, the programmer lists directories
and archives that form a "search path". Once the search path is
defined, it becomes a single, transparent hierarchical filesystem. This
makes for easy access to ZIP files in the same way as you access a file
directly on the disk, and it makes it easy to ship a new archive that
will override a previous archive on a per-file basis. Finally,
PhysicsFS gives you platform-abstracted means to determine if CD-ROMs
are available, the user's home directory, where in the real filesystem
your program is running, etc.

%package -n lib%{name}%{so_nr}
Summary:        PhysicsFS file abstraction layer for games
# physfs was last used in openSUSE 11.3
Group:          System/Libraries
Provides:       physfs = %{version}
Obsoletes:      physfs <= 1.0.1

%description -n lib%{name}%{so_nr}
PhysicsFS is a library to provide abstract access to various archives.
It is intended for use in video games, and the design was somewhat
inspired by Quake 3's file subsystem. The programmer defines a "write
directory" on the physical filesystem. No file writing done through the
PhysicsFS API can leave that write directory, for security. For
example, an embedded scripting language cannot write outside of this
path if it uses PhysFS for all of its I/O, which means that untrusted
scripts can run more safely. Symbolic links can be disabled as well,
for added safety. For file reading, the programmer lists directories
and archives that form a "search path". Once the search path is
defined, it becomes a single, transparent hierarchical filesystem. This
makes for easy access to ZIP files in the same way as you access a file
directly on the disk, and it makes it easy to ship a new archive that
will override a previous archive on a per-file basis. Finally,
PhysicsFS gives you platform-abstracted means to determine if CD-ROMs
are available, the user's home directory, where in the real filesystem
your program is running, etc.

%package -n lib%{name}-devel
Summary:        Libraries, includes and more to develop PhysicsFS applications
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{so_nr} = %{version}
# physfs-devel was last used in openSUSE 11.3
Provides:       physfs-devel = %{version}
Obsoletes:      physfs-devel <= 1.0.1

%description -n lib%{name}-devel
Development package for libphysfs, a library to provide abstract access to
various archives.

%prep
%setup -q -n physfs-release-%{version}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DPHYSFS_BUILD_STATIC=FALSE \
  -DPHYSFS_BUILD_TEST=FALSE
%make_build

%install
%cmake_install

install -d %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=\${prefix}
libdir=\${exec_prefix}/%{_lib}
includedir=\${prefix}/include

Name:           PhysicsFS
Description: PhysicsFS, a library to provide abstract access to various archives
URL:            %{url}
Version:        %{version}
Libs: -L\${libdir} -lphysfs
Cflags: -I\${includedir}
EOF

%post -n lib%{name}%{so_nr} -p /sbin/ldconfig
%postun -n lib%{name}%{so_nr} -p /sbin/ldconfig

%files -n lib%{name}%{so_nr}
%defattr(0644,root,root,0755)
%license LICENSE.txt
%doc docs/CREDITS.txt docs/INSTALL.txt docs/TODO.txt
%{_libdir}/libphysfs.so.%{so_nr}
%{_libdir}/libphysfs.so.%{version}

%files -n lib%{name}-devel
%defattr(0644,root,root,0755)
%{_libdir}/libphysfs.so
%{_includedir}/physfs.h
%{_libdir}/cmake/PhysFS
%{_libdir}/pkgconfig/%{name}.pc

%changelog
