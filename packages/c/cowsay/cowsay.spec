#
# spec file for package cowsay
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


%if 0%{?suse_version} >= 1140
%{?!perl_requires:%define perl_requires() Requires: perl = %{perl_version}}
%endif
Name:           cowsay
Version:        3.03
Release:        0
Summary:        Configurable talking cow (and some other creatures)
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Amusements/Toys/Other
URL:            http://nog.net/~tony/warez/
Source:         http://nog.net/~tony/warez/%{name}-%{version}.tar.gz
Source1:        http://nog.net/~tony/warez/%{name}-%{version}.tar.gz.sig
Source2:        http://nog.net/~tony/tony-monroe-gpgkey.txt#/cowsay.keyring
Patch0:         one-eye.patch
Patch1:         chami.patch
BuildRequires:  bash
BuildRequires:  perl
BuildArch:      noarch
%{perl_requires}

%description
cowsay is a configurable talking cow, written in Perl.  It operates
much as the figlet program does, and it written in the same spirit
of silliness.

%prep
%setup -q
sed -i "s|,\$%{nil}PREFIX,|,%{_prefix},|" install.sh
%patch0 -p1
%patch1 -p1

%build
perl -c cowsay

%install
bash ./install.sh %{buildroot}%{_prefix}
mv -T %{buildroot}%{_prefix}/man/ %{buildroot}%{_mandir}
rm -f %{buildroot}%{_datadir}/cows/mech-and-cow

%files
%license LICENSE
%doc ChangeLog MANIFEST README
%{_bindir}/%{name}
%{_bindir}/cowthink
%{_datadir}/cows
%{_mandir}/man1/*

%changelog
