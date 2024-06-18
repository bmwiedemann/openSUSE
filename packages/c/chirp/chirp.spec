#
# spec file for package chirp
#
# Copyright (c) 2023 Wojciech Kazubski <wk@ire.pw.edu.pl>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define pythons python3
Name:           chirp
Version:        20240614
Release:        0
Summary:        Tool for programming amateur radio sets
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://chirpmyradio.com/projects/chirp/
Source:         https://archive.chirpmyradio.com/chirp_next/next-%{version}/%{name}-%{version}.tar.gz
Patch0:         chirp-no-phone-home.patch
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wxPython}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       python3-pyserial
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-suds
Requires:       python3-wxPython
Requires:       python3-yattag
BuildArch:      noarch

%description
CHIRP is a free, open-source tool for programming your amateur radio. It
supports a large number of manufacturers and models, as well as provides
a way to interface with multiple data sources and formats.

%prep
%autosetup -p1
# remove shebang from lib files
sed -i '1{/^#!\//d}' %{name}/cli/experttune.py
sed -i '1{/^#!\//d}' %{name}/cli/main.py

%build
%python_build

%install
%python_install
rm -rf %{buildroot}%{_datadir}/doc/%{name}
%find_lang CHIRP
%fdupes %{buildroot}%{_prefix}
%suse_update_desktop_file -c chirp CHIRP "Amateur Radio Rig Programming Tool" chirp chirp "Network;HamRadio"
install -Dpm 0644 chirp/share/chirp.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dpm 0644 chirp/share/chirp.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files -f CHIRP.lang
%license COPYING
%doc PKG-INFO
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{python_sitelib}/*.egg-info
%{python_sitelib}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png

%changelog
