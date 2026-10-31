#
# spec file for package hcxtools
#
# Copyright (c) 2021-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           hcxtools
Version:        8.0.0
Release:        0
Summary:        Capturing wlan traffic and conversion to hashcat and John the Ripper formats
License:        MIT
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/ZerBea/hcxtools
#Git-Clone:     https://github.com/ZerBea/hcxtools.git
Source:         https://github.com/ZerBea/hcxtools/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Portable solution for capturing wlan traffic and conversion to
hashcat and John the Ripper formats.

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license license.txt
%doc changelog README.md
%{_bindir}/hcxeiutool
%{_bindir}/hcxhash2cap
%{_bindir}/hcxhashtool
%{_bindir}/hcxpcapngtool
%{_bindir}/hcxpmktool
%{_bindir}/hcxpottool
%{_bindir}/hcxpsktool
%{_bindir}/hcxwltool
%{_bindir}/whoismac
%{_bindir}/wlancap2wpasec

%changelog
