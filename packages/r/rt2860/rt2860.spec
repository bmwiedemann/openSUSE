#
# spec file for package rt2860 (Version 1.8.0.0)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

%define SourceDir 2008_0918_RT2860_Linux_STA_v1.8.0.0

Name:           rt2860
Version:        1.8.0.0
Release:        3
Summary:        Userspace configuration files for rt2860 driver
Group:          Hardware/Wifi
License:        GPL-2.0+
Url:            http://www.ralinktech.com/ralink/Home/Support/Linux.html
Source0:        http://www.ralinktech.com.tw/data/drivers/%{SourceDir}.tar.bz2
Source1:        http://www.ralinktech.com.tw/data/drivers/ReleaseNote-RT2860.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Supplements:    modalias(pci:v00001A3Bd00001059sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001814d00000781sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001814d00000701sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001814d00000681sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001814d00000601sv*sd*bc*sc*i*)

%description
This package contains a small configuration file of the rt2860 driver,
currently read by the kernel module. In later versions this will go
away.



Authors:
--------
    Ralink Tech Inc.

%prep
%setup -q -n %{SourceDir}
iconv -f JOHAB -t UTF8 %{SOURCE1} -o ./ReleaseNotes
sed -i 's/\r//' ./ReleaseNotes
iconv -f JOHAB -t UTF8 README_STA -o README_STA
sed -i 's/\r//' README_STA

%build
echo "Nothing to build"

%install
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2860STA
install  -p -m 0644 RT2860STA.dat $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT2860STA

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ReleaseNotes README_STA iwpriv_usage.txt
%dir %{_sysconfdir}/Wireless
%dir %{_sysconfdir}/Wireless/RT2860STA
%config(noreplace) %{_sysconfdir}/Wireless/RT2860STA/RT2860STA.dat

%changelog
