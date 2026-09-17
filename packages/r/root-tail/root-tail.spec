#
# spec file for package root-tail
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           root-tail
Version:        1.3
Release:        0
Summary:        Print Text Directly to the X Window System Root Window
License:        GPL-2.0-or-later
URL:            https://software.schmorp.de/pkg/root-tail.html
Source0:        https://dist.schmorp.de/root-tail/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE default-fontset.patch -- usable default fontset instead of "*"
Patch0:         default-fontset.patch
# PATCH-FEATURE-OPENSUSE root-tail-1.2-shade.diff -- configurable shade offsets (-offsets)
Patch1:         root-tail-1.2-shade.diff
# PATCH-FIX-UPSTREAM makefile-link-order.patch -- libs after objects for --as-needed (Debian #930581)
Patch2:         makefile-link-order.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
Provides:       roottail
Obsoletes:      roottail

%description
Tails a given file anywhere on your X Window System root window with a
transparent background. It is customizable with regards to font, color,
and more.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags} -Wall" \
            LDFLAGS="%{build_ldflags} $(pkg-config --libs x11 xext xfixes)" \
            root-tail

%install
install -D -m 0755 root-tail %{buildroot}%{_bindir}/root-tail
install -D -m 0644 root-tail.man %{buildroot}%{_mandir}/man1/root-tail.1

%files
%doc README Changes
%{_bindir}/root-tail
%{_mandir}/man1/root-tail.1%{?ext_man}

%changelog
