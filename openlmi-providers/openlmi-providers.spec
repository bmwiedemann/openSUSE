#
# spec file for package openlmi-providers
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Redhat, Inc
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


%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%if 0%{?suse_version}
%define cim_server sblim-sfcb
%else
%define cim_server tog-pegasus
%endif

%global logfile %{_localstatedir}/log/openlmi-install.log
%global required_konkret_ver 0.9.0-2
%global required_libuser_ver 0.60
%global required_packagekit_ver 1.0.3

# For compilation on machine without internet access, download sphinx inventory
# http://docs.openlmi.org/en/latest/objects.inv, place it to the same
# directory as openlmi-providers.spec and set offline_build below to 1.
# This will keep links to docs.openlmi.org working.
# NOTE: refresh objects.inv once in a while, ideally before each build!
%global offline_build 1

# interop namepsace for %{cim_server}, sfcbd always uses root/interop
%global interop root/interop

%global with_devassistant 1
%global with_journald 1
%global with_service 1
%global with_service_legacy 0
%global with_account 1
%global with_pcp 1
%global with_realmd 1
%global with_fan 1
%global with_locale 1
%global with_indsender 1
%global with_jobmanager 1
%global with_sssd 1
%global with_selinux 1
%global with_software_dbus 0

%if 0%{?rhel} == 6
%global with_journald 0
%global with_service 0
%global with_service_legacy 1
%global with_pcp 0
%global with_realmd 0
%global with_fan 0
%global with_locale 0
%global with_indsender 0
%global with_jobmanager 0
%global with_sssd 0
%global with_selinux 0
%global interop root/PG_InterOp
%endif

%if 0%{?suse_version}
%global with_devassistant 0
# boo#916766, boo#916767
%global with_realmd 0
%global with_selinux 0
%if 0%{?suse_version} < 1320
%global with_sssd 0
%endif
%if 0%{?suse_version} == 1315
# openlmi-realmd would need realmd and more
%global with_realmd 0
%endif
%ifarch s390 s390x
# no libsensors on s390(x)
%global with_fan 0
%endif
%endif

%if 0%{?rhel}
%global with_devassistant 0
%endif

%if 0%{?rhel} || (0%{?fedora} && 0%{?fedora} < 21)
%global with_software_dbus 0
%endif

Name:           openlmi-providers
Version:        0.6.0
Release:        1%{?dist}
Summary:        Set of basic CIM providers
License:        LGPL-2.1+
Group:          System/Management

%if 0%{?suse_version}
%else
%endif
Url:            http://fedorahosted.org/openlmi/
Source0:        http://fedorahosted.org/released/openlmi-providers/%{name}-%{version}.tar.gz

%if 0%{offline_build}
Source1:        http://docs.openlmi.org/en/latest/objects.inv
%endif

# PATCH-FIX-OPENSUSE, no libexec in SUSE, kkaempf@suse.de
Patch1:         0001-cimprovagt-is-under-usr-lib-pegasus-on-SUSE.patch
# PATCH-FIX-OPENSUSE, run dmidecode with full path, kkaempf@suse.de
Patch2:         0002-Run-dmidecode-with-full-path.patch
# PATCH-FIX-OPENSUSE, install cimprovagt scripts into /usr/share/openlmi-providers, kkaempf@suse.de
Patch3:         0003-Install-cimprovagt-scripts-into-usr-share-openlmi-pr.patch
# PATCH-FIX-OPENSUSE, install scripts for service management into /usr/share/openlmi-providers, kkaempf@suse.de
Patch4:         0004-Install-service-scripts-to-usr-share-openlmi-provide.patch
# PATCH-FIX-OPENSUSE, default SystemCreationClassName to Linux_ComputerSystem for sfcb, kkaempf@suse.de
Patch5:         0005-Default-SystemCreationClassName-to-Linux_ComputerSys.patch
Patch6:         openlmi-systemd-231.patch

# Upstream name has been changed from cura-providers to openlmi-providers
Provides:       cura-providers = %{version}-%{release}
Obsoletes:      cura-providers < 0.0.10-1

# == Provider versions ==

# Don't use %%{version} and %%{release} later on, it will be overwritten by openlmi metapackage
%global providers_version %{version}
%global providers_release %{release}
%global providers_version_release %{version}-%{release}
# Providers built from this package need to be strictly
# matched, so that they are always upgraded together.
%global hw_version %{providers_version_release}
%global sw_version %{providers_version_release}
%global pwmgmt_version %{providers_version_release}
%global acct_version %{providers_version_release}
%global svc_version %{providers_version_release}
%global pcp_version %{providers_version_release}
%global journald_version %{providers_version_release}
%global realmd_version %{providers_version_release}
%global sssd_version %{providers_version_release}
%global selinux_version %{providers_version_release}

# Storage and networking providers are built out of tree
# We will require a minimum and maximum version of them
# to ensure that they are tested together.
%global storage_min_version 0.8.1
%global storage_max_version 0.9

%global nw_min_version 0.3.1
%global nw_max_version 0.4

BuildRequires:  cim-schema
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  konkretcmpi-devel >= %{required_konkret_ver}
BuildRequires:  sblim-cmpi-devel
%if 0%{?suse_version}
BuildRequires:  gcc-c++
BuildRequires:  libselinux-devel
BuildRequires:  libudev-devel
BuildRequires:  pkg-config
%endif

%if 0%{?with_fan}
%if 0%{?suse_version}
BuildRequires:  libsensors4-devel
%else
BuildRequires:  lm_sensors-devel
%endif
%endif

%if 0%{with_software_dbus}
BuildRequires:  PackageKit-glib-devel >= %{required_packagekit_ver}
BuildRequires:  rpm-devel
%endif

%if 0%{?with_account}
BuildRequires:  libuser-devel >= %{required_libuser_ver}
%endif

