#
# spec file for package cowsay
#
# Copyright (c) 2025 SUSE LLC
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


%{?!perl_requires:%define perl_requires() Requires: perl = %{perl_version}}
Name:           cowsay
Version:        3.8.4
Release:        0
Summary:        Configurable talking cow (and some other creatures)
License:        GPL-3.0-or-later
Group:          Amusements/Toys/Other
URL:            https://cowsay.diamonds/
Source:         https://github.com/cowsay-org/cowsay/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         chami.patch
BuildRequires:  make
BuildRequires:  perl
BuildArch:      noarch
%{perl_requires}

%description
cowsay is a configurable talking cow, written in Perl. It operates
much as the figlet program does, and it written in the same spirit
of silliness.

%prep
%autosetup -p1
sed -i '1 s/env //' bin/cow*

%build
:

%install
%make_install prefix=%{_prefix}

%check
# no test suite available at all

%files
%license LICENSE.txt
%doc README.md CONTRIBUTORS.md CHANGELOG.md
%{_bindir}/cowsay
%{_bindir}/cowthink
%{_datadir}/cowsay
%{_mandir}/man1/cowsay.1%{?ext_man}
%{_mandir}/man1/cowthink.1%{?ext_man}

%changelog
