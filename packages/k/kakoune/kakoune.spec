#
# spec file for package kakoune
#
# Copyright (c) 2020 SUSE LLC
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


Name:           kakoune
Version:        2020.09.01
Release:        0
Summary:        A code editor heavily inspired by Vim
License:        Unlicense
Group:          Productivity/Text/Editors
URL:            https://kakoune.org/
Source:         https://github.com/mawww/kakoune/releases/download/v%{version}/kakoune-%{version}.tar.bz2
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 5.0
BuildRequires:  libboost_regex-devel >= 1.50
BuildRequires:  libxslt-tools
BuildRequires:  ncurses-devel >= 6.0

%description
Kakoune is a code editor heavily inspired by Vim.
It's faster as in less keystrokes, supports multiple selections and uses orthogonal design.

%prep
%setup -q -n %{name}-%{version}/src

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags} -std=gnu++17"

%install
make %{?_smp_mflags} install PREFIX=%{buildroot}%{_prefix}
rm -rf %{buildroot}%{_datadir}/doc
%fdupes %{buildroot}

%check
LANG=en_US.utf8 make %{?_smp_mflags} test

%files
%license ../UNLICENSE
%{_bindir}/kak
%{_datadir}/kak
%{_mandir}/man1/kak.1%{?ext_man}

%changelog
