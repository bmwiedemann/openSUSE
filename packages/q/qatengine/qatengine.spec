#
# spec file for package qatengine
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


Name:           qatengine
Version:        0.6.17
Release:        0
Summary:        Intel QuickAssist Technology (QAT) QATengine Library
License:        BSD-3-Clause
Group:          Hardware/Other
URL:            https://github.com/intel/QAT_Engine
Source:         https://github.com/intel/QAT_Engine/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc >= 4.8.5
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  qatlib-devel >= 21.08.0
BuildRequires:  zlib-devel >= 1.2.7
# This package can be built on all archs, but is useful only on enterprise-class intel.
ExclusiveArch:  x86_64

%description
Intel® QuickAssist Technology OpenSSL* Engine (QAT_Engine) supports
acceleration for both hardware as well as optimized software based
on vectorized instructions. This package contains an OpenSSL engine
module that utilises QAT.

%prep
%autosetup -n QAT_Engine-%{version}

%build
%{set_build_flags}
autoreconf -fiv
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license LICENSE*
%{_libdir}/engines-*/%{name}.so

%changelog
