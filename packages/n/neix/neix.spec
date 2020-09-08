#
# spec file for package neix
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


Name:           neix
Version:        0.1.3
Release:        0
Summary:        News Reader for Text Terminals
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://github.com/tomschwarz/neix
Source:         https://github.com/tomschwarz/neix/archive/v%{version}.tar.gz
Patch0:         neix-include.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  ncurses-devel

%description
neix is a RSS/Atom news feed reader.

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make_build

%install
%cmake_install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/neix
%{_mandir}/man1/neix.1%{?ext_man}
%dir %{_datadir}/neix
%{_datadir}/neix/feeds.conf
%{_datadir}/neix/neix.conf

%changelog
