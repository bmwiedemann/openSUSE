#
# spec file for package linux-glibc-devel
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


Name:           linux-glibc-devel
Version:        6.1
Release:        0
Summary:        Linux headers for userspace development
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://www.kernel.org/
Source:         %{name}-%{version}.tar.xz
Source1:        install_all.sh
BuildRequires:  xz
# rpm-build requires gettext-tools; ignore this, in order to shorten cycles (we have no translations)
#!BuildIgnore:  gettext-tools
# glibc-devel requires linux-kernel-headers, which we are in progress of building
#!BuildIgnore:  linux-kernel-headers
PreReq:         coreutils
Provides:       kernel-headers
Provides:       linux-kernel-headers = %{version}
Obsoletes:      linux-kernel-headers < %{version}

%{lua:
function cross_archs()
  return "aarch64", "arm", "hppa", "i386", "m68k", "mips", "ppc64", "ppc64le", "riscv64", "s390x", "sparc", "sparc64", "x86_64"
end

function kernel_arch(arch)
  local map = {
     ["aarch64"] = "arm64",
     ["armv6hl"] = "arm",
     ["armv7hl"] = "arm",
     ["hppa"] = "parisc",
     ["i386"] = "x86",
     ["i586"] = "x86",
     ["i686"] = "x86",
     ["ppc"] = "powerpc",
     ["ppc64"] = "powerpc",
     ["ppc64le"] = "powerpc",
     ["riscv64"] = "riscv",
     ["s390x"] = "s390",
     ["sparc64"] = "sparc",
     ["x86_64"] = "x86",
  }
  return map[arch] or arch
end

function gcc_target(arch)
  local map = {
    ["arm"] = "arm-suse-linux-gnueabi",
    ["i386"] = "i586-suse-linux",
    ["ppc64"] = "powerpc64-suse-linux",
    ["ppc64le"] = "powerpc64le-suse-linux",
  }
  return map[arch] or arch.."-suse-linux"
end
}

%description
This package provides Linux kernel headers, the kernel API description
required for compilation of almost all programs. This is the userspace
interface; compiling external kernel modules requires
kernel-(flavor)-devel, or kernel-syms to pull in all kernel-*-devel,
packages, instead.

%{lua:
  for i,arch in ipairs({cross_archs()}) do
    print(rpm.expand([[

%package -n cross-]]..arch..[[-linux-glibc-devel
Summary:        Linux headers for ]]..arch..[[ userspace cross development
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description -n cross-]]..arch..[[-linux-glibc-devel
This package provides Linux kernel headers for ]]..arch..[[, the kernel API description
required for compilation of almost all programs.
]]))
  end}

%prep
%setup -q -n linux-glibc-devel-%{version}

%build
for karch in *; do
  cd $karch
  cat > version.h <<\BOGUS
#ifdef __KERNEL__
#error "======================================================="
#error "You should not include %{_includedir}/{linux,asm}/ header"
#error "files directly for the compilation of kernel modules."
#error ""
#error "glibc now uses kernel header files from a well-defined"
#error "working kernel version (as recommended by Linus Torvalds)"
#error "These files are glibc internal and may not match the"
#error "currently running kernel. They should only be"
#error "included via other system header files - user space"
#error "programs should not directly include <linux/*.h> or"
#error "<asm/*.h> as well."
#error ""
#error "Since Linux 2.6, the kernel module build process has been"
#error "updated such that users building modules should not typically"
#error "need to specify additional include directories at all."
#error ""
#error "To build kernel modules, ensure you have the build environment "
#error "available either via the kernel-devel and kernel-<flavor>-devel "
#error "packages or a properly configured kernel source tree."
#error ""
#error "Then, modules can be built using:"
#error "make -C <path> M=$PWD"
#error ""
#error "For the currently running kernel there will be a symbolic "
#error "link pointing to the build environment located at "
#error "/lib/modules/$(uname -r)/build for use as <path>."
#error ""
#error "If you are seeing this message, your environment is "
#error "not configured properly. "
#error ""
#error "Please adjust the Makefile accordingly."
#error "======================================================="
#else
BOGUS
  # Get LINUX_VERSION_CODE and KERNEL_VERSION directly from kernel
  cat usr/include/linux/version.h >> version.h
  cat >> version.h <<\BOGUS
#endif
BOGUS
  cd ..
done

%install
cd %{lua:print(kernel_arch(rpm.expand("%_target_cpu")))}
cp -a usr %{buildroot}/
cp -a version.h %{buildroot}%{_includedir}/linux/
cd ..
%{lua:
  for i,arch in ipairs({cross_archs()}) do
    print(rpm.expand([[
sysroot=%{_prefix}/]]..gcc_target(arch)..[[/sys-root
mkdir -p %{buildroot}${sysroot}/%{_includedir}/linux/
cd ]]..kernel_arch(arch)..[[

cp -a usr %{buildroot}${sysroot}
cp -a version.h %{buildroot}${sysroot}/%{_includedir}/linux/
cd ..
]]))
  end}

%pre
if test -L %{_includedir}/asm; then
  rm -f %{_includedir}/asm
fi

%files
%{_includedir}/*

%{lua:
  for i,arch in ipairs({cross_archs()}) do
    print(rpm.expand([[

%files -n cross-]]..arch..[[-linux-glibc-devel
%{_prefix}/]]..gcc_target(arch).."\n"))
  end}

%changelog
