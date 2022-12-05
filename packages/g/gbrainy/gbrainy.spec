#
# spec file for package gbrainy
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gbrainy
Version:        2.4.5
Release:        0
Summary:        A brain teaser game and trainer
License:        GPL-2.0-or-later
Group:          Amusements/Games/Logic
URL:            https://wiki.gnome.org/Apps/gbrainy
Source:         https://gent.softcatala.org/jmas/gbrainy/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- gbrainy-use-libexecdir.patch
Patch0:         gbrainy-use-libexecdir.patch

BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gtk-sharp-3.0) >= 2.99.1
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(mono) >= 4.0.0
# For the help system to work, we require a ghelp:// URI handler.
Recommends:     mimehandler(x-scheme-handler/ghelp)
BuildArch:      noarch
%if !0%{?is_opensuse}
BuildRequires:  translation-update-upstream
%endif

%description
gbrainy is a brain teaser game and trainer to have fun and to keep
your brain trained.

It provides the following types of games:

* Logic puzzles. Games designed to challenge your reasoning and
  thinking skills.

* Mental calculation. Games based on arithmetical operations
  designed to prove your mental calculation skills.

* Memory trainers. Games designed to challenge your short term
  memory.

* Verbal analogies. Games that challenge your verbal aptitude.

%prep
%autosetup -p1
%if !0%{?is_opensuse}
translation-update-upstream
%endif

%lang_package

%build
export MONO_SHARED_DIR=%{_localstatedir}/tmp
%configure \
	--disable-static \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}
rm -rf %{buildroot}%{_datadir}/pixmaps
# There are no extensions yet, Thus creating a -devel package sounds overkill (file can't reside in noarch package).
rm %{buildroot}%{_libdir}/pkgconfig/gbrainy.pc

# When below tests fail, we can now remove the chmod
test -x %{buildroot}%{_libexecdir}/%{name}/gbrainy.exe.config
chmod -x %{buildroot}%{_libexecdir}/%{name}/gbrainy.exe.config

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/games/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
