#
# spec file for package alsa-firmware
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


Name:           alsa-firmware
URL:            http://www.alsa-project.org/
Summary:        Firmware Data Files for ALSA
# BuildRequires:  automake
License:        GPL-2.0-or-later
Group:          Hardware/Other
BuildRequires:  fdupes
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
%endif
Version:        1.2.4
Release:        0
Source:         ftp://ftp.alsa-project.org/pub/firmware/alsa-firmware-%{version}.tar.bz2
Source1:        usx2yaudio.rules
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       alsa
# for asihpi
Supplements:    modalias(pci:v0000104Cd0000AC60sv0000175Csd*bc*sc*i*)
Supplements:    modalias(pci:v0000104Cd0000A106sv0000175Csd*bc*sc*i*)
# for ca0132
Supplements:    modalias(pci:v00001102d00000010sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001102d00000012sv*sd*bc*sc*i*)
# for cs46xx
Supplements:    modalias(pci:v00001013d00006004sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001013d00006003sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001013d00006001sv*sd*bc*sc*i*)
# for echoaudio
Supplements:    modalias(pci:v00001057d00001801sv0000ECC0sd*bc*sc*i*)
Supplements:    modalias(pci:v00001057d00003410sv0000ECC0sd*bc*sc*i*)
# for emu10k1
Supplements:    modalias(pci:v00001102d00000008sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001102d00000004sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001102d00000002sv*sd*bc*sc*i*)
# for hdsp
Supplements:    modalias(pci:v000010EEd00003FC5sv*sd*bc*sc*i*)
# for mixart
Supplements:    modalias(pci:v00001057d00000003sv*sd*bc*sc*i*)
# for pcxhr
Supplements:    modalias(pci:v000010B5d00009056sv00001369sd*bc*sc*i*)
# for usx2y
Supplements:    modalias(usb:v1604p8005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1604p8007d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1604p8001d*dc*dsc*dp*ic*isc*ip*in*)
# for vx
Supplements:    modalias(pci:v000010B5d00009030sv00001369sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B5d00009050sv00001369sd*bc*sc*i*)

%if 0%{?suse_version} > 1220
%define _udevdir %(pkg-config --variable=udevdir udev)
%else
%define _udevdir /etc/udev
%endif

%description
Various firmware data files for ALSA drivers.

%prep
%setup -q

%build
# autoreconf -fi
%configure \
    --enable-loader \
    --enable-hotplug \
    --with-hotplug-dir=/lib/firmware
make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" install
# remove duplicated entries that are already in kernel-firmware package
rm -f %{buildroot}/lib/firmware/ctefx.bin
rm -f %{buildroot}/lib/firmware/ctspeq.bin
# remove unnecessary loader firmwares
for d in vxloader mixartloader pcxhrloader; do
  rm -rf %{buildroot}%{_datadir}/alsa/firmware/$d
done
# some files are included in the new "kernel-firmware" package
for d in ess korg sb16 yamaha; do
  rm -rf %{buildroot}/lib/firmware/$d
done
# change identical files to symlinks for hdsploader
pushd %{buildroot}%{_datadir}/alsa/firmware/hdsploader
for i in *.bin; do
  hotplug=%{buildroot}/lib/firmware/$i
  if [ -f $hotplug ]; then
    if cmp -s -b $hotplug $i; then
      rm $i
      ln -s /lib/firmware/$i
    fi
  fi
done
popd
# FIXME: remove non-existing msnd firmware symlinks
rm -rf %{buildroot}/lib/firmware/turtlebeach
# install documents
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_licensedir}/%{name}
install -c -m 0644 COPYING %{buildroot}%{_licensedir}/%{name}
install -c -m 0644 README %{buildroot}%{_docdir}/%{name}
for d in echoaudio hdsploader mixartloader pcxhrloader usx2yloader vxloader asihpi ca0132; do
  (cd $d
  n=${d##*/}
  mkdir -p %{buildroot}%{_docdir}/%{name}/$n
  for f in AUTHORS ChangeLog README* TODO *.txt; do
    test -f $f || continue
    case $f in
	licen[cs]e*)
	    mkdir -p %{buildroot}%{_licensedir}/%{name}/$n
	    install -c -m 0644 $f %{buildroot}%{_licensedir}/%{name}/$n
	    ;;
	*)
	    install -c -m 0644 $f %{buildroot}%{_docdir}/%{name}/$n
	    ;;
    esac
  done
  )
done
# udev rules
install -D -c -m 0644 %{SOURCE1} %{buildroot}%{_udevdir}/rules.d/52-usx2yaudio.rules
%fdupes -s %{buildroot}

%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}
%license %{_licensedir}/%{name}
/lib/firmware/*
%{_datadir}/alsa
%{_udevdir}

%changelog
