#
# spec file for package dpdk
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
# needssslcertforbuild


%define flavor @BUILD_FLAVOR@%{nil}
%define aarch64_machine2 armv8a
%define exclusive_arch aarch64 x86_64 ppc64le
%define name_tag %{nil}
%define summary_tag %{nil}
%if "%flavor" == "thunderx"
%define name_tag -thunderx
%define summary_tag (thunderx)
%define aarch64_machine2 thunderx
%define exclusive_arch aarch64
%endif
%define machine native
%define machine2 default
%ifarch x86_64
%define machine native
%define target x86_64-%{machine}-linuxapp-gcc
%endif
%ifarch aarch64
%define machine2 %aarch64_machine2
%define target arm64-%{machine2}-linuxapp-gcc
%endif
%ifarch ppc64le
%define machine2 power8
%define target ppc_64-%{machine2}-linuxapp-gcc
%endif
# This is in sync with <src>/ABI_VERSION
# TODO: automate this sync
%define maj 20
%define min 0
%define lname libdpdk-%{maj}_%{min}
%bcond_without shared
# Add option to build without examples
%bcond_without examples
# Add option to build without tools
%bcond_without tools
Name:           dpdk%{name_tag}
Version:        19.11.4
Release:        0
Summary:        Set of libraries and drivers for fast packet processing
License:        BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-only
Group:          System/Libraries
URL:            http://dpdk.org
Source:         http://fast.dpdk.org/rel/dpdk-%{version}.tar.xz
Source1:        preamble
Patch1:         0001-fix-cpu-compatibility.patch
Patch2:         0001-SLE15-SP3-compatibility-patch-for-kni.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libelf-devel
BuildRequires:  libmnl-devel
BuildRequires:  libnuma-devel
BuildRequires:  libpcap-devel
BuildRequires:  pesign-obs-integration
BuildRequires:  zlib-devel
Conflicts:      dpdk-any
Provides:       dpdk-any = %{version}
ExclusiveArch:  %exclusive_arch
%if 0%{?sle_version} >= 120400
BuildRequires:  rdma-core-devel
%endif

%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package devel
Summary:        Data Plane Development Kit development files %{summary_tag}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Conflicts:      dpdk-any-devel
Provides:       dpdk-any-devel = %{version}

%description devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%package -n %{lname}
Summary:        Data Plane Development Kit runtime libraries %{summary_tag}
Group:          Development/Libraries/C and C++
Provides:       %{lname}-any = %{version}

%description -n %{lname}
This package contains the runtime libraries needed for 3rd party application
to use the Data Plane Development Kit.

%package doc
Summary:        Data Plane Development Kit API documentation %{summary_tag}
Group:          System/Libraries
Conflicts:      dpdk-any-doc
Provides:       dpdk-any-doc = %{version}
BuildArch:      noarch

%description doc
API programming documentation for the Data Plane Development Kit.

%if %{with tools}
%package tools
Summary:        Tools for setting up Data Plane Development Kit environment %{summary_tag}
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires:       findutils
Requires:       iproute
Requires:       kmod
Requires:       pciutils
Conflicts:      dpdk-any-tools
Provides:       dpdk-any-tools = %{version}

%description tools
This package contains tools for setting up Data Plane Development Kit environment
%endif

%if %{with examples}
%package examples
Summary:        Data Plane Development Kit example applications %{summary_tag}
Group:          System/Libraries
BuildRequires:  libvirt-devel
Conflicts:      dpdk-any-examples
Provides:       dpdk-any-examples = %{version}

%description examples
Example applications utilizing the Data Plane Development Kit, such
as L2 and L3 forwarding.
%endif

%package kmp
Summary:        DPDK KNI kernel module %{summary_tag}
Group:          System/Kernel
BuildRequires:  %{kernel_module_package_buildreqs}
Conflicts:      dpdk-any-kmp
%suse_kernel_module_package -p %{_sourcedir}/preamble pae 64kb

%description kmp
The DPDK Kernel NIC Interface (KNI) allows userspace applications access to the Linux* control plane.

%define sdkdir  %{_datadir}/dpdk
%define docdir  %{_docdir}/dpdk
%define incdir %{_includedir}/dpdk
%define pmddir %{_libdir}/dpdk-pmds-%{maj}.%{min}

%prep
# can't use %{name} because of dpdk-thunderx
%setup -q -n dpdk-stable-%{version}
%patch1 -p1 -z .init
%patch2 -p1 -z .init

# This fixes CROSS compilation (broken) in the mk file for ThunderX
sed -i '/^CROSS /s/^/#/'  mk/machine/thunderx/rte.vars.mk

