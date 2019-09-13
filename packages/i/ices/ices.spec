#
# spec file for package ices
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           ices
BuildRequires:  alsa-devel libshout-devel libtheora-devel libvorbis-devel libxml2-devel pkgconfig speex-devel
BuildRequires:  libtool
Summary:        Source Client for icecast Streaming Server
Version:        2.0.1
Release:        239
Group:          Productivity/Multimedia/Other
AutoReqProv:    on
License:        GPL-2.0+
Url:            http://www.icecast.org/
Source:         %{name}-%{version}.tar.bz2
Source1:        run_ices
Patch:          ices-gcc-warning-fix.diff
Patch1:         ices-missing-fclose.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
IceS is a source client for a streaming server. The purpose of this
client is to provide an audio stream to a streaming server such that
one or more listeners can access the stream.  With this layout, this
source client can be situated remotely from the icecast server.



Authors:
--------
    Xiph.org Foundation <team@icecast.org>

%prep
%setup -q
%patch
%patch1 -p1

%build
autoreconf --force --install
%configure
make

%install
%makeinstall
install -c -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/ices

%clean
[ "$RPM_BUILD_ROOT" != "/" -a -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING TODO
%doc doc/*.html
%doc doc/*.css
%doc conf/*.xml
%{_bindir}/*

%changelog
