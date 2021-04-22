#
# spec file for package compat-usrmerge
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


%define nvr %{name}-%{version}-%{release}

Name:           compat-usrmerge
Version:        84.87
Release:        0
Summary:        UsrMerge related scripts
License:        MIT
URL:            https://en.opensuse.org/openSUSE:Usr_merge
Source0:        usrmerge.lua
# ./usrmergefiles.py --files https://download.opensuse.org/tumbleweed/repo/oss
Source1:        usrmerge_files.lua
Source2:        usrmergecheck.c
Source3:        convertfs
Source4:        xmv.c
Source5:        usrmerge.attr
# ./usrmergefiles.py --requires https://download.opensuse.org/tumbleweed/repo/oss
Source6:        usrmerge_binsbindeps.lua
Source7:        usrmergefiles.py
BuildRequires:  gcc
BuildRequires:  pkgconfig(rpm)

%description
Scripts and data files related to UsrMerge
(https://en.opensuse.org/openSUSE:Usr_merge). Normally not needd.

%package tools
Summary:        UsrMerge tools
# have to turn requires off this off to avoid pulling in stuff
# before filessytem.
# xmv has very minimal glibc requirements and could probably be
# reduced further. The script runs only in the upgrade case,
# assuming that the tools work on the target system anyway.
AutoReq:        0

%description tools
Tools related to UsrMerge to check the state of the system and to
convert an existing system to UsrMerge.

%package build
Summary:        UsrMerge build tools
Requires:       lua

%description build
Build tools related to UsrMerge. This is required for rpmbuild to
generate proper provides tags for packages that used to have
binaries in /(s)bin.

%prep
%setup -qcT

%build
gcc -Wall %optflags -o usrmergecheck %{SOURCE2} `pkg-config --libs rpm`
gcc -Wall %optflags -o xmv %{SOURCE4}

%install
install -D -m755 usrmergecheck %{buildroot}%{_bindir}/usrmergecheck
mkdir -p %{buildroot}%{_rpmconfigdir}/lua
install -m644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/lua
install -m644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/lua
install -D -m755 %{SOURCE3} %{buildroot}%{_libexecdir}/convertfs
install -m755 xmv %{buildroot}%{_libexecdir}/xmv
install -D -m755 %{SOURCE5} %{buildroot}%{_fileattrsdir}/usrmerge.attr
install -m644 %{SOURCE6} %{buildroot}%{_rpmconfigdir}/lua
###
mkdir -p %{buildroot}/lib
mkdir -p %{buildroot}/%{_lib}
while read file; do
	echo "usrmerge_files[\"$file\"] = 1" >> %{buildroot}%{_rpmconfigdir}/lua/usrmerge_files.lua
done <<EOF
/%{_lib}/libc-`rpm -q --qf "%%{version}" glibc`.so
/%{_lib}/libc.so.6
%ifarch %arm
%ifarch armv6hl armv7hl
/%{_lib}/ld-linux-armhf.so.3
/%{_lib}/ld-linux.so.3
%else
/%{_lib}/ld-linux.so.3
%endif
%endif
%ifarch ia64
/%{_lib}/ld-linux-ia64.so.2
%endif
%ifarch ppc s390 mips hppa m68k
/%{_lib}/ld.so.1
%endif
%ifarch ppc64
/%{_lib}/ld64.so.1
%endif
%ifarch ppc64le
/%{_lib}/ld64.so.2
%endif
%ifarch s390x
/lib/ld64.so.1
/%{_lib}/ld64.so.1
%endif
%ifarch x86_64
/%{_lib}/ld-linux-x86-64.so.2
%endif
%ifarch %ix86 %sparc
/%{_lib}/ld-linux.so.2
%endif
%ifarch aarch64
/lib/ld-linux-aarch64.so.1
/%{_lib}/ld-linux-aarch64.so.1
%endif
%ifarch riscv64
/lib/ld-linux-riscv64-lp64d.so.1
/%{_lib}/ld-linux-riscv64-lp64d.so.1
%endif
EOF
#
%if 0
mkdir -p %{buildroot}/{sbin,bin,%{_lib}}
while read file; do
	[ -n "$file" ] || continue
	ln -s ../usr$file %{buildroot}$file
	echo "%ghost %config(noreplace) $file"
done > files.list << EOF
%{lua:
package.path = package.path .. string.format(";%s/?.lua", rpm.expand("%{_sourcedir}"))
require("usrmerge_files")
for rp in pairs(usrmerge_files) do
print(rp.."\n")
end
}
EOF
%endif

%if 0%{?usrmerge_filetriggers}

%filetriggerin  -p <lua> -- %{_sbindir} %{_bindir} %{_libdir}
require("usrmerge")
if posix.getenv("VERBOSE_FILETRIGGERS") then
    usrmerge.debug = "%{nvr}(in)"
end
file = rpm.next_file()
while file do
    usrmerge.add(file)
    file = rpm.next_file()
end
io.flush()

%filetriggerpostun  -p <lua> -- %{_sbindir} %{_bindir} %{_libdir}
-- the module is already gone if we get called for ourselves
if pcall(require, 'usrmerge') then
    if posix.getenv("VERBOSE_FILETRIGGERS") then
        usrmerge.debug = "%{nvr}(postun)"
    end
    file = rpm.next_file()
    while file do
        usrmerge.remove(file)
        file = rpm.next_file()
    end
    io.flush()
end

%filetriggerpostun  -p <lua> -- /sbin /bin /%{_lib}
-- the module is already gone if we get called for ourselves
if pcall(require, 'usrmerge') then
    if posix.getenv("VERBOSE_FILETRIGGERS") then
        usrmerge.debug = "%{nvr}(postun)"
    end
    file = rpm.next_file()
    while file do
        usrmerge.add_postun(file)
        file = rpm.next_file()
    end
    io.flush()
end

%endif

%files
%dir %{_rpmconfigdir}/lua
%{_rpmconfigdir}/lua/usrmerge.lua
%{_rpmconfigdir}/lua/usrmerge_files.lua

%files tools
%{_bindir}/usrmergecheck
%{_libexecdir}/convertfs
%{_libexecdir}/xmv

%files build
%{_fileattrsdir}/usrmerge.attr
%dir %{_rpmconfigdir}/lua
%{_rpmconfigdir}/lua/usrmerge_binsbindeps.lua

%changelog
