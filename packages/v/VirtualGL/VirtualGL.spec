#
# spec file for package VirtualGL
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


Name:           VirtualGL
Version:        3.1
Release:        0
Summary:        A toolkit for displaying OpenGL applications to thin clients
License:        LGPL-2.1-only AND SUSE-wxWidgets-3.1
Group:          Productivity/Networking/Other
URL:            http://www.virtualgl.org
Source0:        https://sourceforge.net/projects/virtualgl/files/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         VirtualGL-link-libs.patch
BuildRequires:  Mesa-devel
BuildRequires:  Mesa-libGLU-devel
BuildRequires:  cmake
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libjpeg-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)

%description
VirtualGL is a library which allows most Linux OpenGL applications to be
remotely displayed to a thin client without the need to alter the
applications in any way.  VGL inserts itself into an application at run time
and intercepts a handful of GLX calls, which it reroutes to the server's
display (which presumably has a 3D accelerator attached.)  This causes all
3D rendering to occur on the server's display.  As each frame is rendered
by the server, VirtualGL reads back the pixels from the server's framebuffer
and sends them to the client for re-compositing into the appropriate X
Window.  VirtualGL can be used to give hardware-accelerated 3D capabilities to
VNC or other remote display environments that lack GLX support.  In a LAN
environment, it can also be used with its built-in motion-JPEG video delivery
system to remotely display full-screen 3D applications at 20+ frames/second.

VirtualGL is based upon ideas presented in various academic papers on
this topic, including "A Generic Solution for Hardware-Accelerated Remote
Visualization" (Stegmaier, Magallon, Ertl 2002) and "A Framework for
Interactive Hardware Accelerated Remote 3D-Visualization" (Engel, Sommer,
Ertl 2000.)

%package devel
Summary:        A toolkit for displaying OpenGL applications to thin clients
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
VirtualGL is a library which allows most Linux OpenGL applications to be
remotely displayed to a thin client without the need to alter the
applications in any way.  VGL inserts itself into an application at run time
and intercepts a handful of GLX calls, which it reroutes to the server's
display (which presumably has a 3D accelerator attached.)  This causes all
3D rendering to occur on the server's display.  As each frame is rendered
by the server, VirtualGL reads back the pixels from the server's framebuffer
and sends them to the client for re-compositing into the appropriate X
Window.  VirtualGL can be used to give hardware-accelerated 3D capabilities to
VNC or other remote display environments that lack GLX support.  In a LAN
environment, it can also be used with its built-in motion-JPEG video delivery
system to remotely display full-screen 3D applications at 20+ frames/second.

VirtualGL is based upon ideas presented in various academic papers on
this topic, including "A Generic Solution for Hardware-Accelerated Remote
Visualization" (Stegmaier, Magallon, Ertl 2002) and "A Framework for
Interactive Hardware Accelerated Remote 3D-Visualization" (Engel, Sommer,
Ertl 2000.)

%prep
%autosetup -p1

# Use /var/lib
sed -e "s#%{_sysconfdir}/opt#%{_localstatedir}/lib#g" \
    -i doc/unixconfig.txt doc/index.html \
    -i doc/advancedopengl.txt \
    -i server/vglrun.in \
    -i server/vglgenkey \
    -i server/vglserver_config

%build
%cmake \
    -DVGL_SYSTEMFLTK=ON \
    -DVGL_SYSTEMGLX=ON \
    -DVGL_SYSTEMXCB=ON \
    -DVGL_USESSL=OFF \
    -DVGL_USEXV=ON \
    -DTJPEG_INCLUDE_DIR=%{_includedir} \
    -DVGL_LIBDIR=%{_libdir} \
    -DTJPEG_LIBRARY=%{_libdir}/libturbojpeg.so \
    -DCMAKE_LIBRARY_PATH=%{_libdir}
make %{?_smp_mflags}

%install
%cmake_install
# Fix placement of 64b glxspheres
%ifarch x86_64 s390x ppc64 ppc64le aarch64 riscv64
mv %{buildroot}%{_bindir}/glxspheres* %{buildroot}%{_bindir}/glxspheres
mv %{buildroot}%{_bindir}/eglxspheres* %{buildroot}%{_bindir}/eglxspheres
%endif
# Fix fakelib placement
rm -rf %{buildroot}%{_prefix}/fakelib
mkdir -p %{buildroot}%{_libdir}/fakelib
ln -sf ../libvglfaker.so %{buildroot}%{_libdir}/fakelib/libGL.so
# Docs had wrong names
chmod 644 doc/LGPL.txt doc/LICENSE.txt doc/index.html doc/*.png doc/*.gif doc/*.css
rm -rf %{buildroot}%{_datadir}/doc
mv -f %{buildroot}%{_bindir}/glxinfo %{buildroot}%{_bindir}/vglxinfo
mv -f %{buildroot}%{_bindir}/eglinfo %{buildroot}%{_bindir}/veglinfo
mv -f %{buildroot}%{_bindir}/eglxinfo %{buildroot}%{_bindir}/veglxinfo
# bsc#1097210 rely on env settings
rm -rf %{buildroot}/%{_bindir}/.vglrun.*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LGPL.txt LICENSE.txt ChangeLog.md doc/index.html doc/legalinfo.txt doc/*.png doc/*.gif doc/*.css
%dir %{_libdir}/fakelib
%{_bindir}/tcbench
%{_bindir}/nettest
%{_bindir}/cpustat
%{_bindir}/veglinfo
%{_bindir}/vglxinfo
%{_bindir}/veglxinfo
%{_bindir}/glxspheres
%{_bindir}/eglxspheres
%{_bindir}/vglclient
%{_bindir}/vglconfig
%{_bindir}/vglconnect
%{_bindir}/vglgenkey
%{_bindir}/vgllogin
%{_bindir}/vglserver_config
%{_bindir}/vglrun
%{_bindir}/glreadtest
%{_libdir}/fakelib/libGL.so
%{_libdir}/libvglfaker.so
%{_libdir}/libdlfaker.so
%{_libdir}/libvglfaker-nodl.so
%{_libdir}/libvglfaker-opencl.so
%{_libdir}/libgefaker.so

%files devel
%{_includedir}/rrtransport.h
%{_includedir}/rr.h

%changelog
