#
# spec file for package spack
#
# Copyright (c) 2021 SUSE LLC
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

%if %{with doc} && (0%{?sle_version} > 0) && (150200 >= 0%{?sle_version})
ExclusiveArch:  do_not_build
%endif

%define spack_dir  %_prefix/lib/spack/
%define spack_group spack
# These packages are found and can be used by spack, /etc/spack/packages-yaml
# needs to be updated when one of these packages is updated or uninstalled.
# Distinguish between packages we recommend and packages which
%define spack_trigger_recommended autoconf bash bison bzip2 cmake-full ccache cpio diffutils findutils flex gcc gcc-c++ gcc-fortran git-lfs make m4 ncurses-devel libtool openssl perl-base pkgconf pkgconf-pkg-config python3-basetar info xz
# packages recognized by spack, but not recommended
%define spack_trigger_packages ghostscript go fish fzf hugo java-11-openjdk-devel java-14-openjdk-devel java-15-openjdk-devel java-16-openjdk-devel java-1_8_0-openjdk-devel ruby openmpi1-devel openmpi2-devel openmpi3-devel openmpi4-devel openmpi1-gnu-hpc-devel openmpi2-gnu-hpc-devel openmpi3-gnu-hpc-devel openmpi4-gnu-hpc-devel mvapich2-devel mpich-devel gcc7 gcc8 gcc9 gcc10 gcc11 gcc7-c++ gcc8-c++ gcc9-c++ gcc10-c++ gcc11-c++ gcc7-fortran gcc8-fortran gcc9-fortran gcc10-fortran gcc11-fortran
# non oss packages
%define spack_trigger_external cuda-nvcc
Name:           spack
Version:        0.16.1
Release:        0
Summary:        Package manager for HPC systems
License:        Apache-2.0 AND MIT AND Python-2.0 AND BSD-3-Clause
URL:            https://spack.io
Source0:        https://github.com/spack/spack/archive/v%{version}.tar.gz#/spack-%{version}.tar.gz
Source1:        README.SUSE
Source2:        spack-rpmlintrc
Source3:        run-find-external.sh
Patch0:         Make-spack-paths-compliant-to-distro-installation.patch
Patch1:         fix-tumbleweed-naming.patch
Patch2:         Adapt-shell-scripts-that-set-up-the-environment-for-different-shells.patch
Patch3:         added-dockerfile-for-opensuse-leap-15.patch
Patch4:         added-target-and-os-calls-to-output-of-spack-spec-co.patch
Patch5:         Fix-documentation-so-that-parser-doesn-t-stumble.patch
Patch6:         Fix-error-during-documentation-build-due-to-recursive-module-inclusion.patch
Patch7:         basic-exclude-pattern-for-external-find.patch
# upstream patch removes also problemtatic binaries
#Patch4:         spack-test-15702.patch
%if %{without doc}
BuildRequires:  fdupes
BuildRequires:  lua-lmod
BuildRequires:  polkit
BuildRequires:  python-base
BuildRequires:  python3-urllib3
BuildRequires:  sudo
Requires:       %{name}-recipes = %{version}
Requires:       bzip2
Requires:       curl
Requires:       gcc-c++
Requires:       gcc-fortran
Requires:       gpg2
Requires:       libbz2-devel
Requires:       lua-lmod
Requires:       patch
Requires:       polkit
Requires:       spack-recipes
Requires:       sudo
Requires:       xz
Recommends:     %spack_trigger_recommended
Recommends:     spack-recipes = %version
%else
BuildRequires:  %{python_module Sphinx >= 1.8}
BuildRequires:  %{python_module sphinxcontrib-programoutput}
BuildRequires:  git
BuildRequires:  makeinfo
BuildRequires:  spack
# html
BuildRequires:  graphviz
# info
BuildRequires:  graphviz-gnome
## pdf
# BuildRequires:  python3-Sphinx-latex
Requires:       spack
%endif
BuildArch:      noarch
%if  0%{?sle_version} <= 120500 && !0%{?is_opensuse}
%define __python3 python3
%endif

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
Requires:       %{name} >= %version

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

