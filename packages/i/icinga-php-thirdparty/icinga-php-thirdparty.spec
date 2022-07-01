#
# spec file for package icinga-php-thirdparty
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


%global revision 1
%global module_name icinga-php-thirdparty
%global basedir %{_datadir}/icinga-php/vendor
Name:           %{module_name}
Version:        0.11.0
Release:        %{revision}%{?dist}
Summary:        Icinga PHP Thirdparty for Icinga Web 2
License:        MIT
Group:          System/Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/%{module_name}/archive/v%{version}/%{module_name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  icinga-php-common
Requires:       icinga-php-common
# php extension requirements
Requires:       php-soap
Requires:       php-curl
Requires:       php-json
Requires:       php-sockets

%description
This package bundles all 3rd party PHP libraries
used by Icinga Web products into one piece,
which can be integrated as library into Icinga Web 2.

%prep
%setup -q

%build
# noting to build

%install
mkdir -vp %{buildroot}%{basedir}

cp -vr asset %{buildroot}%{basedir}
cp -vr vendor %{buildroot}%{basedir}
cp -vr composer.* %{buildroot}%{basedir}
cp -vr VERSION %{buildroot}%{basedir}

%fdupes %{buildroot}%{basedir}

%files
%doc README.md
%license LICENSE
%{basedir}

%changelog
