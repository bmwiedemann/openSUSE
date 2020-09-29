#
# spec file for package ibus-rime
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.4.1~git20200712.33b2755
Release:        0
Summary:        Rime for Linux/IBus
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/rime/ibus-rime
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
%dir %{_datadir}/rime-data
%{_ibus_componentdir}/rime.xml
%{_datadir}/ibus-rime/
%{_datadir}/rime-data/ibus_rime.yaml
%{_prefix}/lib/ibus-rime/

%changelog
