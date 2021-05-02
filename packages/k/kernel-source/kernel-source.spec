#
# spec file for package kernel-source
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# icecream 0


%define srcversion 5.12
%define patchversion 5.12.0
%define variant %{nil}
%define vanilla_only 0

%include %_sourcedir/kernel-spec-macros

%define src_install_dir usr/src/linux-%kernelrelease%variant

Name:           kernel-source
Summary:        The Linux Kernel Sources
License:        GPL-2.0
Group:          Development/Sources
Version:        5.12.0
%if 0%{?is_kotd}
Release:        <RELEASE>.gc4830af
%else
Release:        0
%endif
Url:            http://www.kernel.org/
AutoReqProv:    off
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  sed
Requires(post): coreutils sed
Provides:       %name = %version-%source_rel
Provides:       %name-srchash-c4830af6d8ac9e225996ef8da38bf6184be9c882
Provides:       linux
Provides:       multiversion(kernel)
Source0:        http://www.kernel.org/pub/linux/kernel/v5.x/linux-%srcversion.tar.xz
Source2:        source-post.sh
Source3:        kernel-source.rpmlintrc
Source8:        devel-pre.sh
Source9:        devel-post.sh
Source10:       preun.sh
Source11:       postun.sh
Source12:       pre.sh
Source13:       post.sh
Source14:       series.conf
Source16:       guards
Source17:       apply-patches
Source21:       config.conf
Source23:       supported.conf
Source33:       check-for-config-changes
Source35:       group-source-files.pl
Source36:       README.PATCH-POLICY.SUSE
Source37:       README.SUSE
Source38:       README.KSYMS
Source39:       config-options.changes.txt
Source40:       source-timestamp
Source46:       split-modules
Source47:       modversions
Source48:       macros.kernel-source
Source49:       kernel-module-subpackage
Source50:       kabi.pl
Source51:       mkspec
Source52:       kernel-source%variant.changes
Source53:       kernel-source.spec.in
Source54:       kernel-binary.spec.in
Source55:       kernel-syms.spec.in
Source56:       kernel-docs.spec.in
Source57:       kernel-cert-subpackage
Source58:       constraints.in
Source60:       config.sh
Source61:       compute-PATCHVERSION.sh
Source62:       old-flavors
Source63:       arch-symbols
Source64:       package-descriptions
Source65:       kernel-spec-macros
Source67:       log.sh
Source68:       host-memcpy-hack.h
Source69:       try-disable-staging-driver
Source70:       kernel-obs-build.spec.in
Source71:       kernel-obs-qa.spec.in
Source72:       compress-vmlinux.sh
Source73:       dtb.spec.in.in
Source74:       mkspec-dtb
Source75:       release-projects
Source76:       check-module-license
Source77:       klp-symbols
Source78:       modules.fips
Source79:       splitflist
Source80:       mergedep
Source81:       moddep
Source82:       modflist
Source83:       kernel-subpackage-build
Source84:       kernel-subpackage-spec
Source85:       kernel-default-base.spec.txt
Source100:      config.tar.bz2
Source101:      config.addon.tar.bz2
Source102:      patches.arch.tar.bz2
Source103:      patches.drivers.tar.bz2
Source104:      patches.fixes.tar.bz2
Source105:      patches.rpmify.tar.bz2
Source106:      patches.suse.tar.bz2
Source108:      patches.addon.tar.bz2
Source109:      patches.kernel.org.tar.bz2
Source110:      patches.apparmor.tar.bz2
Source111:      patches.rt.tar.bz2
Source113:      patches.kabi.tar.bz2
Source120:      kabi.tar.bz2
Source121:      sysctl.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Prefix:         /usr/src
# Source is only complete with devel files.
Requires:       kernel-devel%variant = %version-%source_rel
# extra packages needed for building a kernel from scratch
Recommends:     bc
Recommends:     bison
Recommends:     flex
Recommends:     libelf-devel
Recommends:     openssl-devel
%obsolete_rebuilds %name

%(chmod +x %_sourcedir/{guards,apply-patches,check-for-config-changes,group-source-files.pl,split-modules,modversions,kabi.pl,mkspec,compute-PATCHVERSION.sh,arch-symbols,log.sh,try-disable-staging-driver,compress-vmlinux.sh,mkspec-dtb,check-module-license,klp-symbols,splitflist,mergedep,moddep,modflist,kernel-subpackage-build})

# Force bzip2 instead of lzma compression to
# 1) allow install on older dist versions, and
# 2) decrease build times (bsc#962356 boo#1175882)
%define _binary_payload w9.bzdio

%define symbols %(set -- $([ -e %_sourcedir/extra-symbols ] && cat %_sourcedir/extra-symbols) ; echo $*)
%define variant_symbols %(case %name in (*-rt) echo "RT" ;; esac)

%define do_vanilla "%variant" == ""

%description
Linux kernel sources with many fixes and improvements.


%source_timestamp
%package -n kernel-devel%variant
%obsolete_rebuilds kernel-devel%variant
Summary:        Development files needed for building kernel modules
Group:          Development/Sources
AutoReqProv:    off
Provides:       kernel-devel%variant = %version-%source_rel
Provides:       multiversion(kernel)
Requires:       kernel-macros
Requires(post): coreutils

%description -n kernel-devel%variant
Kernel-level headers and Makefiles required for development of
external kernel modules.

%source_timestamp

# Note: The kernel-macros package intentionally does not provide
# multiversion(kernel) nor is its name decorated with the variant (-rt)
%package -n kernel-macros
Summary:        RPM macros for building Kernel Module Packages
Group:          Development/Sources
Provides:       kernel-subpackage-macros