# Verify ABI
[ "$(cat ABI_VERSION)" = "%{maj}.%{min}" ] || exit 1

%build

cp mk/machine/armv8a/rte.vars.mk mk/machine/thunderx

# set up a method for modifying the resulting .config file
function setconf() {
	if grep -q ^$1= $3/.config; then
		sed -i "s:^$1=.*$:$1=$2:g" $3/.config
	else
		echo $1=$2 >> $3/.config
	fi
}

function setdefaultconf()
{
	# Remove the below once upstream fixes the DPAA for NXP ARM
	setconf CONFIG_RTE_LIBRTE_DPAA_BUS n $1
	setconf CONFIG_RTE_LIBRTE_DPAA_MEMPOOL n $1
	setconf CONFIG_RTE_LIBRTE_DPAA_PMD n $1
	setconf CONFIG_RTE_LIBRTE_PMD_CAAM_JR n $1
	setconf CONFIG_RTE_LIBRTE_PMD_DPAA_SEC n $1
	setconf CONFIG_RTE_LIBRTE_PMD_DPAA_EVENTDEV n $1
	%ifarch aarch64
	setconf CONFIG_RTE_LIBRTE_PFE_PMD n $1
	%endif

	setconf CONFIG_RTE_MACHINE '"%{machine2}"' $1
	# Disable experimental features
	setconf CONFIG_RTE_NEXT_ABI n $1

	# Enable automatic driver loading from this path
	setconf CONFIG_RTE_EAL_PMD_PATH '"%{pmddir}"' $1

	setconf CONFIG_RTE_LIBRTE_BNX2X_PMD y $1
	setconf CONFIG_RTE_LIBRTE_BNX2X_MF_SUPPORT y $1
	setconf CONFIG_RTE_LIBRTE_PMD_PCAP y $1
	setconf CONFIG_RTE_LIBRTE_VHOST_NUMA y $1
%if 0%{?sle_version} >= 120400
	setconf CONFIG_RTE_LIBRTE_MLX5_PMD y $1
	setconf CONFIG_RTE_LIBRTE_MLX4_PMD y $1
%endif
	setconf CONFIG_RTE_EAL_IGB_UIO n $1
	setconf CONFIG_RTE_KNI_KMOD n $1

	%if %{with shared}
	setconf CONFIG_RTE_BUILD_SHARED_LIB y $1
	%endif

	%ifarch aarch64 ppc64le
	setconf CONFIG_RTE_LIBRTE_DISTRIBUTOR n $1
	%endif
	%ifarch ppc64le
	setconf CONFIG_RTE_LIBRTE_PMD_RING n $1
	setconf CONFIG_RTE_LIBRTE_IXGBE_PMD n $1
	setconf CONFIG_RTE_LIBRTE_POWER n $1
	%endif
}
# In case dpdk-devel is installed, we should ignore its hints about the SDK directories
unset RTE_SDK RTE_INCLUDE RTE_TARGET

export EXTRA_CFLAGS="%{optflags} -Wformat -fPIC -U_FORTIFY_SOURCE"

# DPDK defaults to using builder-specific compiler flags.  However,
# the config has been changed by specifying CONFIG_RTE_MACHINE=default
# in order to build for a more generic host.  NOTE: It is possible that
# the compiler flags used still won't work for all Fedora-supported
# machines, but runtime checks in DPDK will catch those situations.

make V=1 O=%{target} T=%{target} %{?_smp_mflags} config
setdefaultconf %{target}

export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
for flavor in %{flavors_to_build}; do
	export RTE_KERNELDIR=%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor
	make V=1 O=%{target}-$flavor T=%{target} %{?_smp_mflags} config
	setdefaultconf %{target}-$flavor
	setconf CONFIG_RTE_EAL_IGB_UIO y %{target}-$flavor
	setconf CONFIG_RTE_KNI_KMOD y %{target}-$flavor
	cd  %{target}-$flavor
	make V=1 %{?_smp_mflags}
	cd -
done

make V=1 O=%{target} %{?_smp_mflags}
make V=1 O=%{target} %{?_smp_mflags} doc-api-html

%if %{with examples}
make V=1 O=%{target}/examples T=%{target} %{?_smp_mflags} examples
%endif

%install
# export needed for kmp package
export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
export BRP_PESIGN_FILES="*.ko"

