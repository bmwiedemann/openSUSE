#
# spec file for package clamtk
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           clamtk
Version:        6.06
Release:        0
Summary:        GUI for the ClamAV Antivirus
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Productivity/Security
URL:            https://github.com/dave-theunsub/clamtk
Source:         https://bitbucket.org/davem_/clamtk-gtk3/downloads/clamtk-%{version}.tar.xz
Source1:        https://bitbucket.org/davem_/clamtk-gtk3/downloads/clamtk-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch0:         clamtk-add_searchpath.patch
BuildRequires:  update-desktop-files
Requires:       clamav >= 0.88
Requires:       gnome-icon-theme
Requires:       zenity
Requires:       perl(Cwd)
Requires:       perl(Digest::SHA)
Requires:       perl(Encode)
Requires:       perl(File::Basename)
Requires:       perl(File::Copy)
Requires:       perl(File::Path)
Requires:       perl(Glib)
Requires:       perl(Gtk3)
Requires:       perl(JSON)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Locale::gettext)
Requires:       perl(Net::DNS)
Requires:       perl(Text::CSV)
Requires:       perl(Time::Piece)
Requires:       typelib(Gdk) = 3.0
Requires:       typelib(GdkPixbuf) = 2.0
Requires:       typelib(GdkPixdata) = 2.0
Requires:       typelib(Gtk) = 3.0
Requires:       typelib(Pango) = 1.0
Recommends:     clamav-db
BuildArch:      noarch
%{perl_requires}

%description
ClamTk is a GUI front-end for ClamAV using Gtk3-perl.
It is designed to be an easy-to-use, point and click virus scanner.

%lang_package

%prep
%setup -q
%patch0

%build
gzip -dc clamtk.1.gz > clamtk.1
rm clamtk.1.gz

%install
install -D -m 0755 clamtk %{buildroot}%{_bindir}/clamtk
install -D -m 0644 images/clamtk.png %{buildroot}%{_datadir}/pixmaps/clamtk.png
install -D -m 0644 clamtk.1 %{buildroot}%{_mandir}/man1/clamtk.1

# install in the perl vendorlib location:
install -d %{buildroot}/%{perl_vendorlib}/ClamTk
install -m0644 lib/*.pm %{buildroot}/%{perl_vendorlib}/ClamTk/

pushd po
for mo in *.mo; do
    lang="${mo%%.mo}"
    install -D -m 0644 ${mo} %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/%{name}.mo
done
popd #po
for l in cs_CZ el_GR nl_BE ast; do
    rm -rf %{buildroot}%{_datadir}/locale/$l
done

%suse_update_desktop_file -i -r %{name} System Security

%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc CHANGES DISCLAIMER README.md
%{_bindir}/clamtk
%{perl_vendorlib}/ClamTk
%{_datadir}/pixmaps/clamtk.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/clamtk.1%{ext_man}

%files lang -f %{name}.lang

%changelog
