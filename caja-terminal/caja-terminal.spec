#
# spec file for package caja-terminal
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# Package 'requires' two versions, confusing the typelib finder.
%define __requires_exclude typelib\\((Vte))\ =
Name:           caja-terminal
Version:        0.10
Release:        0
Summary:        Caja extension to enable an embedded terminal
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/yselkowitz/caja-terminal
Source:         https://github.com/yselkowitz/caja-terminal/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  python2
%else
BuildRequires:  python
%endif

%description
Caja Terminal is an embedded terminal for Caja, the MATE file
manager. It embeds a terminal pane into Caja that is accessible by
a hotkey (default F4) and automatically follows the currently
active directory in Caja.

%package -n caja-extension-terminal
Summary:        Caja extension to enable an embedded terminal
Group:          System/GUI/Other
Requires:       caja
Recommends:     caja-extension-terminal-lang
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires:       python2-caja
Requires:       python2-gobject
Requires:       python2-gobject-Gdk
Requires:       python2-pyxdg
%else
Requires:       python-caja
Requires:       python-gobject
Requires:       python-gobject-Gdk
Requires:       python-pyxdg
%endif

%description -n caja-extension-terminal
Caja Terminal is an embedded terminal for Caja, the MATE file
manager. It embeds a terminal pane into Caja that is accessible by
a hotkey (Ctrl+Shift+T) and automatically follows the currently
active directory in Caja.

%lang_package -n caja-extension-terminal

%prep
%setup -q

%build
# Nothing to build.

%install
./install.sh --package %{buildroot}
rm -r %{buildroot}%{_datadir}/doc/

%py_compile %{buildroot}%{_datadir}/caja-python/extensions/
%find_lang %{name}

%files -n caja-extension-terminal
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS README
%{_datadir}/%{name}/
%dir %{_datadir}/caja-python/
%dir %{_datadir}/caja-python/extensions/
%{_datadir}/caja-python/extensions/%{name}.py*

%files -n caja-extension-terminal-lang -f %{name}.lang

%changelog
