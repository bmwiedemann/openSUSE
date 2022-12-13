#
# spec file
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


%global flavor @BUILD_FLAVOR@%nil

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%global pname gnu
%global compiler_family %pname

%define myname   %{compiler_family}%{?c_f_ver}-compilers-hpc

%if "%flavor" == "gnu-hpc"
%undefine c_f_ver
%endif

%if "%flavor" == "gnu6-hpc"
%define c_f_ver 6
%endif

%if "%flavor" == "gnu7-hpc"
%define c_f_ver 7
%endif

%if "%flavor" == "gnu8-hpc"
%define c_f_ver 8
%endif

%if "%flavor" == "gnu9-hpc"
%define c_f_ver 9
%endif

%if "%flavor" == "gnu10-hpc"
%define c_f_ver 10
%endif

%if "%flavor" == "gnu11-hpc"
%define c_f_ver 11
%endif

%if "%flavor" == "gnu12-hpc"
%define c_f_ver 12
%endif

# For Factory only build the default
%if 0%{?suse_version} > 1500 && "%flavor" != "gnu-hpc"
ExclusiveArch:  do-not-build
%endif

%{!?_rpmmacrodir:%define _rpmmacrodir %{_sysconfdir}/rpm}
# Keep in sync with macros.hpc-gnu
# ab >= 40 - version: a.b to accompodate for old gcc version scheme of gcc < 5
%global hpc_gnu_bin_version %{?c_f_ver:-%(v=%c_f_ver; [ $v -lt 40 ] && echo $v ||
                              sed -e "s@\\([0-9]\\)@\\1.@g" \\
                                  -e "s@\\([0-9]\\)\\.\\$@\\1@g" <<< $v)}
%global hpc_gnu_full_version %( gcc%{hpc_gnu_bin_version} --version |\
                head -1 |\
                sed -e "s#.* \\([0-9]\\+\\.[0-9.]\\+\\)\\(\$\\| .*\\)#\\1#" )
%global hpc_gnu_dep_version %(HPC_CF_FULL_VERSION=%hpc_gnu_full_version; \
                    [ ${HPC_CF_FULL_VERSION%%%%.*} -lt 5 ] && \
                    echo ${HPC_CF_FULL_VERSION%%.*} || \
                    echo ${HPC_CF_FULL_VERSION%%%%.*} )
%global hpc_prov_version %{!?c_f_ver:%(var=%hpc_gnu_dep_version; echo ${var/./_})}
%global hpc_gnu_pack_version %{?c_f_ver}
%if 0%{!?leap_version:1} && 0%{!?sle_version:1}
%global hpc_rolling_release_version %(echo %hpc_gnu_dep_version | tr -d '.')
%endif
%global hpc_gnu_dir gnu%{hpc_gnu_dep_version}
%hpc_init -C -c %compiler_family %{?c_f_ver:-v %{c_f_ver}}

Summary:        SUSE HPC GNU Compiler Toolchain environment
License:        BSD-3-Clause
Group:          Development/Tools/Other
Name:           %myname
Version:        1.4
Release:        0

URL:            https://github.com/openhpc/ohpc
Source0:        https://raw.githubusercontent.com/openSUSE/hpc/master/compiler/macros.hpc-gnu
Source1:        LICENSE
Source2:        gnu-compilers-hpc-rpmlintrc
Source3:        _multibuild
BuildRequires:  gcc%{?c_f_ver}
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%{!?c_f_ver: #
Provides:       %{compiler_family}%{?hpc_prov_version}-compilers-hpc = %version-%release
}
Requires:       lua-lmod
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Provides HPC-compatible setup and configuration for the GNU compiler toolchain.

%define meta README.meta

%package devel
Summary:        Devel package for HPC GNU compiler environment
Group:          Development/Tools/Other
BuildArch:      noarch
%{!?c_f_ver: #
Provides:       %{compiler_family}%{?hpc_prov_version}-compilers-hpc-devel = %version-%release
}
Requires:       %{name} = %{version}
Requires:       gcc%{hpc_cf_pack_version}
Requires:       gcc%{hpc_cf_pack_version}-c++
Requires:       gcc%{hpc_cf_pack_version}-fortran
%if 0%{?hpc_rolling_release_version:1}
Requires:       gcc%{hpc_rolling_release_version}
Requires:       gcc%{hpc_rolling_release_version}-c++
Requires:       gcc%{hpc_rolling_release_version}-fortran
%endif

%description devel
Provides package dependencies for building with the GNU compiler toolchain.

%package macros-devel
Summary:        Macro package for HPC GNU compiler environment
Group:          Development/Tools/Other
Provides:       %{pname}-hpc-macros-devel = %{version}
Conflicts:      otherproviders(%{pname}-hpc-macros-devel)
BuildArch:      noarch
%{!?c_f_ver: #
Provides:       %{compiler_family}%{?hpc_prov_version}-compilers-hpc-macros-devel = %version-%release
}
Requires:       %{name}-devel = %{version}

%description macros-devel
Provides macros for building HPC compliant RPM with the GNU compiler toolchain.

%prep

