#
# spec file for package fs-uae-launcher
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           fs-uae-launcher
Version:        3.2.35
Release:        0
Summary:        Graphical configuration frontend and launcher for FS-UAE
License:        GPL-2.0-or-later
Group:          System/Emulators/Other
URL:            https://fs-uae.net/
Source:         https://github.com/FrodeSolheim/fs-uae-launcher/releases/download/v%{version}/fs-uae-launcher-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       fs-uae
Requires:       python3-opengl
%if 0%{?suse_version} < 1600
Requires:       python3-qt5
%else
Requires:       python3-PyQt6
%endif
Requires:       python3-requests
Recommends:     python3-lhafile
BuildArch:      noarch

%description
FS-UAE Launcher is a graphical configuration program and launcher for FS-UAE.

%prep
%setup -q

%build
python3 setup.py build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%suse_update_desktop_file -r %{name} System Emulator
rm -rf %{buildroot}/%{_datadir}/doc
%fdupes %{buildroot}%{_datadir}
%find_lang %{name}

# fix the shebang
sed -i '1 s|#.*$|#!/usr/bin/python3|g' %{buildroot}%{_bindir}/%{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
