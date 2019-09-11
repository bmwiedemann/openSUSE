#
# spec file for package devilspie2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           devilspie2
Version:        0.43
Release:        0
Summary:        A window matching utility
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            http://www.nongnu.org/devilspie2/
Source0:        http://download.savannah.gnu.org/releases/devilspie2/%{name}_%{version}-src.tar.gz
Source1:        http://download.savannah.gnu.org/releases/devilspie2/%{name}_%{version}-src.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(lua) >= 5.1
Recommends:     %{name}-lang = %{version}

%description
Devilspie 2 is based on the excellent program Devil's Pie by Ross Burton, and
takes a folder as in-data, and checks that folder for LUA scripts. These
scripts are run each time a window is opened, and the rules in them are applied
on the window.

Unfortunately the rules of the original Devil's Pie are not supported.

%lang_package

%prep
%setup -q

%build
make %{?_smp_mflags} CC="cc %{optflags}"

%install
%make_install PREFIX=%{_usr}
install -D -p -m 644 %{name}.1 \
  %{buildroot}/%{_mandir}/man1/%{name}.1

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
