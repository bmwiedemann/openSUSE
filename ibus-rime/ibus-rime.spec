#
# spec file for package ibus-rime
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


Name:           ibus-rime
Version:        1.4.1~git20190223.c80c02f
Release:        0
Summary:        Rime for Linux/IBus
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
Url:            https://github.com/rime/ibus-rime
Source:         %{name}-%{version}.tar.xz
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  brise
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  ibus-devel
BuildRequires:  libkyotocabinet-devel
BuildRequires:  libnotify-devel
BuildRequires:  librime-devel >= 1.0
BuildRequires:  opencc
BuildRequires:  opencc-devel
Requires:       rime

%description
Rime Input Method Engine for Linux/IBus

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc README.md
%{_ibus_componentdir}/rime.xml
%{_datadir}/ibus-rime/
%{_libexecdir}/ibus-rime/

%changelog
