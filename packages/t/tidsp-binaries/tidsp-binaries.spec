#
# spec file for package tidsp-binaries
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guillaume GARDET <guillaume@opensuse.org>
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



Name:           tidsp-binaries
Version:        23.i3.8
Release:        0.0
Summary:        The TI OMAP3 DSP algorithms
Group:          Hardware/Other
Url:            https://gforge.ti.com/gf/project/openmax/
Source:         tidsp-binaries-%{version}.tar.gz
License:        SUSE-Firmware
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %arm

%description
The TI OMAP3 DSP algorithms.
This package contains the algorithms for use on OMAP-like with DSP SoC (arm platform only).

%prep
%setup -q

%build
# Nothing to do since we only copy *.dll64D algo files (DSP binaries) from archive during installation

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /%{_lib}/dsp
/%{_lib}/dsp/baseimage.dof
/%{_lib}/dsp/conversions.dll64P
/%{_lib}/dsp/dctn_dyn.dll64P
/%{_lib}/dsp/h264vdec_sn.dll64P
/%{_lib}/dsp/jpegdec_sn.dll64P
/%{_lib}/dsp/jpegenc_sn.dll64P
/%{_lib}/dsp/LICENSE
/%{_lib}/dsp/m4venc_sn.dll64P
/%{_lib}/dsp/mp4vdec_sn.dll64P
/%{_lib}/dsp/mpeg4aacdec_sn.dll64P
/%{_lib}/dsp/qosdyn_3430.dll64P
/%{_lib}/dsp/ringio.dll64P
/%{_lib}/dsp/test.dll64P
/%{_lib}/dsp/usn.dll64P
/%{_lib}/dsp/vpp_sn.dll64P

%changelog
