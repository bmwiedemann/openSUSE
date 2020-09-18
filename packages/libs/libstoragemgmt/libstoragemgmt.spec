#
# spec file for package libstoragemgmt
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


%define libname %{name}1
%bcond_with test
%if 0%{?suse_version} >= 1500 || %{with python3}
%define python3 1
%define python_sitelib %{python3_sitelib}
%else
%define python3 0
%endif
Name:           libstoragemgmt
Version:        1.8.5
Release:        0
Summary:        Storage array management library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libstorage/libstoragemgmt
Source0:        https://github.com/libstorage/libstoragemgmt/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libconfig-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%systemd_requires
%if 0%{python3}
BuildRequires:  python3-devel
BuildRequires:  python3-pywbem
BuildRequires:  python3-six
Requires:       python3-six
%else
BuildRequires:  python-devel
BuildRequires:  python-pywbem
BuildRequires:  python-six
Requires:       python-six
%endif
%if 0%{python3}
Requires:       python3-%{name}
%else
Requires:       python2-%{name}
%endif
%if %{with test}
BuildRequires:  chrpath
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  procps
BuildRequires:  valgrind
BuildRequires:  pkgconfig(check)
%endif

%description
The libStorageMgmt library will provide a vendor agnostic open source storage
application programming interface (API) that will allow management of storage
arrays.  The library includes a command line interface for interactive use and
scripting (command lsmcli).  The library also has a daemon that is used for
executing plug-ins in a separate process (lsmd).

%package        -n %{libname}
Summary:        Storage array management library
Group:          System/Libraries

%description    -n %{libname}
The libStorageMgmt library will provide a vendor agnostic open source storage
application programming interface (API) that will allow management of storage
arrays.  The library includes a command line interface for interactive use and
scripting (command lsmcli).  The library also has a daemon that is used for
executing plug-ins in a separate process (lsmd).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{python3}
%package        -n python3-%{name}
%else
%package        -n python2-%{name}
%endif

%{?python_provide:%python_provide python3-%{name}}
Summary:        Python client libraries and plug-in support for %{name}
Group:          Development/Languages/Python
BuildArch:      noarch
Requires:       %{name} = %{version}
%if 0%{python3}
Requires:       python3-%{name}-clibs

%description        -n python3-%{name}
%else
Requires:       python2-%{name}-clibs

%description        -n python2-%{name}
%endif
The python-%{name} package contains python client libraries as
well as python framework support and open source plug-ins written in python.

%if 0%{python3}
%package        -n python3-%{name}-clibs
%else
%package        -n python2-%{name}-clibs
%endif

%{?python_provide:%python_provide python3-%{name}-clibs}
Summary:        Python C extension for %{name}
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}
%if 0%{python3}
%description    -n python3-%{name}-clibs
%else
%description    -n python2-%{name}-clibs
%endif
The python-%{name}-clibs package contains python C extentions for %{name}.

%package        smis-plugin
Summary:        Files for SMI-S generic array support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch
%if 0%{python3}
Requires:       python3-pywbem
%else
Requires:       python-pywbem
%endif

%description    smis-plugin
The %{name}-smis-plugin package contains plug-in for generic
Storage Management Initiative Specification (SMI-S) array support.

%package        netapp-plugin
Summary:        Files for NetApp array support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    netapp-plugin
The %{name}-netapp-plugin package contains plug-in for NetApp array
support.

%package        targetd-plugin
Summary:        Files for targetd array support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    targetd-plugin
The %{name}-targetd-plugin package contains plug-in for targetd
array support.

%package        nstor-plugin
Summary:        Files for NexentaStor array support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    nstor-plugin
The %{name}-nstor-plugin package contains plug-in for NexentaStor
array support.

%package        udev
Summary:        Udev files for %{name}
Group:          System/Base

%description    udev
The %{name}-udev package contains udev rules and helper utilities for
uevents generated by the kernel.

