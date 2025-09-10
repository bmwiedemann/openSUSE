#
# spec file for package lsdvd
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2006-2009 Manfred Tremmel <Manfred.Tremmel@iiv.de>
# Copyright (c) 2004 Rainer Lay <rainer@links2linux.de>
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


Name:           lsdvd
Version:        0.20
Release:        0
Summary:        A ls for video DVDs
Summary(de):    Ein ls für Video DVDs
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Other
URL:            http://untrepid.com/lsdvd
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dvdread) >= 4.1.3.
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0

%description
A tool to display the directory of a video DVDs

%description -l de
Ein Programm zur Anzeige des Inhalts einer Video-DVD

%prep
%autosetup -p1

%build
export CC=gcc
test -x "$(type -p gcc-13)" && export CC=gcc-13
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
