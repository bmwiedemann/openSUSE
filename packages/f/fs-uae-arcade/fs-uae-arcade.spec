#
# spec file for package fs-uae-arcade
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


Name:           fs-uae-arcade
Version:        3.0.5
Release:        0
Summary:        Fullscreen game browser for FS-UAE
License:        GPL-2.0-or-later
Group:          System/Emulators/Other
URL:            https://fs-uae.net/
Source0:        https://fs-uae.net/stable/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       fs-uae
Requires:       python3-qt5
Requires:       python3-requests
Recommends:     python3-lhafile
BuildArch:      noarch

%description
FS-UAE Arcade is a fullscreen Amiga game browser for FS-UAE.

%prep
%setup -q

%build
python3 setup.py build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%suse_update_desktop_file -r %{name} System Emulator
rm -rf %{buildroot}/%{_datadir}/doc
%fdupes %{buildroot}%{_datadir}/%{name}

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
