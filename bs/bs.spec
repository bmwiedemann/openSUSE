#
# spec file for package bs
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           bs
Version:        2.10
Release:        0
Summary:        Battleships solitaire game with a color interface
License:        BSD-3-Clause
Group:          Amusements/Games/Strategy/Turn Based
Url:            http://www.catb.org/~esr/bs/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The classic game of Battleships against the computer. Uses character-cell
graphics with a visual point-and-shoot interface. If you're using an xterm
under Linux the mouse will work.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/appdata/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
