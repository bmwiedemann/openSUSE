#
# spec file for package gnusocialshell
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


%define _name   GnuSocialShell
Name:           gnusocialshell
Version:        1.3.0
Release:        0
Summary:        Text-based GNU social client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://dalme.net/gnusocialshell
Source:         https://gitlab.com/DalmeGNU/GnuSocialShell/-/archive/v%{version}/%{_name}-v%{version}.tar.bz2
Patch0:         gnusocialshell-fix-cflags.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libcurl)

%description
GnuSocialShell is a text-based GNU social client written in C.

%prep
%setup -q -n %{_name}-v%{version}
%patch0 -p1
touch config.rpath
mv config config.example

%build
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%license LICENSE
%doc README.md config.example
%{_bindir}/%{name}

%changelog
