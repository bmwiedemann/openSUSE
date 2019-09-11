#
# spec file for package vegastrike
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


Name:           vegastrike
Version:        0.5.1.r1
Release:        0
Summary:        3D OpenGL spaceflight simulator
License:        GPL-2.0+
Group:          Amusements/Games/3D/Simulation
Url:            http://vegastrike.sourceforge.net/
Source0:        http://master.dl.sourceforge.net/project/%{name}/%{name}/0.5.1/%{name}-src-%{version}.tar.bz2
# Found in the mandriva srpm, origin Debian ?
Source1:        %{name}-manpages.tar.bz2
Source2:        %{name}-wrapper.sh
# PATCH-FIX-OPENSUSE vegastrike-0.4.2-vssetup-fix.patch
Patch0:         vegastrike-0.4.2-vssetup-fix.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-r13353-r13354.patch -- fix music reproduction, already upstreamed, not yet in tarball
Patch1:         vegastrike-src-0.5.1.r1-r13353-r13354.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-license.patch -- update FSF address, already upstreamed, not yet in tarball
Patch2:         vegastrike-src-0.5.1.r1-license.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-gcc47_compat.patch -- GCC 4.7 compatibility fixes, already upstreamed, not yet in tarball
Patch3:         vegastrike-src-0.5.1.r1-gcc47_compat.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-r13498-al_fix.patch -- fix build without openAL (SLE)
Patch4:         vegastrike-src-0.5.1.r1-r13498-al_fix.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-libpng16.patch -- fix build with libpng16 pgajdos@suse.com; klaussfreire@gmail.com notified
Patch5:         vegastrike-src-0.5.1.r1-libpng16.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-boost150_compat.patch -- fix build with latest boost (seemingly unrelated change but boost makes it blow without)
Patch6:         vegastrike-src-0.5.1.r1-boost150_compat.patch
Patch7:         vegastrike-aarch64.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-gcc6_compat.patch -- GCC 6 compatibility fixes, already upstreamed, not yet in tarball
Patch8:         vegastrike-src-0.5.1.r1-gcc6_compat.patch
# PATCH-FIX-OPENSUSE vegastrike-src-0.5.1.r1-gcc6_math_h.patch -- GCC 6 compatibility fixes, not upstreamable, autotools build system deprecated by upstream
Patch9:         vegastrike-src-0.5.1.r1-gcc6_math_h.patch
Patch10:        vegastrike_ppc64.patch
# PATCH-FIX-UPSTREAM vegastrike-src-0.5.1.r1-r13729-gcc7fix.patch -- GCC 7 fixes, already upstreamed, not yet in tarball
Patch11:        vegastrike-src-0.5.1.r1-r13729-gcc7fix.patch
BuildRequires:  SDL_mixer-devel
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_python-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  libexpat-devel
BuildRequires:  xorg-x11-libXmu-devel
BuildRequires:  pkgconfig(openal)
%if 0%{?suse_version} > 1210
BuildRequires:  pkgconfig(glu)
%endif
%endif
%if 0%{?fedora} > 0
BuildRequires:  expat-devel
%endif
%if 0%{?mdkversion} >= 2006
%ifarch x86_64
BuildRequires:  lib64expat1-devel
BuildRequires:  lib64mesagl1-devel
BuildRequires:  lib64x11_6-devel
%else
BuildRequires:  libexpat1-devel
BuildRequires:  libmesagl1-devel
BuildRequires:  libmesaglu1-devel
BuildRequires:  libx11_6-devel
%endif
%else
BuildRequires:  Mesa-devel
BuildRequires:  xorg-x11-devel
%endif
Requires:       opengl-games-utils
Requires:       xdg-utils
%if 0%{?suse_version}
Recommends:     %{name}-data >= %{version}
%endif

%description
Vega Strike is a GPL 3D OpenGL Action RPG space sim that allows a player to
trade and bounty hunt. You start in an old beat up Wayfarer cargo ship, with
endless possibility before you and just enough cash to scrape together a life.
Yet danger lurks in the space beyond.

%prep
%setup -q -a 1 -n %{name}-src-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p0
%patch10 -p1
%patch11 -p1
iconv -f ISO-8859-1 -t UTF-8 README > README.tmp
touch -r README README.tmp
mv README.tmp README
sed -i 's/-lboost_python-st/-lboost_python/g' Makefile.in
# we want to use the system version of expat.h
rm objconv/mesher/expat.h

%build
autoreconf -fi
%configure --with-data-dir=%{_datadir}/%{name} --with-boost=system \
  --enable-release --enable-flags="%{optflags} -DBOOST_PYTHON_NO_PY_SIGNATURES" \
  --disable-ffmpeg --disable-ogre --enable-stencil-buffer
make -j1

%install
make DESTDIR=%{buildroot} install
install -p -m 755 %{SOURCE2} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
chmod +x %{buildroot}%{_prefix}/objconv/*
mv %{buildroot}%{_prefix}/objconv/* \
  %{buildroot}%{_libexecdir}/%{name}
for i in asteroidgen base_maker mesh_xml mesher replace tempgen trisort \
         vsrextract vsrmake; do
  mv %{buildroot}%{_bindir}/$i %{buildroot}%{_libexecdir}/%{name}
done
mkdir -p %{buildroot}%{_mandir}/man6
install -p -m 644 *.6 %{buildroot}%{_mandir}/man6
%if 0%{?suse_version}
%fdupes -s %{buildroot}%{_mandir}/man6
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING DOCUMENTATION README ToDo.txt
%{_bindir}/vega*
%{_bindir}/vs*
%{_libexecdir}/%{name}
%{_mandir}/man6/*

%changelog
