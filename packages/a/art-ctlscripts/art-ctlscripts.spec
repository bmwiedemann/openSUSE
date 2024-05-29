#
# spec file for package art-ctlscripts
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


Name:           art-ctlscripts
Version:        1.0.1
Release:        0
Summary:        Custom CTL scripts for the ART raw processor.
License:        GPL-3.0-only
URL:            https://bitbucket.org/agriggio/art-ctlscripts
Source:         %{name}-%{version}.tar.xz
Requires:       ART
Supplements:    ART
BuildArch:      noarch

%description
This package provides the following scripts for ART:
  * colormix.ctl: mixes a user-selected RGB color with the image, using various blending modes
  * density.ctl: increase saturation while also lowering luminance, emulating "film density" filters available for some video editors
  * gamutcompress.ctl: gamut compression using the ACES method
  * hueeq.ctl: adjust the hue, saturation or luminance of each pixel according to its hue
  * lumeq.ctl: adjust the hue, saturation or luminance of each pixel according to its luminance
  * odt.ctl: ART's take on tone mapping from scene to display
  * posterize.ctl: simulates a posterization effect given by reducing the bit depth of the image
  * sateq.ctl: adjust the hue, saturation or luminance of each pixel according to its saturation
  * submix.ctl: mixes a user-selected RGB color with the image in a subtractive manner (i.e. as if the two colors were mixed like paint colors)
  * tetrahsl.ctl: color warping by means of tetrahedral division of the RGB color cube, using a HSL interface
  * tetrargb.ctl: tetrahedral color warping using the original RGB interface
  * tinteq.ctl: add a color cast to each pixel according to its luminance
  * wbchmix.ctl: white balance and RGB primaries correction

%prep
%autosetup -p1

%build

%install
install -D -m 0644 *.ctl -t %{buildroot}%{_datadir}/ART/ctlscripts

%files
%dir %{_datadir}/ART
%dir %{_datadir}/ART/ctlscripts
%{_datadir}/ART/ctlscripts/*

%changelog
