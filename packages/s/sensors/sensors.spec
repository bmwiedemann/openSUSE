#
# spec file for package sensors
#
# Copyright (c) 2024 SUSE LLC
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


#%%define   commit          1c48b191c8a2b9fc747e3db3816247c666c5c3f1
#%%define   shortcommit     1c48b19
%define   _name           lm-sensors
%define   _version        3-6-2
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           sensors
Version:        %(echo %{_version} | tr '-' '.')
Release:        0
Summary:        Hardware health monitoring for Linux
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/lm-sensors/%{_name}
Source0:        https://github.com/hramrach/%{_name}/archive/V%{_version}.tar.gz#/%{_name}-%{_version}.tar.gz
Source1:        sysconfig.sensord
Source2:        baselibs.conf
Patch1:         lm_sensors-3.1.1-build.patch
Patch2:         lm_sensors-3.0.0-sensord-separate.patch
Patch3:         lm_sensors-3.0.0-sysconfig_metadata.patch
Patch4:         lm_sensors-3.0.3-hint-at-kernel-extra-package.patch
Patch8:         lm_sensors-3.5.0-libsensors-fix-soname.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  perl-Test-Cmd
BuildRequires:  rrdtool-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  valgrind
Requires:       modutils
%{?systemd_requires}

%description
This package includes programs that show data from some sensor chips.
The interface /proc/bus/i2c/ is provided by loading kernel modules.
Which modules to load can be interactively detected as root by calling
%{_sbindir}/sensors-detect. Warning, before using the sensors the default
configuration in %{_sysconfdir}/sensors.conf has to be checked and changed to fit
the actual set up of the mainboard and the BIOS used on that specific
mainboard!

%package -n sensord
Summary:        Hardware health monitoring daemon
License:        GPL-2.0-or-later
Group:          System/Monitoring
Requires(pre):  %fillup_prereq
Provides:       sensors:%{_sbindir}/sensord

%description -n sensord
sensord is a daemon that can be used to periodically log sensor
readings from hardware health-monitoring chips to the system logs or a
round-robin database (RRD) and to alert when a sensor alarm is
signalled; for example, if a fan fails, a temperature limit is
exceeded, etc.

%package -n libsensors4
Summary:        Hardware health monitoring library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libsensors4
libsensors offers a way for applications to access the hardware
monitoring chips of the system. A system-dependent configuration file
controls how the different inputs are labeled and what scaling factors
have to be applied for the specific hardware, so that the output makes
sense to the user.

%package -n libsensors4-devel
Summary:        Hardware health monitoring library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libsensors4 = %{version}
Provides:       sensors:%{_includedir}/sensors/sensors.h

%description -n libsensors4-devel
libsensors offers a way for applications to access the hardware
monitoring chips of the system. A system-dependent configuration file
controls how the different inputs are labeled and what scaling factors
have to be applied for the specific hardware, so that the output makes
sense to the user.

%prep
%autosetup -p1 -n %{_name}-%{_version}

%build
RPM_OPT_FLAGS="%{optflags}"
make %{?_smp_mflags} PROG_EXTRA:=sensord BUILD_STATIC_LIB:=0 PREFIX=%{_prefix} MANDIR=%{_mandir} LIBDIR=%{_libdir}

