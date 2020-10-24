#
# spec file for package sc-controller
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


Name:           sc-controller
Version:        0.4.8.1.20201002
Release:        0
Summary:        User-mode driver and GTK3-based GUI for the Steam Controller
License:        GPL-2.0-only
Group:          Hardware/Joystick
URL:            https://github.com/Ryochan7/sc-controller/tree/python3
Source:         %{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(udev)
Requires:       python3-evdev
Requires:       python3-gobject-Gdk
Requires:       python3-pylibacl
Requires:       python3-setuptools

%description
Application allowing to setup, configure and use the Steam Controller
without using the Steam client.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --optimize=1

%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE
%doc README.md ADDITIONAL-LICENSES TODO.md
%{_bindir}/*
%{python3_sitearch}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/scc/
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*
%{_udevrulesdir}/69-sc-controller.rules

%changelog
