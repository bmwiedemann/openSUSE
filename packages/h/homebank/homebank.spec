#
# spec file for package homebank
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


Name:           homebank
Version:        5.6.1
Release:        0
Summary:        Application to manage personal accounts
License:        GPL-2.0-or-later
Group:          Productivity/Office/Finance
URL:            http://homebank.free.fr/
Source:         http://homebank.free.fr/public/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libofx-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.39
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26

%description
HomeBank is an application to manage personal accounts at home. The main
concept is to be light, simple and very easy to use. It brings many
features that allows to analyze finances in a detailed way instantly and
dynamically with powerful report tools based on filtering and graphical
charts.

%lang_package

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -G "Personal Accounting" %{name}
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}
# Application Registry is obsolete since GNOME 2.8.
rm -r %{buildroot}%{_datadir}/application-registry
rm -r %{buildroot}%{_datadir}/mime-info
# Remove duplicate file
rm %{buildroot}%{_datadir}/%{name}/datas/ChangeLog

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang

%changelog
