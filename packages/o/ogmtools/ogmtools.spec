#
# spec file for package ogmtools
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ogmtools
Version:        1.5
Release:        0
Summary:        Tools for OGG Media Streams
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.bunkus.org/videotools/ogmtools/
Source:         https://www.bunkus.org/videotools/ogmtools/%{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}.diff
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libdvdread-devel
BuildRequires:  libvorbis-devel

%description
These tools allow information about (ogminfo), extraction from
(ogmdemux), creation of (ogmmerge), or the division of (ogmsplit) OGG
media streams.	OGM stands for OGG media streams.

%prep
%autosetup -p0

%build
autoreconf -fiv
export CXXFLAGS="-std=c++14 %{optflags}"
%configure --disable-dependency-tracking
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/dvdxchap
%{_bindir}/ogmcat
%{_bindir}/ogmdemux
%{_bindir}/ogminfo
%{_bindir}/ogmmerge
%{_bindir}/ogmsplit
%{_mandir}/man1/dvdxchap.1%{?ext_man}
%{_mandir}/man1/ogmcat.1%{?ext_man}
%{_mandir}/man1/ogmdemux.1%{?ext_man}
%{_mandir}/man1/ogminfo.1%{?ext_man}
%{_mandir}/man1/ogmmerge.1%{?ext_man}
%{_mandir}/man1/ogmsplit.1%{?ext_man}

%changelog
