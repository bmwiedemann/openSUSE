#
# spec file for package ices
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


Name:           ices
Version:        2.0.3
Release:        0
Summary:        Source Client for icecast Streaming Server
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.icecast.org/ices/
Source:         https://downloads.xiph.org/releases/ices/ices-%{version}.tar.bz2
Source1:        run_ices
Patch0:         ices-missing-fclose.diff
BuildRequires:  alsa-devel
BuildRequires:  libshout-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  speex-devel

%description
IceS is a source client for a streaming server. The purpose of this
client is to provide an audio stream to a streaming server such that
one or more listeners can access the stream.  With this layout, this
source client can be situated remotely from the icecast server.

%prep
%setup -q
%patch0 -p1

%build
autoreconf --force --install
%configure
%make_build

%install
%make_install
install -c -m 755 %{SOURCE1} %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_datadir}/ices

%files
%license COPYING
%doc README.md AUTHORS
%doc doc/*.html
%doc doc/*.css
%doc conf/*.xml
%{_bindir}/*

%changelog
