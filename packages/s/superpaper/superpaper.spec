#
# spec file for package superpaper
#
# Copyright (c) 2021 SUSE LLC
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


Name:           superpaper
Version:        2.1.0
Release:        0
Summary:        An advanced multi monitor wallpaper manager
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hhannine/superpaper
Source:         https://github.com/hhannine/superpaper/archive/v%{version}.tar.gz#/superpaper-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Pillow >= 7.0.0
BuildRequires:  python3-numpy >= 1.18.0
BuildRequires:  python3-screeninfo >= 0.6.1
BuildRequires:  python3-setuptools
BuildRequires:  python3-system_hotkey >= 1.0.3
BuildRequires:  python3-wxPython
BuildRequires:  python3-xcffib >= 0.8.0
BuildRequires:  python3-xpybutil >= 0.0.5
BuildRequires:  update-desktop-files
Requires:       python3-Pillow >= 7.0.0
Requires:       python3-numpy >= 1.18.0
Requires:       python3-screeninfo >= 0.6.1
Requires:       python3-system_hotkey >= 1.0.2
Requires:       python3-wxPython
Requires:       python3-xcffib >= 0.8.0
Requires:       python3-xpybutil >= 0.0.5
# this package used the python-rpm-macros singlespec system until May 2021.
Provides:       python3-superpaper = %{version}-%{release}
Obsoletes:      python3-superpaper < %{version}-%{release}
Provides:       python38-superpaper = %{version}-%{release}
Obsoletes:      python38-superpaper < %{version}-%{release}
BuildArch:      noarch

%description
Cross-platform wallpaper manager that focuses on multi-monitor support.
Features include ppi corrections, keyboard shortcuts, and slideshow.

%prep
%setup -q
# fix shebang
sed -i '/^#!/d' %{name}/__main__.py
# fix icon path
sed -i 's|share/icons/hicolor/256x256/apps|%{_datadir}/pixmaps|' setup.py

%build
%python3_build

%install
%python3_install
%suse_update_desktop_file %{name} DesktopSettings
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}*-info

%changelog
