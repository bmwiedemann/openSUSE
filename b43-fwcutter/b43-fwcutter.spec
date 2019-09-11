#
# spec file for package b43-fwcutter
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           b43-fwcutter
Version:        019
Release:        0
Summary:        Tool for extracting firmware from newer Broadcom WLAN drivers
License:        BSD-2-Clause
Group:          Hardware/Wifi
Url:            http://linuxwireless.org/en/users/Drivers/b43
Source:         http://bues.ch/b43/fwcutter/%{name}-%{version}.tar.bz2
Source1:        install_bcm43xx_firmware
Requires:       curl
Supplements:    modalias(pci:v000014E4d000043*sv*sd*bc*sc*i*)
#b43legacy
Supplements:    modalias(ssb:v4243id0812rev04*)
Supplements:    modalias(ssb:v4243id0812rev02*)
#b43
Supplements:    modalias(pcmcia:m02D0c0476f*fn*pfn*pa*pb*pc*pd*)
Supplements:    modalias(pcmcia:m02D0c0448f*fn*pfn*pa*pb*pc*pd*)
Supplements:    modalias(bcma:m04BFid0812rev1Dcl*)
Supplements:    modalias(bcma:m04BFid0812rev18cl*)
Supplements:    modalias(bcma:m04BFid0812rev17cl*)
Supplements:    modalias(bcma:m04BFid0812rev11cl*)
Supplements:    modalias(ssb:v4243id0812rev10*)
Supplements:    modalias(ssb:v4243id0812rev0F*)
Supplements:    modalias(ssb:v4243id0812rev0D*)
Supplements:    modalias(ssb:v4243id0812rev0C*)
Supplements:    modalias(ssb:v4243id0812rev0B*)
Supplements:    modalias(ssb:v4243id0812rev0A*)
Supplements:    modalias(ssb:v4243id0812rev09*)
Supplements:    modalias(ssb:v4243id0812rev07*)
Supplements:    modalias(ssb:v4243id0812rev06*)
Supplements:    modalias(ssb:v4243id0812rev05*)

Obsoletes:      bcm43xx-fwcutter < %{version}
Provides:       bcm43xx-fwcutter = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
b43-fwcutter can be used to extract firmware from Windows WLAN drivers
for Broadcom bcm43xx devices. The firmware is necessary to run such a
card under Linux using the b43 or b43legacy driver.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
#make PREFIX=%{buildroot}/usr \
#     MANDIR=%{buildroot}/%{_mandir} install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_sbindir}/
install -m 755 b43-fwcutter %{buildroot}%{_bindir}/
install -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}/lib/firmware/b43/
mkdir -p %{buildroot}/lib/firmware/b43legacy/
for i in a0g0bsinitvals5.fw a0g0bsinitvals9.fw a0g0initvals5.fw a0g0initvals9.fw a0g1bsinitvals13.fw a0g1bsinitvals5.fw a0g1bsinitvals9.fw a0g1initvals13.fw a0g1initvals5.fw a0g1initvals9.fw b0g0bsinitvals13.fw b0g0bsinitvals5.fw b0g0bsinitvals9.fw b0g0initvals13.fw b0g0initvals5.fw b0g0initvals9.fw lp0bsinitvals13.fw lp0bsinitvals14.fw lp0bsinitvals15.fw lp0bsinitvals16.fw lp0initvals13.fw lp0initvals14.fw lp0initvals15.fw lp0initvals16.fw n0absinitvals11.fw n0bsinitvals11.fw n0bsinitvals16.fw n0initvals11.fw n0initvals16.fw pcm5.fw sslpn0bsinitvals16.fw sslpn0initvals16.fw sslpn1bsinitvals20.fw sslpn1initvals20.fw sslpn2bsinitvals17.fw sslpn2bsinitvals19.fw sslpn2initvals17.fw sslpn2initvals19.fw sslpn4bsinitvals22.fw sslpn4initvals22.fw ucode11.fw ucode13.fw ucode14.fw ucode15.fw ucode16_lp.fw ucode16_mimo.fw ucode16_sslpn.fw ucode16_sslpn_nobt.fw ucode17.fw ucode19.fw ucode20.fw ucode22_sslpn.fw ucode5.fw ucode9.fw
do
     touch %{buildroot}/lib/firmware/b43/$i
done
for j in a0g0bsinitvals2.fw a0g0bsinitvals5.fw a0g0initvals2.fw a0g0initvals5.fw a0g1bsinitvals5.fw a0g1initvals5.fw b0g0bsinitvals2.fw b0g0bsinitvals5.fw b0g0initvals2.fw b0g0initvals5.fw pcm4.fw pcm5.fw ucode11.fw ucode2.fw ucode4.fw ucode5.fw
do
     touch %{buildroot}/lib/firmware/b43legacy/$j
done