%description info
Spack is a configurable Python-based HPC package manager, automating
the installation and fine-tuning of simulations and libraries.
It operates on a wide variety of HPC platforms and enables users
to build many code configurations. Software installed by Spack
runs correctly regardless of environment, and file management
is streamlined. Spack can install many variants of the same build
using different compilers, options, and MPI implementations.

This package contains the info page.

%prep
%setup -q
%autopatch -p1
%if %{without doc}

# set SPACK_ROOT
for i in share/spack/setup-env.*; do
    sed -i -e "s;@@_prefix@@;%_prefix;g" $i
done
%endif

%build
# Nothing to build
%if %{with doc}
cd lib/spack/docs
# Causes issues building texinfo as a suitable image cannot be found
grep -rl ":target:" | xargs sed  -i -e "/:target:/s/^/#/" -e "/figure::/s/^/#/"
# Fix path to var - we install this to the 'real' /var
grep -rl "\$SPACK_ROOT/var" | xargs sed -i -e "s@\(.*\)\$SPACK_ROOT/var\(/spack.*\)@\1/var/lib\2@g"
# spack cannot run without knowing at least the compiler, so we inject
# a dummy one
mkdir -p ${HOME}/.spack/linux/
cat >  ${HOME}/.spack/linux/compilers.yaml <<EOF
compilers:
- compiler:
    spec: gcc@7.5.0
    paths:
      cc: /usr/bin/gcc
      cxx: /usr/bin/g++
      f77: /usr/bin/gfortran
      fc: /usr/bin/gfortran
    flags: {}
    operating_system: SUSE
    target: x86_64
    modules: []
    environment:
      unset: []
    extra_rpaths: []
EOF
make man info #text dirhtml
gzip _build/texinfo/Spack.info _build/man/spack.1
%endif

%install