%if 0%{?suse_version}
BuildRequires:  python
%else
BuildRequires:  python2-devel
%endif
# for openlmi-*-doc packages
BuildRequires:  konkretcmpi-python >= %{required_konkret_ver}
%if 0%{?suse_version}
BuildRequires:  python-Sphinx
%else
BuildRequires:  python-sphinx
%endif
BuildRequires:  python-sphinx_rtd_theme

# For openlmi-hardware
BuildRequires:  pciutils-devel
# For openlmi-logicalfile
BuildRequires:  libselinux-devel
BuildRequires:  libudev-devel

# For openlmi-mof-register script
%if 0%{?suse_version}
BuildRequires:  python
%else
Requires:       python2
%endif
# for openlmi-journald
%if 0%{?with_journald}
BuildRequires:  systemd-devel
%endif
# for openlmi-realmd:
%if 0%{?suse_version} >= 1110
BuildRequires:  dbus-1-devel
%else
BuildRequires:  dbus-devel
%endif
%if 0%{?with_sssd}
BuildRequires:  libsss_simpleifp-devel
%endif
%if 0%{?with_selinux}
BuildRequires:  libsemanage-devel
BuildRequires:  libxml2-devel
%endif

# sblim-sfcb or %{cim_server}
# (required to be present during install/uninstall for registration)
Requires:       cim-server
Requires(pre):  cim-server
Requires(preun): cim-server
Requires(post): cim-server
%if 0%{?suse_version}
Recommends:     sblim-sfcb
Requires:       openlmi-pegasus-compat
%endif
Requires:       pywbem
Requires(pre):  pywbem
Requires(preun): pywbem
Requires(post):  pywbem
Requires:       cim-schema
# for lmi.base.mofparse:
Requires:       openlmi-providers-libs%{?_isa} = %{providers_version_release}
Requires:       openlmi-python-base = %{providers_version_release}

# XXX
# Just because we have wired python's scripts
# Remove in future
%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1110
# SLE_11_SP3: unresolvable: conflict for provider of python-distribute needed by python-Pygments, (provider python-distribute obsoletes installed python-setuptools)
BuildRequires:  python-setuptools
%endif

%if 0%{?with_jobmanager}
BuildRequires:  json-glib-devel
%endif

%if 0%{?suse_version} > 1010
BuildRequires:  fdupes
%endif

%description
%{name} is set of (usually) small CMPI providers (agents) for basic
monitoring and management of host system using Common Information
Model (CIM).

%package devel
Summary:        Development files for %{name}
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
Requires:       konkretcmpi-python >= %{required_konkret_ver}
%if 0%{?suse_version}
# for cmake/Modules/FindCMPI.cmake, cmake/Modules/FindKonkretCMPI.cmake
Requires:       konkretcmpi-devel >= %{required_konkret_ver}
%endif
Provides:       cura-providers-devel = %{providers_version_release}
Obsoletes:      cura-providers-devel < 0.0.10-1
Provides:       openlmi-indicationmanager-libs-devel = %{providers_version_release}
Obsoletes:      openlmi-indicationmanager-libs-devel <= 0.4.2-18

%description devel
%{summary}.

%package libs
Summary:        Libraries for %{name}
Group:          System/Management
Provides:       openlmi-indicationmanager-libs = %{providers_version_release}
Obsoletes:      openlmi-indicationmanager-libs <= 0.4.2-18

%description libs
%{summary}.

%if 0%{?with_fan}
%package -n openlmi-fan
Summary:        CIM provider for controlling fans
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
Provides:       cura-fan = %{providers_version_release}
Obsoletes:      cura-fan < 0.0.10-1

%description -n openlmi-fan
%{summary}.

%endif

%package -n openlmi-powermanagement
Summary:        Power management CIM provider
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
Provides:       cura-powermanagement = %{providers_version_release}
%if 0%{?suse_version}
Requires:       upower
# For Linux_ComputerSystem
Requires:       sblim-cmpi-base
%endif
Obsoletes:      cura-powermanagement < 0.0.10-1

%description -n openlmi-powermanagement
%{summary}.

%if 0%{?with_service} || 0%{?with_service_legacy}
%package -n openlmi-service
Summary:        CIM provider for controlling system services
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
Provides:       cura-service = %{providers_version_release}
Obsoletes:      cura-service < 0.0.10-1

%description -n openlmi-service
%{summary}.
%endif

%if 0%{?with_account}
%package -n openlmi-account
Summary:        CIM provider for managing accounts on system
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
Requires:       libuser >= %{required_libuser_ver}
%if 0%{?suse_version}
# For Linux_ComputerSystem
Requires:       sblim-cmpi-base
%endif
Provides:       cura-account = %{providers_version_release}
Obsoletes:      cura-account < 0.0.10-1

%description -n openlmi-account
%{summary}.
%endif

%package -n openlmi-hardware
Summary:        CIM provider for hardware on system
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
# For Hardware information
%ifarch %{ix86} x86_64 ia64
Requires:       dmidecode
%endif
%if 0%{?suse_version}
# For Linux_ComputerSystem
Requires:       sblim-cmpi-base
%endif
Requires:       smartmontools
Requires:       util-linux
Requires:       virt-what

%description -n openlmi-hardware
%{summary}.

%package -n openlmi-python-base
Summary:        Python namespace package for OpenLMI python projects
Group:          System/Management
Requires:       cmpi-bindings-pywbem
Requires:       python-setuptools
BuildArch:      noarch
Obsoletes:      openlmi-python < 0.1.0-1
Provides:       openlmi-python = %{providers_version_release}
%if 0%{?suse_version}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python2_sitelib: %global python2_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?py_requires: %define py_requires Requires: python}
%{py_requires}
%endif

%description -n openlmi-python-base
The openlmi-python-base package contains python namespace package
for all OpenLMI related projects running on python.

%package -n openlmi-python-providers
Summary:        Python namespace package for pywbem providers
Group:          System/Management
Requires:       %{name} = %{providers_version_release}
Requires:       openlmi-python-base = %{providers_version_release}
BuildArch:      noarch

