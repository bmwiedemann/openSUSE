#
# spec file for package Mesa-demo
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


Name:           Mesa-demo
Version:        8.4.0
Release:        0
Summary:        Mesa demo programs for the OpenGL stack
License:        MIT
Group:          Development/Tools/Other
Url:            http://www.mesa3d.org
Source0:        https://mesa.freedesktop.org/archive/demos/mesa-demos-%{version}.tar.bz2
Source1:        https://mesa.freedesktop.org/archive/demos/mesa-demos-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Obsoletes:      %name-egl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL.* To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc.(SGI). However, the author does not possess an
OpenGL license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI. Those who
want a licensed implementation of OpenGL should contact a licensed
vendor.

Please do not refer to the library as MesaGL (for legal reasons). It's
just Mesa or The Mesa 3-D graphics library.

This package contains the demos shipped with Mesa.

* OpenGL is a trademark of Silicon Graphics Incorporated.

%package x
Summary:        GLX-based demos
Group:          Development/Tools/Other

%description x
This package contains some common GLX-based demos.

%prep
%setup -q -n mesa-demos-%{version} -b0

%build
autoreconf -fi
%configure --bindir=%{_libdir}/mesa-demos/bin \
           --enable-gles1 \
           --enable-gles2
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
cp -r src %{buildroot}%{_libdir}/mesa-demos
find %{buildroot}%{_libdir}/mesa-demos -depth \( -name Makefile\* -o -name .\?\?\* -o -name \*.\[acho] \) -exec rm -rf \{\} +
find %{buildroot}%{_libdir}/mesa-demos -depth -type d -exec rmdir --ignore-fail-on-non-empty \{\} +
find %{buildroot}%{_libdir}/mesa-demos -name \*.py -exec chmod 755 \{\} +
chmod -R go=rX %{buildroot}/usr
mkdir -p %{buildroot}/%{_bindir}
ln -s %{_libdir}/mesa-demos/xdemos/glxgears %{buildroot}/%{_bindir}/glxgears
ln -s %{_libdir}/mesa-demos/xdemos/glxinfo %{buildroot}/%{_bindir}/glxinfo
ln -s %{_libdir}/mesa-demos/xdemos/pbinfo %{buildroot}/%{_bindir}/pbinfo

%files
%defattr(-,root,root)
%{_libdir}/mesa-demos
%exclude %{_libdir}/mesa-demos/xdemos/glxgears
%exclude %{_libdir}/mesa-demos/xdemos/glxinfo
%exclude %{_libdir}/mesa-demos/xdemos/pbinfo

%files x
%defattr(-,root,root)
%dir %{_libdir}/mesa-demos/
%dir %{_libdir}/mesa-demos/xdemos/
%{_libdir}/mesa-demos/xdemos/glxgears
%{_libdir}/mesa-demos/xdemos/glxinfo
%{_libdir}/mesa-demos/xdemos/pbinfo
%{_bindir}/glxgears
%{_bindir}/glxinfo
%{_bindir}/pbinfo

%changelog
