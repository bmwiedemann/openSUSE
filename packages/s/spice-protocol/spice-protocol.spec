#
# spec file for package spice-protocol
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


Name:           spice-protocol
Version:        0.14.0
Release:        0
Summary:        SPICE-protocol definitions
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            https://www.spice-space.org/
Source:         https://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
Source1:        https://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  meson >= 0.41.0
BuildRequires:  pkgconfig
Requires:       python-pyparsing
Requires:       python-six
BuildArch:      noarch

%description
Headers defining the SPICE-protocol

%package devel
Summary:        SPICE-protocol definitions
Group:          Development/Languages/C and C++

%description devel
Headers defining the SPICE-protocol

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files devel
%license COPYING
%doc CHANGELOG.md README.md
%{_datadir}/pkgconfig/spice-protocol.pc
%{_includedir}/spice-1/

%changelog
