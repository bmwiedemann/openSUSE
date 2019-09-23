#
# spec file for package enblend-enfuse
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


# We use pregenerated documentation, as packages for rsvg-convert and hevea are
# not packaged yet.
%global _build_doc 0

#%%define __builder ninja

Name:           enblend-enfuse
Url:            http://enblend.sourceforge.net/
Summary:        Tool for Composing Images
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
Version:        4.2
Release:        0
Source0:        http://sourceforge.net/projects/enblend/files/%{name}/%{name}-4.2/%{name}-%{version}.tar.gz

Source10:       enblend.pdf
Source11:       enfuse.pdf

# PATCH-FIX-UPSTREAM enblend-enfuse-4.2-add-missing-cmakelists.patch
Patch0:         enblend-enfuse-4.2-add-missing-cmakelists.patch
# PATCH-FIX-UPSTREAM reproducible.patch by bmwiedemann
Patch1:         reproducibledate.patch
# PATCH-FIX-OPENSUSE by bmwiedemann
Patch2:         reproducible.patch

BuildRequires:  OpenEXR-devel
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  gsl-devel
BuildRequires:  help2man
BuildRequires:  libICE-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel >= 2.5
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-tools
BuildRequires:  opencl-headers
BuildRequires:  perl-TimeDate
BuildRequires:  pkg-config
BuildRequires:  plotutils-devel
BuildRequires:  vigra-devel

# Documentation
%if %{_build_doc}
BuildRequires:  ImageMagick
BuildRequires:  gnuplot
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  hevea
BuildRequires:  m4
BuildRequires:  rsvg-convert
BuildRequires:  texinfo
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  tidy
BuildRequires:  transfig
%endif

Provides:       enblend = %{version}
Provides:       enfuse = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         %install_info_prereq

%description
Enblend is a tool for compositing images using a Burt & Adelson
multiresolution spline. This technique tries to make the seams between
the input images invisible. The basic idea is that image features
should be blended across a transition zone, proportional in size to the
spatial frequency of the features. For example, objects like trees and
window panes have rapid changes in color. By blending these features in
a narrow zone, you cannot see the seam because the eye already expects
to see color changes at the edge of these features. Clouds and sky are
the opposite. These features must be blended across a wide transition
zone because any sudden change in color is immediately noticeable.

%package doc
Summary:        Usage Documentation for enblend and enfuse
Group:          Documentation/PDF

%description doc
PDF usage documentation for the enblend and enfuse command line tools.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if ! %{_build_doc}
cp %{SOURCE10} doc/
cp %{SOURCE11} doc/
%endif

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DMARCHNATIVE=FALSE \
    -DMTUNENATIVE=FALSE \
    -DENABLE_OPENMP=ON \
%ifarch x86_64
    -DENABLE_SSE2=ON \
%endif
%if %{_build_doc}
    -DDOC=ON \
    -DINSTALL_PS_DOC=ON \
    -DINSTALL_PDF_DOC=ON \
%endif
    || cat CMakeFiles/CMakeError.log

%make_jobs

%install
%cmake_install

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS NEWS README

%{_bindir}/enblend
%{_bindir}/enfuse
%{_mandir}/man1/*

%files doc
%defattr(-,root,root)
%license COPYING
%doc doc/enblend.pdf doc/enfuse.pdf

%changelog
