#
# spec file for package gmrun
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2011 R. Tyler Croy <tyler@linux.com>
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


Name:           gmrun
Version:        1.4w
Release:        0
Summary:        A simple gtk-based command runner dialog with auto-complete
License:        ISC
Group:          Productivity/Other
URL:            https://github.com/wdlkmpx/gmrun
Source0:        https://github.com/wdlkmpx/gmrun/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel

%description
A smaller and lighter-weight alternative to grun or gnome-run, with auto-completion and ~ expansion.

%lang_package

%prep
%setup -q

%build
./configure --prefix=/usr --sysconfdir=/etc
%make_build

%install
%make_install

%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README.md ChangeLog AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/gmrun.desktop
%{_mandir}/man1/gmrun.1%{?ext_man}
%{_datadir}/pixmaps/gmrun.png
%config %{_sysconfdir}/%{name}rc

%files lang -f %{name}.lang

%changelog