%install
    make PROG_EXTRA:=sensord BUILD_STATIC_LIB:=0 PREFIX=%{_prefix} MANDIR=%{_mandir} LIBDIR=%{_libdir} DESTDIR=%{buildroot} install
    mkdir -p				%{buildroot}/%{_docdir}/sensors %{buildroot}/%{_docdir}/sensord
    cp -a doc/donations doc/fan-divisors \
	  doc/fancontrol.txt doc/libsensors-API.txt \
	  doc/progs doc/temperature-sensors \
	  doc/vid COPYING COPYING.LGPL	%{buildroot}/%{_docdir}/sensors/
    cp -a COPYING			%{buildroot}/%{_docdir}/sensord/
    chmod -R u+rwX,g+rX,o+rX		%{buildroot}/%{_docdir}/sensors/ %{buildroot}/%{_docdir}/sensord/
    chmod 0755 %{buildroot}/%{_libdir}/libsensors.so.*
    mkdir -p				%{buildroot}/%{_unitdir} %{buildroot}/%{_fillupdir}
    cp -a prog/init/*.service 		%{buildroot}/%{_unitdir}/
    ln -sf service			%{buildroot}%{_sbindir}/rclm_sensors
    ln -sf service			%{buildroot}%{_sbindir}/rcfancontrol
    ln -sf service			%{buildroot}%{_sbindir}/rcsensord
    cp -a %{SOURCE1}			%{buildroot}/%{_fillupdir}

%check
make test

%pre
%service_add_pre lm_sensors.service fancontrol.service

%post
sh -c '
CONFIG=%{_sysconfdir}/sysconfig/lm_sensors
test -r "$CONFIG" || exit 0
unset ${!MODULE_*} $HWMON_MODULES
. "$CONFIG"
test -n "$HWMON_MODULES" && exit 0
for i in ${!MODULE_*} ; do
        eval module=\$$i
        if test -z "$HWMON_MODULES" ; then
                HWMON_MODULES="$module"
        else
                HWMON_MODULES="$HWMON_MODULES $module"
        fi
done
test -z "$HWMON_MODULES" && exit 0
echo >> "$CONFIG"
echo "# New configuration format generated by rpm post-install script" >> "$CONFIG"
echo "HWMON_MODULES=\"$HWMON_MODULES\"" >> "$CONFIG"
'
if test -e %{_sysconfdir}/modprobe.d/lm_sensors -a ! -e %{_sysconfdir}/modprobe.d/lm_sensors.conf ; then
	mv -f %{_sysconfdir}/modprobe.d/lm_sensors %{_sysconfdir}/modprobe.d/lm_sensors.conf
fi
%service_add_post lm_sensors.service fancontrol.service

%preun
%service_del_preun fancontrol.service lm_sensors.service

%postun
%service_del_postun fancontrol.service lm_sensors.service

%pre -n sensord
%service_add_pre sensord.service

%post -n sensord
%service_add_post sensord.service
%{fillup_only -n sensord}

%preun -n sensord
%service_del_preun sensord.service

%postun -n sensord
%service_del_postun sensord.service

%post -n libsensors4 -p /sbin/ldconfig
%postun -n libsensors4 -p /sbin/ldconfig

%files
%{_unitdir}/lm_sensors.service
%{_sbindir}/rclm_sensors
%{_unitdir}/fancontrol.service
%{_sbindir}/rcfancontrol
%{_bindir}/*
%{_sbindir}/fancontrol
%ifarch i386 i486 i586 i686 x86_64
%{_sbindir}/isadump
%{_sbindir}/isaset
%endif
%{_sbindir}/pwmconfig
%{_sbindir}/sensors-detect
%dir %{_docdir}/sensors
%doc %{_docdir}/sensors/donations
%doc %{_docdir}/sensors/fan-divisors
%doc %{_docdir}/sensors/fancontrol.txt
%doc %{_docdir}/sensors/progs
%doc %{_docdir}/sensors/temperature-sensors
%doc %{_docdir}/sensors/vid
%license %{_docdir}/sensors/COPYING
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man8/fancontrol.8%{?ext_man}
%ifarch i386 i486 i586 i686 x86_64
%{_mandir}/man8/isadump.8%{?ext_man}
%{_mandir}/man8/isaset.8%{?ext_man}
%endif
%{_mandir}/man8/pwmconfig.8%{?ext_man}
%{_mandir}/man8/sensors-conf-convert.8%{?ext_man}
%{_mandir}/man8/sensors-detect.8%{?ext_man}
%{_datadir}/zsh/site-functions/

%files -n sensord
%{_unitdir}/sensord.service
%{_sbindir}/rcsensord
%{_fillupdir}/sysconfig.sensord
%{_sbindir}/sensord
%dir %{_docdir}/sensord
%license %{_docdir}/sensord/COPYING
%{_mandir}/man8/sensord.8%{?ext_man}

%files -n libsensors4
%config %{_sysconfdir}/sensors3.conf
%config %{_sysconfdir}/sensors.d/
%{_libdir}/libsensors.so.4*
%dir %{_docdir}/sensors
%license %{_docdir}/sensors/COPYING.LGPL
%{_mandir}/man5/*.5%{?ext_man}

%files -n libsensors4-devel
%{_includedir}/sensors/
%{_libdir}/libsensors.so
%dir %{_docdir}/sensors
%doc %{_docdir}/sensors/libsensors-API.txt
%{_mandir}/man3/*.3%{?ext_man}

%changelog
