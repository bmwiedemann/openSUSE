#
# spec file for package hercules
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hercules
Version:        3.13
Release:        0
Summary:        Hercules IBM Mainframe Emulator
License:        QPL-1.0
Group:          System/Emulators/Other
Url:            http://www.hercules-390.eu/
Source:         http://downloads.hercules-390.eu/%{name}-%{version}.tar.gz
BuildRequires:  libbz2-devel
BuildRequires:  zlib-devel

%description
Hercules is an emulator for the IBM System/370, ESA/390, and
z/Architecture series of mainframe computers. It is capable of running
any IBM operating system and applications that a real system will run,
as long as the hardwre needed is emulated. Hercules can emulate FBA and
CKD DASD, tape, printer, card reader, card punch, channel-to-channel
adapter, and printer-keyboard and 3270 terminal devices.

Hercules information can be found on the web at
http://www.conmicro.cx/hercules .

%prep
%setup -q

%build
%configure \
  --enable-cckd-bzip2 \
  --enable-het-bzip2 \
  --enable-optimization="%{optflags}" \
  --enable-multi-cpu=8
make %{?_smp_mflags} V=1

%install
%make_install

# Get rid of the libtool files
rm -f %{buildroot}/%{_libdir}/*.la
# ... but keep the s390 .la files, because that's the only way that they can be loaded
#### rm -f $RPM_BUILD_ROOT/%_libdir/%{name}/*.la

install -D -p -m 0644 hercules.cnf \
  %{buildroot}%{_sysconfdir}/%{name}/sample.cnf

%files
%defattr(-, root, root)
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/*.so
%{_mandir}/man1/*
%{_mandir}/man4/*
%{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/sample.cnf

%changelog
