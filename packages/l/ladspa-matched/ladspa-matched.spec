#
# spec file for package ladspa-matched
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


Name:           ladspa-matched
Version:        1
Release:        0
Summary:        LADSPA matched plugin
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://quitte.de/dsp/
Source:         http://quitte.de/dsp/matched.tar.gz
Source1:        http://quitte.de/dsp/unmatched.tar.gz
Patch1:         unmatched.dif
BuildRequires:  gcc
BuildRequires:  ladspa-devel
Supplements:    ladspa
Provides:       ladspa-unmatched = %{version}
Obsoletes:      ladspa-unmatched < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides LADSPA (Linux Audio Developer's Simple Plug-in API)
plugins for emulating certain aspects of the tone of a real musical
instrument amplifier, in real time.  It contains two plugins, matched and
unmatched.

%prep
%setup -q -c -a 0 -a 1
cd matched
%patch1
cd ../unmatched
%patch1

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
make -C matched %{?_smp_mflags} CFLAGS="%{optflags} -fPIC -ggdb"
make -C unmatched %{?_smp_mflags} CFLAGS="%{optflags} -fPIC -ggdb"

%install
mkdir -p %{buildroot}%{_libdir}/ladspa
install -c {matched,unmatched}/*.so %{buildroot}%{_libdir}/ladspa

%files
%defattr(-,root,root)
%{_libdir}/ladspa
%doc matched/COPYING

%changelog
