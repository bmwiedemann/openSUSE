#
# spec file for package ansilove-term
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           ansilove-term
Version:        0.0.0+git.20190908
Release:        0
Summary:        CLI tool to render text-mode art files as PNG files
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            https://www.ansilove.org
#Git-Clone:     https://github.com/ansilove/ansilove-term.git
Source:         %{name}-%{version}.tar.xz
Patch0:         ansilove-term-use-gcc.patch
BuildRequires:  gcc-c++

%description
Ansilove-Term is a command line tool to render text-mode art files as
PNG files, as well as displaying in several different mediums.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags} -Wno-return-type"
make %{?_smp_mflags}

%install
install -D -m0755 ans %{buildroot}/%{_bindir}/ans

%files
%license LICENSE.txt
%doc Readme.md
%{_bindir}/ans

%changelog
