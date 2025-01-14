#
# spec file for package qarma
#
# Copyright (c) 2025 Shawn W. Dunn <sfalken@opensuse.org>
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


Name:           qarma
Version:        1.0.0
Release:        0
Summary:        Tool for creating Qt dialog boxes
License:        GPL-2.0-Only
URL:            https://github.com/luebking/qarma
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

%description
Qarma is a tool to create dialog boxes, based on Qt. It's a clone of
Zenity which was written for GTK+.

%prep
%autosetup -p1

%build
qmake6 QMAKE_CFLAGS+="%optflags" \
       QMAKE_CXXFLAGS+="%optflags" \
       QMAKE_STRIP="/bin/true"
%make_build


%install
%make_install INSTALL_ROOT="%buildroot"

%check
%ctest

%files
%license LICENSE
%{_bindir}/%{name}

%changelog

