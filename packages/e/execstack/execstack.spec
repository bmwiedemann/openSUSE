#
# spec file for package execstack
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#               2014 Wolfgang Rosenauer
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

Name:           execstack
Version:        0.5.0
Release:        0%{?dist}
Summary:        Utility to set/clear/query executable stack bit

%global commit 4c79120bcdbde0616f592458ccde7035e92ca3d8
%global shortcommit 4c79120
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})
# do not use dynamic shortcommit, Source0 with git format and autosetup
# because "osc service localrun source_validator" would report error

License: GPL-2.0+
Url:	 https://github.com/keszybz/prelink/archive
Source0: prelink-%{shortcommit}.tar.gz
#ource0: https://github.com/keszybz/prelink/archive/%%{commit}.tar.gz#/prelink-%%{shortcommit}.tar.gz

Patch0:  Add-PL_ARCH-for-AArch64.patch
Patch1:  prelink_update_fsf_address.patch
# bypass where gcc linker do not add the GNU_STACK default header in elf file
Patch2:  prelink_add_no_execstack_for_ppc64.patch

BuildRequires: libelf-devel
BuildRequires: libselinux-devel, selinux-tools
BuildRequires: git
Requires: glibc >= 2.2.4-18, coreutils, findutils
Requires: util-linux, gawk, grep
Conflicts: prelink <= %{version}

%description
This package is built from prelink sources but contains just the
execstack binary. It can be used manipulate ELF binaries to run
with or without executable stack.

%prep
#autosetup -n prelink-%%{commit} -p1 -Sgit
%setup -q -n prelink-%{commit}
%patch0 -p1
%patch1 -p1
%ifarch ppc64
%patch2 -p1
%endif

%build
sed -i -e '/^prelink_LDADD/s/$/ -lpthread/' src/Makefile.{am,in}
%configure
make %{?_smp_mflags} -C gelf
make %{?_smp_mflags} -C gelfx
make %{?_smp_mflags} -C gelfx32
make %{?_smp_mflags} -C src execstack

%check
cp src/execstack test
src/execstack -q test | grep '^-'
src/execstack -s test
src/execstack -q test | grep '^X'
src/execstack -c test
src/execstack -q test | grep '^-'

%install
install -D src/execstack %{buildroot}%{_bindir}/execstack
install -Dm0644 doc/execstack.8 %{buildroot}%{_mandir}/man8/execstack.8

%files
%defattr(-,root,root,-)
%{_bindir}/execstack
%{_mandir}/man8/execstack.8.*
%doc ChangeLog NEWS README TODO THANKS COPYING

%changelog

