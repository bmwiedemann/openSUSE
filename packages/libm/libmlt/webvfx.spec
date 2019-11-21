#
# spec file for package webvfx
#
# Copyright (c) 2019 SUSE LLC.
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


%define _name mlt
%define mltversion 6.18.0
%define mltsoversion 6.18.0
%define sover 1
%define mltmaj %(echo %{mltversion} |cut -d "." -f 1)
# Find qt version used to build
%define qt5version %(pkg-config --modversion Qt5Core)
Name:           webvfx
Version:        1.1.0
Release:        0
Summary:        Video effects engine based on web technologies
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/mltframework/webvfx
Source0:        %{_name}-%{mltversion}.tar.gz
# This is needed by shotcut and will only build within the mlt sources.
Source1:        https://github.com/mltframework/webvfx/archive/%{version}.tar.gz#/webvfx-%{version}.tar.gz
# PATCH-FIX-OPENSUSE libmlt-0.8.2-vdpau.patch reddwarf@opensuse.org -- Make VDPAU support work without the devel package
Patch1:         libmlt-0.8.2-vdpau.patch
#PATCH-FIX-UPSTREAM webvfx-versioned-libdir.patch davejplater@gmail.com -- install webvfx lib in versioned _libdir
Patch10:        webvfx-versioned-libdir.patch
Patch11:        webvfx-nobrowser.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(mlt++)
BuildRequires:  pkgconfig(mlt-framework)

%description
WebVfx is a video effects library that allows effects to be
implemented using WebKit HTML or Qt QML.

%package -n libwebvfx%{sover}
Summary:        Video effects engine based on web technologies
Group:          System/Libraries

%description -n libwebvfx%{sover}
WebVfx is a video effects library that allows effects to be
implemented using WebKit HTML or Qt QML.

%package devel
Summary:        Video effects engine based on web technologies
Group:          Development/Libraries/C and C++
Requires:       libwebvfx%{sover} = %{version}
Requires:       pkgconfig(mlt-framework) = %{mltsoversion}

%description devel
WebVfx is a video effects library that allows effects to be
implemented using WebKit HTML or Qt QML. This package contains
the development library link.

%package module
Summary:        Webvfx module for MLT
Group:          Productivity/Multimedia/Video/Editors and Convertors

%description module
A module plugin for the MLT multimedia framework.

%package -n qmelt
Summary:        A Melt that works with webvfx
Group:          Productivity/Multimedia/Video/Editors and Convertors

%description -n qmelt
MLT is a multimedia framework, designed and developed for television
broadcasting. It provides a toolkit for broadcasters, video editors,
media players, transcoders, web streamers and many more types of
applications. The functionality of the system is provided via an
assortment of tools, XML authoring components, and an plug-in based API.

%prep
%setup -q -n %{_name}-%{mltversion} -a 1
%autopatch -p0

%build
pushd webvfx-%{version}
%qmake5 \
	QMAKE_STRIP="" \
	MLT_SOURCE="%{_builddir}/%{_name}-%{mltversion}/" \
	WLIB=%{_lib} \
        PREFIX="%{_prefix}" -Wall -recursive

make VERBOSE=1 %{?_smp_mflags}
popd

%install
pushd webvfx-%{version}
%qmake5_install
chmod 0644 LICENSE README.md
popd
#Add webvfx module to versioned mlt module directory
mv %{buildroot}%{_libdir}/mlt %{buildroot}%{_libdir}/mlt-%{mltmaj}
chmod 0755 %{buildroot}%{_bindir}/*
#Create man pages for executables.
mkdir -p %{buildroot}%{_mandir}/man1
pushd %{buildroot}%{_bindir}
for i in *; do
	help2man -N --no-discard-stderr -h "-help" -v "-version" ./${i} -o %{buildroot}%{_mandir}/man1/${i}.1 || touch %{buildroot}%{_mandir}/man1/${i}.1
done
popd

%post -n libwebvfx%{sover} -p /sbin/ldconfig
%postun -n libwebvfx%{sover} -p /sbin/ldconfig

%files
%{_bindir}/webvfx*
%{_mandir}/man1/webvfx*
%license webvfx-%{version}/LICENSE
%doc webvfx-%{version}/README.md

%files module
%defattr(0755, root, root, 0755)
%{_libdir}/mlt-%{mltmaj}/

%files -n libwebvfx%{sover}
%defattr(0755, root, root, 0755)
%{_libdir}/libwebvfx.so.*

%files devel
%defattr(0755, root, root, 0755)
%{_libdir}/libwebvfx.so

%files -n qmelt
%{_bindir}/qmelt
%{_mandir}/man1/qmelt*

%changelog
