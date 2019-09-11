#
# spec file for package pmidi
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pmidi
BuildRequires:  alsa-devel
BuildRequires:  automake
Summary:        A Command Line MIDI Player for ALSA
License:        GPL-2.0
Group:          Productivity/Multimedia/Sound/Midi
Version:        1.7.0
Release:        0
Source:         pmidi-%{version}.tar.gz
Url:            http://www.parabola.demon.co.uk/alsa/pmidi.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pmidi is a command line MIDI player for ALSA.



Authors:
--------
    Steve Ratcliffe <steve@parabola.demon.co.uk>

%prep
%setup

%build
autoreconf -fi
%configure --with-included-glib
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/man*/*

%changelog
