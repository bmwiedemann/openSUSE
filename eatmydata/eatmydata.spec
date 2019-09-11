#
# spec file for package eatmydata
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           eatmydata
Version:        105
Release:        0
Summary:        A library to disable fsync calls
License:        GPL-3.0
Group:          Development/Tools/Other
Url:            http://www.flamingspork.com/projects/libeatmydata/
# https://launchpad.net/libeatmydata
Source0:        http://www.flamingspork.com/projects/libeatmydata/libeatmydata-%{version}.tar.gz
Source1:        http://www.flamingspork.com/projects/libeatmydata/libeatmydata-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{name}-rpmlintrc
Patch1:         libeatmydata-105-remove-dpkg.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:
#Requires:       bash

%description
libeatmydata is a small LD_PRELOAD library designed to (transparently) disable fsync (and friends, like open(O_SYNC)). This has two side-effects: making software that writes data safely to disk a lot quicker and making this software no longer crash safe.

%prep
%setup -q -n lib%{name}-%{version}
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -rf %{buildroot}%{_libexecdir}/debug
rm -f %{buildroot}/%{_libdir}/libeatmydata.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%attr(0755,root,root) %{_bindir}/eatmydata
%attr(0755,root,root) %{_libexecdir}/eatmydata.sh
%{_libdir}/libeatmydata.so*

%changelog
