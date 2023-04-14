#
# spec file for package sdcv
#
# Copyright (c) 2022 SUSE LLC
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


Name:           sdcv
Version:        0.5.4
Release:        0
Summary:        Console version of the Stardict program
License:        GPL-2.0-only
Group:          Productivity/Office/Dictionary
URL:            https://dushistov.github.io/sdcv/
Source:         https://github.com/Dushistov/sdcv/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib2-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel

%description
Console version of the Stardict program.
It can employ all the dictionary files that belong to StarDict.
The word sdcv stands for StarDict under Console Version.

%prep
%setup -q

%build
%cmake
%make_build
# force recreation of the locale files
%make_build lang

%install
%cmake_install
%find_lang %{name} --with-man
%if 0%{?suse_version} < 1550
# Ukrainian translations used to be absent from filesystem package
echo '%%dir %{_mandir}/uk/' >> %{name}.lang
echo '%%dir %{_mandir}/uk/man1/' >> %{name}.lang
%endif

%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%license LICENSE
%doc README.org NEWS AUTHORS

%changelog
