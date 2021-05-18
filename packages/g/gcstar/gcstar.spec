#
# spec file for package gcstar
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gcstar
Version:        1.7.3
Release:        0
Summary:        Application to manage collections
License:        GPL-2.0-only
URL:            https://wiki.gcstar.org/en
Source0:        https://gitlab.com/Kerenoc/GCstar/-/archive/v%{version}/GCstar-v%{version}.tar.bz2
# PATCH-FIX-OPENSUSE gcstar-fix-desktop.patch vuntz@opensuse.org -- Fix desktop file for openSUSE
Patch0:         gcstar-fix-desktop.patch
BuildRequires:  fdupes
BuildRequires:  perl
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(Gtk3::SimpleList)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(XML::Simple)
BuildRequires:  typelib-1_0-GdkPixdata-2_0
BuildRequires:  typelib-1_0-Gtk-3_0
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
Requires:       perl
Requires:       perl(DateTime::Format::Strptime)
Requires:       perl(Gtk3)
Requires:       perl(Gtk3::SimpleList)
Requires:       perl(JSON)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(XML::Simple)
Recommends:     perl(Archive::Tar)
Recommends:     perl(Archive::Zip)
Recommends:     perl(Compress::Zlib)
Recommends:     perl(Date::Calc)
Recommends:     perl(Digest::MD5)
Recommends:     perl(GD)
Recommends:     perl(GD::Graph)
Recommends:     perl(GD::Text)
Recommends:     perl(Image::ExifTool)
Recommends:     perl(MIME::Base64)
Recommends:     perl(MP3::Info)
Recommends:     perl(MP3::Tag)
Recommends:     perl(Net::FreeDB)
Recommends:     perl(Ogg::Vorbis::Header::PurePerl)
Recommends:     perl(Time::Piece)
BuildArch:      noarch

%description
GCstar is a free open source application for managing collections of
movies, books, music, etc. Detailed information on each item can be
automatically retrieved from the internet and you can store additional
data, such as the location or who you've lent it to. You may also
search and filter your collection by many criteria.

%prep
%setup -q -n GCstar-v%{version}
%patch0 -p0

%build

%install
pushd %{name}
./install --prefix=%{buildroot}%{_prefix}/
rm -rf %{buildroot}%{_datadir}/{mime,applications}
for icon in share/gcstar/icons/gcstar_*.png; do
  size=`echo $icon | sed 's,.*gcstar_,,;s,\.png,,'`
  # Only install sizes that exist in hicolor
  if test -d %{_datadir}/icons/hicolor/$size/apps; then
    install -D -m644 $icon %{buildroot}%{_datadir}/icons/hicolor/$size/apps/gcstar.png
  fi
  if test -d %{_datadir}/icons/hicolor/$size/mimetypes; then
    install -D -m644 $icon %{buildroot}%{_datadir}/icons/hicolor/$size/mimetypes/application-x-gcstar.png
  fi
done
install -D -m644 share/gcstar/icons/gcstar_scalable.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/gcstar.svg
install -D -m644 share/gcstar/icons/gcstar_scalable.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-gcstar.svg
mkdir -p %{buildroot}%{_datadir}/mime/packages
install -m 644 share/applications/gcstar.xml %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
%suse_update_desktop_file -i gcstar Database
%fdupes %{buildroot}%{_datadir}
popd

%files
%{_bindir}/gcstar
%{_prefix}/lib/gcstar/
%{_datadir}/applications/gcstar.desktop
%{_datadir}/gcstar/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/gcstar.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-gcstar.*
%{_datadir}/mime/packages/gcstar.xml
%{_mandir}/man1/gcstar.1%{?ext_man}

%changelog
