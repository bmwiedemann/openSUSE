#
# spec file for package screenkey
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


Name:           screenkey
Version:        1.5
Release:        0
Summary:        A screen-cast tool to show keys
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.thregr.org/~wavexx/software/screenkey/
Source0:        https://www.thregr.org/~wavexx/software/screenkey/releases/%{name}-%{version}.tar.gz
Source1:        https://www.thregr.org/~wavexx/software/screenkey/releases/%{name}-%{version}.tar.gz.asc
Source2:        https://www.thregr.org/~wavexx/files/wavexx.asc#/%{name}.keyring
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Babel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pycairo
Requires:       slop
Requires:       typelib(Gtk) = 3.0
Recommends:     fontawesome-fonts
BuildArch:      noarch

%description
A screencast tool to show keys. Inspired by Screenflick and based on
the key-mon project.

%prep
%autosetup

%build
%python3_build

%install
%python3_install
%find_lang %{name}
 %fdupes -s %{buildroot}

%files -f %{name}.lang
%license COPYING.txt
%{_bindir}/%{name}
%{python3_sitelib}/Screenkey/
%{python3_sitelib}/%{name}-%{version}-*.egg-info/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.thregr.screenkey.metainfo.xml
%doc %{_datadir}/doc/%{name}/

%changelog
