#
# spec file for package wireless-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _udevdir %(pkg-config --variable=udevdir udev)

Name:           wireless-tools
Version:        30.pre9
Release:        0
Summary:        Tools for a wireless LAN
License:        GPL-2.0
Group:          Hardware/Wifi
Url:            http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
Source:         http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}.tar.gz
Source2:        suse-files.tar.gz
Source4:        ipw2200.modprobe
Source5:        prism54.modprobe
Source6:        lwepgen.tar.bz2
Source8:        iwlwifi-led.sh
Source9:        99-iwlwifi-led.rules
Source10:       iwl3945.modprobe
Patch0:         wireless_tools.dif
Patch1:         lwepgen-as-needed.patch
BuildRequires:  openssl-devel
Requires:       libiw = %{version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)

%package -n libiw30
Summary:        Tools for a wireless LAN
Group:          Hardware/Wifi
Provides:       libiw

%package -n libiw-devel
Summary:        Tools for a wireless LAN
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libiw30 = %{version}

%description
This package contains the wireless tools, used to manipulate the
wireless extensions. The wireless extension is an interface that allows
you to set wireless LAN specific parameters and get specific stats.

%description -n libiw30
This package contains the wireless tools, used to manipulate the
wireless extensions. The wireless extension is an interface that allows
you to set wireless LAN specific parameters and get specific stats.

%description -n libiw-devel
This package contains the wireless tools, used to manipulate the
wireless extensions. The wireless extension is an interface that allows
you to set wireless LAN specific parameters and get specific stats.

%prep
%setup -q -T -b 6 -n lwepgen
%setup -q -n wireless_tools.30
%patch0
pushd ../lwepgen
%patch1
popd

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"
make %{?_smp_mflags} CFLAGS="%{optflags}" -C ../lwepgen

%install
make INSTALL_DIR="%{buildroot}/%{_sbindir}" \
	 INSTALL_INC="%{buildroot}/%{_includedir}" \
	 INSTALL_LIB="%{buildroot}/%{_libdir}" \
	 INSTALL_MAN="%{buildroot}/%{_mandir}" \
	 DOCDIR=%{_defaultdocdir}/wireless-tools \
	 PREFIX="%{buildroot}%{_prefix}" \
	 install

tar -xvzf %{SOURCE2}
install -m755 install_intersil_firmware %{buildroot}%{_sbindir}
install -m755 install_acx100_firmware %{buildroot}%{_sbindir}
install -m755 ../lwepgen/lwepgen %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/modprobe.d/50-ipw2200.conf
install -m644 %{SOURCE10} %{buildroot}%{_sysconfdir}/modprobe.d/50-iwl3945.conf
install -m644 %{SOURCE5} %{buildroot}%{_sysconfdir}/modprobe.d/50-prism54.conf

mkdir -p %{buildroot}%{_udevdir}
install -m755 %{SOURCE8} %{buildroot}%{_udevdir}/iwlwifi-led.sh
mkdir -p %{buildroot}%{_udevrulesdir}
install -m644 %{SOURCE9} %{buildroot}%{_udevrulesdir}/99-iwlwifi-led.rules
sed -i -e "s|@UDEVDIR@|%{_udevdir}|g" %{buildroot}%{_udevrulesdir}/99-iwlwifi-led.rules
%find_lang %{name} --with-man --all-name

%post -n libiw30 -p /sbin/ldconfig
%postun -n libiw30 -p /sbin/ldconfig

%files -f %{name}.lang
%doc CHANGELOG.h PCMCIA.txt README*
%dir %{_sysconfdir}/modprobe.d
%{_sbindir}/*
%config %{_sysconfdir}/modprobe.d/*
%{_udevdir}
%{_udevdir}/iwlwifi-led.sh
%dir %{_mandir}/cs
%dir %{_mandir}/fr.ISO8859-1
%dir %{_mandir}/fr.UTF-8
%{_mandir}/man?/*%{ext_man}
%{_udevrulesdir}/99-iwlwifi-led.rules

%files -n libiw30
%{_libdir}/libiw.so.*

%files -n libiw-devel
%{_libdir}/libiw.so
%{_includedir}/iwlib.h
%{_includedir}/wireless.h

%changelog
