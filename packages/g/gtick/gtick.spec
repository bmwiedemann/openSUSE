#
# spec file for package gtick
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gtick
Version:        0.5.4
Release:        0
Summary:        A metronome application
License:        GPL-3.0
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://www.antcom.de/gtick/
Source0:        http://www.antcom.de/gtick/download/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix-desktop-categories.patch p.drouand@gmail.com -- Fix .desktop categories and no abs path for icon
Patch0:         fix-desktop-categories.patch
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libpulse-devel
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GTick is a metronome application written for GNU/Linux and other UN*X-like
operting systems supporting different meters (Even, 2/4, 3/4, 4/4 and more)
and speeds ranging from 10 to 1000 bpm.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%dir %{_datadir}/appdata
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/gtick.appdata.xml
%{_datadir}/icons/hicolor/64x64/apps/gtick.xpm
%{_datadir}/pixmaps/gtick_32x32.xpm

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
