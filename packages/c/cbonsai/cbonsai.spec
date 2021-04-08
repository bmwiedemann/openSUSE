#
# spec file for package cbonsai
#
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


Name:           cbonsai
Version:        1.0.4
Release:        0
Summary:        A bonsai tree generator for your terminal
License:        GPL-3.0-or-later
Group:          Amusements/Toys/Other
URL:            https://gitlab.com/jallbrit/cbonsai
Source:         https://gitlab.com/jallbrit/cbonsai/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  help2man
BuildRequires:  ncurses-devel

%description
A beautifully random bonsai tree generator. It intelligently
creates, colors, and positions a bonsai tree, and is entirely
configurable via CLI options.

%prep
%setup -q -n %{name}-v%{version}

%build
export CFLAGS="%{optflags} $(pkg-config --cflags ncurses)"
%make_build

%install
install -D -m 0755 cbonsai %{buildroot}%{_bindir}/cbonsai
install -d %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} --no-discard-stderr --no-info > %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/cbonsai
%{_mandir}/man1/cbonsai.1%{?ext_man}

%changelog
