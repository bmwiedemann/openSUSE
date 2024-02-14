#
# spec file for package focus-stack
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


Name:           focus-stack
Version:        1.4
Release:        0
Summary:        Fast and easy focus stacking
License:        MIT
URL:            https://github.com/PetteriAimonen/focus-stack 
Source:         https://github.com/PetteriAimonen/focus-stack/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-version.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(opencv4)

%description
This project implements a cross-platform tool for focus stacking images. The
application takes a set of images captured at different focus distances and
combines them so that the complete subject is in focus.

%prep
%autosetup -p1

%build
%make_build CXXFLAGS="%{optflags} -Wno-sign-compare -DRPM_VERSION=%{version}"

%install
%make_install prefix=%{_prefix}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/focus-stack
%{_mandir}/man1/focus-stack.1%{ext_man}

%changelog
