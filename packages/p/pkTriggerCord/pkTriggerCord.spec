#
# spec file for package pkTriggerCord
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


%define sname pktriggercord

Summary:        Remote control program for Pentax DSLR cameras
License:        LGPL-3.0-only
Group:          Hardware/Camera
Name:           pkTriggerCord
Version:        0.85.00+git.20220806
Release:        0
Source:         %{sname}-%{version}.tar.xz
Patch1:         0001-rules-handle-permissions-by-uaccess.patch
URL:            http://pktriggercord.melda.info/
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make

%description
pkTriggerCord is a remote control program for Pentax DSLR cameras.

%prep
%autosetup -n %{sname}-%{version} -p1

%build
make %{?_smp_mflags} PREFIX=%{_prefix} CFLAGS="%optflags -Isrc/external/js0n"

%install
%{makeinstall} PREFIX=%{_prefix}

install -d %{buildroot}/%{_udevrulesdir}
cp %{buildroot}/%{_sysconfdir}/udev/rules.d/*.rules %{buildroot}/%{_udevrulesdir}
rm -rf %{buildroot}/%{_sysconfdir}/udev/
pushd %{buildroot}/%{_udevrulesdir}
# move them before uaccess handling
for F in samsung.rules pentax.rules; do
	mv 95_$F 40-$F
done
popd

%files
%defattr(-,root,root)
%doc Changelog BUGS
%license COPYING
%{_bindir}/%{sname}*
%{_datadir}/%{sname}
%{_mandir}/*/%{sname}*
%{_udevrulesdir}/*.rules

%changelog
