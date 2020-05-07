#
# spec file for package LibVNCServer
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


%define libnum  1
Name:           LibVNCServer
Version:        0.9.12
Release:        0
Summary:        VNC Development Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/X11
URL:            https://github.com/LibVNC/libvncserver
# Archive is renamed by github
Source0:        https://github.com/LibVNC/libvncserver/archive/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
#PATCH-FIX-OPENSUSE: redefine keysyms only if needed
Patch0:         redef-keysym.patch
# https://github.com/LibVNC/libvncserver/issues/281
Patch1:         cmake-libdir.patch
# CVE-2019-15681 [bsc#1155419]
Patch3:         LibVNCServer-CVE-2019-15681.patch
# PATCH-FIX-UPSTREAM: https://github.com/LibVNC/libvncserver/commit/d0a76539835d11c0f4723499f8be4bc9c7724eb9
Patch4:         avoid-pthread_join-if-backgroundLoop-is-FALSE.patch
# PATCH-FIX-UPSTREAM: https://github.com/LibVNC/libvncserver/pull/361
Patch5:         fix-crash-on-shutdown.patch
# CVE-2019-20788 [bsc#1170441], integer overflow and heap-based buffer overflow via a large height or width value
Patch6:         LibVNCServer-CVE-2019-20788.patch
# CVE-2019-15690 [bsc#1160471], heap buffer overflow
Patch7:         LibVNCServer-CVE-2019-15690.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libavahi-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  lzo-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  slang-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
VNC is a set of programs using the RFB (Remote Frame Buffer) protocol.
They are designed to "export" a frame buffer via the network. It is
already in wide use for administration, but it is not that easy to
program a server yourself. This has been changed by LibVNCServer.

X.org already has a virtual Xvnc server which you can start as an own
screen (e.g. :1) and connect to with a VNC client (e.g. vncviewer from
tightvnc). The x11vnc binary (that allows you to export the window of a
real running X11 server) has been split off into its own package on
2007-07-16.

%package -n libvncclient%{libnum}
Summary:        Library implementing a VNC client
Group:          System/Libraries
Obsoletes:      linuxvnc < %{version}
Conflicts:      LibVNCServer < %version

%description -n libvncclient%{libnum}
LibVNCServer/LibVNCClient are cross-platform C libraries that allow
implementing VNC server or client functionality in your program.

%package -n libvncserver%{libnum}
Summary:        Library implementing a VNC server
Group:          System/Libraries

%description -n libvncserver%{libnum}
LibVNCServer/LibVNCClient are cross-platform C libraries that allow
implementing VNC server or client functionality in your program.

%package devel
Requires:       gnutls-devel
Requires:       libvncclient%{libnum} = %version
Requires:       libvncserver%{libnum} = %version
Requires:       zlib-devel
Summary:        VNC Development Library
Group:          Development/Libraries/X11

%description devel
VNC is a set of programs using the RFB (Remote Frame Buffer) protocol.
They are designed to "export" a frame buffer via the network. It is
already in wide use for administration, but it is not that easy to
program a server yourself. This has been changed by LibVNCServer.

X.org already has a virtual Xvnc server which you can start as an own
screen (e.g. :1) and connect to with a VNC client (e.g. vncviewer from
tightvnc).

The LibVNCServer-devel package contains the static libraries and header
files for LibVNCServer.

%prep
%setup -q -n libvncserver-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
# fix encoding
for file in ChangeLog ; do
mv ${file} ${file}.OLD && \
iconv -f ISO_8859-1 -t UTF8 ${file}.OLD > ${file} && \
touch --reference ${file}.OLD $file 
done

%build
%cmake
make %{?_smp_mflags}

%check 
pushd build
export LD_LIBRARY_PATH="$(pwd)"
make test

%install
%cmake_install

%post   -n libvncclient%{libnum} -p /sbin/ldconfig
%postun -n libvncclient%{libnum} -p /sbin/ldconfig
%post   -n libvncserver%{libnum} -p /sbin/ldconfig
%postun -n libvncserver%{libnum} -p /sbin/ldconfig

%files -n libvncserver%{libnum}
%defattr(-,root,root)
%doc COPYING README.md
%_libdir/libvncserver.so.%{version}
%_libdir/libvncserver.so.%{libnum}*

%files -n libvncclient%{libnum}
%defattr(-,root,root)
%doc COPYING README.md
%_libdir/libvncclient.so.%{version}
%_libdir/libvncclient.so.%{libnum}*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README.md TODO
%{_includedir}/rfb/*
%dir /usr/include/rfb
%{_libdir}/libvncclient.so
%{_libdir}/libvncserver.so
%{_libdir}/pkgconfig/*.pc

%changelog