%description -n kernel-macros
This package provides the rpm macros and templates for Kernel Module Pakcages

%source_timestamp

%package vanilla
%obsolete_rebuilds %name-vanilla
Summary:        Vanilla Linux kernel sources with minor build fixes
Group:          Development/Sources
AutoReqProv:    off
Provides:       %name-vanilla = %version-%source_rel
Provides:       multiversion(kernel)
Requires:       kernel-macros

%description vanilla
Vanilla Linux kernel sources with minor build fixes.


%source_timestamp

%prep

echo "Symbol(s): %symbols"

# Unpack all sources and patches
%setup -q -c -T -a 100 -a 101 -a 102 -a 103 -a 104 -a 105 -a 106 -a 108 -a 109 -a 110 -a 111 -a 113 -a 120 -a 121

%build
%install
mkdir -p $RPM_BUILD_ROOT/usr/src
pushd $RPM_BUILD_ROOT/usr/src

# Unpack the vanilla kernel sources
tar -xf %{S:0}
find . -type l | while read f; do test -e "$f" || rm -v "$f"; done
if test "%srcversion" != "%kernelrelease%variant"; then
	mv linux-%srcversion linux-%kernelrelease%variant
fi

%if %do_vanilla
%if %vanilla_only
	mv \
%else
	cp -al \
%endif
	linux-%kernelrelease%variant linux-%kernelrelease-vanilla
cd linux-%kernelrelease-vanilla
%_sourcedir/apply-patches --vanilla %_sourcedir/series.conf %my_builddir %symbols
rm -f $(find . -name ".gitignore")
cd ..
%endif

%if ! %vanilla_only
cd linux-%kernelrelease%variant
%_sourcedir/apply-patches %_sourcedir/series.conf %my_builddir %symbols
rm -f $(find . -name ".gitignore")

if [ -f %_sourcedir/localversion ] ; then
    cat %_sourcedir/localversion > localversion
fi
cd ..
%endif

# Hardlink duplicate files automatically (from package fdupes).
%fdupes $RPM_BUILD_ROOT
popd

%if ! %vanilla_only
# Install the documentation and example Kernel Module Package.
DOC=/usr/share/doc/packages/%name-%kernelrelease
mkdir -p %buildroot/$DOC
cp %_sourcedir/README.SUSE %_sourcedir/config-options.changes.txt %buildroot/$DOC
ln -s $DOC/README.SUSE %buildroot/%src_install_dir/

%if "%variant" == ""
install -m 755 -d $RPM_BUILD_ROOT/etc/rpm
install -m 644 %_sourcedir/macros.kernel-source $RPM_BUILD_ROOT/etc/rpm/
install -m 755 -d $RPM_BUILD_ROOT/usr/lib/rpm
install -m 644 %_sourcedir/kernel-{module,cert}-subpackage \
    $RPM_BUILD_ROOT/usr/lib/rpm/
install -m 755 -d $RPM_BUILD_ROOT/usr/lib/rpm/kernel
install -m 755 %_sourcedir/{splitflist,mergedep,moddep,modflist,kernel-subpackage-build} $RPM_BUILD_ROOT/usr/lib/rpm/kernel
install -m 644 %_sourcedir/kernel-subpackage-spec $RPM_BUILD_ROOT/usr/lib/rpm/kernel
install -m 644 -T %_sourcedir/kernel-default-base.spec.txt $RPM_BUILD_ROOT/usr/lib/rpm/kernel/kernel-default-base.spec
%endif

sed -e "s:@KERNELRELEASE@:%kernelrelease:g" \
	-e "s:@SRCVARIANT@:%variant:g" \
	%_sourcedir/source-post.sh > %name-post.sh

pushd "%buildroot"
perl "%_sourcedir/group-source-files.pl" \
	-D "$OLDPWD/devel.files" -N "$OLDPWD/nondevel.files" \
	-L "%src_install_dir"
popd

find %{buildroot}/usr/src/linux* -type f -name '*.[ch]' -perm /0111 -exec chmod -v a-x {} +
# OBS checks don't like /usr/bin/env in script interpreter lines
grep -Elr '^#! */usr/bin/env ' %{buildroot}/usr/src/linux* | while read f; do
    sed -re '1 { s_^#! */usr/bin/env +/_#!/_ ; s_^#! */usr/bin/env +([^/])_#!/usr/bin/\1_ }' -i "$f"
done
# kernel-source and kernel-$flavor-devel are built independently, but the
# shipped sources (/usr/src/linux/) need to be older than generated files
# (/usr/src/linux-obj). We rely on the git commit timestamp to not point into
# the future and be thus lower than the timestamps of files built from the
# source (bnc#669669).
ts="$(head -n1 %_sourcedir/source-timestamp)"
find %buildroot/usr/src/linux* ! -type l | xargs touch -d "$ts"

%post -f %name-post.sh

%post -n kernel-devel%variant -f %name-post.sh

%files -f nondevel.files
%defattr(-, root, root)

%files -n kernel-devel%variant -f devel.files
%defattr(-,root,root)
%ghost /usr/src/linux%variant
%doc /usr/share/doc/packages/*

%if "%variant" == ""
%files -n kernel-macros
%defattr(-,root,root)
/etc/rpm/macros.kernel-source
/usr/lib/rpm/kernel-*-subpackage
%dir /usr/lib/rpm/kernel
/usr/lib/rpm/kernel/*
%endif

%endif

%if %do_vanilla

%files vanilla
%defattr(-, root, root)
/usr/src/linux-%kernelrelease-vanilla
%endif

%changelog
