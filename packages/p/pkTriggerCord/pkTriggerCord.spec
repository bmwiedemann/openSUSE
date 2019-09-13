#
# spec file for package pkTriggerCord
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sname %(echo %{name}|tr A-Z a-z)

Summary:        Remote control program for Pentax DSLR cameras
License:        LGPL-3.0
Group:          Hardware/Camera
Name:           pkTriggerCord
Version:        0.84.04
Release:        0
Source:         https://github.com/asalamon74/pktriggercord/releases/download/v%{version}/%{name}-%{version}.src.tar.gz
Url:            http://pktriggercord.melda.info/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
Requires(post): libcap-progs

%description
pkTriggerCord is a remote control program for Pentax DSLR cameras.

%prep
%setup -q -n %{sname}-%{version}

%build
make clean
make %{?_smp_mflags} PREFIX=%{_prefix} CFLAGS="%optflags"

%install
%{makeinstall} PREFIX=%{_prefix}

install -d %{buildroot}/%{_prefix}/lib/udev/rules.d/
cp %{buildroot}/%{_sysconfdir}/udev/rules.d/*.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/
rm -rf %{buildroot}/%{_sysconfdir}/udev/

%post
setcap CAP_SYS_RAWIO+eip %{_bindir}/%{sname}-cli
setcap CAP_SYS_RAWIO+eip %{_bindir}/%{sname}

%files
%defattr(-,root,root)
%doc Changelog COPYING BUGS
%{_bindir}/%{sname}*
%{_datadir}/%{sname}
%{_mandir}/*/%{sname}*
%dir %{_prefix}/lib/udev/
%dir %{_prefix}/lib/udev/rules.d/
%{_prefix}/lib/udev/rules.d/*.rules

%changelog
