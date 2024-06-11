#
# spec file for package spack
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


%global flavor @BUILD_FLAVOR@%{?nil}
%if "%{flavor}" == "doc"
%bcond_without doc
%endif

ExcludeArch:    i586 %arm s390 s390x %power64 ppc

%if %{with doc} && (0%{?sle_version} > 0) && (150200 >= 0%{?sle_version})
ExclusiveArch:  do_not_build
%endif

%define spack_dir  %_prefix/lib/spack/
%define spack_group spack
# These packages are missing from a BCI-style base container but may
# be used by Spack for building. To avoid unresolved libraries, make
# sure these are installed in the runtime container.
%if 0%{suse_version} == 1500
%define spack_container_packages libgfortran4 libfl2 libzip5
%else
%if 0%{suse_version} >  1600
%define spack_container_packages libgfortran5 libfl2 libzip5
%endif
%endif

# These packages are found and can be used by spack, %{_sysconfdir}/spack/packages-yaml
# needs to be updated when one of these packages is updated or uninstalled.
# Distinguish between packages we recommend and packages which
%define spack_trigger_recommended_packages autoconf bash bison bzip2 libzip-devel cmake-full ccache cpio diffutils findutils flex git-lfs info make makeinfo m4 ncurses-devel libtool libcurl-devel libopenssl-devel perl-base pkgconf pkg-config python3-base tar xz xz-devel

%define spack_trigger_recommended_compilers  gcc gcc-c++ gcc-fortran

# packages recognized by spack, but not recommended
%define spack_trigger_packages ghostscript go fish fzf hwloc-devel hugo java-11-openjdk-devel java-14-openjdk-devel java-15-openjdk-devel java-16-openjdk-devel java-1_8_0-openjdk-devel ruby sqlite3 openmpi1-devel openmpi2-devel openmpi3-devel openmpi4-devel openmpi1-gnu-hpc-devel openmpi2-gnu-hpc-devel openmpi3-gnu-hpc-devel openmpi4-gnu-hpc-devel mpich-gnu-hpc-devel mvapich2-devel mpich-devel

%define spack_trigger_compilers gcc7 gcc8 gcc9 gcc10 gcc11 gcc12 gcc13 gcc7-c++ gcc8-c++ gcc9-c++ gcc10-c++ gcc11-c++ gcc12-c++ gcc13-c++ gcc7-fortran gcc8-fortran gcc9-fortran gcc10-fortran gcc11-fortran gcc12-fortran gcc13-fortran

# non oss packages
%define spack_trigger_external cuda-nvcc

%if  0%{?sle_version} <= 120500 && !0%{?is_opensuse}
%define __python3 python3
%endif

%define mypyver 3
%define mypython python%{?mypyver}

