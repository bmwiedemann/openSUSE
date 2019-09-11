#
# spec file for package nautilus-terminal
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


%define have_lang 0
Name:           nautilus-terminal
Version:        1.0
Release:        0
Summary:        Integrated Terminal for the Nautilus File Browser
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            http://software.flogisoft.com/nautilus-terminal/
Source:         %{name}_%{version}_src.tar.gz
# PATCH-FIX-UPSTREAM nautilus-terminal-vte2.91.patch dimstar@opensuse.org -- Fix usage with Vte 2.91.
Patch0:         nautilus-terminal-vte2.91.patch
# For directory ownership:
BuildRequires:  gobject-introspection
BuildRequires:  python-nautilus
BuildRequires:  vte-devel
Requires:       nautilus
Recommends:     python-xdg
BuildArch:      noarch
%if %{have_lang}
Recommends:     %{name}-lang
%endif

%description
Nautilus Terminal is an integrated terminal for the Nautilus file browser.

%if %{have_lang}
%lang_package
%endif

%prep
%setup -q -n %{name}_%{version}_src
if pkg-config --exists vte-2.91; then
# patch0 only applies when built against Vte 2.91
%patch0 -p1
fi
sed -i '
s:%{_datadir}/doc:%{_docdir}/%{name}:
s:%{_prefix}/share:%{_datadir}:
s:%{_prefix}/lib:%{_libdir}:
' install.sh

%build

%install
./install.sh --package %{buildroot}
%if %{have_lang}
%find_lang %{name}
%endif

%files
%doc %{_docdir}/%{name}/
%{_datadir}/nautilus-python/extensions/nautilus_terminal.py
%{_datadir}/nautilus-terminal/

%if %{have_lang}
%files lang -f %{name}.lang
%endif

%changelog