%package        megaraid-plugin
Summary:        Files for LSI MegaRAID support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    megaraid-plugin
The %{name}-megaraid-plugin package contains the plugin for LSI MegaRAID
storage management via storcli.

%package        hpsa-plugin
Summary:        Files for HP SmartArray support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    hpsa-plugin
The %{name}-hpsa-plugin package contains the plugin for HP SmartArray storage
management via hpssacli.

%package        nfs-plugin
Summary:        Files for nfs support for %{name}
Group:          Development/Languages/Python
Requires:       %{name}-nfs-plugin-clibs = %{version}
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    nfs-plugin
The %{name}-nfs-plugin package contains the plugin for nfs based storage.

%package        nfs-plugin-clibs
Summary:        Python C extension module for %{name} NFS plugin
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description    nfs-plugin-clibs
The %{name}-nfs-plugin-clibs package contains python C extension for %{name}
NFS plugin.

%package        local-plugin
Summary:        Files for HP local pseudo support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    local-plugin
The %{name}-local-plugin package contains the plugin for local pseudo
storage.

%package        arcconf-plugin
Summary:        Files for Microsemi storage support for %{name}
Group:          Development/Languages/Python
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    arcconf-plugin
The %{name}-arcconf-plugin package contains the plugin for Microsemi
storage.

%prep
%setup -q

%build
# Needed for patch0
autoreconf -fiv
%configure \
  --disable-static \
  --with-bash-completion-dir=%{_datadir}/bash-completion/completions/ \
%if 0%{python3}
  --with-python3 \
%endif
%if ! %{with test}
  --without-test
%endif

#Fix rpmlint Error: env-script-interpreter
#Should change it  after configure
pyfiles=(plugin/megaraid/megaraid_lsmplugin \
         plugin/hpsa/hpsa_lsmplugin \
         plugin/targetd/targetd_lsmplugin \
         plugin/sim/sim_lsmplugin \
         plugin/local/local_lsmplugin \
         plugin/nstor/nstor_lsmplugin \
         plugin/arcconf/arcconf_lsmplugin \
         plugin/smispy/smispy_lsmplugin \
         plugin/ontap/ontap_lsmplugin \
         plugin/nfs/nfs_lsmplugin \
         tools/lsmcli/lsmcli \
         test/cmdtest.py \
         test/plugin_test.py \
        )

head -vn 1 ${pyfiles[@]}
sed -i '/^#!\/usr\/bin/s|env python|python|' ${pyfiles[@]}
head -vn 1 ${pyfiles[@]}

#Fix rpmlint Warning: non-executable-script
pyfiles=(tools/use_cases/find_unused_lun.py \
        )

head -vn 1 ${pyfiles[@]}
sed -i '/^#!/d' ${pyfiles[@]}
head -vn 1 ${pyfiles[@]}

make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

install -d -m755 %{buildroot}%{_sbindir}

install -Dpm 0644 packaging/daemon/libstoragemgmt.service \
    %{buildroot}%{_unitdir}/libstoragemgmt.service
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

#Files for udev handling
install -d %{buildroot}%{_udevrulesdir}
install -m 644 tools/udev/90-scsi-ua.rules \
    %{buildroot}%{_udevrulesdir}/90-scsi-ua.rules
install -m 755 tools/udev/scan-scsi-target \
    %{buildroot}%{_prefix}/lib/udev/scan-scsi-target

# find all duplicates
%fdupes -s %{buildroot}%{python_sitelib}

%if %{with test}
%check
if ! make check
then
    cat test-suite.log || true
    exit 1
fi
%endif

%pre
if [ $1 -eq 1 ]; then
    # New install
    getent group %{name} >/dev/null || groupadd -r %{name}
    getent passwd %{name} >/dev/null || \
        useradd -r -g %{name} -d %{_localstatedir}/run/lsm -s /sbin/nologin \
        -c "daemon account for libstoragemgmt" %{name}
fi

