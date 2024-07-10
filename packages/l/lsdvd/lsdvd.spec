#
# spec file for package lsdvd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           lsdvd
Version:        0.17
Release:        0
Summary:        A ls for video DVDs
Summary(de):    Ein ls für Video DVDs
License:        GPL-2.0
Group:          Productivity/Multimedia/Other
URL:            http://untrepid.com/lsdvd
Source0:        https://sourceforge.net/projects/lsdvd/files/lsdvd/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dvdread)

%description
A tool to display the directory of a video DVDs

%description -l de
Ein Programm zur Anzeige des Inhalts einer Video-DVD

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