%description -n openlmi-python-providers
The openlmi-python-providers package contains library with common
code for implementing CIM providers using cmpi-bindings-pywbem.

%package -n openlmi-python-test
Summary:        OpenLMI test utilities
Group:          System/Management
Requires:       %{name} = %{providers_version_release}
Requires:       openlmi-python-base = %{providers_version_release}
Requires:       openlmi-tools >= 0.9
BuildArch:      noarch

%description -n openlmi-python-test
The openlmi-python-test package contains test utilities and base
classes for provider test cases.

%package -n openlmi-software
Summary:        CIM providers for software management
Group:          System/Management
Requires:       %{name} = %{providers_version_release}
%if 0%{?suse_version}
# For Linux_ComputerSystem
Requires:       sblim-cmpi-base
%endif
Provides:       cura-software = %{providers_version_release}
Obsoletes:      cura-software < 0.0.10-1
%if 0%{with_software_dbus}
Requires:       PackageKit >= %{required_packagekit_ver}
Requires:       openlmi-logicalfile = %{providers_version_release}
%else
Requires:       openlmi-python-providers = %{providers_version_release}
Requires:       yum
BuildArch:      noarch
%endif

%description -n openlmi-software
The openlmi-software package contains CMPI providers for software management
through Common Information Management (CIM) protocol.

%package -n openlmi-logicalfile
Summary:        CIM provider for reading files and directories
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
%if 0%{?suse_version}
# For Linux_ComputerSystem
Requires:       sblim-cmpi-base
%endif

%description -n openlmi-logicalfile
%{summary}.

%if 0%{?with_realmd}
%package -n openlmi-realmd
Summary:        CIM provider for Realmd
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}
Requires:       realmd
%if 0%{?suse_version}
# For Linux_ComputerSystem
Requires:       sblim-cmpi-base
%endif

%description -n openlmi-realmd
The openlmi-realmd package contains CMPI providers for Realmd, which is an on
demand system DBus service, which allows callers to configure network
authentication and domain membership in a standard way.

%endif

%if 0%{?with_pcp}
%package -n openlmi-pcp
Summary:        Pywbem providers for accessing PCP metrics
Group:          System/Management
Requires:       %{name} = %{providers_version_release}
BuildArch:      noarch
Requires:       cmpi-bindings-pywbem
Requires:       python-pcp
Requires:       python-setuptools
%if 0%{?suse_version}
Requires:       cron
%endif

%description -n openlmi-pcp
openlmi-pcp exposes metrics from a local PMCD (Performance Co-Pilot server)
to the CIMOM.  They appear as potentially hundreds of MOF classes, e.g.
class "PCP_Metric_kernel__pernode__cpu__use", with instances for each PCP
metric instance, e.g. "node0".  PCP metric values and metadata are transcribed
into strings on demand.
%endif

%package -n openlmi
Summary:        OpenLMI managed system software components
Group:          System/Management
Version:        1.0.3
Release:        0
Requires:       %{name} = %{providers_version}
BuildArch:      noarch
Requires:       cim-server
# List of "safe" providers
Requires:       openlmi-account = %{acct_version}
Requires:       openlmi-hardware = %{hw_version}
Requires:       openlmi-powermanagement = %{pwmgmt_version}
Requires:       openlmi-service = %{svc_version}
Requires:       openlmi-software = %{sw_version}

%if 0%{?suse_version} == 0
# Mandatory, out-of-tree providers
Requires:       openlmi-storage >= %{storage_min_version}
Conflicts:      openlmi-storage >= %{storage_max_version}
Requires:       openlmi-networking >= %{nw_min_version}
Conflicts:      openlmi-networking >= %{nw_max_version}
%endif

# Optional Providers
# This ensures that only the appropriate version is installed but does
# not install it by default. If these packages are installed, this will
# guarantee that they are updated to the appropriate version on upgrade.
Conflicts:      openlmi-pcp > %{pcp_version}
Conflicts:      openlmi-pcp < %{pcp_version}

Conflicts:      openlmi-journald > %{journald_version}
Conflicts:      openlmi-journald < %{journald_version}

Conflicts:      openlmi-realmd > %{realmd_version}
Conflicts:      openlmi-realmd < %{realmd_version}

%description -n openlmi
OpenLMI provides a common infrastructure for the management of Linux systems.
This package installs a core set of OpenLMI providers and necessary
infrastructure packages enabling the system to be managed remotely.

%if 0%{?with_journald}
%package -n openlmi-journald
Summary:        CIM provider for Journald
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}

%description -n openlmi-journald
The openlmi-journald package contains CMPI providers for systemd journald
service, allowing listing, iterating through and writing new message log
records.
%endif

%if 0%{?with_sssd}
%package -n openlmi-sssd
Summary:        CIM provider for SSSD
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}

%description -n openlmi-sssd
The openlmi-sssd package contains CMPI providers for SSSD service.
%endif

%if 0%{?with_selinux}
%package -n openlmi-selinux
Summary:        CIM provider for SELinux
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}

%description -n openlmi-selinux
The openlmi-selinux package contains CMPI providers for SELinux.
%endif

%if 0%{?with_devassistant}
%package -n openlmi-devassistant
Summary:        OpenLMI provider templates for Developer Assistant
Group:          System/Management
BuildArch:      noarch
Requires:       %{name}-devel = %{providers_version_release}
Requires:       devassistant >= 0.9.0

%description -n openlmi-devassistant
This package contains template files for Developer Assistant.
%endif

%if 0%{?with_locale}
%package -n openlmi-locale
Summary:        CIM provider for controlling system locale and keyboard mapping
Group:          System/Management
Requires:       %{name}%{?_isa} = %{providers_version_release}

%description -n openlmi-locale
%{summary}.
%endif