%service_add_pre %{name}.service

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post
%service_add_post %{name}.service
# Create tmp socket file on package new install.
if [ $1 -eq 1 -a -x %{_bindir}/systemd-tmpfiles ]; then
%if 0%{?suse_version} <= 1320
    systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || :
%else
    %tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%endif
fi

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%post smis-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun smis-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post netapp-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun netapp-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post targetd-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun targetd-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post nstor-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun nstor-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post megaraid-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun megaraid-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post hpsa-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun hpsa-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post nfs-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun nfs-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post local-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun local-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post arcconf-plugin
if [ $1 -eq 1 ]; then
    # New install.
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%postun arcconf-plugin
if [ $1 -eq 0 ]; then
    # Remove
    %{_bindir}/systemctl try-restart ${name}.service || :
fi

%post udev
%udev_rules_update

%files
%{_mandir}/man1/lsmcli.1%{ext_man}
%{_mandir}/man1/lsmd.1%{ext_man}
%{_mandir}/man5/lsmd.conf.5*
%{_bindir}/lsmcli
%{_bindir}/lsmd
%{_bindir}/simc_lsmplugin
%{_mandir}/man1/simc_lsmplugin.1%{ext_man}
%{_unitdir}/libstoragemgmt.service
%{_tmpfilesdir}/%{name}.conf
%dir %{_sysconfdir}/lsm
%{_datadir}/bash-completion/completions/lsmcli
%config(noreplace) %{_sysconfdir}/lsm/lsmd.conf
%dir %{_sysconfdir}/lsm/pluginconf.d
%{_sbindir}/rclibstoragemgmt
%ghost %dir /run/lsm
%ghost %dir /run/lsm/ipc

%files udev
%{_prefix}/lib/udev/scan-scsi-target
%{_udevrulesdir}/90-scsi-ua.rules

%files -n %{libname}
%license COPYING.LIB
%doc README
%{_libdir}/libstoragemgmt.so.*

