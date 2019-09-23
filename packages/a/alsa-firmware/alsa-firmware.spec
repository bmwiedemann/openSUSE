#
# spec file for package alsa-firmware
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           alsa-firmware
%define package_version	1.0.29
Url:            http://www.alsa-project.org/
Summary:        Firmware Data Files for ALSA
License:        GPL-2.0+
Group:          Hardware/Other
BuildRequires:  automake
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
%endif
Version:        1.0.29
Release:        0
Source:         ftp://ftp.alsa-project.org/pub/firmware/alsa-firmware-%{package_version}.tar.bz2
Source1:        usx2yaudio.rules
Source2:        usx2yaudio-old.rules
Source3:        ctefx-desktop.bin
Source4:        ctefx-r3di.bin
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       alsa
%if 0%{?suse_version} > 1220
%define _udevdir %(pkg-config --variable=udevdir udev)
%else
%define _udevdir /etc/udev
%endif

%description
Various firmware data files for ALSA drivers.

%prep
%setup -q -n %{name}-%{package_version}

%build
# autoreconf -fi
%configure \
    --enable-loader \
    --enable-hotplug \
    --with-hotplug-dir=/lib/firmware
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install
# remove unnecessary loader firmwares
for d in vxloader mixartloader pcxhrloader; do
  rm -rf $RPM_BUILD_ROOT%{_datadir}/alsa/firmware/$d
done
%if 0%{?suse_version} >= 1120
# some files are included in the new "kernel-firmware" package
for d in ess korg sb16 yamaha; do
  rm -rf $RPM_BUILD_ROOT/lib/firmware/$d
done
%endif
install -c -m 0644 %{SOURCE3} %{buildroot}/lib/firmware/
install -c -m 0644 %{SOURCE4} %{buildroot}/lib/firmware/
# change identical files to symlinks for hdsploader
pushd $RPM_BUILD_ROOT%{_datadir}/alsa/firmware/hdsploader
for i in *.bin; do
  hotplug=$RPM_BUILD_ROOT/lib/firmware/$i
  if [ -f $hotplug ]; then
    if cmp -s -b $hotplug $i; then
      rm $i
      ln -s /lib/firmware/$i
    fi
  fi
done
popd
# FIXME: remove non-existing msnd firmware symlinks
rm -rf $RPM_BUILD_ROOT/lib/firmware/turtlebeach
# install documents
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
for d in echoaudio hdsploader mixartloader pcxhrloader usx2yloader vxloader asihpi ca0132; do
  (cd $d
  n=${d##*/}
  mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/$n
  for f in AUTHORS COPYING ChangeLog NEWS README* TODO creative.txt; do
    test -f $f || continue
    install -c -m 0644 $f $RPM_BUILD_ROOT%{_docdir}/%{name}/$n
  done
  )
done
# udev rules
%if 0%{?suse_version} > 1020
install -D -c -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_udevdir}/rules.d/52-usx2yaudio.rules
%else
install -D -c -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_udevdir}/rules.d/52-usx2yaudio.rules
%endif

%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}
/lib/firmware/*
%{_datadir}/alsa
%{_udevdir}

%changelog
