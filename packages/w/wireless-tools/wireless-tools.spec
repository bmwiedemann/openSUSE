#
# spec file for package wireless-tools
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


%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files 50-ipw2200.conf 50-iwl3945.conf 50-prism54.conf

%define _udevdir %(pkg-config --variable=udevdir udev)

Name:           wireless-tools
Version:        30.pre9
Release:        0
Summary:        Tools for a wireless LAN
License:        GPL-2.0-only
Group:          Hardware/Wifi
URL:            https://hewlettpackard.github.io/wireless-tools/
Source:         https://hewlettpackard.github.io/wireless-tools/wireless_tools.30.pre9.tar.gz
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
mkdir -p %{buildroot}%{_modprobedir}
install -m644 %{SOURCE4} %{buildroot}%{_modprobedir}/50-ipw2200.conf
install -m644 %{SOURCE10} %{buildroot}%{_modprobedir}/50-iwl3945.conf
install -m644 %{SOURCE5} %{buildroot}%{_modprobedir}/50-prism54.conf

mkdir -p %{buildroot}%{_udevdir}
install -m755 %{SOURCE8} %{buildroot}%{_udevdir}/iwlwifi-led.sh
mkdir -p %{buildroot}%{_udevrulesdir}
install -m644 %{SOURCE9} %{buildroot}%{_udevrulesdir}/99-iwlwifi-led.rules
sed -i -e "s|@UDEVDIR@|%{_udevdir}|g" %{buildroot}%{_udevrulesdir}/99-iwlwifi-led.rules
%find_lang %{name} --with-man --all-name

%pre
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done

%post -n libiw30 -p /sbin/ldconfig
%postun -n libiw30 -p /sbin/ldconfig

%files -f %{name}.lang
%doc CHANGELOG.h PCMCIA.txt README*
%dir %{_modprobedir}
%{_sbindir}/*
%{_modprobedir}/*
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
