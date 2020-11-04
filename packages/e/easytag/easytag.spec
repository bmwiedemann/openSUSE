#
# spec file for package easytag
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


Name:           easytag
Version:        2.4.3
Release:        0
Summary:        GTK+ tag editor for audio files
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://projects.gnome.org/easytag/
Source0:        http://download.gnome.org/sources/easytag/2.4/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM easytag-revert-open-handle-ogg.patch bgo#776110 boo#1069789 bjorn.lie@gmail.com -- Revert commit causing corruption in oggfiles
Patch0:         easytag-revert-open-handle-ogg.patch
BuildRequires:  appstream-glib-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  id3lib-devel
BuildRequires:  intltool >= 0.50.0
BuildRequires:  pkgconfig >= 0.24
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(flac) >= 1.1.4
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(libnautilus-extension) >= 3.0
BuildRequires:  pkgconfig(ogg) >= 1.0
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(taglib_c) >= 1.6.0
BuildRequires:  pkgconfig(vorbis) >= 1.0.1
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack) >= 4.40

%description
EasyTAG is a utility for viewing and editing tags for MP3, MP2, MP4/AAC, FLAC, Ogg Vorbis,
MusePack, Monkey's Audio and WavPack files.

Its simple and nice GTK+ interface makes tagging easier.

%package -n nautilus-plugin-easytag
Summary:        Nautilus extension for opening in EasyTAG
Group:          Productivity/File utilities
Requires:       %{name} = %{version}
Supplements:    (%{name} and nautilus)

%description -n nautilus-plugin-easytag
Nautilus extension to add "Open with EasyTAG" to the Nautilus context menu, for
easier access to EasyTAG when opening directories and audio files.

%lang_package

%prep
%setup -q
%patch0 -p1 -R

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}
%find_lang %{name}
# We take the HACKERS and AUTHORS file to the standard package doc
rm -rf %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc ChangeLog README HACKING THANKS TODO
%{_bindir}/%{name}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/easytag.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.EasyTAG.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.EasyTAG.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%files -n nautilus-plugin-easytag
%{_datadir}/appdata/easytag-nautilus.metainfo.xml
%{_libdir}/nautilus/extensions-3.0/libnautilus-easytag.so

%changelog