Name:           spack
Version:        0.22.0
Release:        0
Summary:        Package manager for HPC systems
License:        Apache-2.0 AND MIT AND Python-2.0 AND BSD-3-Clause
URL:            https://spack.io
Source0:        https://github.com/spack/spack/archive/v%{version}.tar.gz#/spack-%{version}.tar.gz
Source1:        README.SUSE
Source2:        spack-rpmlintrc
Source3:        run-find-external.sh.in
# without `--header "Accept-Language: en" en.opensuse.org returns 406
#Source4:        https://en.opensuse.org/index.php?title=Spack&action=raw&ref=157522#/README-oo-wiki
Source4:        README-oo-wiki
# Source5 is from https://docs.python.org/3/objects.inv, but has permanent changes so using a static version
Source5:        objects.inv
Source6:        spack_get_libs.sh
Patch2:         Adapt-shell-scripts-that-set-up-the-environment-for-different-shells.patch
Patch4:         added-target-and-os-calls-to-output-of-spack-spec-co.patch
Patch5:         Make-spack-paths-compliant-to-distro-installation.patch
Patch6:         Fix-error-during-documentation-build-due-to-recursive-module-inclusion.patch
Patch7:         Fix-Spinx-configuration-to-avoid-throwing-errors.patch
Patch8:         Set-modules-default-to-lmod.patch
Patch9:         Add-support-for-container-building-using-a-SLE-base-container.patch
Patch10:        Move-site-config-scope-before-system-scope.patch
%if %{without doc}
BuildRequires:  %{mypython}-urllib3
BuildRequires:  fdupes
BuildRequires:  lua-lmod
BuildRequires:  polkit
BuildRequires:  sudo
BuildRequires:  sysuser-tools
Requires:       %{mypython}-clingo
Requires:       %{name}-recipes = %{version}
Requires:       awk
Requires:       bzip2
Requires:       coreutils
Requires:       curl
Requires:       gcc-c++
Requires:       gcc-fortran
Requires:       git
Requires:       gpg2
Requires:       gzip
Requires:       libbz2-devel
Requires:       lsb-release
Requires:       make
Requires:       patch
Requires:       polkit
Requires:       sudo
Requires:       system-user-nobody
Requires:       tar
Requires:       unzip
Requires:       xz
Requires:       zstd
Requires:       (patchelf if (product(SUSE_SLE) >= 15.6 or product(Leap) or product(openSUSE)))
Recommends:     %spack_trigger_recommended_packages %spack_trigger_recommended_compilers
Recommends:     lua-lmod
Recommends:     patchelf
Requires:       (hwloc if hwloc-devel)
Requires:       (hwloc-devel if hwloc)
%else
BuildRequires:  git
BuildRequires:  makeinfo
# Hardcode this - there is no python2 version of this around any more.
BuildRequires:  %{mypython}-Sphinx >= 3.4
BuildRequires:  %{mypython}-sphinxcontrib-programoutput
BuildRequires:  spack
# html
BuildRequires:  graphviz
# info
BuildRequires:  graphviz-gnome
## pdf
# BuildRequires:  %{mypython}-Sphinx-latex
Recommends:     spack
%endif
BuildArch:      noarch

%description
Spack is a configurable Python-based HPC package manager, automating
the installation and fine-tuning of simulations and libraries.
It operates on a wide variety of HPC platforms and enables users
to build many code configurations. Software installed by Spack
runs correctly regardless of environment, and file management
is streamlined. Spack can install many variants of the same build
using different compilers, options, and MPI implementations.

This package provides a module file that must be loaded to use spack.

%package recipes
Summary:        Spack built-in package recipes
Requires:       %{name} = %version

%description recipes
Spack is a configurable Python-based HPC package manager, automating
the installation and fine-tuning of simulations and libraries.
It operates on a wide variety of HPC platforms and enables users
to build many code configurations. Software installed by Spack
runs correctly regardless of environment, and file management
is streamlined. Spack can install many variants of the same build
using different compilers, options, and MPI implementations.

This package contains the built-in package recipes.

%package man
Summary:        Man Page for Spack - Package manager for HPC systems
Requires:       man

%description man
Spack is a configurable Python-based HPC package manager, automating
the installation and fine-tuning of simulations and libraries.
It operates on a wide variety of HPC platforms and enables users
to build many code configurations. Software installed by Spack
runs correctly regardless of environment, and file management
is streamlined. Spack can install many variants of the same build
using different compilers, options, and MPI implementations.

This package contains the man page.

%package info
Summary:        Info Page for Spack - Package manager for HPC systems
Requires:       info
%if 0%{?suse_version} <= 1500
Requires(post): %{install_info_prereq}
Requires(pre):  %{install_info_prereq}
%endif

%description info
Spack is a configurable Python-based HPC package manager, automating
the installation and fine-tuning of simulations and libraries.
It operates on a wide variety of HPC platforms and enables users
to build many code configurations. Software installed by Spack
runs correctly regardless of environment, and file management
is streamlined. Spack can install many variants of the same build
using different compilers, options, and MPI implementations.

This package contains the info page.

%package build-dependencies
Summary:        Spack Build Dependencies
Requires:       bison
Requires:       cmake-full
Requires:       flex
Requires:       libcurl-devel
Requires:       libopenssl-devel
Requires:       libtool
Requires:       libzip-devel
Requires:       ncurses-devel
Requires:       xz-devel
Requires:       zip

