#
# spec file for package bin86
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bin86
Version:        0.16.21
Release:        0
Summary:        An 8086 Assembler and Linker
License:        GPL-2.0-or-later
Url:            http://v3.sk/~lkundrak/dev86/
Source0:        http://v3.sk/~lkundrak/dev86/Dev86src-%{version}.tar.gz
Source1:        bin86-rpmlintrc
Patch0:         dev86-0.16.20.dif
Patch2:         dev86-noelks.patch
Patch3:         dev86-x86_64.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

%description
An 8086 assembler and linker.

%package -n dev86
Summary:        8086 Development Suite
Requires:       bin86

%description -n dev86
This package contains tools for generating Elks/8086 programs and the
Elksemu for execution of these programs in Linux.

%prep
%setup -q -n dev86-%{version}
%patch0
%patch2 -p1 -b .noelks
%ifarch x86_64
%patch3 -p1 -b .x86_64
%endif

%build
make GCCFLAG="%{optflags} -fno-strict-aliasing"

%install
make install DIST=%{buildroot} PREFIX=/usr MANDIR=%{_mandir} \
	LIBDIR=%{_libdir}/bcc \
	INCLDIR=%{_libdir}/bcc
make other
make install-other DIST=%{buildroot} MANDIR=%{_datadir}/man
mv bootblocks/README bootblocks/README.bootblocks
mv copt/README copt/README.copt
mv dis88/README dis88/README.dis88
mv unproto/README unproto/README.unproto
mv bin86/README bin86/README.bin86
mkdir %{buildroot}/%{_libdir}/bcc/kinclude
cp -a libc/kinclude/arch %{buildroot}/%{_libdir}/bcc/kinclude
cp -a libc/kinclude/linuxmt %{buildroot}/%{_libdir}/bcc/kinclude
%if 0%{?suse_version} > 1020
%fdupes %{buildroot}
%endif

%files
%defattr(-,root,root)
%doc README
%{_bindir}/as86
%{_bindir}/ld86
%{_bindir}/nm86
%{_bindir}/objdump86
%{_bindir}/size86
%doc %{_mandir}/man1/as86.1.gz
%doc %{_mandir}/man1/ld86.1.gz

%files -n dev86
%defattr(-,root,root)
%doc MAGIC Contributors bootblocks/README.bootblocks copt/README.copt
%doc dis88/README.dis88
%doc unproto/README.unproto bin86/README-0.4
%doc bin86/README.bin86 bin86/ChangeLog
%{_bindir}/ar86
%{_bindir}/bcc
%{_bindir}/dis86
%{_bindir}/makeboot
%{_libdir}/bcc
%doc %{_mandir}/man1/bcc.1.gz
%doc %{_mandir}/man1/dis86.1.gz
%exclude %{_mandir}/man1/elks.1.gz
%exclude %{_mandir}/man1/elksemu.1.gz

%changelog
