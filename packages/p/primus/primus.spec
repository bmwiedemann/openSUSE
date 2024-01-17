#
# spec file for package primus
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


Name:           primus
Version:        0+git20150328.d1afbf6
Release:        0
Summary:        Faster OpenGL offloading for Bumblebee
License:        HPND
Group:          Hardware/Other
Url:            https://github.com/amonakov/primus
Source0:        %{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch0:         primusrun-bsc1061561.diff
BuildRequires:  Mesa-libGL-devel
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  unzip
Requires:       bumblebee
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Primus is a shared library that provides OpenGL and GLX APIs and
implements low-overhead local-only client-side OpenGL offloading via GLX
forking, similar to VirtualGL. It intercepts GLX calls and redirects GL
rendering to a secondary X display, presumably driven by a faster GPU.
On swapping buffers, rendered contents are read back using a PBO and
copied onto the drawable it was supposed to be rendered on in the first
place.

%prep
%setup -q
%patch0 -p1 

%build
export CXXFLAGS="%{optflags}"
export PRIMUS_libGLd=%{_libdir}/primus/libGL.so.1
export PRIMUS_libGLa=%{_libdir}/primus/libGL.so.1
make %{?_smp_mflags}

%install
install -D lib/libGL.so.1 "%{buildroot}%{_libdir}/primus/libGL.so.1"
install -D primusrun "%{buildroot}%{_bindir}/primusrun"

%files
%defattr(-,root,root)
%doc LICENSE.txt README.md
%{_libdir}/primus
%{_libdir}/primus/libGL.so.1
%{_bindir}/primusrun

%changelog
