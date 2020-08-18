#
# spec file for package pmidi
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pmidi
Version:        1.7.1
Release:        0
Summary:        A Command Line MIDI Player for ALSA
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Midi
URL:            http://www.parabola.demon.co.uk/alsa/pmidi.html
Source:         https://sourceforge.net/projects/pmidi/files/pmidi/%{version}/pmidi-%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  automake

%description
pmidi is a command line MIDI player for ALSA.

%prep
%setup -q

%build
autoreconf -fi
%configure --with-included-glib
%make_build

%install
%make_install

%files
%{_bindir}/*
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_mandir}/man*/*

%changelog
