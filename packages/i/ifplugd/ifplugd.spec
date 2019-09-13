#
# spec file for package ifplugd
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


Name:           ifplugd
BuildRequires:  gcc-c++
BuildRequires:  libdaemon-devel
BuildRequires:  pkgconfig
Version:        0.28
Release:        0
Summary:        Daemon Activating Network Interfaces on Cable Plug
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Url:            http://0pointer.de/lennart/projects/ifplugd/
Source:         http://0pointer.de/lennart/projects/ifplugd/%{name}-%{version}.tar.gz
Source1:        README.initscript
Patch:          ifplugd.dif
Patch1:         ifplugd-0.28.dif
Patch2:         ifplugd.action.diff
Patch3:         ifplugd-nlapi-increase-packetsize.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ifplugd is a lightweight Linux daemon that configures the network
automatically when a cable is plugged in and unconfigures it when the
cable is pulled. It is primarily intended for use with laptops. It
relies on the distribution's native network configuration subsystem, so
is not very intrusive.

%prep
%setup -q
%patch -p1
%patch1
%patch2
%patch3 -p1
cp %{S:1} .
mv doc/README.SuSE doc/README.SUSE

%build
export CFLAGS="$RPM_OPT_FLAGS -D__KERNEL_STRICT_NAMES -fno-strict-aliasing"
%configure --disable-xmltoman --disable-subversion --disable-lynx
%{__make} %{?_smp_mflags}

%install
%make_install
chmod -x conf/ifplugd.init
rm -fv $RPM_BUILD_ROOT/etc/init.d/ifplugd
#UsrMerge
mkdir $RPM_BUILD_ROOT/sbin
ln -s %{_sbindir}/ifplugd $RPM_BUILD_ROOT/sbin
ln -s %{_sbindir}/ifplugstatus $RPM_BUILD_ROOT/sbin
#EndUsrMerge

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc LICENSE README doc/README.SUSE
%doc conf/ifplugd.init README.initscript
%{_sbindir}/*
#UsrMerge
/sbin/*
#EndUsrMerge
%doc %{_mandir}/man5/ifplugd.conf.5.gz
%doc %{_mandir}/man8/ifplugd.8.gz
%doc %{_mandir}/man8/ifplugstatus.8.gz
%config %{_sysconfdir}/ifplugd

%changelog
