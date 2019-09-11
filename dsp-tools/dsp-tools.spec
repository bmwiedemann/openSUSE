#
# spec file for package dsp-tools
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dsp-tools
Version:        2.0
Release:        0
Summary:        Utilities for TI OMAP3 DSP
License:        LGPL-2.1
Group:          Hardware/Other
Url:            https://github.com/felipec/dsp-tools
Source:         https://github.com/felipec/dsp-tools/archive/v%{version}.tar.gz
Recommends:     tidsp-binaries
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %arm

%description
Utilities for TI OMAP3 DSP.
This package contains some tools (dsp-load, dsp-probe, dsp-test, dsp-exec) for OMAP-like with DSP SoC (arm platform only).

%prep
%setup -q

%build
make %{?_smp_mflags} CROSS_COMPILE=""

%install
%make_install CROSS_COMPILE=""

%files
%defattr(-,root,root)
%{_bindir}/dsp-load
%{_bindir}/dsp-probe
%{_bindir}/dsp-test
%{_bindir}/dsp-exec

%changelog
