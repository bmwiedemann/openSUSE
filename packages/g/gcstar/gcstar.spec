#
# spec file for package gcstar
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


Name:           gcstar
Version:        1.7.1
Release:        0
Summary:        Application to manage collections
License:        GPL-2.0-only
URL:            http://www.gcstar.org/
Source0:        http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE gcstar-fix-desktop.patch vuntz@opensuse.org -- Fix desktop file for openSUSE
Patch0:         gcstar-fix-desktop.patch
BuildRequires:  fdupes
BuildRequires:  perl
BuildRequires:  perl-libwww-perl
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(Gtk2) >= 1.054
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Simple)
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
Requires:       perl
Requires:       perl-libwww-perl
Requires:       perl(Crypt::SSLeay)
Requires:       perl(Gtk2) >= 1.054
Requires:       perl(HTML::Parser)
Requires:       perl(XML::Parser)
Requires:       perl(XML::Simple)
Recommends:     perl(Archive::Zip)
Recommends:     perl(GD)
Recommends:     perl(GD::Graph::area)
Recommends:     perl(GD::Graph::bars)
Recommends:     perl(GD::Graph::pie)
Recommends:     perl(GD::Text)
BuildArch:      noarch

%description
GCstar is a free open source application for managing collections of
movies, books, music, etc. Detailed information on each item can be
automatically retrieved from the internet and you can store additional
data, such as the location or who you've lent it to. You may also
search and filter your collection by many criteria.

%prep
%setup -q -n %{name}
%patch0 -p1

%build

%install
./install --prefix=%{buildroot}%{_prefix}/
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
mkdir -p %{buildroot}%{_mandir}/man1/
mv %{buildroot}%{_prefix}/man/man1/gcstar.1.gz %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_datadir}/mime/packages
install -m 644 share/applications/gcstar.xml %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
%suse_update_desktop_file -i gcstar Database
%fdupes %{buildroot}%{_datadir}

%files
%{_bindir}/gcstar
%{_prefix}/lib/gcstar/
%{_datadir}/applications/gcstar.desktop
%{_datadir}/gcstar/
%{_datadir}/icons/hicolor/*/apps/gcstar.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-gcstar.*
%{_datadir}/mime/packages/gcstar.xml
%{_mandir}/man1/gcstar.1%{?ext_man}

%changelog
