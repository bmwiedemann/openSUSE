#
# spec file for package transmageddon
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
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


Name:           transmageddon
Version:        1.5
Release:        0
Summary:        A Video Transcoder
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.linuxrising.org/
Source:         http://www.linuxrising.org/files/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE transmageddon-gtk3.patch dimstar@opensuse.org -- Require GTK+ 3.0
Patch0:         transmageddon-gtk3.patch
# PATCH-FIX-OPENSUSE transmageddon-appdata-prjgroup.patch dimstar@opensuse.org -- Change AppStream project group to GNOME
Patch1:         transmageddon-appdata-prjgroup.patch
BuildRequires:  fdupes
# Needed to create typelib() Requires.
BuildRequires:  gobject-introspection
BuildRequires:  intltool >= 0.40.0
BuildRequires:  python3
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
Requires:       gstreamer-plugins-base >= 1.2.0
Requires:       python3
Requires:       python3-gobject
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-good
BuildArch:      noarch

%description
Transmageddon is a video transcoder for Linux and Unix systems
built using GStreamer. It supports almost any format as its input
and can generate a very large host of output files. The goal of the
application was to help people to create the files they need to be
able to play on their mobile devices and for people not hugely
experienced with multimedia to generate a multimedia file without
having to resort to command line tools with ungainly syntaxes.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
translation-update-upstream

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} PYTHON=%{_bindir}/python3
%fdupes %{buildroot}%{_datadir}
%suse_update_desktop_file %{name} AudioVideoEditing
%find_lang %{name} %{?no_lang_C}

%files
%defattr(-, root, root)
%{_bindir}/%{name}
%dir %{_datadir}/appdata
%{_datadir}/appdata/transmageddon.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
