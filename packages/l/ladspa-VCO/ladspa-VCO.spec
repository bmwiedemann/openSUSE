#
# spec file for package ladspa-VCO
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ladspa-VCO
Version:        0.3.0
Release:        0
Summary:        LADSPA VCO-plugin
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://users.skynet.be/solaris/linuxaudio/
Source:         VCO-plugins-%{version}.tar.bz2
BuildRequires:  gcc-c++
Supplements:    ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides LADSPA (Linux Audio Developer's Simple Plug-in API)
plugin to implement three anti-aliased oscillators.

%prep
%setup -q -n VCO-plugins-%{version}

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
make %{?_smp_mflags} CXXFLAGS="%{optflags} -ggdb -fPIC"

%install
mkdir -p %{buildroot}%{_libdir}/ladspa
install -c *.so %{buildroot}%{_libdir}/ladspa

%files
%defattr(-,root,root)
%{_libdir}/ladspa
%doc AUTHORS COPYING README

%changelog
