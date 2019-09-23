#
# spec file for package zenity
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           zenity
Version:        3.32.0
Release:        0
Summary:        GNOME Command Line Dialog Utility
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/Zenity
Source0:        https://download.gnome.org/sources/zenity/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libnotify) >= 0.6.1
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.8.1
Recommends:     %{name}-lang

%description
Zenity is a basic rewrite of gdialog, without the pain involved of
trying to figure out commandline parsing.  Zenity is zen-like; simple
and easy to use.

Zenity Dialogs: Calendar, Text Entry, Error, Informational, File
Selection, List, Progress, Question, Text Information, Warning and
Password.

Zenity is especially useful in scripts.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%license COPYING
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gdialog
%{_bindir}/zenity
%{_datadir}/zenity/
%{_mandir}/man?/zenity.1%{ext_man}

%files lang -f %{name}.lang

%changelog
