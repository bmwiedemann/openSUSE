#
# spec file for package opa-ff
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


%define git_ver .0.35.0.bd8b24a56fcb
%define opamgt_major 0
%define opasadb_major 1_0_0

%define pseudo_opt %{_prefix}/lib/opa/
%define opasysconfdir %{_sysconfdir}/opa/

Name:           opa-ff
Version:        10.10.1
Release:        0
Summary:        Intel Omni-Path basic tools and libraries for fabric managment
License:        BSD-3-Clause OR GPL-2.0-only
Group:          Productivity/Networking/System
URL:            https://github.com/intel/opa-ff
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        opa-ff.rpmlintrc
Patch1:         opa-ff-add-shebang-for-exp-files.patch
Patch2:         opa-ff-suse-build-fixes.patch
Patch3:         workaround-bsc-1172755.patch
BuildRequires:  gcc-c++
BuildRequires:  infiniband-diags-devel
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
BuildRequires:  librdmacm1
BuildRequires:  ncurses-devel
BuildRequires:  rdma-core-devel
BuildRequires:  tcl-devel
BuildRequires:  zlib-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Currently ONLY builds on x86_64
ExclusiveArch:  x86_64

%description
The %{name} contains basic tools and libraries for Intel Omni-Path fabric management applications. This
includes: the opa-fastfabric opa-basic-tools, opa-address-resolution

%package     -n opa-basic-tools
Summary:        OmniPath managment level tools and scripts
Group:          Productivity/Networking/System
Requires:       rdma

%description -n opa-basic-tools
Contains basic tools for fabric managment necessary on all compute nodes.

%package -n opa-fastfabric
Summary:        OmniPath management level tools and scripts
Group:          Productivity/Networking/System
Requires:       cron
Requires:       opa-basic-tools
%if 0%{?rhel}
Requires:       atlas
%endif

%description -n opa-fastfabric
Contains tools for managing fabric on a managment node.

%package -n libopasadb%{opasadb_major}
Summary:        OmniPath Subnet Administrator database library
Group:          System/Libraries

%description -n libopasadb%{opasadb_major}
This package contains the library necessary for opa-address-resolution.

%package -n opa-address-resolution
Summary:        OmniPath Address Resolution manager
Group:          Productivity/Networking/System
Requires:       opa-basic-tools

%description -n opa-address-resolution
This package contains the ibacm distributed SA provider (dsap) for name and address resolution on OPA platform.
It also contains the library and tools to access the shared memory database exported by dsap.

%package -n opa-address-resolution-devel
Summary:        Development files for the OmniPath Address Resolution manager
Group:          Development/Libraries/C and C++
Requires:       libopasadb%{opasadb_major} = %{version}
Requires:       opa-address-resolution = %{version}
Requires:       opa-basic-tools

%description -n opa-address-resolution-devel
This package contains the include files and libraries
required to develop programs for the opa-address-resolution package.

%package -n libopamgt%{opamgt_major}
Summary:        Omni-Path management API library
Group:          System/Libraries

%description -n libopamgt%{opamgt_major}
This package contains the library necessary to build applications that interface with an Omni-Path FM.


%package -n libopamgt-devel
Summary:        Omni-Path library development headers
Group:          Development/Libraries/C and C++
Requires:       libopamgt%{opamgt_major} = %{version}

%description -n libopamgt-devel
This package contains the necessary headers for opamgt development.

%package -n     opa-snapconfig
Summary:        Tools for configureing fabrics with snapshot files
Group:          Productivity/Networking/System
Requires:       opa-fastfabric

%description -n opa-snapconfig
Tools for parsing information from provided snapshot files and issuing packets to program.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch1
%patch2
%patch3

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-address-of-packed-member"
if [ -d OpenIb_Host ]
then
        cd OpenIb_Host && ./ff_build.sh %{_builddir} $FF_BUILD_ARGS
else
        ./ff_build.sh %{_builddir} $FF_BUILD_ARGS
fi

%install
. OpenIb_Host/ff_filegroups.sh
%define release_string IntelOPA-Tools-FF.$BUILD_TARGET_OS_ID.$MODULEVERSION

#rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{pseudo_opt}/{tools,fm_tools,help,samples,samples/opamgt}
mkdir -p %{buildroot}%{_libdir}/ibacm
mkdir -p %{buildroot}%{_sysconfdir}/rdma
mkdir -p %{buildroot}%{_sysconfdir}/opa
mkdir -p %{buildroot}%{opasysconfdir}
mkdir -p %{buildroot}%{_includedir}/infiniband
mkdir -p %{buildroot}%{_includedir}/opamgt/iba/public
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/opa
mkdir -p  %{buildroot}%{_sysconfdir}/cron.daily/
#Binaries and scripts installing (basic tools)
#cd builtbin.OPENIB_FF.release
cd $(cat %{_builddir}/RELEASE_PATH)