%build
echo "hpc_gnu_full_version: %hpc_gnu_full_version"
echo "hpc_gnu_dep_version: %hpc_gnu_dep_version"
echo "hpc_gnu_bin_version: %hpc_gnu_bin_version"
%{!?c_f_ver:echo "hpc_prov_version: %hpc_prov_version"}

%{__cat} <<EOF > %{meta}
%{name}-devel is a meta package to ensure installation of the
gnu toolchain.
EOF

%install
mkdir -p %{buildroot}/%{_rpmmacrodir}
cp %{S:0} %{buildroot}/%{_rpmmacrodir}
cp %{S:1} .
%define lmod_base %{lua_lmod_modulesdir}/%pname
mkdir -p %{buildroot}%{hpc_cf_install_path}
mkdir -p %{buildroot}%{hpc_install_base}
mkdir -p %{buildroot}%{hpc_modulepath}
mkdir -p %{buildroot}%{lua_lmod_modulesdir}/%pname
%{__cat} <<EOF > %{buildroot}/%{lmod_base}/%{hpc_cf_dep_version}
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the GNU compiler collection"
puts stderr " "
puts stderr "Consult the man pages for detailed information"
puts stderr "on the commandline syntax and compiler options."
puts stderr " "

puts stderr "\nVersion %{hpc_cf_dep_version}\n"

}
module-whatis "Name: GNU Compiler Collection"
module-whatis "Version: %{version}"
module-whatis "Category: compiler, runtime support"
module-whatis "Description: GNU Compiler Family (C/C++/Fortran for %_arch)"
module-whatis "URL: http://gcc.gnu.org"

set     version                     %{hpc_cf_dep_version}
prepend-path    MODULEPATH          %{hpc_modulepath}
prepend-path    PATH    %{hpc_cf_install_path}/bin
%if 0%{?c_f_ver:1} > 0
if {[file isfile  %{_bindir}/gcc%{hpc_gnu_bin_version}]} {
prepend-path    MANPATH %{hpc_cf_install_path}/man
setenv		CC      gcc%{hpc_gnu_bin_version}
setenv		CXX     g++%{hpc_gnu_bin_version}
setenv		FC      gfortran%{hpc_gnu_bin_version}
setenv		F77     gfortran%{hpc_gnu_bin_version}
}
%else
# nothing to do since gcc is in the default path
%endif

family "compiler"

EOF

export hpc_cf_dep_version=%{hpc_cf_dep_version}
%{__cat} <<EOF > %{buildroot}/%{lmod_base}/.version.%{hpc_cf_dep_version}
#%%Module1.0#####################################################################
##
## version file for GNU-compilers-${hpc_cf_dep_version}
##
set     ModulesVersion      "%{hpc_cf_dep_version}"

EOF

%if 0%{?c_f_ver:1}
%preun devel
rm -rf %{hpc_cf_install_path}/bin %{hpc_cf_install_path}/bin
%endif

%posttrans devel
mkdir -p %{hpc_cf_install_path}/bin
%if 0%{?c_f_ver:1}
export list="cpp%{hpc_cf_pack_version} gcc%{hpc_cf_pack_version} \
            gcc%{hpc_cf_pack_version}-c++ gcc%{hpc_cf_pack_version}-fortran"
for i in $(rpm -ql ${list} | grep -E -e "/usr/bin|/usr/share/man")
do
    dir=$(dirname $i)
    base=$(basename $i)
    base=${base/%{hpc_gnu_bin_version}/}
    base=${base/.././}
    case $dir in
        /usr/share/man*)
            mandir=$(basename $dir)
            mkdir -p %{hpc_cf_install_path}/man/${mandir}
            ln -sf $i %{hpc_cf_install_path}/man/${mandir}/$base
            ;;
        /usr/bin*)
            ln -sf $i %{hpc_cf_install_path}/bin/$base
            ;;
    esac
done
for i in cc,gcc c++,g++; do
    test -e %{hpc_cf_install_path}/bin/${i##*,}%{hpc_gnu_bin_version} \
	&& ln -s %{hpc_cf_install_path}/bin/${i%%%%,*} ${i##*,}%{hpc_gnu_bin_version}
fi
%else
# for the base compiler version link to the 'default' binary:
localbindir=%_bindir/
for i in cc cpp c++
do
    test -e %{hpc_cf_install_path}/bin/${i} || ln -sf ${localbindir}${i}%{hpc_gnu_bin_version} %{hpc_cf_install_path}/bin/${i}
done
test -e %{hpc_cf_install_path}/bin/fortran || ln -sf ${localbindir}gfortran%{hpc_gnu_bin_version} %{hpc_cf_install_path}/bin/fc
%endif

%files
%defattr(-,root,root,-)
%license LICENSE
%dir %{lua_lmod_modulesdir}/%{pname}
%dir %{hpc_modulepath}
%dir %{hpc_base}
%dir %hpc_install_base
%hpc_cf_dirs
%{lua_lmod_modulesdir}/%{pname}/%{hpc_cf_dep_version}
%{lua_lmod_modulesdir}/%{pname}/.version.%{hpc_cf_dep_version}

%files devel
%defattr(-,root,root,-)
%doc %{meta}

%files macros-devel
%defattr(-,root,root,-)
%config %{_rpmmacrodir}/macros.hpc-gnu

%changelog