%if %{without doc}
cp %{S:1} .
# Fix some rpmlint warnings
## Remove files not required to run spack
rm -rf lib/spack/spack/test
rm -rf share/spack/qa
rm -rf share/spack/logo
rm -rf var/spack/repos/builtin.mock  var/spack/gpg.mock var/spack/mock_configs
rm -rf lib/spack/external/ruamel/yaml/.ruamel
find . -type f -name .gitignore -delete
find . -type f -name .nojekyll -delete
# Fix _spack_root link
rm -f lib/spack/docs/_spack_root
ln -sf ../.. lib/spack/docs/_spack_root
# Do not ship Docker and container building for now - needs fixing
rm -rf share/spack/{templates/container}
rm -rf share/spack/docker/{centos,ubuntu}*.dockerfile
# Do not ship AWS specifics
rm -f share/spack/setup-tutorial-env.sh
# Fix rpmlint warnings
## No need for the standalone scripts
rm -f lib/spack/external/macholib/macho_*.py
## Fix shebangs
sed -i 's@#!/bin/env sh@#!/bin/bash@' var/spack/repos/builtin/packages/beast-tracer/tracer
sed -i 's@#! /usr/bin/env bash@ #!/bin/bash@' share/spack/docker/entrypoint.bash
sed -i 's@#!/usr/bin/env bash@#!/bin/bash@' share/spack/docker/package-index/split.sh

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
cp -r lib/spack/{env,external,llnl,spack} %{buildroot}%{spack_dir}
cp -r share/spack/* %{buildroot}%{_datarootdir}/spack
cp -r var/spack/* %{buildroot}%{_localstatedir}/lib/spack
cp -r bin/sbang %{buildroot}/%{_bindir}
cp -r bin/spack* %{buildroot}%{_bindir}/
cp etc/spack/defaults/config.yaml %{buildroot}%{_sysconfdir}/skel/.spack/
install -m 755 %{S:3} %{buildroot}/%{spack_dir}/run-find-external.sh

# Fix more paths
sed -i 's@\(\sroot:\) $spack/opt/spack@\1 ~/spack/packages@' %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml
sed -i 's@\(\ssource_cache:\).*@\1 /var/tmp/$user/spack-cache@' %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml
sed -i 's@\(\stcl:\).*@\1 ~/spack/modules@' %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml
sed -i 's@\(\slmod:\).*@\1 ~/spack/lmod@' %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml
cat >>  %{buildroot}%{_sysconfdir}/skel/.spack/config.yaml <<EOF
# Timeout in seconds used for downloading sources etc. This only applies
# to the connection phase and can be increased for slow connections or
# servers. 0 means no timeout.
  binary_index_root: ~/.spack/indices
EOF

# compile python files for python3
# %%{buildroot}%%{spack_dir}/spack
%py_compile .

# make shell scripts executeable
find %{buildroot}%{_localstatedir}/lib/spack/ -type f -name \*.sh  -exec chmod 755 {} \;

# Create /etc/spack/compilers.yaml
mkdir -p %{buildroot}%{spack_dir}/etc/spack/
cat >  %{buildroot}%{spack_dir}/etc/spack/compilers.yaml <<EOF
compilers:
- compiler:
    spec: gcc@GCC_FULL_VERSION
    paths:
      cc: /usr/bin/gcc-GCC_VERSION
      cxx: /usr/bin/g++-GCC_VERSION
      f77: /usr/bin/gfortran-GCC_VERSION
      fc: /usr/bin/gfortran-GCC_VERSION
    flags: {}
    operating_system: SUSE_VERSION
    target: HOSTTYPE
    modules: []
    environment:
      unset: []
    extra_rpaths: []
EOF

# Create /etc/profile.d/spack.sh
# This file properly sets MODULEPATH so lua-lmod can find the modules created by spack
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
cat > %{buildroot}/%{_sysconfdir}/profile.d/spack.sh <<EOF
source /etc/os-release
if [ "\${ID}" == "opensuse-tumbleweed" ] ; then
  SPACK_NAME="\${ID/-/}"
else
  SPACK_NAME="\${ID/-/_}\${VERSION_ID/.*/}"
fi
export SPACK_ROOT=%{spack_dir}
export MODULEPATH=~/spack/modules/linux-\${SPACK_NAME}-\${CPU}:%{_prefix}/share/spack/modules/linux-\${SPACK_NAME}-\${CPU}:\${MODULEPATH}
# copy local configuration, if its not there
if [ ! -e ~/.spack/config.yaml ] ; then
  # test if user is in spack group by touching database
  if ! touch %{spack_dir}/.spack-db &> /dev/null ; then
    test -e ~/.spack || mkdir -p ~/.spack
    [ -e ~/.spack/config.yaml ] || \
     cp -r %{_sysconfdir}/skel/.spack/config.yaml ~/.spack/
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
set SPACK_ROOT="%{spack_dir}"
set MODULEPATH="~/spack/modules/linux-\${SPACK_NAME}-\${CPU}:%{_prefix}/share/spack/modules/linux-\${SPACK_NAME}-\${CPU}:\${MODULEPATH}"
if ( ! -e ~/.spack/config.yaml )  then
  # test if user is in spack group by touching database
  touch %{spack_dir}/.spack-db  >& /dev/null
  if ( \$? == 1  ) then
    test -e ~/.spack || mkdir -p ~/.spack
    test -e ~/.spack/config.yaml  || \
     cp -r %{_sysconfdir}/skel/.spack/config.yaml ~/.spack/
  endif
endif

EOF
# Create modules.yaml file, so that hierarchy module files are created
cat >  %{buildroot}%{spack_dir}/etc/spack/modules.yaml <<EOF
modules:
  enable:
    - lmod
  lmod:
    core_compilers:
      - 'gcc@GCC_FULL_VERSION'
    projections:
      all: '{compiler.name}-{compiler.version}/{name}/{version}'
      ^mpi: '{compiler.name}-{compiler.version}/{^mpi.name}-{^mpi.version}/{name}/{version}'