%package doc
Summary:        OpenLMI Providers documentation
Group:          Documentation
BuildArch:      noarch
Obsoletes:      openlmi-fan-doc < 0.5.0-3
Provides:       openlmi-fan-doc = %{providers_version_release}
Obsoletes:      openlmi-powermanagement-doc < 0.5.0-3
Provides:       openlmi-powermanagement-doc = %{providers_version_release}
Obsoletes:      openlmi-service-doc < 0.5.0-3
Provides:       openlmi-service-doc = %{providers_version_release}
Obsoletes:      openlmi-account-doc < 0.5.0-3
Provides:       openlmi-account-doc = %{providers_version_release}
Obsoletes:      openlmi-hardware-doc < 0.5.0-3
Provides:       openlmi-hardware-doc = %{providers_version_release}
Obsoletes:      openlmi-software-doc < 0.5.0-3
Provides:       openlmi-software-doc = %{providers_version_release}
Obsoletes:      openlmi-logicalfile-doc < 0.5.0-3
Provides:       openlmi-logicalfile-doc = %{providers_version_release}
Obsoletes:      openlmi-realmd-doc < 0.5.0-3
Provides:       openlmi-realmd-doc = %{providers_version_release}
Obsoletes:      openlmi-journald-doc < 0.5.0-3
Provides:       openlmi-journald-doc = %{providers_version_release}
Obsoletes:      openlmi-sssd-doc < 0.5.0-3
Provides:       openlmi-sssd-doc = %{providers_version_release}
Obsoletes:      openlmi-selinux-doc < 0.5.0-3
Provides:       openlmi-selinux-doc = %{providers_version_release}
Obsoletes:      openlmi-locale-doc < 0.5.0-3
Provides:       openlmi-locale-doc = %{providers_version_release}

%description doc
This package contains the documentation for OpenLMI Providers.


