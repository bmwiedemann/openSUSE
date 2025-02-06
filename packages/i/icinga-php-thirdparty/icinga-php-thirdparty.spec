#
# spec file
#
# Copyright (c) 2025 SUSE LLC
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
Version:        0.12.1
Release:        %{revision}%{?dist}
Summary:        Icinga PHP Thirdparty for Icinga Web 2
License:        MIT
Group:          System/Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/%{module_name}/archive/v%{version}/%{module_name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  fdupes
Requires:       php-curl
Requires:       php-iconv
Requires:       php-json
# php extension requirements
Requires:       php-soap
Requires:       php-sockets
Obsoletes:      icinga-php-common < %{version}
Obsoletes:      icinga-php-common > %{version}
Provides:       icinga-php-common = %{version}
BuildArch:      noarch

%description
This package bundles all 3rd party PHP libraries
used by Icinga Web products into one piece,
which can be integrated as library into Icinga Web 2.

%prep
%setup -q
# rpmlintrc
find vendor/shardj -type f -name "*.php" -exec chmod -x {} \;
find vendor/predis -type f -name "*.sh" -exec chmod +x {} \;
chmod -x vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer/README
chmod -x vendor/shardj/zf1-future/README-GIT.md
chmod -x vendor/shardj/zf1-future/library/Zend/Locale/Data/fy.xml

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
%dir %{_datadir}/icinga-php
%{basedir}

%changelog