cd bin
cp -t %{buildroot}%{_sbindir} ${basic_tools_sbin}
cp -t %{buildroot}/%{pseudo_opt}/tools/ ${basic_tools_opt}
ln -s ./opaportinfo %{buildroot}%{_sbindir}/opaportconfig
ln -s ./opasmaquery %{buildroot}%{_sbindir}/opapmaquery

cd ../opasadb
cp -t %{buildroot}%{_bindir} ${opasadb_bin}
cp -t %{buildroot}%{_includedir}/infiniband ${opasadb_header}

cd ../opamgt
cp -t %{buildroot}%{_includedir}/opamgt $opamgt_headers
cp -t %{buildroot}%{_includedir}/opamgt/iba $opamgt_iba_headers
cp -t %{buildroot}%{_includedir}/opamgt/iba/public $opamgt_iba_public_headers
cp -t %{buildroot}%{pseudo_opt}/samples/opamgt $opamgt_examples

cd ../bin
cp -t %{buildroot}/%{pseudo_opt}/tools/ ${ff_tools_opt}
#cp -t %{buildroot}/%{pseudo_opt}/tools/ ${opasnapconfig_bin}

cd ../fastfabric
cp -t %{buildroot}%{_sbindir} ${ff_tools_sbin}
cp -t %{buildroot}%{pseudo_opt}tools/ ${ff_tools_misc}
cp -t %{buildroot}%{pseudo_opt}help ${help_doc}
cp -t %{buildroot}%{opasysconfdir} ${basic_configs}

cd ../etc
cp -t %{buildroot}/%{pseudo_opt}fm_tools/ ${ff_tools_fm}
ln -s %{pseudo_opt}/fm_tools/config_check %{buildroot}%{_sbindir}/opafmconfigcheck
ln -s %{pseudo_opt}/fm_tools/config_diff %{buildroot}%{_sbindir}/opafmconfigdiff
cd cron.d
# We do not want there cron.d stuff. Directly link the proper bin in cron.daily
ln -s /%{pseudo_opt}tools/opacablehealthcron %{buildroot}%{_sysconfdir}/cron.daily/opa-cablehealth
cd ..
cd ../fastfabric/samples
cp -t %{buildroot}%{pseudo_opt}samples ${ff_iba_samples} ${basic_samples}
cd ..

cd ../fastfabric/tools
chmod 755 *.exp
cp -t %{buildroot}%{pseudo_opt}tools/ ${ff_tools_exp}
cp -t %{buildroot}%{pseudo_opt}tools/ ${ff_libs_misc}
cp -t %{buildroot}%{pseudo_opt}tools/ osid_wrapper
cp -t %{buildroot}%{opasysconfdir}  allhosts chassis esm_chassis hosts ports switches
cd ..

cd ../man/man1
cp -t %{buildroot}%{_mandir}/man1 ${basic_mans}
cp -t %{buildroot}%{_mandir}/man1 ${opasadb_mans}
cd ../man8
cp -t %{buildroot}%{_mandir}/man8 ${ff_mans}
cd ..

#Config files
cd ../config
cp -t %{buildroot}%{_sysconfdir}/rdma dsap.conf op_path_rec.conf opasadb.xml
cp -t %{buildroot}/%{opasysconfdir} opamon.conf opamon.si.conf

#Libraries installing
cd $(cat %{_builddir}/LIB_PATH)
cp -t %{buildroot}%{_libdir} libopasadb.so.*
ln -s libopasadb.so.* %{buildroot}%{_libdir}/libopasadb.so
cp -t %{buildroot}%{_libdir}/ibacm libdsap.so.*
ln -s libdsap.so.* %{buildroot}%{_libdir}/ibacm/libdsap.so
cp -t %{buildroot}%{_libdir}/ libopamgt.so.*
ln -s libopamgt.so.* %{buildroot}%{_libdir}/libopamgt.so

# Now that we've put everything in the buildroot, copy any default config files to their expected location for user
# to edit. To prevent nuking existing user configs, the files section of this spec file will reference these as noreplace
# config files.
cp %{buildroot}%{pseudo_opt}tools/opafastfabric.conf.def %{buildroot}/%{opasysconfdir}/opafastfabric.conf