for flavor in %{flavors_to_build}; do
	cd  %{target}-$flavor
	export RTE_KERNELDIR=%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor
	dir=%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor
	krel=$(make -s -C "$dir" kernelrelease)
	mkdir -p %{buildroot}/lib/modules/$krel/extra/dpdk/
	#make install expects same kernel for build and target, lets copy it manually
	install -m644 ../%{target}-$flavor/kmod/*.ko %{buildroot}/lib/modules/$krel/extra/dpdk/
	cd -
done
# In case dpdk-devel is installed
unset RTE_SDK RTE_INCLUDE RTE_TARGET

%make_install O=%{target} prefix=%{_usr} libdir=%{_libdir}

%if ! %{with tools}
rm -rf %{buildroot}%{sdkdir}/usertools/
rm -rf %{buildroot}%{_sbindir}/dpdk_nic_bind
%endif
rm -f %{buildroot}%{sdkdir}/usertools/setup.sh
#TODO pip elftools has issues to fix
rm -rf %{buildroot}%{_bindir}/dpdk-pmdinfo

%if %{with examples}
find %{target}/examples/ -name "*.map" | xargs rm -f
for f in %{target}/examples/*/%{target}/app/*; do
    bn=`basename ${f}`
    cp -p ${f} %{buildroot}%{_bindir}/dpdk_example_${bn}
done
%endif

# Create a driver directory with symlinks to all pmds
mkdir -p %{buildroot}/%{pmddir}
for f in %{buildroot}/%{_libdir}/*_pmd_*.so.*; do
    bn=$(basename ${f})
    ln -s ../${bn} %{buildroot}%{pmddir}/${bn}
done
#mempool is a driver now from 16.07
mkdir -p %{buildroot}/%{pmddir}
for f in %{buildroot}/%{_libdir}/*_mempool_*.so.*; do
    bn=$(basename ${f})
    ln -s ../${bn} %{buildroot}%{pmddir}/${bn}
done

# Setup RTE_SDK environment as expected by apps etc
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
cat << EOF > %{buildroot}/%{_sysconfdir}/profile.d/dpdk-sdk-%{_arch}.sh
if [ -z "\${RTE_SDK}" ]; then
    export RTE_SDK="%{sdkdir}"
    export RTE_TARGET="%{target}"
    export RTE_INCLUDE="%{incdir}"
fi
EOF

cat << EOF > %{buildroot}/%{_sysconfdir}/profile.d/dpdk-sdk-%{_arch}.csh
if ( ! \${?RTE_SDK} ) then
    setenv RTE_SDK "%{sdkdir}"
    setenv RTE_TARGET "%{target}"
    setenv RTE_INCLUDE "%{incdir}"
endif
EOF

# Fixup target machine mismatch
sed -i -e 's:-%{machine}-:-%{machine2}-:g' %{buildroot}/%{_sysconfdir}/profile.d/dpdk-sdk*

#doc
mkdir %{buildroot}%{_docdir}/
mv   %{buildroot}%{_datadir}/doc/dpdk %{buildroot}%{_docdir}/

ln -s %{_bindir}/dpdk-procinfo %{buildroot}%{_bindir}/dpdk_proc_info
ln -s %{_sbindir}/dpdk-devbind %{buildroot}%{_sbindir}/dpdk_nic_bind

# Remove duplicates
%fdupes %{buildroot}/%{_prefix}

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig
%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
# BSD
%{_bindir}/testpmd
%{_bindir}/testbbdev
%{_bindir}/testsad
%{_bindir}/dpdk-procinfo
%{_bindir}/dpdk_proc_info
%{_bindir}/dpdk-pdump

%files -n %{lname}
%defattr(-,root,root)
%if %{with shared}
%{_libdir}/*.so.*
%{pmddir}
%endif

%files doc
%defattr(-,root,root)
#BSD
%docdir
%doc license/gpl-2.0.txt license/lgpl-2.1.txt

%files devel
%defattr(-,root,root)
#BSD
%{incdir}/
%{sdkdir}
%if %{with tools}
%exclude %{sdkdir}/usertools/
%endif
%if %{with examples}
%exclude %{sdkdir}/examples/
%endif
%{_sysconfdir}/profile.d/dpdk-sdk-*.*
%if ! %{with shared}
%{_libdir}/*.a
%else
%{_libdir}/*.so
%endif

%if %{with tools}
%files tools
%defattr(-,root,root)
%{sdkdir}/usertools/
%{_sbindir}/dpdk-devbind
%{_sbindir}/dpdk_nic_bind
%{_bindir}/dpdk-test-eventdev
%{_bindir}/dpdk-test-compress-perf
%{_bindir}/dpdk-test-crypto-perf
%endif

%if %{with examples}
%files examples
%defattr(-,root,root)
%{_bindir}/dpdk_example_*
%doc %{sdkdir}/examples
%endif

%changelog
