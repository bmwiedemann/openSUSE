#
# spec file for package mda-lv2
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


Name:           mda-lv2
Version:        1.2.2+git20190317
Release:        0
Summary:        LV2 port of MDA plugins
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://drobilla.net/software/mda-lv2/
Source:         mda.lv2-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  lv2
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(lv2)

%description
MDA-LV2 is an LV2 port of the MDA plugins by Paul Kellett. It
contains 36 high-quality plugins for a variety of tasks.

The instrument plugins make use of the new atom:AtomPort to receive
MIDI. Apologies for any inconvenience, but this means they will
only work in modern hosts which have implemented atom-based MIDI.
The effects should work fine in any LV2 host.

%prep
%setup -q -n mda.lv2-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
python3 ./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
python3 ./waf -v

%install
python3 ./waf --destdir=%{buildroot} install

%files
%{_libdir}/lv2/mda.lv2

%changelog
