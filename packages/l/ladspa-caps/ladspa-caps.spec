#
# spec file for package ladspa-caps
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


Name:           ladspa-caps
Version:        0.9.26
Release:        0
Summary:        LADSPA caps plugins
License:        GPL-3.0-or-later
URL:            http://quitte.de/dsp/
Source:         http://quitte.de/dsp/caps_%{version}.tar.bz2
# PATCH-FIX-UPSTREAM bmwiedemann -- ToDo
Patch2:         reproducible.patch
BuildRequires:  gcc-c++
Supplements:    ladspa

%description
This package provides a LADSPA (Linux Audio Developer's Simple Plug-in API)
caps plugins, the C* Audio Plugin Suite including instrument amplifier
emulation, stomp-box classics, versatile virtual analog oscillators,
fractal oscillation, reverb, equalization and others.

%prep
%setup -q -n caps-%{version}
%patch2 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -ggdb -fPIC"

%install
mkdir -p %{buildroot}%{_libdir}/ladspa
install -c *.so %{buildroot}%{_libdir}/ladspa

%files
%license COPYING
%doc README CHANGES
%{_libdir}/ladspa

%changelog
