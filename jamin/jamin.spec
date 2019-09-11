#
# spec file for package jamin
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jamin
BuildRequires:  alsa-devel
BuildRequires:  fftw3-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  jack-devel
BuildRequires:  ladspa-devel
BuildRequires:  liblo-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
Summary:        JACK Audio Mastering Interface
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Version:        0.95.0
Release:        0
Url:            http://jamin.sf.net
Requires:       jack
Requires:       ladspa
Source:         %{name}-%{version}.tar.bz2
Patch1:         jamin-ladspa-path-fix.diff
Patch2:         jamin-link-to-dl.patch
Patch3:         jamin-gtk-type-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         shared-mime-info

%description
JAMin is the JACK Audio Connection Kit (JACK) audio mastering
interface.  JAMin is designed to perform professional audio mastering
of stereo input streams.  It uses LADSPA for digital signal processing
(DSP).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
intltoolize -f
autoreconf -fi
%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT%{_datadir}/icons $RPM_BUILD_ROOT%{_datadir}/pixmaps
rm -f $RPM_BUILD_ROOT%{_libdir}/ladspa/*.la

%suse_update_desktop_file %name AudioVideo AudioVideoEditing
%find_lang %{name}

%post
usr/bin/update-mime-database usr/share/mime >/dev/null || :

%postun
usr/bin/update-mime-database usr/share/mime >/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README* TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/ladspa
%{_datadir}/jamin
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*.xml

%changelog
