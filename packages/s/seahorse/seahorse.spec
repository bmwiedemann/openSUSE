#
# spec file for package seahorse
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


Name:           seahorse
Version:        43.0
Release:        0
Summary:        GNOME interface for gnupg
License:        GFDL-1.1-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://wiki.gnome.org/Apps/Seahorse
Source0:        https://download.gnome.org/sources/seahorse/43/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gpg2 >= 2.2.0
BuildRequires:  libxslt-tools
BuildRequires:  meson >= 0.51
BuildRequires:  openldap2-devel
BuildRequires:  openssh
BuildRequires:  pkcs11-helper-devel
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib) >= 0.6
BuildRequires:  pkgconfig(gcr-3) >= 3.18
BuildRequires:  pkgconfig(gcr-ui-3) >= 3.18
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.66
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.66
BuildRequires:  pkgconfig(gobject-2.0) >= 2.66
BuildRequires:  pkgconfig(gpgme) >= 1.14.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libhandy-1) >= 1.5.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.16
BuildRequires:  pkgconfig(libsoup-3.0) >= 2.33.92
BuildRequires:  pkgconfig(pwquality)
Obsoletes:      %{name}-devel < %{version}

%description
Seahorse is a GNOME interface for gnupg. It uses gpgme as the backend.

%package -n gnome-shell-search-provider-seahorse
Summary:        GNOME interface for gnupg -- Search Provider for GNOME Shell
Group:          Productivity/Security
Supplements:    (%{name} and gnome-shell)
BuildArch:      noarch

%description -n gnome-shell-search-provider-seahorse
Seahorse is a GNOME interface for gnupg. It uses gpgme as the backend.

This package contains a search provider to enable GNOME Shell to get
search results from seahorse.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dpgp-support=true \
	-Dcheck-compatible-gpg=true \
	-Dpkcs11-support=true \
	-Dkeyservers-support=true \
	-Dhkp-support=true \
	-Dldap-support=true \
	-Dkey-sharing=true \
	-Dmanpage=true \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING COPYING-DOCS COPYING.LIB
%doc NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/seahorse
%{_libexecdir}/seahorse/
%{_datadir}/applications/org.gnome.seahorse.Application.desktop
%{_datadir}/dbus-1/services/org.gnome.seahorse.Application.service
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.*xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.gnome.seahorse.Application.appdata.xml
%{_datadir}/seahorse/
%{_mandir}/man1/seahorse.1%{?ext_man}

%files -n gnome-shell-search-provider-seahorse
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/seahorse-search-provider.ini

%files lang -f %{name}.lang

%changelog
