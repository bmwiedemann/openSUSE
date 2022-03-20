#
# spec file for package impressive
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


%define dist_name Impressive
Name:           impressive
Version:        0.13.1
Release:        0
Summary:        PDF and image viewer optimized for presentations
License:        GPL-2.0-only
Group:          Productivity/Office/Other
URL:            http://impressive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{dist_name}/%{version}/%{dist_name}-%{version}.tar.gz
Requires:       ghostscript
Requires:       python3-imaging
Requires:       python3-opengl
Requires:       python3-pygame
Recommends:     mupdf
BuildArch:      noarch

%description
Impressive is a program that displays presentation slides.
Features:
- Page transitions
- Overview screen
- Highlight boxes
- Spotlight effect

%prep
%autosetup -p1 -n %{dist_name}-%{version}

sed -i 's/env python$/python3/' impressive.py

%build

%install
install -Dm 0755 %{name}.py %{buildroot}%{_bindir}/%{name}
install -Dm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license license.txt
%doc changelog.txt demo.pdf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