%prep
%setup -q
%if 0%{?suse_version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%endif
if pkg-config --atleast-version=231 libsystemd; then
%patch6 -p1
fi

%build
%if 0%{offline_build}
cp %{SOURCE1} doc/admin/objects.inv
%endif

%if 0%{?suse_version}
# SUSE %%cmake creates build/ subdir
%global target_builddir %{_target_platform}/build
%global source_dir ../..
%else
%global target_builddir %{_target_platform}
%global source_dir ..
%endif

mkdir -p %{_target_platform}
pushd %{_target_platform}

%{cmake} \
%if ! 0%{with_devassistant}
    -DWITH-DEVASSISTANT=OFF \
%else
    -DWITH-DEVASSISTANT=ON \
%endif
%if ! 0%{with_journald}
    -DWITH-JOURNALD=OFF \
%endif
%if ! 0%{with_service}
    -DWITH-SERVICE=OFF \
%endif
%if 0%{with_service_legacy}
    -DWITH-SERVICE-LEGACY=ON \
%endif
%if ! 0%{with_account}
    -DWITH-ACCOUNT=OFF \
%endif
%if ! 0%{with_pcp}
    -DWITH-PCP=OFF \
%endif
%if ! 0%{with_realmd}
    -DWITH-REALMD=OFF \
%endif
%if ! 0%{with_fan}
    -DWITH-FAN=OFF \
%endif
%if ! 0%{with_locale}
    -DWITH-LOCALE=OFF \
%endif
%if ! 0%{with_indsender}
    -DWITH-INDSENDER=OFF \
%endif
%if ! 0%{with_jobmanager}
    -DWITH-JOBMANAGER=OFF \
%endif
%if ! 0%{with_sssd}
    -DWITH-SSSD=OFF \
%endif
%if ! 0%{with_selinux}
    -DWITH-SELINUX=OFF \
%endif
%if 0%{with_software_dbus}
    -DWITH-SOFTWARE-DBUS=ON \
%endif
    %{source_dir}

popd

make -k %{?_smp_mflags} -C %{target_builddir} all doc

pushd src/python
%{__python} setup.py build
popd # src/python
# for software providers
pushd src/software
%{__python} setup.py build
popd # src/software

%if 0%{with_pcp}
pushd src/pcp
%{__python} setup.py build
popd
%endif

%install
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{target_builddir}

# The log file must be created
mkdir -p "$RPM_BUILD_ROOT/%{_localstatedir}/log"
touch "$RPM_BUILD_ROOT/%logfile"

# The registration database and directories
mkdir -p "$RPM_BUILD_ROOT/%{_sharedstatedir}/openlmi-registration/mof"
mkdir -p "$RPM_BUILD_ROOT/%{_sharedstatedir}/openlmi-registration/reg"
touch "$RPM_BUILD_ROOT/%{_sharedstatedir}/openlmi-registration/regdb.sqlite"

# XXX
# Remove pythonies
# Don't forget to remove this dirty hack in the future
rm -rf "$RPM_BUILD_ROOT"/usr/bin/*.py
rm -rf "$RPM_BUILD_ROOT"/usr/lib/python*

pushd src/python
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
cp -p lmi/__init__.* $RPM_BUILD_ROOT%{python2_sitelib}/lmi
popd # src/python

%if ! 0%{with_software_dbus}
# for software providers
pushd src/software
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%if 0%{?suse_version}
install -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/openlmi-providers
install -m 755 pycmpiLMI_Software-cimprovagt $RPM_BUILD_ROOT/%{_datadir}/openlmi-providers
%else
install -m 755 -d $RPM_BUILD_ROOT/%{_libexecdir}/pegasus
install -m 755 pycmpiLMI_Software-cimprovagt $RPM_BUILD_ROOT/%{_libexecdir}/pegasus/
%endif
popd # src/software
sed -i 's#/usr/lib/python2.7/site-packages#%{python2_sitelib}#g' $RPM_BUILD_ROOT/%{_datadir}/%{name}/60_LMI_Software.reg
%endif

# pcp
%if 0%{with_pcp}
pushd src/pcp
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
cp -p %{target_builddir}/src/pcp/openlmi-pcp-generate $RPM_BUILD_ROOT/%{_bindir}/openlmi-pcp-generate
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily
cp -p src/pcp/openlmi-pcp.cron $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/openlmi-pcp
sed -i -e 's,^_LOCALSTATEDIR=.*,_LOCALSTATEDIR="%{_localstatedir}",' \
       -e 's,^_DATADIR=.*,_DATADIR="%{_datadir}",' \
       -e 's,^NAME=.*,NAME="%{name}",' \
       -e 's,^PYTHON2_SITELIB=.*,PYTHON2_SITELIB="%{python2_sitelib}",' \
    $RPM_BUILD_ROOT/%{_bindir}/openlmi-pcp-generate \
    $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/openlmi-pcp
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/%{name}
touch $RPM_BUILD_ROOT/%{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.mof
touch $RPM_BUILD_ROOT/%{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.reg
touch $RPM_BUILD_ROOT/%{_localstatedir}/lib/%{name}/stamp
%endif

# documentation
install -m 755 -d $RPM_BUILD_ROOT/%{_docdir}/%{name}
install -m 644 README COPYING $RPM_BUILD_ROOT/%{_docdir}/%{name}

install -m 755 -d $RPM_BUILD_ROOT/%{_docdir}/%{name}/admin_guide
cp -pr %{target_builddir}/doc/admin/html/* $RPM_BUILD_ROOT/%{_docdir}/%{name}/admin_guide

%if 0%{?suse_version} > 1010
%fdupes $RPM_BUILD_ROOT/%{python_sitelib}
%endif

%if 0%{?suse_version}
# provided by konkretcmpi-devel
rm -f $RPM_BUILD_ROOT%{_datadir}/cmake/Modules/FindCMPI.cmake
rm -f $RPM_BUILD_ROOT%{_datadir}/cmake/Modules/FindKonkretCMPI.cmake
%endif

%files
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/COPYING
%dir %{_datadir}/%{name}
%dir %{_sysconfdir}/openlmi
%config(noreplace) %{_sysconfdir}/openlmi/openlmi.conf
%{_datadir}/%{name}/05_LMI_Qualifiers.mof
%{_datadir}/%{name}/30_LMI_Jobs.mof
%attr(755, root, root) %{_bindir}/openlmi-mof-register
%ghost %logfile
%dir %{_sharedstatedir}
%dir %{_sharedstatedir}/openlmi-registration
%dir %{_sharedstatedir}/openlmi-registration/mof
%dir %{_sharedstatedir}/openlmi-registration/reg
%ghost %{_sharedstatedir}/openlmi-registration/regdb.sqlite
%if 0%{?suse_version}
%dir %{_datadir}/%{name}
%dir %{_libdir}/cmpi
%endif

%files libs
%defattr(-,root,root)
%doc README COPYING src/libs/indmanager/README.indmanager
%{_libdir}/libopenlmicommon.so.*
%{_libdir}/libopenlmiindmanager.so.*
%if 0%{?with_indsender}
%{_libdir}/libopenlmiindsender.so.*
%endif
%if 0%{?with_jobmanager}
%doc src/libs/jobmanager/README.jobmanager
%{_libdir}/libopenlmijobmanager.so.*
%endif

%files devel
%defattr(-,root,root)
%doc README COPYING src/libs/indmanager/README.indmanager src/libs/jobmanager/README.jobmanager
%{_bindir}/openlmi-doc-class2rst
%{_bindir}/openlmi-doc-class2uml
%{_libdir}/libopenlmicommon.so
%{_libdir}/pkgconfig/openlmi.pc
%dir %{_includedir}/openlmi
%{_includedir}/openlmi/openlmi.h
%{_includedir}/openlmi/openlmi-utils.h
%{_datadir}/cmake/Modules/OpenLMIMacros.cmake
%{_datadir}/cmake/Modules/FindOpenLMI.cmake
%if 0%{?suse_version} == 0
%{_datadir}/cmake/Modules/FindCMPI.cmake
%{_datadir}/cmake/Modules/FindKonkretCMPI.cmake
%endif
%{_datadir}/cmake/Modules/FindOpenLMIIndManager.cmake
%{_libdir}/libopenlmiindmanager.so
%{_libdir}/pkgconfig/openlmiindmanager.pc
%{_includedir}/openlmi/ind_manager.h
%if 0%{?with_indsender}
%{_libdir}/libopenlmiindsender.so
%{_libdir}/pkgconfig/openlmiindsender.pc
%{_includedir}/openlmi/ind_sender.h
%endif
%if 0%{?with_jobmanager}
%{_libdir}/libopenlmijobmanager.so
%{_libdir}/pkgconfig/openlmijobmanager.pc
%{_includedir}/openlmi/job_manager.h
%{_includedir}/openlmi/lmi_job.h
%endif

%if 0%{with_fan}
%files -n openlmi-fan
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Fan.so
%{_datadir}/%{name}/60_LMI_Fan.mof
%{_datadir}/%{name}/60_LMI_Fan.reg
%{_datadir}/%{name}/90_LMI_Fan_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Fan-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Fan-cimprovagt
%endif
%endif

%files -n openlmi-powermanagement
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_PowerManagement.so
%{_datadir}/%{name}/60_LMI_PowerManagement.mof
%{_datadir}/%{name}/60_LMI_PowerManagement.reg
%{_datadir}/%{name}/90_LMI_PowerManagement_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_PowerManagement-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_PowerManagement-cimprovagt
%endif

%files -n openlmi-service
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Service.so
%{_datadir}/%{name}/60_LMI_Service.mof
%{_datadir}/%{name}/60_LMI_Service.reg
%if 0%{?with_service_legacy}
%{_libexecdir}/servicedisc.sh
%{_libexecdir}/serviceutil.sh
%endif
%{_datadir}/%{name}/90_LMI_Service_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Service-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Service-cimprovagt
%endif

%if 0%{with_account}
%files -n openlmi-account
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Account.so
%{_datadir}/%{name}/60_LMI_Account.mof
%{_datadir}/%{name}/60_LMI_Account.reg
%{_datadir}/%{name}/90_LMI_Account_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Account-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Account-cimprovagt
%endif
%endif

%files -n openlmi-hardware
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Hardware.so
%{_datadir}/%{name}/60_LMI_Hardware.mof
%{_datadir}/%{name}/60_LMI_Hardware.reg
%{_datadir}/%{name}/90_LMI_Hardware_Profile.mof
%{_datadir}/%{name}/90_LMI_Hardware_Profile_DMTF.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Hardware-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Hardware-cimprovagt
%endif

%files -n openlmi-python-base
%defattr(-,root,root)
%doc README COPYING
%dir %{python2_sitelib}/lmi
%{python2_sitelib}/lmi/__init__.py
%{python2_sitelib}/lmi/__init__.py[co]
%{python2_sitelib}/openlmi-*
%{python2_sitelib}/lmi/base/

%files -n openlmi-python-providers
%defattr(-,root,root)
%doc README COPYING
%dir %{python2_sitelib}/lmi/providers
%{python2_sitelib}/lmi/providers/*.py
%{python2_sitelib}/lmi/providers/*.py[co]

%files -n openlmi-python-test
%defattr(-,root,root)
%doc README COPYING
%dir %{python2_sitelib}/lmi/test
%{python2_sitelib}/lmi/test/*.py
%{python2_sitelib}/lmi/test/*.py[co]

%files -n openlmi-software
%defattr(-,root,root)
%doc README COPYING
%if 0%{?suse_version}
%dir %{_sysconfdir}/openlmi/software
%endif
%if 0%{with_software_dbus}
%{_libdir}/cmpi/libcmpiLMI_Software.so
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Software-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Software-cimprovagt
%endif
%else
%config(noreplace) %{_sysconfdir}/openlmi/software/software.conf
%config(noreplace) %{_sysconfdir}/openlmi/software/yum_worker_logging.conf
%{python2_sitelib}/lmi/software/
%{python2_sitelib}/openlmi_software-*
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/pycmpiLMI_Software-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/pycmpiLMI_Software-cimprovagt
%endif
%endif

%{_datadir}/%{name}/60_LMI_Software.mof
%{_datadir}/%{name}/60_LMI_Software_MethodParameters.mof
%{_datadir}/%{name}/70_LMI_SoftwareIndicationFilters.mof
%{_datadir}/%{name}/90_LMI_Software_Profile.mof
%{_datadir}/%{name}/60_LMI_Software.reg

%if 0%{with_pcp}
%files -n openlmi-pcp
%defattr(-,root,root)
%doc README COPYING
%{_datadir}/%{name}/60_LMI_PCP.mof
%{python2_sitelib}/lmi/pcp/
%{python2_sitelib}/openlmi_pcp-*
%attr(755, root, root) %{_bindir}/openlmi-pcp-generate
%attr(755, root, root) %{_sysconfdir}/cron.daily/openlmi-pcp
%dir %{_localstatedir}/lib/%{name}
%ghost %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.mof
%ghost %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.reg
%ghost %{_localstatedir}/lib/%{name}/stamp
%endif

%files -n openlmi-logicalfile
%defattr(-,root,root)
%doc README COPYING
%dir %{_sysconfdir}/openlmi
%dir %{_sysconfdir}/openlmi/logicalfile
%config(noreplace) %{_sysconfdir}/openlmi/logicalfile/logicalfile.conf
%{_libdir}/cmpi/libcmpiLMI_LogicalFile.so
%{_datadir}/%{name}/50_LMI_LogicalFile.mof
%{_datadir}/%{name}/50_LMI_LogicalFile.reg
%{_datadir}/%{name}/90_LMI_LogicalFile_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_LogicalFile-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_LogicalFile-cimprovagt
%endif

%if 0%{with_realmd}
%files -n openlmi-realmd
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Realmd.so
%{_datadir}/%{name}/60_LMI_Realmd.mof
%{_datadir}/%{name}/60_LMI_Realmd.reg
%{_datadir}/%{name}/90_LMI_Realmd_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Realmd-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Realmd-cimprovagt
%endif
%endif

%files -n openlmi
%defattr(-,root,root)
%doc COPYING README

%if 0%{with_journald}
%files -n openlmi-journald
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Journald.so
%{_datadir}/%{name}/60_LMI_Journald.mof
%{_datadir}/%{name}/60_LMI_Journald.reg
%{_datadir}/%{name}/70_LMI_JournaldIndicationFilters.mof
%{_datadir}/%{name}/90_LMI_Journald_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Journald-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Journald-cimprovagt
%endif
%endif

%if 0%{with_sssd}
%files -n openlmi-sssd
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_SSSD.so
%{_datadir}/%{name}/60_LMI_SSSD.mof
%{_datadir}/%{name}/60_LMI_SSSD.reg
%{_datadir}/%{name}/90_LMI_SSSD_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_SSSD-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_SSSD-cimprovagt
%endif
%endif

%if 0%{with_selinux}
%files -n openlmi-selinux
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_SELinux.so
%{_datadir}/%{name}/60_LMI_SELinux.mof
%{_datadir}/%{name}/60_LMI_SELinux.reg
%{_datadir}/%{name}/60_LMI_SELinux_MethodParameters.mof
%{_datadir}/%{name}/90_LMI_SELinux_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_SELinux-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_SELinux-cimprovagt
%endif
%endif

%if 0%{with_devassistant}
%files -n openlmi-devassistant
%defattr(-,root,root)
%if 0%{?suse_version}
%dir %{_datadir}/devassistant
%dir %{_datadir}/devassistant/files
%dir %{_datadir}/devassistant/files/crt
%dir %{_datadir}/devassistant/files/crt/c
%dir %{_datadir}/devassistant/files/crt/python
%endif
%dir %{_datadir}/devassistant/files/crt/python/openlmi/
%dir %{_datadir}/devassistant/files/crt/c/openlmi/
%{_datadir}/devassistant/assistants/
%{_datadir}/devassistant/files/crt/python/openlmi/*
%{_datadir}/devassistant/files/crt/c/openlmi/*
%endif

%if 0%{with_locale}
%files -n openlmi-locale
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Locale.so
%{_datadir}/%{name}/60_LMI_Locale.mof
%{_datadir}/%{name}/60_LMI_Locale.reg
%{_datadir}/%{name}/90_LMI_Locale_Profile.mof
%if 0%{?suse_version}
%{_datadir}/openlmi-providers/cmpiLMI_Locale-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Locale-cimprovagt
%endif
%endif

%files doc
%defattr(-,root,root)
%doc README COPYING
%{_docdir}/%{name}/admin_guide

%pre
# If upgrading, deregister old version
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register --just-mofs unregister \
        %{_datadir}/%{name}/05_LMI_Qualifiers.mof \
        %{_datadir}/%{name}/30_LMI_Jobs.mof || :;
fi >> %logfile 2>&1

%post
/sbin/ldconfig
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register --just-mofs register \
        %{_datadir}/%{name}/05_LMI_Qualifiers.mof \
        %{_datadir}/%{name}/30_LMI_Jobs.mof || :;
fi >> %logfile 2>&1

%preun
# Deregister only if not upgrading
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register --just-mofs unregister \
        %{_datadir}/%{name}/05_LMI_Qualifiers.mof \
        %{_datadir}/%{name}/30_LMI_Jobs.mof || :;
fi >> %logfile 2>&1

%postun -p /sbin/ldconfig

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%if 0%{with_fan}
%pre -n openlmi-fan
# If upgrading, deregister old version
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Fan.mof \
        %{_datadir}/%{name}/60_LMI_Fan.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Fan_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%pre -n openlmi-powermanagement
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_PowerManagement.mof \
        %{_datadir}/%{name}/60_LMI_PowerManagement.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_PowerManagement_Profile.mof || :;
fi >> %logfile 2>&1

%pre -n openlmi-service
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Service.mof \
        %{_datadir}/%{name}/60_LMI_Service.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Service_Profile.mof || :;
fi >> %logfile 2>&1

%if 0%{with_account}
%pre -n openlmi-account
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Account.mof \
        %{_datadir}/%{name}/60_LMI_Account.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Account_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%pre -n openlmi-software
if [ "$1" -gt 1 ]; then
    # delete indication filters
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop -c sfcbd unregister \
        %{_datadir}/%{name}/70_LMI_SoftwareIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/70_LMI_SoftwareIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Software_Profile.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -c %{cim_server} unregister \
        %{_datadir}/%{name}/60_LMI_Software_MethodParameters.mof || :;
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Software.mof \
        %{_datadir}/%{name}/60_LMI_Software.reg || :;
fi >> %logfile 2>&1

%pre -n openlmi-logicalfile
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/50_LMI_LogicalFile.mof \
        %{_datadir}/%{name}/50_LMI_LogicalFile.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_LogicalFile_Profile.mof || :;
fi >> %logfile 2>&1

%if 0%{with_realmd}
%pre -n openlmi-realmd
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Realmd.mof \
        %{_datadir}/%{name}/60_LMI_Realmd.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Realmd_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%pre -n openlmi-hardware
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Hardware.mof \
        %{_datadir}/%{name}/60_LMI_Hardware.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Hardware_Profile.mof \
        %{_datadir}/%{name}/90_LMI_Hardware_Profile_DMTF.mof || :;
fi >> %logfile 2>&1

%if 0%{with_pcp}
%pre -n openlmi-pcp
if [ "$1" -gt 1 ]; then
    # Only unregister when the provider was already registered
    if [ -e %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.mof ]; then
        %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
            %{_datadir}/%{name}/60_LMI_PCP.mof \
            %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.mof \
            %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.reg || :;
    fi
fi >> %logfile 2>&1
%endif

%if 0%{with_journald}
%pre -n openlmi-journald
if [ "$1" -gt 1 ]; then
    # delete indication filters
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop -c sfcbd unregister \
        %{_datadir}/%{name}/70_LMI_JournaldIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/70_LMI_JournaldIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Journald.mof \
        %{_datadir}/%{name}/60_LMI_Journald.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Journald_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_locale}
%pre -n openlmi-locale
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Locale.mof \
        %{_datadir}/%{name}/60_LMI_Locale.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Locale_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_sssd}
%pre -n openlmi-sssd
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_SSSD.mof \
        %{_datadir}/%{name}/60_LMI_SSSD.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_SSSD_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_selinux}
%pre -n openlmi-selinux
if [ "$1" -gt 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_SELinux.mof \
        %{_datadir}/%{name}/60_LMI_SELinux.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -c %{cim_server} unregister \
        %{_datadir}/%{name}/60_LMI_SELinux_MethodParameters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_SELinux_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_fan}
%post -n openlmi-fan
# Register Schema and Provider
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Fan.mof \
        %{_datadir}/%{name}/60_LMI_Fan.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Fan_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%post -n openlmi-powermanagement
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_PowerManagement.mof \
        %{_datadir}/%{name}/60_LMI_PowerManagement.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_PowerManagement_Profile.mof || :;
fi >> %logfile 2>&1

%post -n openlmi-service
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Service.mof \
        %{_datadir}/%{name}/60_LMI_Service.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Service_Profile.mof || :;
fi >> %logfile 2>&1

%if 0%{with_account}
%post -n openlmi-account
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Account.mof \
        %{_datadir}/%{name}/60_LMI_Account.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Account_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%post -n openlmi-software
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Software.mof \
        %{_datadir}/%{name}/60_LMI_Software.reg || :;
    # install indication filters for sfcbd
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop -c sfcbd register \
        %{_datadir}/%{name}/70_LMI_SoftwareIndicationFilters.mof || :;
        %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/70_LMI_SoftwareIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Software_Profile.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -c %{cim_server} register \
        %{_datadir}/%{name}/60_LMI_Software_MethodParameters.mof || :;
fi >> %logfile 2>&1

%post -n openlmi-logicalfile
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/50_LMI_LogicalFile.mof \
        %{_datadir}/%{name}/50_LMI_LogicalFile.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_LogicalFile_Profile.mof || :;
fi >> %logfile 2>&1

%if 0%{with_realmd}
%post -n openlmi-realmd
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Realmd.mof \
        %{_datadir}/%{name}/60_LMI_Realmd.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Realmd_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%post -n openlmi-hardware
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Hardware.mof \
        %{_datadir}/%{name}/60_LMI_Hardware.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Hardware_Profile.mof \
        %{_datadir}/%{name}/90_LMI_Hardware_Profile_DMTF.mof || :;
fi >> %logfile 2>&1

%if 0%{with_journald}
%post -n openlmi-journald
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Journald.mof \
        %{_datadir}/%{name}/60_LMI_Journald.reg || :;
    # install indication filters for sfcbd
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop -c sfcbd register \
        %{_datadir}/%{name}/70_LMI_JournaldIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/70_LMI_JournaldIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Journald_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_locale}
%post -n openlmi-locale
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_Locale.mof \
        %{_datadir}/%{name}/60_LMI_Locale.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_Locale_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_sssd}
%post -n openlmi-sssd
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_SSSD.mof \
        %{_datadir}/%{name}/60_LMI_SSSD.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_SSSD_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_selinux}
%post -n openlmi-selinux
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} register \
        %{_datadir}/%{name}/60_LMI_SELinux.mof \
        %{_datadir}/%{name}/60_LMI_SELinux.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -c %{cim_server} register \
        %{_datadir}/%{name}/60_LMI_SELinux_MethodParameters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} register \
        %{_datadir}/%{name}/90_LMI_SELinux_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_fan}
%preun -n openlmi-fan
# Deregister only if not upgrading
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Fan.mof \
        %{_datadir}/%{name}/60_LMI_Fan.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Fan_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%preun -n openlmi-powermanagement
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_PowerManagement.mof \
        %{_datadir}/%{name}/60_LMI_PowerManagement.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_PowerManagement_Profile.mof || :;
fi >> %logfile 2>&1

%preun -n openlmi-service
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Service.mof \
        %{_datadir}/%{name}/60_LMI_Service.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Service_Profile.mof || :;
fi >> %logfile 2>&1

%if 0%{with_account}
%preun -n openlmi-account
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Account.mof \
        %{_datadir}/%{name}/60_LMI_Account.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Account_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%preun -n openlmi-software
if [ "$1" -eq 0 ]; then
    # delete indication filters
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop -c sfcbd unregister \
        %{_datadir}/%{name}/70_LMI_SoftwareIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/70_LMI_SoftwareIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Software_Profile.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -c %{cim_server} unregister \
        %{_datadir}/%{name}/60_LMI_Software_MethodParameters.mof || :;
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Software.mof \
        %{_datadir}/%{name}/60_LMI_Software.reg || :;
fi >> %logfile 2>&1

%preun -n openlmi-logicalfile
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/50_LMI_LogicalFile.mof \
        %{_datadir}/%{name}/50_LMI_LogicalFile.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_LogicalFile_Profile.mof || :;
fi >> %logfile 2>&1

%if 0%{with_realmd}
%preun -n openlmi-realmd
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Realmd.mof \
        %{_datadir}/%{name}/60_LMI_Realmd.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Realmd_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%preun -n openlmi-hardware
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Hardware.mof \
        %{_datadir}/%{name}/60_LMI_Hardware.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Hardware_Profile.mof \
        %{_datadir}/%{name}/90_LMI_Hardware_Profile_DMTF.mof || :;
fi >> %logfile 2>&1

%if 0%{with_pcp}
%preun -n openlmi-pcp
if [ "$1" -eq 0 ]; then
    # Only unregister when the provider was already registered
    if [ -e %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.mof ]; then
        %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
            %{_datadir}/%{name}/60_LMI_PCP.mof \
            %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.mof \
            %{_localstatedir}/lib/%{name}/60_LMI_PCP_PMNS.reg || :;
    fi
fi >> %logfile 2>&1
%endif

%if 0%{with_journald}
%preun -n openlmi-journald
if [ "$1" -eq 0 ]; then
    # delete indication filters
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop -c sfcbd unregister \
        %{_datadir}/%{name}/70_LMI_JournaldIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/70_LMI_JournaldIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Journald.mof \
        %{_datadir}/%{name}/60_LMI_Journald.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Journald_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_locale}
%preun -n openlmi-locale
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_Locale.mof \
        %{_datadir}/%{name}/60_LMI_Locale.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_Locale_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_sssd}
%preun -n openlmi-sssd
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_SSSD.mof \
        %{_datadir}/%{name}/60_LMI_SSSD.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_SSSD_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%if 0%{with_selinux}
%preun -n openlmi-selinux
if [ "$1" -eq 0 ]; then
    %{_bindir}/openlmi-mof-register -v %{providers_version} unregister \
        %{_datadir}/%{name}/60_LMI_SELinux.mof \
        %{_datadir}/%{name}/60_LMI_SELinux.reg || :;
    %{_bindir}/openlmi-mof-register --just-mofs -c %{cim_server} unregister \
        %{_datadir}/%{name}/60_LMI_SELinux_MethodParameters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n %{interop} -c %{cim_server} unregister \
        %{_datadir}/%{name}/90_LMI_SELinux_Profile.mof || :;
fi >> %logfile 2>&1
%endif

%changelog
