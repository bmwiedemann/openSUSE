#
# spec file for package sc-controller
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


Name:           sc-controller
Version:        1.0.4
Release:        0
Summary:        User-mode driver, mapper, and GTK3-based GUI for the Steam Controller and many other controllers.
License:        GPL-2.0-only
Group:          Hardware/Joystick
URL:            https://github.com/C0rn3j/sc-controller
Source:         %{URL}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-libgtk4-layer-shell-so-name.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  shared-mime-info
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(udev)
Requires:       python3-evdev
Requires:       python3-gobject
Requires:       python3-ioctl-opt
Requires:       python3-libusb1
Requires:       python3-pycairo
Requires:       python3-pylibacl
Requires:       python3-setuptools
Requires:       python3-vdf

%description
User-mode driver and GTK4-based GUI for game controllers, including but not limited to the Steam Controller (2015 & 2026).

%prep
%autosetup -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -mpip wheel --verbose --progress-bar off --disable-pip-version-check --use-pep517 --no-build-isolation --no-deps --wheel-dir ./build .

%install
python3 -m installer --destdir=%{buildroot} build/*.whl

%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE
%doc README.md ADDITIONAL-LICENSES TODO.md
%{_bindir}/sc-controller
%{_bindir}/scc*
%{python3_sitearch}/*
%{_datadir}/applications/*
%{_datadir}/metainfo/io.github.c0rn3j.sc-controller.metainfo.xml
%{_datadir}/scc/
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*
%{_udevrulesdir}/69-sc-controller.rules

%changelog
