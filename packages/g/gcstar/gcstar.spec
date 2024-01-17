#
# spec file for package gcstar
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.8.0
Release:        0
Summary:        Application to manage collections
License:        GPL-2.0-or-later
URL:            https://www.gcstar.org/
Source0:        https://gitlab.com/Kerenoc/GCstar/-/archive/v%{version}/GCstar-v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  perl
BuildRequires:  update-desktop-files
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(Gtk3::SimpleList)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Cookies::Netscape)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(filetest)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  typelib(GdkPixdata) = 2.0
BuildRequires:  typelib(Gtk) = 3.0
BuildArch:      noarch

# Mandatory dependencies
Requires:       perl(Cwd)
Requires:       perl(Cwd)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::MD5)
Requires:       perl(Encode)
Requires:       perl(Encode::Locale)
Requires:       perl(Exporter)
Requires:       perl(File::Basename)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(File::Path)
Requires:       perl(File::Path)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(Glib::Object::Introspection)
Requires:       perl(Gtk3)
Requires:       perl(Gtk3::SimpleList)
Requires:       perl(HTML::Entities)
Requires:       perl(HTTP::Cookies::Netscape)
Requires:       perl(IO::File)
Requires:       perl(IO::Handle)
Requires:       perl(IO::Socket)
Requires:       perl(IO::Socket::INET)
Requires:       perl(LWP)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::Simple)
Requires:       perl(List::Util)
Requires:       perl(Net::SMTP)
Requires:       perl(POSIX)
Requires:       perl(POSIX)
Requires:       perl(Storable)
Requires:       perl(Text::Wrap)
Requires:       perl(URI::Escape)
Requires:       perl(Unicode::Normalize)
Requires:       perl(XML::Parser)
Requires:       perl(XML::Simple)
Requires:       perl(filetest)
Requires:       perl(threads)
Requires:       perl(threads::shared)

# Optional dependencies (It's probably a good idea to figure out what can be
#                        split this between Recommends and Suggests)
Recommends:     liberation-fonts
Recommends:     perl(Archive::Tar)
Recommends:     perl(Archive::Zip)
Recommends:     perl(Compress::Zlib)
Recommends:     perl(Date::Calc)
Recommends:     perl(DateTime::Format::Strptime)
Recommends:     perl(Digest::MD5)
Recommends:     perl(GD)
Recommends:     perl(GD::Graph::area)
Recommends:     perl(GD::Graph::bars)
Recommends:     perl(GD::Graph::pie)
Recommends:     perl(GD::Text)
Recommends:     perl(Image::ExifTool)
Recommends:     perl(JSON)
Recommends:     perl(Locale::Codes)
Recommends:     perl(MIME::Base64)
Recommends:     perl(MP3::Info)
Recommends:     perl(MP3::Tag)
Recommends:     perl(Net::FreeDB)
Recommends:     perl(Ogg::Vorbis::Header::PurePerl)
Recommends:     perl(Time::Piece)

%description
GCstar is a free open source application for managing collections of
movies, books, music, etc. Detailed information on each item can be
automatically retrieved from the internet and you can store additional
data, such as the location or who you've lent it to. You may also
search and filter your collection by many criteria.

Documentation can be found at https://gcstar.gitlab.io/gcstar_docs/en/

%prep
%autosetup -n GCstar-v%{version}

%build
# Nothing to build here.

%install
pushd %{name}
./install --prefix=%{buildroot}%{_prefix}/
rm -rf %{buildroot}%{_datadir}/{mime,applications}
%define _hicolordir %{_datadir}/icons/hicolor

for icon in share/gcstar/icons/gcstar_*.png; do
  size=$(echo $icon | grep -oE '[0-9]+x[0-9]+')
  # Only install sizes that exist in hicolor
  if test -d %{_datadir}/icons/hicolor/${size}/apps; then
    installdir=%{buildroot}%{_hicolordir}/${size}/apps
    install -D -m644 ${icon} ${installdir}/gcstar.png
  fi
  if test -d %{_datadir}/icons/hicolor/${size}/mimetypes; then
    installdir="%{buildroot}%{_hicolordir}/${size}/mimetypes"
    install -D -m644 ${icon} ${installdir}/application-x-gcstar.png
  fi
done

install -D -m644 share/gcstar/icons/gcstar_scalable.svg \
  %{buildroot}%{_hicolodir}/scalable/apps/gcstar.svg
install -D -m644 share/gcstar/icons/gcstar_scalable.svg \
  %{buildroot}%{_hicolordir}/scalable/mimetypes/application-x-gcstar.svg
install -D -m644 share/applications/gcstar.xml \
  -t %{buildroot}%{_datadir}/mime/packages/
popd

mkdir -p %{buildroot}%{_datadir}/applications
%suse_update_desktop_file -N GCstar -i gcstar Database GTK
%fdupes %{buildroot}%{_datadir}

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
