#
# spec file for package jacktrip
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           jacktrip
Version:        1.2.1
Release:        0
Summary:        Multi-machine network music performance over the Internet
License:        MIT
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/jcacerec/jacktrip
Source:         https://github.com/jcacerec/jacktrip/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)

%description
JackTrip is a system used for multi-machine network performance over the
Internet. It supports any number of channels (as many as the
computer/network can handle) of bidirectional, high quality, uncompressed
audio signal streaming.

%prep
%setup -q

%build
cd src
%qmake5 jacktrip.pro
%make_build

%install
cd src
make INSTALL_ROOT=%{buildroot} install
rm -v %{buildroot}/%{_bindir}/jacktrip_debug

%files
%doc CHANGESLOG.txt README.md TODO.txt
%{_bindir}/jacktrip

%changelog
