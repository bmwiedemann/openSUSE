#
# spec file for package spack
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
%define spack_trigger_recommended autoconf bash bison bzip2 libzip-devel cmake-full ccache cpio diffutils findutils flex gcc gcc-c++ gcc-fortran git-lfs make m4 ncurses-devel libtool openssl-devel perl-base pkgconf pkg-config python3-base tar info xz xz-devel
# packages recognized by spack, but not recommended
%define spack_trigger_packages ghostscript go fish fzf hugo java-11-openjdk-devel java-14-openjdk-devel java-15-openjdk-devel java-16-openjdk-devel java-1_8_0-openjdk-devel ruby openmpi1-devel openmpi2-devel openmpi3-devel openmpi4-devel openmpi1-gnu-hpc-devel openmpi2-gnu-hpc-devel openmpi3-gnu-hpc-devel openmpi4-gnu-hpc-devel mvapich2-devel mpich-devel gcc7 gcc8 gcc9 gcc10 gcc11 gcc7-c++ gcc8-c++ gcc9-c++ gcc10-c++ gcc11-c++ gcc7-fortran gcc8-fortran gcc9-fortran gcc10-fortran gcc11-fortran
# non oss packages
%define spack_trigger_external cuda-nvcc
Name:           spack
Version:        0.19.0
Release:        0
Summary:        Package manager for HPC systems
License:        Apache-2.0 AND MIT AND Python-2.0 AND BSD-3-Clause
URL:            https://spack.io
Source0:        https://github.com/spack/spack/archive/v%{version}.tar.gz#/spack-%{version}.tar.gz
Source1:        README.SUSE
Source2:        spack-rpmlintrc
Source3:        run-find-external.sh.in
Source4:        https://en.opensuse.org/index.php?title=Spack&action=raw&ref=157522#/README-oo-wiki
# Source5 is from https://docs.python.org/3/objects.inv, but has permanent changes so using a static version
Source5:        objects.inv
Patch2:         Adapt-shell-scripts-that-set-up-the-environment-for-different-shells.patch
Patch4:         added-target-and-os-calls-to-output-of-spack-spec-co.patch
Patch5:         Make-spack-paths-compliant-to-distro-installation.patch
Patch6:         Fix-error-during-documentation-build-due-to-recursive-module-inclusion.patch
Patch7:         Fix-Spinx-configuration-to-avoid-throwing-errors.patch
Patch8:         Set-modules-default-to-lmod.patch
Patch9:         Add-support-for-container-building-using-a-SLE-base-container.patch
%if %{without doc}
BuildRequires:  fdupes
BuildRequires:  lua-lmod
BuildRequires:  polkit
BuildRequires:  python3-urllib3
BuildRequires:  sudo
BuildRequires:  sysuser-tools
Requires:       %{name}-recipes = %{version}
Requires:       bzip2
Requires:       coreutils
Requires:       curl
Requires:       gcc-c++
Requires:       gcc-fortran
Requires:       gpg2
Requires:       libbz2-devel
Requires:       lua-lmod
Requires:       make
Requires:       patch
Requires:       polkit
Requires:       python3-clingo
Requires:       sudo
Requires:       tar
Requires:       xz
Recommends:     %spack_trigger_recommended
%else
BuildRequires:  git
BuildRequires:  makeinfo
# Hardcode this - there is no python2 version of this around any more.
BuildRequires:  python3-Sphinx >= 3.4
BuildRequires:  python3-sphinxcontrib-programoutput
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
%else
cp %{S:5} lib/spack/docs/
%endif
grep -rl '#! /usr/bin/env bash' . | xargs -i@ sed -i 's|#! /usr/bin/env bash|#!/usr/bin/bash|g' @
grep -rl '#!/bin/env sh' . | xargs -i@ sed -i 's|#!/bin/env sh|#!/usr/bin/sh|g' @
grep -rl '#!/usr/bin/env bash' . | xargs -i@ sed -i 's|#!/usr/bin/env bash|#!/usr/bin/bash|g' @
grep -rl "spack/" . | xargs -i@ sed -i \
  -e 's|$spack/opt|/opt|g' \
  -e 's|$spack/var|/var/lib|g'\
  -e 's|$spack/share/spack/lmod|/opt/spack/modules|g'\
  -e 's|$spack/share/spack/modules|/opt/spack/modules|g'\
  @

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
    graph|spec) exit 0 ;;
    *) exec /usr/bin/spack ${args} ;;
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
source /usr/share/spack/setup-env.sh
make man info || { cat /tmp/sphinx-err-*.log; exit 1; } #text dirhtml
rm -rf $tmpdir
gzip _build/texinfo/Spack.info _build/man/spack.1
%endif

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
rm -rf var/spack/repos/builtin.mock  var/spack/gpg.mock var/spack/mock_configs
rm -rf lib/spack/external/ruamel/yaml/.ruamel
find . -type f -name .gitignore -delete
find . -type f -name .nojekyll -delete
find . -type f -name .gitlab-ci.yml -delete

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
## Remove non linux stuff
rm -f bin/spack.bat bin/spack_cmd.bat bin/spack_pwsh.ps1
## Fix shebangs
#sed -i 's@#!/bin/env sh@#!/bin/bash@' var/spack/repos/builtin/packages/beast-tracer/tracer
#sed -i 's@#! /usr/bin/env bash@ #!/bin/bash@' share/spack/docker/entrypoint.bash
#sed -i 's@#!/usr/bin/env bash@#!/bin/bash@' share/spack/docker/package-index/split.sh

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
cp -r bin/sbang %{buildroot}/%{_bindir}
cp -r bin/spack* %{buildroot}%{_bindir}/
cp etc/spack/defaults/config.yaml %{buildroot}%{_sysconfdir}/skel/.spack/
install -m 755 %{S:3} %{buildroot}/%{spack_dir}/run-find-external.sh
sed -i -e 's#@@_sysconfdir@@#%{_sysconfdir}#' %{buildroot}/%{spack_dir}/run-find-external.sh

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

# compile python files for python3
# %%{buildroot}%%{spack_dir}/spack
%py3_compile .

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
if [ "\${ID}" = "opensuse-tumbleweed" ] ; then
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
set SPACK_ROOT="%{spack_dir}"
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
rm -r %{buildroot}%{_localstatedir}/lib/spack/repos/builtin/packages/patchelf/test/

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

%pre -f %{name}.pre

%post
# Replace /etc/spack/compilers.yaml
export GCC_VERSION=`gcc -dumpversion`
export GCC_FULL_VERSION=`gcc -dumpfullversion`

sed -i "s@GCC_FULL_VERSION@$GCC_FULL_VERSION@" %{spack_dir}/etc/spack/compilers.yaml
#sed -i "s@GCC_FULL_VERSION@$GCC_FULL_VERSION@" %{spack_dir}/etc/spack/modules.yaml
sed -i "s@GCC_VERSION@$GCC_VERSION@" %{spack_dir}/etc/spack/compilers.yaml
if [ -e /etc/os-release ] ;  then
  source /etc/os-release
  if [ "${ID}" = "opensuse-tumbleweed" ] ; then
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
mkdir -p /opt/spack
chgrp spack /opt/spack
chmod 0775 /opt/spack

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
%config %{_sysconfdir}/skel/.spack/modules.yaml
# repos directory is installed in -recipes
%{_sysusersdir}/system-group-%{name}.conf
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