for file in $(ls  %{buildroot}/%{opasysconfdir}); do
	ln -s %{opasysconfdir}/$file %{buildroot}/etc/sysconfig/opa/$file
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
		echo "%{pseudo_opt}tools/${file}"
	done
	#Basic man pages
	for file in ${basic_mans}; do
		# Extra wildcard to accept .1.gz
		echo "%{_mandir}/man1/${file}*"
	done
	#Basic config pages
	for file in ${basic_configs}; do
		echo "%config(noreplace) %{opasysconfdir}${file}"
	done
) >  %{_builddir}/basic_file.list

# List for opa-fastfabric
(
	#FF tools opt
	for file in ${ff_tools_opt}; do
		echo "%{pseudo_opt}tools/${file}"
	done

	#FF exp files opt
	for file in ${ff_tools_exp}; do
		echo "%{pseudo_opt}tools/${file}"
	done

	#FF misc files opt
	for file in ${ff_tools_misc}; do
		echo "%{pseudo_opt}tools/${file}"
	done

	#FF libs misc
	for file in ${ff_libs_misc}; do
		echo "%{pseudo_opt}tools/${file}"
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

# List for snapconfig
(
	for file in ${opasnapconfig_bin}; do
		echo "%{pseudo_opt}tools/${file}"
	done
) >  %{_builddir}/snapconfig_file.list

%post   -n libopasadb%{opasadb_major} -p /sbin/ldconfig
%postun -n libopasadb%{opasadb_major} -p /sbin/ldconfig

%post   -n libopamgt%{opamgt_major} -p /sbin/ldconfig
%postun -n libopamgt%{opamgt_major} -p /sbin/ldconfig

%files -n opa-basic-tools -f %{_builddir}/basic_file.list
%defattr(-,root,root,-)
%dir %{pseudo_opt}
%dir %{pseudo_opt}tools/
%dir %{opasysconfdir}

%doc README
%license LICENSE

%files -n opa-fastfabric -f %{_builddir}/ff_file.list
%defattr(-,root,root,0755)
%dir %{pseudo_opt}
%dir %{pseudo_opt}fm_tools
%dir %{pseudo_opt}help
%dir %{pseudo_opt}samples
%dir %{pseudo_opt}tools

%dir %{_sysconfdir}/sysconfig/opa
%dir %{opasysconfdir}
/etc/sysconfig/opa/*

%config(noreplace) %{opasysconfdir}/opafastfabric.conf
%config(noreplace) %{opasysconfdir}/opamon.conf
%config(noreplace) %{opasysconfdir}/allhosts
%config(noreplace) %{opasysconfdir}/chassis
%config(noreplace) %{opasysconfdir}/esm_chassis
%config(noreplace) %{opasysconfdir}/hosts
%config(noreplace) %{opasysconfdir}/ports
%config(noreplace) %{opasysconfdir}/switches
%dir %{_sysconfdir}/cron.daily
%config(noreplace) %{_sysconfdir}/cron.daily/opa-cablehealth
%{opasysconfdir}/opamon.si.conf
# Replace opamon.si.conf, as it's a template config file.
%{pseudo_opt}tools/osid_wrapper
%{_sbindir}/opafmconfigcheck
%{_sbindir}/opafmconfigdiff

# /opt/opa

%files -n libopasadb%{opasadb_major}
%defattr(-,root,root)
%{_libdir}/libopasadb.so.1*

%files -n opa-address-resolution
%defattr(-,root,root,-)
%dir %{_sysconfdir}/rdma/
%dir %{_libdir}/ibacm/
#Everything under the bin directory belongs exclusively to opasadb at this time.
%{_bindir}/*
%{_libdir}/ibacm/*.so.*
%{_mandir}/man1/opa_osd_dump.1*
%{_mandir}/man1/opa_osd_exercise.1*
%{_mandir}/man1/opa_osd_perf.1*
%{_mandir}/man1/opa_osd_query.1*
%config(noreplace) %{_sysconfdir}/rdma/dsap.conf
%config(noreplace) %{_sysconfdir}/rdma/op_path_rec.conf
%config %{_sysconfdir}/rdma/opasadb.xml

%files -n opa-address-resolution-devel
%{_includedir}/infiniband
%{_libdir}/libopasadb.so
%{_libdir}/ibacm/libdsap.so

%files -n libopamgt%{opamgt_major}
%{_libdir}/libopamgt.so.0*

%files -n libopamgt-devel
%{_libdir}/libopamgt.so
%{_includedir}/opamgt
%{pseudo_opt}/samples/opamgt

%files -n opa-snapconfig -f %{_builddir}/snapconfig_file.list
%defattr(-,root,root,-)
%dir %{pseudo_opt}
%dir %{pseudo_opt}tools/

%doc README
%license LICENSE

%changelog
