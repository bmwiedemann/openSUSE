#
# spec file for package imagej
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


%define SrcVersion 153t
Name:           imagej
Version:        1.53t
Release:        0
Summary:        A Java image processing program
License:        SUSE-Public-Domain
Group:          Productivity/Graphics/Convertors
URL:            https://rsbweb.nih.gov/ij/
Source:         https://rsbweb.nih.gov/ij/download/src/ij%{SrcVersion}-src.zip
Source1:        %{name}.in
Source2:        %{name}.desktop
Patch0:         imagej-nosourcetarget.patch
BuildRequires:  ImageMagick
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       java >= 1.8
BuildArch:      noarch

%description
ImageJ is a multithreaded image processing program inspired by NIH
Image for the Macintosh, running either as an applet or as a
standalone program.

It can read many image formats including TIFF, GIF, JPEG, BMP, DICOM,
FITS and "raw", and display, edit, anazlye, process and print
8/16/32-bit images. It supports "stacks", a series of images that
share a single window. It can calculate area and pixel value
statistics of user-defined selections, measure distances and angles,
create density histograms and line profile plots, supports standard
image processing functions such as contrast manipulation, sharpening,
smoothing, edge detection and median filtering. It does geometric
transformations such as scaling, rotation and flips. Zoom in/out up
to 32:1/1:32. Spatial calibration is available to provide real-world
dimensional measurements in units such as millimeters. Density or
gray scale calibration is also available.

ImageJ can be extended via Java plugins, and has a built-in editor and
compiler.

%prep
%autosetup -p1 -n source

%build
%{ant} -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 build

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 ij.jar %{buildroot}%{_datadir}/%{name}/%{name}.jar

# startscript
cat > %{name} << 'EOF'
#!/bin/sh
#
# imagej startscript
#
# Source functions library
echo Starting %{name} version %{version} ...
echo with options : ${@}

java -jar %{_datadir}/%{name}/imagej.jar ${@}

EOF

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/

# Icon
convert -strip build/microscope.gif build/%{name}.png
install -Dm 644 build/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Desktop menu entry
install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}

%files
%doc release-notes.html
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/%{name}/*.jar
#%{_datadir}/%{name}/lib/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
