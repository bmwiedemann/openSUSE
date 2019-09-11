#
# spec file for package vit
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


Name:           vit
Version:        1.3~20190107.g96134b3
Release:        0
Summary:        Curses-based front end to Taskwarrior
License:        GPL-3.0-only
Group:          Productivity/Office/Organizers
Url:            https://github.com/scottkosty/vit
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  taskwarrior
BuildRequires:  perl(Curses)
Requires:       taskwarrior
Requires:       perl(Curses)
Requires:       perl(Text::CharWidth)
BuildArch:      noarch

%description
VIT - a minimalistic Taskwarrior full-screen terminal interface with Vim key
bindings

%prep
%setup -q
echo %{version} > VERSION

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc AUTHORS CHANGES README
%{_bindir}/vit
%{_datadir}/vit
%{_mandir}/man1/vit.1%{ext_man}
%{_mandir}/man5/vitrc.5%{ext_man}

%changelog
