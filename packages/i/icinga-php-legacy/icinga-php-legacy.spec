#
# spec file for package icinga-php-library
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global revision 1
%global module_name icinga-php-legacy
%global basedir %{_datadir}/icinga-php/legacy
Name:           %{module_name}
Version:        1.1.0
Release:        %{revision}%{?dist}
Summary:        Icinga PHP Legacy for Icinga Web 2
License:        MIT
Group:          System/Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/%{module_name}/archive/v%{version}/%{module_name}-%{version}.tar.gz
BuildRequires:  fdupes
Requires:       icingaweb2 >= 2.9
Requires:       php >= 8.2
Requires:       php-gettext
Requires:       php-intl
Requires:       php-json
Requires:       php-openssl
Requires:       php-pdo
Obsoletes:      icinga-php-common < %{version}
Obsoletes:      icinga-php-common > %{version}
Provides:       icinga-php-common = %{version}
BuildArch:      noarch

%description
Maintenance-only forks of abandoned upstream packages; for internal use only.
Replaces archived Icinga Incubator.

%prep
%setup -q
find . -type f "(" -name '.github' -o -name '.gitignore' -o -name '.keep' ")" -delete

%build
# nothing to build

%install
mkdir -vp %{buildroot}%{basedir}

cp -vr asset %{buildroot}%{basedir}
cp -vr gipfl %{buildroot}%{basedir}
cp -vr vendor %{buildroot}%{basedir}
cp -vr composer.* %{buildroot}%{basedir}
cp -vr VERSION %{buildroot}%{basedir}

%fdupes %{buildroot}%{basedir}

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/icinga-php
%{basedir}

%changelog
