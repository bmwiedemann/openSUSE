#
# spec file for package pfstools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _libname libpfs2
Name:           pfstools
Version:        2.1.0
Release:        0
Summary:        High Dynamic Range Image and Video manipulation tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            http://pfstools.sourceforge.net/
Source:         https://sourceforge.net/projects/pfstools/files/pfstools/%{version}/%{name}-%{version}.tgz
Patch1:         %{name}-gcc.patch
Patch2:         pfstools-octinstall.patch
Patch3:         pfstools-stdlib.patch
Patch4:         pfstools-1.8.1-fix-return-in-nonvoid.patch
# PATCH-FIX-OPENSUSE - https://sourceforge.net/p/pfstools/bugs/45/
Patch5:         pfstools-fix-libpfs-linkage.patch
# patch derived from https://github.com/pld-linux/pfstools/commit/67bd2304e516545f2b203f975ac5dd30d2b479b3
# I guess it could go upstream as is; sent email to mantiuk at gmail
Patch7:         pfstools-ImageMagick7.patch
BuildRequires:  Mesa
BuildRequires:  blas
# previous versions of cmake don't support ImageMagick 7
BuildRequires:  cmake >= 3.9.0
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel
BuildRequires:  hdf5-devel
BuildRequires:  lapack
BuildRequires:  libnetpbm-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(freeglut)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(octave)
Requires:       dcraw

%description
The pfstools package is a set of command line (and one GUI) programs
for reading, writing, manipulating and viewing high-dynamic range
(HDR) images and video frames. All programs in the package exchange
data using the pfs file format for HDR data. The concept of pfstools
is similar to netpbm for low-dynamic range images.

%package -n %{_libname}
Summary:        Library for HDR image and video manipulation
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{_libname}
The pfstools package is a set of command line (and one GUI) programs
for reading, writing, manipulating and viewing high-dynamic range
(HDR) images and video frames. All programs in the package exchange
data using the pfs file format for HDR data. The concept of pfstools
is similar to netpbm for low-dynamic range images.

#Disable until opencv can be enabled.
#%%package -n pfscalign
#Summary:        Align image stack
#License:        GPL-2.0+ and LGPL-2.1+
#Group:          Productivity/Multimedia/Other

#%%description -n pfscalign
#Align multiple exposures using homographic transformation. The command
#uses a similar feature-point based method as most panorama stitching software.

%package -n pfscalibration
Summary:        Photometric Calibration of HDR and LDR Cameras
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
Requires:       dcraw
Requires:       jhead
%{perl_requires}
%{?libperl_requires}

%description -n pfscalibration
A photographic camera with a standard CCD sensor is able to acquire an
image with simultaneous dynamic range of not more than 1:1000. The
basic idea to create an image with a higher dynamic range is to combine
multiple images with different exposure settings, thus making use of
available sequential dynamic range.

%package -n pfstmo
Summary:        Tone Mapping Operators for High Dynamic Range Images
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other

%description -n pfstmo
pfstmo package contains the implementation of tone mapping operators,
suitable for processing of both static images and animations.

%package -n pfsview
Summary:        Qt-based viewer for HDR files
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other

%description -n pfsview
pfsview is a viewer program based on Qt4 for viewing HDR graphic files.

%package -n pfsglview
Summary:        GL-based viewer for HDR files
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other

%description -n pfsglview
pfsglview is a viewer program based on OpenGL for viewing HDR graphic files.

%package exr
Summary:        EXR file import and export for PFS tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other

%description exr
This package contains two-way conversion filters between the EXR file
format and pfstools's HDR graphics file format.

%package imgmagick
Summary:        ImageMagick file import for PFS tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other

%description imgmagick
This package contains input and output filters for ImageMagick to
support pfstools's HDR graphics file format.

%package octave
Summary:        Octave interaction with PFS tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
Requires:       octave

%description octave
The pfstools-octave package contains programs to process RGB
or luminance channels in PFS streams using Octave.

%package devel
Summary:        Development files for libpfs, a library for HDR image and video manipulation
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{_libname} = %{version}

