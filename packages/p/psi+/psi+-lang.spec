#
# spec file for package psi+-lang
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


%define version_unconverted 1.4.1473+0

Name:           psi+-lang
URL:            https://github.com/psi-plus/psi-plus-l10n
Version:        1.4.1473+0
Release:        0
Summary:        Translations for Psi+
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Talk/Clients
Source0:        psi-plus-l10n-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libqt5-linguist
# for qmake-qt5:
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  tar
BuildRequires:  xz
Requires:       psi+
BuildArch:      noarch
Obsoletes:      psi+-lang > 20100101

%description
Various translations for Psi+.

%prep
%setup -q -n psi-plus-l10n-%{version}

sed -i 's@\<lrelease\>@&-qt5@' update-translations.sh

%build
./update-translations.sh make

%install
install -d %{buildroot}%{_datadir}/psi-plus
install -m 0644 -t %{buildroot}%{_datadir}/psi-plus out/*.qm

%files
%defattr(-,root,root)
%dir %{_datadir}/psi-plus/
%{_datadir}/psi-plus/*.qm

%changelog
