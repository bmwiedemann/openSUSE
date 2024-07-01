#
# spec file for package axel
#
# Copyright (c) 2024 SUSE LLC
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


%{!?license: %global license %doc}
%{!?make_build: %global make_build make %{?_smp_mflags}}
Name:           axel
Version:        2.17.14
Release:        0
Summary:        Lightweight Download Accelerator
License:        GPL-2.0-or-later
URL:            https://github.com/axel-download-accelerator/axel
Source:         https://github.com/axel-download-accelerator/axel/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
Axel tries to accelerate HTTP/FTP downloading process by using multiple
connections for one file. It can use multiple mirrors for a download. Axel has
no dependencies and is lightweight, so it might be useful as a wget clone on
byte-critical systems.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang axel

%files -f axel.lang
%doc ChangeLog NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
