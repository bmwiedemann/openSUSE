#
# spec file for package xstereograph
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


Name:           xstereograph
BuildRequires:  libpng-devel
BuildRequires:  xaw3d-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
%define		version_libsx 2.03
Summary:        Stereogram generator
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Amusements/Games/Other
Requires:       ImageMagick
Requires:       emacs-x11
Requires:       xless
Version:        2.1
Release:        0
Url:            http://freshmeat.net/projects/xstereograph/
Source0:        %{name}-%{version}.tar.bz2
Source1:        libsx-%{version_libsx}.tar.bz2
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-ia64.patch
Patch2:         %{name}-%{version}-strings.patch
Patch3:         %{name}-%{version}-dialogs.patch
Patch4:         %{name}-%{version}-gcc4.patch
Patch5:         %{name}-%{version}-uninitialized.patch
# libpng15.patch not sent to upstream (is project alive?)
Patch6:         %{name}-%{version}-libpng15.patch
# libpng16.patch not sent to upstream (is project alive?)
Patch7:         %{name}-%{version}-libpng16.patch
Patch8:         trunc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Stereograph is a stereogram generator. In detail it is a single image
stereogram (SIS) generator. That's a program that produces
two-dimensional images that seem to be three-dimensional (surely you
know the famous works of "The Magic Eye", Stereograph produces the same
output). You do _not_ need any pair of colored spectacles to regard
them - everyone can learn it.



Authors:
--------
    fabian.linux@januszewski.de
    demailly@fourier.ujf-grenoble.fr

%prep
%setup -q -a 1
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8 -p0

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
#
# libsx
cd libsx-%{version_libsx}/src
make
cd ../..
#
# xstereograph
make X11_LIBDIR=/usr/%{_lib}

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -d -m 755 $RPM_BUILD_ROOT/usr/share/xstereograph/
cp -r depth_maps textures mathfiles magic-eye.xpm stereo_dia.png \
      $RPM_BUILD_ROOT/usr/share/xstereograph/      
#
# documentation
install -d -m 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/
install -m 644 AUTHORS COPYING README $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/
#
# documentation stereograph
cd stereograph-0.28a
install -d -m 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/stereograph/
install -m 644 AUTHORS COPYING INSTALL README TODO \
	       $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/stereograph/
cd ..
#
# libsx
cd libsx-%{version_libsx}/src
make DESTDIR=$RPM_BUILD_ROOT \
     LIBDIR=%{_libdir} \
     INCLUDEDIR=%{_includedir}/SX \
     SHAREDIR=%{_datadir}/libsx \
     install
#
# libsx documentation
cd ..
install -d -m 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/libsx/
install -m 644 CHANGES HELP HINTS LICENSE README \
               $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/libsx/
cd ..
%{__rm} -f %{buildroot}%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}/
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_includedir}/SX
%{_datadir}/xstereograph
%{_datadir}/libsx
%{_libdir}/lib*

%changelog
