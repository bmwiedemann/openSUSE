#
# spec file for package xca
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


Name:           xca
Version:        2.4.0
Release:        0
Summary:        An RSA key and certificate management tool
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
Summary(de):    Ein RSA-Schlüssel- und -Zertifikat-Managementprogramm
URL:            https://sourceforge.net/projects/xca/
Source:         https://github.com/chris2511/xca/releases/download/RELEASE.%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-desktop.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
%if 0%{suse_version} < 1550
BuildRequires:  pkgconfig(openssl)
%else
BuildRequires:  libopenssl-1_1-devel
%endif
#Requires:       libQt5Sql5-sqlite

%description
Graphical certification authority is an interface for managing RSA
keys and certificates, and the creation and signing of PKCS#10
requests. It uses the OpenSSL library and a Berkeley DB for key and
certificate storage. It supports importing and exporting keys and
PEM/DER/PKCS8 certificates, signing and revoking of PEM/DER/PKCS12,
and the selection of X509v3 extensions. A tree view of certificates
is presented.

%description -l de
"Graphical certification authority" ist ein Interface zum Verwalten
von RSA-Schlüsseln und -Zertifikaten, und dem Erzeugen und Signieren von
PKCS#10-Requests. Es verwendet die OpenSSL-Biliothek und Berkley DB
zum Speichern von Schlüsseln und Zerifkaten. Es unterstützt den
Import und Export von Schlüsseln und PEM/DER/PKCS#8-Zertifikaten,
das Signieren und Widerrufen von PEM/DER/PKCS12, und die
Auswahl von X509v3-Erweiterungen. Die Zertifikate werden in einer
Baumstruktur präsentiert.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q
%autopatch -p1

%build
%configure --with-qt-version=5 \
           --docdir=%{_datadir}/%{name}

%make_build destdir=%{buildroot} prefix=%{_prefix}

%install
%make_install destdir=%{buildroot} prefix=%{_prefix}
%suse_update_desktop_file -i %{name} DesktopUtility

%files
%doc AUTHORS changelog VERSION
%license COPYRIGHT
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/x-xca-*.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
