#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define pname newlib
%else
%define cross_arch %{flavor}
%define pname cross-%{cross_arch}-newlib-devel
%endif
%if "%{flavor}" == "riscv64"
%define gcc_cross_arch %{cross_arch}-elf
%define target %{cross_arch}-elf
%else
%define gcc_cross_arch %{cross_arch}
%define target %{cross_arch}
%endif
%if "%{cross_arch}" == "epiphany" || "%{cross_arch}" == "riscv32" || "%{cross_arch}" == "rl78" || "%{cross_arch}" == "rx"
%define target %{cross_arch}-elf
%endif
%if "%{cross_arch}" == "arm-none"
%define target %{cross_arch}-eabi
%endif
%if "%{cross_arch}" == "spu"
%define sysroot %{_prefix}/spu
%else
%define sysroot %{_prefix}/%{target}/sys-root
%endif
# In the staging/ring projects, we don't want to build the unneeded packages
%bcond_with ringdisabled
Name:           %{pname}
Version:        4.3.0.20230120
Release:        0
Summary:        C library intended for use on embedded systems
License:        BSD-3-Clause AND MIT AND LGPL-2.0-or-later AND ISC
Group:          Development/Libraries/Cross
URL:            https://sourceware.org/newlib/
Source0:        ftp://sourceware.org/pub/newlib/newlib-%{version}.tar.gz
Patch1:         epiphany-fixes.diff
%if "%{flavor}" == ""
BuildArch:      noarch
%else
BuildRequires:  cross-%{gcc_cross_arch}-gcc%{gcc_version}-bootstrap
BuildRequires:  fdupes
BuildRequires:  makeinfo
%if "%{cross_arch}" != "arm-none" && "%{cross_arch}" != "arm" && %{with ringdisabled}
ExclusiveArch:  do-not-build
%endif
%endif

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products.

%prep
%setup -q -n newlib-%{version}
%patch1 -p1

%build
%if "%{flavor}" != ""
for variant in nano regular; do
    mkdir build-${variant}-dir
    pushd build-${variant}-dir
    # On %%ix86 hosts newlib is documented to be buildable as shared library via --with-newlib,
    # but it fails to build for us and we don't need a host library at the moment.
    export CFLAGS_FOR_TARGET="-O2 -g -ffunction-sections -fdata-sections"
    FEATURES="--disable-nls"
    if [[ "${variant}" == "nano" ]]; then
	export CFLAGS_FOR_TARGET="-Os -g"
	FEATURES="${FEATURES} --enable-newlib-nano-malloc --enable-lite-exit --enable-newlib-nano-formatted-io --disable-newlib-supplied-syscalls"
    fi
    ../configure \
	--prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
	--target=%{target} \
	--with-build-sysroot=%{sysroot} \
	$FEATURES \
%ifarch %{ix86}
%if 0
	--with-newlib \
%endif
%endif
	CFLAGS="%{optflags}" \
	%{nil}

    %make_build
    popd
done
%endif

%install
%if "%{flavor}" != ""
# All binaries built are for the target architecture - don't damage them.
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %{nil}
: >debugfiles.list
: >debugsourcefiles.list
: >debugsources.list

for variant in nano regular; do
    pushd build-${variant}-dir
    if [[ "${variant}" == "regular" ]]; then
        %make_install
    else
        %make_install DESTDIR=/tmp/newlib-nano
	multilibs=$(%{target}-gcc --print-multi-lib)
	for multilib in ${multilibs}; do
	    multilib="${multilib%%;*}"
	    for l in libc libg librdimon libstdc++ libsupc++; do
		test -f /tmp/newlib-nano/%{_prefix}/%{target}/lib/${multilib}/${l}.a || continue
		install -m 0644 -D /tmp/newlib-nano/%{_prefix}/%{target}/lib/${multilib}/${l}.a \
		                        %{buildroot}%{_prefix}/%{target}/lib/${multilib}/${l}_nano.a
	    done
	done
	install -m 0644 -D -t %{buildroot}%{_prefix}/%{target}/include/newlib-nano/ /tmp/newlib-nano/%{_prefix}/%{target}/include/newlib.h
    fi
    popd
done

rm %{buildroot}%{_infodir}/porting.info

%fdupes %{buildroot}
%endif

%files
%if "%{flavor}" == ""
%license COPYING.NEWLIB COPYING.LIBGLOSS COPYING COPYING.LIB COPYING3 COPYING3.LIB
%doc newlib/README newlib/NEWS
%else
%{_prefix}/%{target}/
%endif

%changelog
