#
# spec file for package xaos
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


Name:           xaos
Version:        3.6
Release:        0
Summary:        Powerful fractal generator
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Graphics
Url:            http://matek.hu/xaos/doku.php
Source:         http://sourceforge.net/projects/xaos/files/XaoS/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.sh
Source3:        %{name}.png
Patch0:         %{name}-3.5-strip.patch
Patch1:         fix-prototypes.diff
Patch2:         xaos-fix-implicit-decl.patch
BuildRequires:  aalib-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gsl-devel
BuildRequires:  libpng-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
Provides:       XaoS
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
XaoS is a fast portable real-time interactive fractal zoomer. It
displays the Mandelbrot set (among other escape time fractals) and
allows you to zoom smoothly into the fractal.  Various coloring modes
are provided for both the points inside and outside the selected set.
In addition, switching between Julia and Mandelbrot fractal types and
displaying planes is provided.

%lang_package

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1

%build
# convert all xpf-files to UNIX format
find examples/ -iname "*.xpf" -exec dos2unix {} \;
export CFLAGS="%optflags -fno-strict-aliasing"
%configure --with-svga-driver=no
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_infodir}
%make_install
mv %{buildroot}%{_bindir}/xaos %{buildroot}%{_bindir}/xaos.bin
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/xaos
chmod 755 %{buildroot}%{_bindir}/xaos
chmod 755 %{buildroot}%{_bindir}/xaos.bin
%suse_update_desktop_file -i %{name} Education Math
install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%find_lang %{name}
%fdupes %{buildroot}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%doc %{_infodir}/xaos.info.*
%doc %{_mandir}/man6/xaos.6.*
%{_bindir}/xaos
%{_bindir}/xaos.bin
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/XaoS/

%files lang -f %{name}.lang

%changelog
