#
# spec file for package superpaper
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           superpaper
Version:        2.1.0
Release:        0
Summary:        An advanced multi monitor wallpaper manager
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hhannine/superpaper
Source:         https://github.com/hhannine/superpaper/archive/v%{version}.tar.gz#/superpaper-%{version}.tar.gz
BuildRequires:  %{python_module Pillow >= 7.0.0}
BuildRequires:  %{python_module numpy >= 1.18.0}
BuildRequires:  %{python_module screeninfo >= 0.6.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module system_hotkey >= 1.0.3}
BuildRequires:  %{python_module wxPython}
BuildRequires:  %{python_module xcffib >= 0.8.0}
BuildRequires:  %{python_module xpybutil >= 0.0.5}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       python-Pillow >= 7.0.0
Requires:       python-numpy >= 1.18.0
Requires:       python-screeninfo >= 0.6.1
Requires:       python-system_hotkey >= 1.0.2
Requires:       python-wxPython
Requires:       python-xcffib >= 0.8.0
Requires:       python-xpybutil >= 0.0.5
BuildArch:      noarch
%python_subpackages

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
%python_build

%install
%python_install
%suse_update_desktop_file %{name} DesktopSettings
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{python_sitelib}/%{name}
%{python_sitelib}/*egg-info

%changelog