%description build-dependencies
This package provides dependencies to packages of some frequently used
build tools. If Spack finds these on the system it will not attempt to
build them.

%prep
%setup -q
%autopatch -p1
%if %{without doc}

# set SPACK_ROOT
for i in share/spack/setup-env.*; do
    sed -i -e "s;@@_prefix@@;%_prefix;g" $i
done
%else
cp %{S:5} lib/spack/docs/
%endif

%build
# Nothing to build
%if %{with doc}
mkdir -p ${HOME}/.spack
cat > ${HOME}/.spack/config.yaml <<EOF
config:
  install_tree:
    root: /tmp/spack
    projections:
      all: "${ARCHITECTURE}/${COMPILERNAME}-${COMPILERVER}/${PACKAGE}-${VERSION}-${HASH}"
EOF
# Don't really run spack when building documentation!
tmpdir=$(mktemp -d %{_sourcedir}/tmpd-XXXXXXXXX)
echo -e '#! /bin/sh
args=${1+"$@"}
while [ -n "$1" ]; do
  case $1 in
    --*) shift ;;
    graph|spec|unit-test) exit 0 ;;
    *) exec %{_bindir}/spack ${args} ;;
  esac;
done
exit 0' > $tmpdir/spack
chmod 0755 $tmpdir/spack
PATH=$tmpdir:${PATH}
export PATH
mkdir -p /tmp/spack
cd lib/spack/docs
# fix Makefile of sphinx and ignore warnings due to offline build
sed -i 's/\(^SPHINXOPTS\).*/\1 = --keep-going /' Makefile
# Causes issues building texinfo as a suitable image cannot be found
grep -rl ":target:" | xargs sed  -i -e "/:target:/s/^/#/" -e "/figure::/s/^/#/"
# Fix path to var - we install this to the 'real' /var
grep -rl "\$SPACK_ROOT/var" | xargs sed -i -e "s@\(.*\)\$SPACK_ROOT/var\(/spack.*\)@\1/var/lib\2@g"
grep -rl '/var/lib/spack/repos' | grep -v "cmd/list.py" | \
    xargs -i@ sed -i 's|/var/lib/spack/repos|/usr/share/spack/repos|g' @
# spack cannot run without knowing at least the compiler, so we inject
# a dummy one
mkdir -p ${HOME}/.spack/linux/
source /usr/share/spack/setup-env.sh
make man info || { cat /tmp/sphinx-err-*.log; exit 1; } #text dirhtml
rm -rf $tmpdir
gzip _build/texinfo/Spack.info _build/man/spack.1
# with doc
%endif
cd -
grep -rl '#! /usr/bin/env bash' . | xargs -i@ sed -i '1s|#! /usr/bin/env bash|#!%{_bindir}/bash|g' @
grep -rl '#!/bin/env sh' . | xargs -i@ sed -i '1s|#!/bin/env sh|#!%{_bindir}/sh|g' @
grep -rl '#!/usr/bin/env bash' . | xargs -i@ sed -i '1s|#!/usr/bin/env bash|#!%{_bindir}/bash|g' @
grep -rl '#![[:space:]]*/usr/bin/env python' | \
    xargs -i@ sed -i '1s|#![[:space:]]*/usr/bin/env python|#!%{_bindir}/%{mypython}|g' @
grep -rl '/var/spack/repos' | grep -v "cmd/list.py" | \
    xargs -i@ sed -i 's|/var/spack/repos|/usr/share/spack/repos|g' @
grep -rl "spack/" . | xargs -i@ sed -i \
  -e 's|$spack/opt|/opt|g' \
  -e 's|$spack/var|/var/lib|g'\
  -e 's|$spack/usr|/usr|g'\
  -e 's|$spack/share/spack/lmod|/opt/spack/modules|g'\
  -e 's|$spack/share/spack/modules|/opt/spack/modules|g'\
  @