%description devel
The pfstools package is a set of command line (and one GUI) programs
for reading, writing, manipulating and viewing high-dynamic range
(HDR) images and video frames.

This subpackage contains libraries and header files for developing
applications that want to make use of libpfs.

%prep
%autosetup -p1
chmod -x ChangeLog

%build
%cmake
make %{?_smp_mflags}

%install
cd build
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
grep -r include %{buildroot}%{_includedir} | awk -F: '{print $2}'
%fdupes -s %{buildroot}%{_mandir}

%post -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog README doc/faq.txt
%dir %{_datadir}/%{name}
%{_bindir}/pfsabsolute
%{_bindir}/pfscat
%{_bindir}/pfsclamp
%{_bindir}/pfscolortransform
%{_bindir}/pfscut
%{_bindir}/pfsdisplayfunction
%{_bindir}/pfsextractchannels
%{_bindir}/pfsflip
%{_bindir}/pfsgamma
%{_bindir}/pfsin
%{_bindir}/pfsindcraw
%{_bindir}/pfsinpfm
%{_bindir}/pfsinppm
%{_bindir}/pfsinrgbe
%{_bindir}/pfsintiff
%{_bindir}/pfsinyuv
%{_bindir}/pfsout
%{_bindir}/pfsouthdrhtml
%{_bindir}/pfsoutpfm
%{_bindir}/pfsoutppm
%{_bindir}/pfsoutrgbe
%{_bindir}/pfsouttiff
%{_bindir}/pfsoutyuv
%{_bindir}/pfspad
%{_bindir}/pfspanoramic
%{_bindir}/pfsretime
%{_bindir}/pfsrotate
%{_bindir}/pfssize
%{_bindir}/pfstag
%{_datadir}/pfstools/hdrhtml_c_b2.csv
%{_datadir}/pfstools/hdrhtml_c_b3.csv
%{_datadir}/pfstools/hdrhtml_c_b4.csv
%{_datadir}/pfstools/hdrhtml_c_b5.csv
%{_datadir}/pfstools/hdrhtml_default_templ/
%{_datadir}/pfstools/hdrhtml_hdrlabs_templ/
%{_datadir}/pfstools/hdrhtml_t_b2.csv
%{_datadir}/pfstools/hdrhtml_t_b3.csv
%{_datadir}/pfstools/hdrhtml_t_b4.csv
%{_datadir}/pfstools/hdrhtml_t_b5.csv
%{_mandir}/man1/pfsabsolute.1%{?ext_man}
%{_mandir}/man1/pfscat.1%{?ext_man}
%{_mandir}/man1/pfsclamp.1%{?ext_man}
%{_mandir}/man1/pfscolortransform.1%{?ext_man}
%{_mandir}/man1/pfscut.1%{?ext_man}
%{_mandir}/man1/pfsdisplayfunction.1%{?ext_man}
%{_mandir}/man1/pfsextractchannels.1%{?ext_man}
%{_mandir}/man1/pfsflip.1%{?ext_man}
%{_mandir}/man1/pfsgamma.1%{?ext_man}
%{_mandir}/man1/pfsin.1%{?ext_man}
%{_mandir}/man1/pfsindcraw.1%{?ext_man}
%{_mandir}/man1/pfsinpfm.1%{?ext_man}
%{_mandir}/man1/pfsinppm.1%{?ext_man}
%{_mandir}/man1/pfsinrgbe.1%{?ext_man}
%{_mandir}/man1/pfsintiff.1%{?ext_man}
%{_mandir}/man1/pfsinyuv.1%{?ext_man}
%{_mandir}/man1/pfsout.1%{?ext_man}
%{_mandir}/man1/pfsouthdrhtml.1%{?ext_man}
%{_mandir}/man1/pfsoutpfm.1%{?ext_man}
%{_mandir}/man1/pfsoutppm.1%{?ext_man}
%{_mandir}/man1/pfsoutrgbe.1%{?ext_man}
%{_mandir}/man1/pfsouttiff.1%{?ext_man}
%{_mandir}/man1/pfsoutyuv.1%{?ext_man}
%{_mandir}/man1/pfspad.1%{?ext_man}
%{_mandir}/man1/pfspanoramic.1%{?ext_man}
%{_mandir}/man1/pfsretime.1%{?ext_man}
%{_mandir}/man1/pfsrotate.1%{?ext_man}
%{_mandir}/man1/pfssize.1%{?ext_man}
%{_mandir}/man1/pfstag.1%{?ext_man}

