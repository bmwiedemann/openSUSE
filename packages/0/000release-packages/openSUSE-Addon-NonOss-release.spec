#
# spec file for package openSUSE-Addon-NonOss-release (Version 20200907)
#
# Copyright (c) 2020 openSUSE.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           openSUSE-Addon-NonOss-release
%define         product openSUSE-Addon-NonOss
Summary:        openSUSE NonOSS Addon%{?betaversion: %{betaversion}}
Version:        20200907
Release:        0
License:        BSD-3-Clause
Group:          System/Fhs

Provides:       %name-%version
Provides:       product() = openSUSE-Addon-NonOss
Provides:       product(openSUSE-Addon-NonOss) = 20200907-0
Provides:       product-label() = non%20oss%20addon
Provides:       product-cpeid() = cpe%3A%2Fo%3Aopensuse%3Aopensuse%2Daddon%2Dnonoss%3A20200907


AutoReqProv:    on
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
non oss repo and cd




%prep

%build


%install
mkdir -p $RPM_BUILD_ROOT/etc/products.d
cat >$RPM_BUILD_ROOT/etc/products.d/openSUSE-Addon-NonOss.prod << EOF
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>openSUSE</vendor>
  <name>openSUSE-Addon-NonOss</name>
  <version>20200907</version>
  <release>0</release>
  <arch>%{_target_cpu}</arch>
  <cpeid>cpe:/o:opensuse:opensuse-addon-nonoss:20200907</cpeid>
  <register>
    <pool>
    </pool>
    <updates>
    </updates>
  </register>
  <repositories>
  </repositories>
  <summary>openSUSE NonOSS Addon</summary>
  <shortsummary>non oss addon</shortsummary>
  <description>non oss repo and cd</description>
  <linguas>
    <language>af</language>
    <language>ar</language>
    <language>be_BY</language>
    <language>bg</language>
    <language>br</language>
    <language>ca</language>
    <language>cy</language>
    <language>el</language>
    <language>et</language>
    <language>ga</language>
    <language>gl</language>
    <language>gu_IN</language>
    <language>he</language>
    <language>hi_IN</language>
    <language>hr</language>
    <language>ka</language>
    <language>km</language>
    <language>ko</language>
    <language>lt</language>
    <language>mk</language>
    <language>nn</language>
    <language>pa_IN</language>
    <language>rw</language>
    <language>sk</language>
    <language>sl</language>
    <language>sr_CS</language>
    <language>ss</language>
    <language>st</language>
    <language>tg</language>
    <language>th</language>
    <language>tr</language>
    <language>uk</language>
    <language>ve</language>
    <language>vi</language>
    <language>xh</language>
    <language>zu</language>
  </linguas>
  <urls>
  </urls>
  <buildconfig>
    <producttheme>openSUSE</producttheme>
    <allowresolving>false</allowresolving>
  </buildconfig>
  <installconfig>
    <datadir>suse</datadir>
    <descriptiondir>suse/setup/descr</descriptiondir>
    <releasepackage name="openSUSE-release" flag="EQ" version="13.1" release="%{release}"/>
    <distribution>openSUSE-Addon-NonOss</distribution>
  </installconfig>
  <runtimeconfig/>
</product>

EOF



%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%dir /etc/products.d
/etc/products.d/*.prod

%changelog
