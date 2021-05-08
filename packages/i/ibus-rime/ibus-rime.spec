#
# spec file for package ibus-rime
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.5.0
Release:        0
Summary:        Rime for Linux/IBus
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/rime/ibus-rime
Source:         %{URL}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(rime)

%description
Rime Input Method Engine for Linux/IBus

%prep
%setup -q

%build
%cmake \
  -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
  -DRIME_DATA_DIR=%{_datadir}/rime-data
%make_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/rime-data
%{_ibus_componentdir}/rime.xml
%{_libexecdir}/ibus-rime/
%{_datadir}/ibus-rime/
%{_datadir}/rime-data/ibus_rime.yaml

%changelog