%files -n %{_libname}
%{_libdir}/libpfs.so.*

%files devel
%doc doc/faq.txt
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpfs.so

#Disabled until we can renable opencv
#%%files -n pfscalign
#%%{_bindir}/pfsalign
#%%{_mandir}/man1/pfsalign%%{ext_man}

%files -n pfscalibration
%{_bindir}/dcraw2hdrgen
%{_bindir}/jpeg2hdrgen
%{_bindir}/pfshdrcalibrate
%{_bindir}/pfsinhdrgen
%{_bindir}/pfsinme
%{_bindir}/pfsplotresponse
%{_mandir}/man1/dcraw2hdrgen.1%{?ext_man}
%{_mandir}/man1/jpeg2hdrgen.1%{?ext_man}
%{_mandir}/man1/pfshdrcalibrate.1%{?ext_man}
%{_mandir}/man1/pfsinhdrgen.1%{?ext_man}
%{_mandir}/man1/pfsinme.1%{?ext_man}
%{_mandir}/man1/pfsplotresponse.1%{?ext_man}

%files -n pfstmo
%{_bindir}/pfstmo_drago03
%{_bindir}/pfstmo_durand02
%{_bindir}/pfstmo_fattal02
%{_bindir}/pfstmo_ferradans11
%{_bindir}/pfstmo_mai11
%{_bindir}/pfstmo_mantiuk06
%{_bindir}/pfstmo_mantiuk08
%{_bindir}/pfstmo_pattanaik00
%{_bindir}/pfstmo_reinhard02
%{_bindir}/pfstmo_reinhard05
%{_mandir}/man1/pfstmo_drago03.1%{?ext_man}
%{_mandir}/man1/pfstmo_durand02.1%{?ext_man}
%{_mandir}/man1/pfstmo_fattal02.1%{?ext_man}
%{_mandir}/man1/pfstmo_ferradans11.1%{?ext_man}
%{_mandir}/man1/pfstmo_mai11.1%{?ext_man}
%{_mandir}/man1/pfstmo_mantiuk06.1%{?ext_man}
%{_mandir}/man1/pfstmo_mantiuk08.1%{?ext_man}
%{_mandir}/man1/pfstmo_pattanaik00.1%{?ext_man}
%{_mandir}/man1/pfstmo_reinhard02.1%{?ext_man}
%{_mandir}/man1/pfstmo_reinhard05.1%{?ext_man}

%files -n pfsview
%{_bindir}/pfsv
%{_bindir}/pfsview
%{_mandir}/man1/pfsview.1%{?ext_man}

%files -n pfsglview
%{_bindir}/pfsglview
%{_mandir}/man1/pfsglview.1%{?ext_man}

%files exr
%{_bindir}/pfsinexr
%{_bindir}/pfsoutexr
%{_mandir}/man1/pfsinexr.1%{?ext_man}
%{_mandir}/man1/pfsoutexr.1%{?ext_man}

%files imgmagick
%{_bindir}/pfsinimgmagick
%{_bindir}/pfsoutimgmagick
%{_mandir}/man1/pfsinimgmagick.1%{?ext_man}
%{_mandir}/man1/pfsoutimgmagick.1%{?ext_man}

%files octave
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*/
%{_bindir}/pfsoctavelum
%{_bindir}/pfsoctavergb
%{_bindir}/pfsstat
%{_datadir}/octave/*/site/m/pfstools/
%{_libdir}/octave/*/site/oct/*/pfstools/
%{_mandir}/man1/pfsoctavelum.1%{?ext_man}
%{_mandir}/man1/pfsoctavergb.1%{?ext_man}
%{_mandir}/man1/pfsstat.1%{?ext_man}

%changelog