%install
# combine READMEs
cat %{S:4} >> %{S:1}
%if %{without doc}
cp %{S:1} .
# Fix some rpmlint warnings
## Remove files not required to run spack
rm -rf lib/spack/spack/test
rm -rf share/spack/qa
rm -rf share/spack/logo
rm -rf var/spack/repos/builtin.mock  var/spack/gpg.mock var/spack/mock_configs var/spack/repos/duplicates.test
rm -rf lib/spack/external/ruamel/yaml/.ruamel
find . -type f -name .gitignore -delete
find . -type f -name .nojekyll -delete
find . -type f -name .gitlab-ci.yml -delete

# Fix _spack_root link
rm -f lib/spack/docs/_spack_root
ln -sf ../.. lib/spack/docs/_spack_root
# Do not ship AWS specifics
rm -f share/spack/setup-tutorial-env.sh
# Fix rpmlint warnings
## No need for the standalone scripts
rm -f lib/spack/external/macholib/macho_*.py
## Remove non linux stuff
rm -f bin/spack.bat bin/spack_cmd.bat bin/spack_pwsh.ps1

mkdir -p %{buildroot}%{spack_dir}
mkdir -p %{buildroot}%{spack_dir}/opt
mkdir -p %{buildroot}%{_datarootdir}/spack/lib/spack
mkdir -p %{buildroot}%{_datarootdir}/spack/modules
mkdir -p %{buildroot}%{_localstatedir}/lib/spack
mkdir -p %{buildroot}%{_localstatedir}/lib/spack/junit-report
mkdir -p %{buildroot}%{_localstatedir}/cache/spack
mkdir -p %{buildroot}%{_sysconfdir}/skel/.spack/
mkdir -p %{buildroot}/%{_bindir}
# Link avoids having to fix paths
ln -sf %{buildroot}/%{_localstatedir}/cache/spack %{buildroot}%{_localstatedir}/lib/spack/cache

# Copy files to corresponding paths
cp -r etc %{buildroot}%{_prefix}
cp -r lib/spack/{env,external,llnl,spack,spack_installable} %{buildroot}%{spack_dir}
cp -r share/spack/* %{buildroot}%{_datarootdir}/spack
cp -r var/spack/* %{buildroot}%{_localstatedir}/lib/spack
# No repos in /var
mv %{buildroot}%{_localstatedir}/lib/spack/repos %{buildroot}%{_datarootdir}/spack
cp -r bin/sbang %{buildroot}/%{_bindir}
cp -r bin/spack* %{buildroot}%{_bindir}/
cp %{S:6} %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{_bindir}/%{basename:%{S:6}}
cp etc/spack/defaults/config.yaml %{buildroot}%{_sysconfdir}/skel/.spack/
install -m 755 %{S:3} %{buildroot}/%{spack_dir}/run-find-external.sh
sed -i -e 's#@@_sysconfdir@@#%{_sysconfdir}#' %{buildroot}/%{spack_dir}/run-find-external.sh
sed -i -e '/. \/opt/s#/opt/spack/#/usr/#' %{buildroot}/%{_datarootdir}/spack/templates/container/singularity.def
%{?spack_container_packages:
sed -i -e 's/\(zypper update -y\)/\1 \&\& zypper -n in -y %{spack_container_packages}/' \
					     %{buildroot}%{spack_dir}/spack/container/images.json}
# Make spack only to write to home dir of user, if run as user
sed -i 's@\(\sroot:\) /opt/spack@\1 ~/spack/packages@' %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml
sed -i 's@\(\ssource_cache:\).*@\1 /var/tmp/$user/spack-cache@' %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml
cat >>  %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml <<EOF

  binary_index_root: ~/.spack/indices
EOF

cat >> %{buildroot}%{_sysconfdir}/skel/.spack/modules.yaml <<EOF
modules:
  default:
    roots:
      tcl: ~/spack/modules
      lmod: ~/spack/modules
EOF

# compile python files for %{mypython}
# %%{buildroot}%%{spack_dir}/spack
%{expand:%{py%{?mypyver}_compile .}}

# make shell scripts executeable
find %{buildroot}%{_localstatedir}/lib/spack/ -type f -name \*.sh  -exec chmod 755 {} \;

# Create %{_sysconfdir}/profile.d/spack.sh
# This file properly sets MODULEPATH so lua-lmod can find the modules created by spack
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
cat > %{buildroot}/%{_sysconfdir}/profile.d/spack.sh <<EOF
ID=\$(source /etc/os-release; echo \${ID})
if [ "\${ID}" = "opensuse-tumbleweed" ] ; then
  SPACK_NAME="\${ID/-/}"
else
  SPACK_NAME="\${ID/-/_}\${VERSION_ID/.*/}"