%files devel
%{_includedir}/*
%{_mandir}/man3/*%{ext_man}
%{_libdir}/libstoragemgmt.so
%{_libdir}/pkgconfig/libstoragemgmt.pc

%if 0%{python3}
%files -n python3-%{name}
%else
%files -n python2-%{name}
%endif
%dir %{python_sitelib}/lsm
%{python_sitelib}/lsm/external
%{python_sitelib}/lsm/_*.py*
%{python_sitelib}/lsm/version.*

%if 0%{python3}
%dir %{python_sitelib}/lsm/__pycache__
%{python_sitelib}/lsm/__pycache__/*
%dir %{python_sitelib}/lsm/plugin/__pycache__
%{python_sitelib}/lsm/plugin/__pycache__/*
%dir %{python_sitelib}/lsm/plugin/sim/__pycache__
%{python_sitelib}/lsm/plugin/sim/__pycache__/*
%dir %{python_sitelib}/lsm/lsmcli/__pycache__
%{python_sitelib}/lsm/lsmcli/__pycache__/*
%endif
%{python_sitelib}/lsm/lsmcli/__init__.*
%{python_sitelib}/lsm/lsmcli/data_display.*
%{python_sitelib}/lsm/lsmcli/cmdline.*
%dir %{python_sitelib}/lsm/plugin
%{python_sitelib}/lsm/plugin/__init__.*
%dir %{python_sitelib}/lsm/plugin/sim
%{python_sitelib}/lsm/plugin/sim/*.py*
%dir %{python_sitelib}/lsm/lsmcli
%{_bindir}/sim_lsmplugin
%dir %{_libexecdir}/lsm.d
%{_libexecdir}/lsm.d/find_unused_lun.py*
%{_libexecdir}/lsm.d/local_check.py
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/sim.conf
%{_mandir}/man1/sim_lsmplugin.1%{ext_man}

%files smis-plugin
%dir %{python_sitelib}/lsm/plugin/smispy
%{python_sitelib}/lsm/plugin/smispy/*.py*
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/smispy/__pycache__
%{python_sitelib}/lsm/plugin/smispy/__pycache__/*
%endif
%{_bindir}/smispy_lsmplugin
%{_mandir}/man1/smispy_lsmplugin.1%{ext_man}

%files netapp-plugin
%dir %{python_sitelib}/lsm/plugin/ontap
%{python_sitelib}/lsm/plugin/ontap/*.py*
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/ontap/__pycache__
%{python_sitelib}/lsm/plugin/ontap/__pycache__/*
%endif
%{_bindir}/ontap_lsmplugin
%{_mandir}/man1/ontap_lsmplugin.1%{ext_man}

%files targetd-plugin
%dir %{python_sitelib}/lsm/plugin/targetd
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/targetd/__pycache__
%{python_sitelib}/lsm/plugin/targetd/__pycache__/*
%endif
%{python_sitelib}/lsm/plugin/targetd/*.py*
%{_bindir}/targetd_lsmplugin
%{_mandir}/man1/targetd_lsmplugin.1%{ext_man}

%files nstor-plugin
%dir %{python_sitelib}/lsm/plugin/nstor
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/nstor/__pycache__
%{python_sitelib}/lsm/plugin/nstor/__pycache__/*
%endif
%{python_sitelib}/lsm/plugin/nstor/*.py*
%{_bindir}/nstor_lsmplugin
%{_mandir}/man1/nstor_lsmplugin.1%{ext_man}

%files megaraid-plugin
%dir %{python_sitelib}/lsm/plugin/megaraid
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/megaraid/__pycache__
%{python_sitelib}/lsm/plugin/megaraid/__pycache__/*
%endif
%{python_sitelib}/lsm/plugin/megaraid/*.py*
%{_bindir}/megaraid_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/megaraid.conf
%{_mandir}/man1/megaraid_lsmplugin.1%{ext_man}

%files hpsa-plugin
%dir %{python_sitelib}/lsm/plugin/hpsa
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/hpsa/__pycache__
%{python_sitelib}/lsm/plugin/hpsa/__pycache__/*
%endif
%{python_sitelib}/lsm/plugin/hpsa/*.py*
%{_bindir}/hpsa_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/hpsa.conf
%{_mandir}/man1/hpsa_lsmplugin.1%{ext_man}

%files nfs-plugin
%dir %{python_sitelib}/lsm/plugin/nfs
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/nfs/__pycache__
%{python_sitelib}/lsm/plugin/nfs/__pycache__/*
%endif
%{python_sitelib}/lsm/plugin/nfs/*.py*
%{_bindir}/nfs_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/nfs.conf
%{_mandir}/man1/nfs_lsmplugin.1%{ext_man}

%files nfs-plugin-clibs
%{python_sitelib}/lsm/plugin/nfs/nfs_clib.*

%files local-plugin
%dir %{python_sitelib}/lsm/plugin/local
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/local/__pycache__
%{python_sitelib}/lsm/plugin/local/__pycache__/*
%endif
%{python_sitelib}/lsm/plugin/local/*.py*
%{_bindir}/local_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/local.conf
%{_mandir}/man1/local_lsmplugin.1%{ext_man}

%files arcconf-plugin
%dir %{python_sitelib}/lsm/plugin/arcconf
%if 0%{python3}
%dir %{python_sitelib}/lsm/plugin/arcconf/__pycache__
%{python_sitelib}/lsm/plugin/arcconf/__pycache__/*
%endif
%{python_sitelib}/lsm/plugin/arcconf/*.py*
%{_bindir}/arcconf_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/arcconf.conf
%{_mandir}/man1/arcconf_lsmplugin.1%{ext_man}

%if 0%{python3}
%files -n python3-%{name}-clibs
%else
%files -n python2-%{name}-clibs
%endif
%{python_sitelib}/lsm/_clib.*

%changelog
