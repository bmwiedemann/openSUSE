#
# spec file for package acpica
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


%define src_dir acpica-unix-%{version}
%define kver %(rpm -q --qf '%%{VERSION}' kernel-source)
%define dmp_ver %{kver}
Name:           acpica
Version:        20221020
Release:        0
Summary:        A set of tools to display and debug BIOS ACPI tables
License:        GPL-2.0-only
URL:            https://acpica.org
Source:         https://acpica.org/sites/acpica/files/%{src_dir}.tar_0.gz
Source1:        ec_access.c
Source2:        acpi_genl.tar.bz2
Source3:        acpi_validate
# https://xf.iksaif.net/dev/wmidump.html
Source4:        wmidump-20211011.tar.xz
Patch1:         acpica-no-compiletime.patch
Patch2:         wmidump_add_she_bang.patch
Patch3:         do_not_use_build_date_and_time.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  glibc-devel
BuildRequires:  kernel-source >= 2.6.31
BuildRequires:  patch
Provides:       iasl

%description
The included tools share the same code as it is used in the ACPI
implementation of the kernel. The code of the acpica project is exactly
the same as the ACPI parser and interpreter code of the kernel and the
code gets synced regularly from the acpica project into the kernel.
E.g. if you identify bugs in the kernel's ACPI implementation it might
be easier to debug them in userspace if possible. If the bug is part of
the acpica code, it has to be submitted to the acpica project to get
merged into the mainline kernel sources.

iasl compiles ASL (ACPI Source Language) into AML (ACPI Machine
Language). This AML is suitable for inclusion as a DSDT in system
firmware. It also can disassemble AML, for debugging purposes.

%prep
%setup -q -n %{src_dir} -a 2 -a 4
%autopatch -p1
mkdir acpidump-%{dmp_ver}
cd acpidump-%{dmp_ver}
# acpitools (acpidump) from kernel sources:
# copy necessary files from kernel-source since we need to modify them
(cd %{_prefix}/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile drivers/acpi lib) | tar -xf -

%build
%global optflags %{optflags} -fcommon
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
cc %{SOURCE1} %{optflags} -o ec_access
%make_build -C acpi_genl CFLAGS="%{optflags}"
%make_build -C wmidump CFLAGS="%{optflags}"
%make_build OPT_CFLAGS="%{optflags} -fcommon"  HOST="_LINUX"
cd acpidump-%{dmp_ver}/tools/power/acpi
if [ -f tools/acpidump/Makefile ]; then # 4.3+
	cd tools/acpidump/
fi
%make_build EXTRA_CFLAGS="%{optflags} -fno-strict-aliasing" prefix=%{_prefix} all

%install
install -Dm 755 %{SOURCE3} %{buildroot}%{_bindir}/acpi_validate
install -Dm 755 ec_access %{buildroot}%{_sbindir}/ec_access

install -Dm 755 wmidump/wmidump %{buildroot}%{_bindir}/wmidump
install -Dm 755 wmidump/wmixtract.py %{buildroot}%{_bindir}/wmixtract
install -Dm 644 wmidump/README.md %{buildroot}/%{_docdir}/%{name}/README_wmidump.md

install -Dm 755 acpi_genl/acpi_genl %{buildroot}%{_sbindir}/acpi_genl
install -Dm 644 acpi_genl/README %{buildroot}/%{_docdir}/%{name}/README_acpi_genl

%make_install
# Latest acpidump is coming from kernel and not from acpica sources now.
rm -rf %{buildroot}%{_bindir}/acpidump
cd acpidump-%{dmp_ver}/tools/power/acpi
if [ -f tools/acpidump/Makefile ]; then # 4.3+
	cd tools/acpidump/
fi
export WERROR=0
make V=1 EXTRA_CFLAGS="%{optflags}" mandir=%{_mandir} prefix=%{_prefix} DESTDIR=%{buildroot} install install-man

%files
%doc changes.txt
%doc %{_docdir}/%{name}
%{_bindir}/iasl
%{_bindir}/acpiexec
%{_bindir}/acpixtract
%{_bindir}/acpisrc
%{_bindir}/wmidump
%{_bindir}/wmixtract
%{_bindir}/acpibin
%{_bindir}/acpihelp
%{_bindir}/acpi_validate
%{_bindir}/acpiexamples
%{_sbindir}/acpidump
%{_sbindir}/acpi_genl
%{_sbindir}/ec_access
%{_mandir}/man8/acpidump.8%{?ext_man}

%changelog
