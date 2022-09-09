#
# spec file for package LibVNCServer
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


%define libnum  1
Name:           LibVNCServer
Version:        0.9.13
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
#PATCH-FEATURE-UPSTREAM TLS security type enablement patches gh#LibVNC/libvncserver!234
Patch10:        0001-libvncserver-Add-API-to-add-custom-I-O-entry-points.patch
Patch11:        0002-libvncserver-Add-channel-security-handlers.patch
# https://github.com/LibVNC/libvncserver/commit/87c52ee0551b7c4e76855d270d475b9e3039fe08
Patch12:        0003-libvncserver-auth-don-t-keep-security-handlers-from-.patch
# PATCH-FIX-UPSTREAM Fix crash on all runs after the first gh#LibVNC/libvncserver!444 rh#1882718
Patch13:        0004-zlib-Clear-buffer-pointers-on-cleanup-444.patch
# PATCH-FIX-UPSTREAM Fix another crasher glgo#GNOME/gnome-remote-desktop#45 rh#1882718
Patch14:        0001-libvncserver-don-t-NULL-out-internal-of-the-default-.patch
# CVE-2020-29260 [bsc#1203106], memory leakage via rfbClientCleanup()
Patch15:        LibVNCServer-CVE-2020-29260.patch
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
%autopatch -p1

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
%doc AUTHORS COPYING ChangeLog NEWS.md README.md TODO.md
%{_includedir}/rfb/*
%dir /usr/include/rfb
%{_libdir}/libvncclient.so
%{_libdir}/libvncserver.so
%{_libdir}/pkgconfig/*.pc

%changelog
