#
# spec file for package sl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 <vodoo@vakw.ch>
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


Name:           sl
Version:        5.02
Release:        0
Summary:        Steam Locomotive in ASCII art
# The warranty claim is a bit different, but the rights are the same as in ISC
License:        ISC
Group:          Amusements/Toys/Other
URL:            https://github.com/mtoyoda/sl
Source:         https://github.com/mtoyoda/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         update_to_master_at_923e7d7.patch
BuildRequires:  ncurses-devel
Conflicts:      python3-softlayer

%description
"sl" displays a steam locomotive running across the terminal.
It is a joke command intended to catch any mistypings of "ls".

%prep
%setup -q
%patch0 -p1

%build
make OPTFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
cp sl %{buildroot}%{_bindir}/sl
cp sl.1 %{buildroot}%{_mandir}/man1/sl.1

%files
%{_mandir}/man1/sl.1%{?ext_man}
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
