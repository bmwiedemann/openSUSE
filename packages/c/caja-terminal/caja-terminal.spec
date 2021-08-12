#
# spec file for package caja-terminal
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


# Package 'requires' two versions, confusing the typelib finder.
%define __requires_exclude typelib\\((Vte))\ =
Name:           caja-terminal
Version:        0.10
Release:        0
Summary:        Caja extension to enable an embedded terminal
License:        GPL-3.0-or-later
URL:            https://github.com/yselkowitz/caja-terminal
Source:         https://github.com/yselkowitz/caja-terminal/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         python3-support.patch
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  python3

%description
Caja Terminal is an embedded terminal for Caja, the MATE file
manager. It embeds a terminal pane into Caja that is accessible by
a hotkey (default F4) and automatically follows the currently
active directory in Caja.

%package -n caja-extension-terminal
Summary:        Caja extension to enable an embedded terminal
Requires:       caja
Requires:       python-caja
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pyxdg
Recommends:     caja-extension-terminal-lang
BuildArch:      noarch

%description -n caja-extension-terminal
Caja Terminal is an embedded terminal for Caja, the MATE file
manager. It embeds a terminal pane into Caja that is accessible by
a hotkey (Ctrl+Shift+T) and automatically follows the currently
active directory in Caja.

%lang_package -n caja-extension-terminal

%prep
%setup -q
%autopatch -p1

%build
# Nothing to build.

%install
./install.sh --package %{buildroot}
rm -r %{buildroot}%{_datadir}/doc/

%py3_compile %{buildroot}%{_datadir}/caja-python/extensions/
%find_lang %{name}

%files -n caja-extension-terminal
%license COPYING
%doc AUTHORS README
%{_datadir}/%{name}/
%dir %{_datadir}/caja-python/
%dir %{_datadir}/caja-python/extensions/
%{_datadir}/caja-python/extensions/%{name}.py
%{_datadir}/caja-python/extensions/__pycache__/

%files -n caja-extension-terminal-lang -f %{name}.lang

%changelog