EOF
mkdir -p %{buildroot}%{_sysconfdir}/spack

# Fix link to not point into buildroot
rm -f %{buildroot}%{_localstatedir}/lib/spack/cache
ln -sf %{_localstatedir}/cache/spack %{buildroot}%{_localstatedir}/lib/spack/cache
# Remove problematic binaries which are removed upstream with
# 0889be20e0d9dcdf4346cdeaa0647285187375f3
rm -r %{buildroot}%{_localstatedir}/lib/spack/repos/builtin/packages/patchelf/test/
%fdupes %{buildroot}%{spack_dir}
%fdupes %{buildroot}%{_datarootdir}/spack
%fdupes %{buildroot}%{_localstatedir}/lib/spack
%else
mkdir -p %{buildroot}%{_infodir}
mkdir -p %{buildroot}%{_mandir}/man1
cd lib/spack/docs/_build
cp man/spack.1.gz %{buildroot}%{_mandir}/man1/
cp -r texinfo/Spack.info.gz %{buildroot}%{_infodir}
[ -d texinfo/Spack-figures ] && cp -r texinfo/Spack-figures %{buildroot}%{_infodir}
%endif

%pre
getent group %spack_group >/dev/null || groupadd -r %spack_group

%post
# Replace /etc/spack/compilers.yaml
export GCC_VERSION=`gcc -dumpversion`
export GCC_FULL_VERSION=`gcc -dumpfullversion`

sed -i "s@GCC_FULL_VERSION@$GCC_FULL_VERSION@" %{spack_dir}/etc/spack/compilers.yaml
sed -i "s@GCC_FULL_VERSION@$GCC_FULL_VERSION@" %{spack_dir}/etc/spack/modules.yaml
sed -i "s@GCC_VERSION@$GCC_VERSION@" %{spack_dir}/etc/spack/compilers.yaml
if [ -e /etc/os-release ] ;  then
  source /etc/os-release
  if [ "${ID}" == "opensuse-tumbleweed" ] ; then
    export SPACK_NAME="${ID/-/}"
  else
    export SPACK_NAME="${ID/-/_}${VERSION_ID/.*/}"
  fi
  sed -i "s@SUSE_VERSION@$SPACK_NAME@" %{spack_dir}/etc/spack/compilers.yaml
  sed -i "s@SUSE_VERSION@$SPACK_NAME@g" /etc/profile.d/spack.sh
fi
sed -i "s@HOSTTYPE@$HOSTTYPE@" %{spack_dir}/etc/spack/compilers.yaml
# find installed programms
/usr/lib/spack/run-find-external.sh

%triggerin -- %{?spack_trigger_recommended} %{?spack_trigger_packages} %{?spack_trigger_external}
/usr/lib/spack/run-find-external.sh

%triggerpostun -- %{?spack_trigger_recommended} %{?spack_trigger_packages} %{?spack_trigger_external}
/usr/lib/spack/run-find-external.sh

%if %{without doc}
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
%config %{_sysconfdir}/profile.d/spack.sh
%ghost %config %{_sysconfdir}/spack/packages.yaml
%config %{_sysconfdir}/profile.d/spack.csh
%dir %{_sysconfdir}/skel/.spack
%config %{_sysconfdir}/skel/.spack/config.yaml
# repos directory is installed in -recipes
%exclude %{_localstatedir}/lib/spack/repos

%files recipes
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md NOTICE README.md
%{_localstatedir}/lib/spack/repos

%else

%post info
%install_info --info-dir=%{_infodir} --info-file="%{_infodir}/Spack.info.gz"

%preun info
%install_info_delete --info-dir=%{_infodir} --info-file="%{_infodir}/Spack.info.gz"

%files man
%{_mandir}/man1/*

%files info
%{_infodir}/*

%endif

%changelog
