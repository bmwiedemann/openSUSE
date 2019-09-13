#
# spec file for package mt-st
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


Name:           mt-st
Version:        1.3
Release:        0
Summary:        Utility for Controlling Magnetic Tape Drives
License:        GPL-2.0+
Group:          Productivity/Archiving/Backup
Url:            https://github.com/iustin/%{name}
Source0:        https://github.com/iustin/mt-st/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/iustin/mt-st/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz.asc
Source2:        stinit.def
Source3:        61-storage-tape-init.rules
Source4:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
Provides:       mt
Requires:       udev
Requires(post): update-alternatives
Requires(post): udev
Requires(postun): update-alternatives
Requires(postun): udev
Provides:       mt_st = %{version}-%{release}
Obsoletes:      mt_st < %{version}-%{release}

%description
mt-st tools contains two programs: mt and stinit, used for dealing
with Linux-specific tape-drive handling. mt program is tailored for
SCSI tape drives, but it can also be used with other Linux tape
drivers that use the same ioctls. The program stinit is meant for
initializing of SCSI tape drive modes at system startup, or when
new tape drivers are added.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -pipe" DEFTAPE=/dev/nst0

%install
%make_install EXEC_PREFIX=%{_prefix}
install -D -p -m 0644 %{SOURCE2} \
  %{buildroot}%{_sysconfdir}/stinit.def
install -D -p -m 0644 %{SOURCE3} \
  %{buildroot}%{_udevrulesdir}/61-storage-tape-init.rules
#For alternatives
mv %{buildroot}%{_bindir}/mt %{buildroot}%{_bindir}/mtst
mv %{buildroot}%{_mandir}/man1/mt.1 %{buildroot}%{_mandir}/man1/mtst.1
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/mt %{buildroot}%{_bindir}/mt
ln -s -f %{_sysconfdir}/alternatives/mt.1%{ext_man} %{buildroot}%{_mandir}/man1/mt.1%{ext_man}

%post
%{_sbindir}/update-alternatives --force \
    --install %{_bindir}/mt mt %{_bindir}/mtst 30 \
    --slave %{_mandir}/man1/mt.1%{ext_man}  mt.1%{ext_man}  %{_mandir}/man1/mtst.1%{ext_man}
%udev_rules_update

%postun
if [ "$1" = 0 ] ; then
   "%{_sbindir}/update-alternatives" --remove mt %{_bindir}/mtst
fi
%udev_rules_update

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md COPYING stinit.def.examples
%ghost %{_bindir}/mt
%{_bindir}/mtst
%{_sbindir}/stinit
%ghost %{_mandir}/man1/mt.1%{ext_man}
%{_mandir}/man1/mtst.1%{ext_man}
%{_mandir}/man8/stinit.8%{ext_man}
%config(noreplace) %{_sysconfdir}/stinit.def
%{_udevrulesdir}/61-storage-tape-init.rules
%ghost %{_sysconfdir}/alternatives/mt
%ghost %{_sysconfdir}/alternatives/mt.1%{ext_man}

%changelog