fi
export SPACK_ROOT=%{_prefix}
export MODULEPATH=~/spack/modules/linux-\${SPACK_NAME}-\${CPU}:%{_prefix}/share/spack/modules/linux-\${SPACK_NAME}-\${CPU}:\${MODULEPATH}
# copy local configuration, if its not there
if [ ! -e ~/.spack/config.yaml ] ; then
  # test if user is in spack group by touching database
  if ! touch %{spack_dir}/.spack-db &> /dev/null ; then
    test -e ~/.spack || mkdir -p ~/.spack
    [ -e ~/.spack/config.yaml ] || \
     cp -r %{_sysconfdir}/skel/.spack/config.yaml ~/.spack/
    [ -e ~/.spack/modules.yaml ] || \
     cp -r %{_sysconfdir}/skel/.spack/modules.yaml ~/.spack/
  fi
fi
EOF
# Same for csh
cat > %{buildroot}/%{_sysconfdir}/profile.d/spack.csh <<EOF
# get ID
eval \`awk '/^ID=/ {sub("-","_"); printf("set %%s",\$0);}' /etc/os-release\`
# get VERSION_ID
eval \`awk '/^VERSION_ID=/ {sub("\\\\.[0-9]",""); printf("set %%s",\$0);}' /etc/os-release\`
if ( \$ID == "opensuse_tumbleweed" ) then
  eval \`awk '/^ID=/ {sub("-",""); printf("set %%s",\$0);}' /etc/os-release\`
  set SPACK_NAME=\$ID
else
  set SPACK_NAME="\${ID}\${VERSION_ID}"
endif
set SPACK_ROOT="%{_prefix}"
set MODULEPATH="~/spack/modules/linux-\${SPACK_NAME}-\${CPU}:%{_prefix}/share/spack/modules/linux-\${SPACK_NAME}-\${CPU}:\${MODULEPATH}"
if ( ! -e ~/.spack/config.yaml )  then
  # test if user is in spack group by touching database
  touch %{spack_dir}/.spack-db  >& /dev/null
  if ( \$? == 1  ) then
    test -e ~/.spack || mkdir -p ~/.spack
    test -e ~/.spack/config.yaml  || \
     cp -r %{_sysconfdir}/skel/.spack/config.yaml ~/.spack/
    test -e ~/.spack/modules.yaml  || \
     cp -r %{_sysconfdir}/skel/.spack/modules.yaml ~/.spack/
  endif
endif

EOF
## Create modules.yaml file, so that hierarchy module files are created
#cat >  %{buildroot}%{spack_dir}/etc/spack/modules.yaml <<EOF
#modules:
#  enable:
#    - lmod
#  lmod:
#    core_compilers:
#      - 'gcc@GCC_FULL_VERSION'
#    projections:
#      all: '{compiler.name}-{compiler.version}/{name}/{version}'
#      ^mpi: '{compiler.name}-{compiler.version}/{^mpi.name}-{^mpi.version}/{name}/{version}'
#EOF
mkdir -p %{buildroot}%{_sysconfdir}/spack

# Fix link to not point into buildroot
rm -f %{buildroot}%{_localstatedir}/lib/spack/cache
ln -sf %{_localstatedir}/cache/spack %{buildroot}%{_localstatedir}/lib/spack/cache
# Remove problematic binaries which are removed upstream with
# 0889be20e0d9dcdf4346cdeaa0647285187375f3
rm -r %{buildroot}%{_datarootdir}/spack/repos/builtin/packages/patchelf/test/

echo "g %{name} -" > system-group-%{name}.conf
%sysusers_generate_pre system-group-%{name}.conf %{name} system-group-%{name}.conf
install -D -m 644 system-group-%{name}.conf %{buildroot}%{_sysusersdir}/system-group-%{name}.conf

%fdupes %{buildroot}%{spack_dir}
%fdupes %{buildroot}%{_datarootdir}/spack
%fdupes %{buildroot}%{_localstatedir}/lib/spack
%{?_distconfdir:%fdupes %{buildroot}/%{_distconfdir}/spack}
%else
mkdir -p %{buildroot}%{_infodir}
mkdir -p %{buildroot}%{_mandir}/man1
cd lib/spack/docs/_build
cp man/spack.1.gz %{buildroot}%{_mandir}/man1/
cp -r texinfo/Spack.info.gz %{buildroot}%{_infodir}
[ -d texinfo/Spack-figures ] && cp -r texinfo/Spack-figures %{buildroot}%{_infodir}
%endif

%if %{without doc}
# for sysusers
%pre -f %{name}.pre

%post
if [ -e /etc/os-release ] ;  then
  source /etc/os-release
  if [ "${ID}" = "opensuse-tumbleweed" ] ; then
    export SPACK_NAME="${ID/-/}"
  else
    export SPACK_NAME="${ID/-/_}${VERSION_ID/.*/}"
  fi
  sed -i "s@SUSE_VERSION@$SPACK_NAME@g" %{_sysconfdir}/profile.d/spack.sh
fi
mkdir -p /opt/spack
chgrp spack /opt/spack
chmod 0775 /opt/spack

%triggerin -- %{?spack_trigger_recommended_packages} %{?spack_trigger_packages} %{?spack_trigger_external}
/usr/lib/spack/run-find-external.sh packages

%triggerin -- %{?spack_trigger_recommended_compilers} %{?spack_trigger_compilers}
/usr/lib/spack/run-find-external.sh compilers

%triggerpostun -- %{?spack_trigger_recommended_packages} %{?spack_trigger_packages} %{?spack_trigger_external}
/usr/lib/spack/run-find-external.sh packages

%triggerpostun -- %{?spack_trigger_recommended_compilers} %{?spack_trigger_compilers}
/usr/lib/spack/run-find-external.sh compilers

%files
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md NOTICE README.md README.SUSE
%dir %{_sysconfdir}/spack/
%{_bindir}/*
%if 0%{?suse_version} <= 1500
%dir %{_prefix}/etc
%endif
%{_prefix}/etc/spack
%attr(0775, root, spack) %{_localstatedir}/lib/spack/junit-report
%attr(0775, root, spack) %{spack_dir}/opt
%attr(0775, root, spack) %{_localstatedir}/cache/spack
%attr(0775, root, spack) %{_datarootdir}/spack/modules
%{spack_dir}
%{_localstatedir}/cache/spack
%{_localstatedir}/lib/spack
%{_datarootdir}/spack
%exclude %{_datarootdir}/spack/repos
%config %{_sysconfdir}/profile.d/spack.sh
%ghost %config %{_sysconfdir}/spack/packages.yaml
%config %{_sysconfdir}/profile.d/spack.csh
%dir %{_sysconfdir}/skel/.spack
%config %{_sysconfdir}/skel/.spack/config.yaml
%config %{_sysconfdir}/skel/.spack/modules.yaml
# repos directory is installed in -recipes
%{_sysusersdir}/system-group-%{name}.conf

%files recipes
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md NOTICE README.md
%{_datarootdir}/spack/repos

%files build-dependencies

#%{without doc}
%else

%if 0%{?suse_version} <= 1500
%post info
%install_info --info-dir=%{_infodir} --info-file="%{_infodir}/Spack.info.gz"

%preun info
%install_info_delete --info-dir=%{_infodir} --info-file="%{_infodir}/Spack.info.gz"
%endif

%files man
%{_mandir}/man1/*

%files info
%{_infodir}/*

%endif

%changelog
