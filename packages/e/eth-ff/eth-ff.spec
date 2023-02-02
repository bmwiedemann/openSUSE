#
# spec file for package eth-ff
#
# Copyright (c) 2023 SUSE LLC
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


%define git_ver .0.e2d1dd8cde0e

%define pseudo_opt %{_prefix}/lib/eth-tools/
%define ethsysconfdir %{_sysconfdir}/eth-tools/

Name:           eth-ff
Version:        11.3.0.0
Release:        0
Summary:        Intel Ethernet Fabric Suite basic tools and libraries for fabric management
License:        BSD-3-Clause OR GPL-2.0-only
Group:          Productivity/Networking/System
URL:            https://github.com/intel/eth-fast-fabric
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        eth-ff.rpmlintrc
Patch1:         eth-ff-suse-build-fixes.patch
Patch2:         eth-ff-add-shebang-for-exp-files.patch
Patch3:         topology-fix-support-for-disabled-MD5-authentication.patch
BuildRequires:  gcc-c++
BuildRequires:  infiniband-diags-devel
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
BuildRequires:  librdmacm1
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  rdma-core-devel
BuildRequires:  tcl-devel
BuildRequires:  zlib-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Currently ONLY builds on x86_64
ExclusiveArch:  x86_64

%description
The %{name} contains basic tools and libraries  to manage an Intel Ethernet fabric.

%package     -n eth-basic-tools
Summary:        Management level tools and scripts
Group:          Productivity/Networking/System
Requires:       rdma

%description -n eth-basic-tools
Contains basic tools for fabric management necessary on all compute nodes.

%package -n eth-fastfabric
Summary:        Management level tools and scripts
Group:          Productivity/Networking/System
Requires:       cron
Requires:       eth-basic-tools

%description -n eth-fastfabric
Contains tools for managing fabric on a management node.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch1
%patch2
%patch3

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-address-of-packed-member"
cd OpenIb_Host && ./ff_build.sh %{_builddir} $FF_BUILD_ARGS

%install
. OpenIb_Host/ff_filegroups.sh

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{pseudo_opt}/
mkdir -p %{buildroot}%{pseudo_opt}samples
mkdir -p %{buildroot}%{ethsysconfdir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/eth-tools

#Binaries and scripts installing (basic tools)
cd $(cat %{_builddir}/RELEASE_PATH)

cd bin
cp -t %{buildroot}%{_sbindir} ${basic_tools_sbin}
cp -t %{buildroot}/%{pseudo_opt}/ ${basic_tools_opt}

cd ../fastfabric
cp -t %{buildroot}%{_sbindir} ${ff_tools_sbin}
cp -t %{buildroot}%{pseudo_opt} ${ff_tools_misc}
cp -t %{buildroot}%{ethsysconfdir} ${basic_configs}

cd ../fastfabric/samples
cp -t %{buildroot}%{pseudo_opt}samples ${ff_iba_samples} ${basic_samples}
cd ..

cd ../fastfabric/tools
chmod 755 *.exp
cp -t %{buildroot}%{pseudo_opt}/ ${ff_tools_exp}
cp -t %{buildroot}%{pseudo_opt}/ ${ff_libs_misc}
cp -t %{buildroot}%{pseudo_opt}/ osid_wrapper
cp -t %{buildroot}%{ethsysconfdir}  allhosts hosts switches
cd ..

cd ../man/man1
cp -t %{buildroot}%{_mandir}/man1 ${basic_mans}
cd ../man8
cp -t %{buildroot}%{_mandir}/man8 ${ff_mans}
cd ..

#Config files
cd ../config
cp -t %{buildroot}/%{ethsysconfdir} ethmon.conf ethmon.si.conf

# Now that we've put everything in the buildroot, copy any default config files to their expected location for user
# to edit. To prevent nuking existing user configs, the files section of this spec file will reference these as noreplace
# config files.
cp %{buildroot}%{pseudo_opt}/ethfastfabric.conf.def %{buildroot}/%{ethsysconfdir}/ethfastfabric.conf

for file in $(ls  %{buildroot}/%{ethsysconfdir}); do
	ln -s %{ethsysconfdir}/$file %{buildroot}/etc/sysconfig/eth-tools/$file
done

#Now we do a bunch of work to build the file listing of what belongs to each RPM

# List for basic
(
	#Basic tools sbin
	for file in ${basic_tools_sbin} ${basic_tools_sbin_sym}; do
		echo "%{_sbindir}/${file}"
	done
	#Basic tools opt
	for file in ${basic_tools_opt}; do
		echo "%{pseudo_opt}/${file}"
	done
	#Basic man pages
	for file in ${basic_mans}; do
		# Extra wildcard to accept .1.gz
		echo "%{_mandir}/man1/${file}*"
	done
	#Basic config pages
	for file in ${basic_configs}; do
		echo "%config(noreplace) %{ethsysconfdir}${file}"
	done
) >  %{_builddir}/basic_file.list

# List for eth-fastfabric
(
	#FF tools opt
	for file in ${ff_tools_opt}; do
		echo "%{pseudo_opt}/${file}"
	done

	#FF exp files opt
	for file in ${ff_tools_exp}; do
		echo "%{pseudo_opt}/${file}"
	done

	#FF misc files opt
	for file in ${ff_tools_misc}; do
		echo "%{pseudo_opt}/${file}"
	done

	#FF libs misc
	for file in ${ff_libs_misc}; do
		echo "%{pseudo_opt}/${file}"
	done

	#FF iba samples
	for file in ${ff_iba_samples} ${basic_samples}; do
		echo "%{pseudo_opt}samples/${file}"
	done

	#FF tools to FM configuration
	for file in ${ff_tools_fm}; do
		echo "%{pseudo_opt}fm_tools/${file}"
	done

	#FF man pages
	for file in ${ff_mans}; do
		# Extra wildcard to accept .8.gz
		echo "%{_mandir}/man8/${file}*"
	done

	#FF tools help doc
	for file in ${help_doc}; do
		echo "%{pseudo_opt}help/${file}"
	done

	#FF tools sbin
	for file in ${ff_tools_sbin}; do
		echo "%{_sbindir}/${file}"
	done

) > %{_builddir}/ff_file.list

%files -n eth-basic-tools -f %{_builddir}/basic_file.list
%defattr(-,root,root,-)
%dir %{pseudo_opt}
%dir %{ethsysconfdir}

%doc README
%license LICENSE

%files -n eth-fastfabric -f %{_builddir}/ff_file.list
%defattr(-,root,root,0755)
%dir %{pseudo_opt}
%dir %{pseudo_opt}samples
%{pseudo_opt}/osid_wrapper

%dir %{_sysconfdir}/sysconfig/eth-tools
%dir %{ethsysconfdir}
%{_sysconfdir}/sysconfig/eth-tools/*

%config(noreplace) %{ethsysconfdir}/ethfastfabric.conf
%config(noreplace) %{ethsysconfdir}/ethmon.conf
%config(noreplace) %{ethsysconfdir}/ethmon.si.conf
%config(noreplace) %{ethsysconfdir}/allhosts
%config(noreplace) %{ethsysconfdir}/hosts
%config(noreplace) %{ethsysconfdir}/switches

%changelog