%files
%defattr(-, root, root)
%doc README
%{_bindir}/b43-fwcutter
%{_sbindir}/install_bcm43xx_firmware
#%{_mandir}/man1/b43-fwcutter.1.gz
#/usr/man/man1/b43-fwcutter.1.gz
%dir /lib/firmware/b43
%dir /lib/firmware/b43legacy
# ghost b43 firmware
%ghost /lib/firmware/b43/a0g0bsinitvals5.fw
%ghost /lib/firmware/b43/a0g0bsinitvals9.fw
%ghost /lib/firmware/b43/a0g0initvals5.fw
%ghost /lib/firmware/b43/a0g0initvals9.fw
%ghost /lib/firmware/b43/a0g1bsinitvals13.fw
%ghost /lib/firmware/b43/a0g1bsinitvals5.fw
%ghost /lib/firmware/b43/a0g1bsinitvals9.fw
%ghost /lib/firmware/b43/a0g1initvals13.fw
%ghost /lib/firmware/b43/a0g1initvals5.fw
%ghost /lib/firmware/b43/a0g1initvals9.fw
%ghost /lib/firmware/b43/b0g0bsinitvals13.fw
%ghost /lib/firmware/b43/b0g0bsinitvals5.fw
%ghost /lib/firmware/b43/b0g0bsinitvals9.fw
%ghost /lib/firmware/b43/b0g0initvals13.fw
%ghost /lib/firmware/b43/b0g0initvals5.fw
%ghost /lib/firmware/b43/b0g0initvals9.fw
%ghost /lib/firmware/b43/lp0bsinitvals13.fw
%ghost /lib/firmware/b43/lp0bsinitvals14.fw
%ghost /lib/firmware/b43/lp0bsinitvals15.fw
%ghost /lib/firmware/b43/lp0bsinitvals16.fw
%ghost /lib/firmware/b43/lp0initvals13.fw
%ghost /lib/firmware/b43/lp0initvals14.fw
%ghost /lib/firmware/b43/lp0initvals15.fw
%ghost /lib/firmware/b43/lp0initvals16.fw
%ghost /lib/firmware/b43/n0absinitvals11.fw
%ghost /lib/firmware/b43/n0bsinitvals11.fw
%ghost /lib/firmware/b43/n0bsinitvals16.fw
%ghost /lib/firmware/b43/n0initvals11.fw
%ghost /lib/firmware/b43/n0initvals16.fw
%ghost /lib/firmware/b43/pcm5.fw
%ghost /lib/firmware/b43/sslpn0bsinitvals16.fw
%ghost /lib/firmware/b43/sslpn0initvals16.fw
%ghost /lib/firmware/b43/sslpn1bsinitvals20.fw
%ghost /lib/firmware/b43/sslpn1initvals20.fw
%ghost /lib/firmware/b43/sslpn2bsinitvals17.fw
%ghost /lib/firmware/b43/sslpn2bsinitvals19.fw
%ghost /lib/firmware/b43/sslpn2initvals17.fw
%ghost /lib/firmware/b43/sslpn2initvals19.fw
%ghost /lib/firmware/b43/sslpn4bsinitvals22.fw
%ghost /lib/firmware/b43/sslpn4initvals22.fw
%ghost /lib/firmware/b43/ucode11.fw
%ghost /lib/firmware/b43/ucode13.fw
%ghost /lib/firmware/b43/ucode14.fw
%ghost /lib/firmware/b43/ucode15.fw
%ghost /lib/firmware/b43/ucode16_lp.fw
%ghost /lib/firmware/b43/ucode16_mimo.fw
%ghost /lib/firmware/b43/ucode16_sslpn.fw
%ghost /lib/firmware/b43/ucode16_sslpn_nobt.fw
%ghost /lib/firmware/b43/ucode17.fw
%ghost /lib/firmware/b43/ucode19.fw
%ghost /lib/firmware/b43/ucode20.fw
%ghost /lib/firmware/b43/ucode22_sslpn.fw
%ghost /lib/firmware/b43/ucode5.fw
%ghost /lib/firmware/b43/ucode9.fw
# ghost b43legacy firmware
%ghost /lib/firmware/b43legacy/a0g0bsinitvals2.fw
%ghost /lib/firmware/b43legacy/a0g0bsinitvals5.fw
%ghost /lib/firmware/b43legacy/a0g0initvals2.fw
%ghost /lib/firmware/b43legacy/a0g0initvals5.fw
%ghost /lib/firmware/b43legacy/a0g1bsinitvals5.fw
%ghost /lib/firmware/b43legacy/a0g1initvals5.fw
%ghost /lib/firmware/b43legacy/b0g0bsinitvals2.fw
%ghost /lib/firmware/b43legacy/b0g0bsinitvals5.fw
%ghost /lib/firmware/b43legacy/b0g0initvals2.fw
%ghost /lib/firmware/b43legacy/b0g0initvals5.fw
%ghost /lib/firmware/b43legacy/pcm4.fw
%ghost /lib/firmware/b43legacy/pcm5.fw
%ghost /lib/firmware/b43legacy/ucode11.fw
%ghost /lib/firmware/b43legacy/ucode2.fw
%ghost /lib/firmware/b43legacy/ucode4.fw
%ghost /lib/firmware/b43legacy/ucode5.fw

%changelog
