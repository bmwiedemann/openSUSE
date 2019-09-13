#
# spec file for package sdcv
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sdcv
Version:        0.5.2
Release:        0
Summary:        Console version of the Stardict program
License:        GPL-2.0
Group:          Productivity/Office/Dictionary
Url:            http://dushistov.github.io/sdcv/
Source:         https://github.com/Dushistov/sdcv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib2-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Console version of the Stardict program.
It can employ all the dictionary files that belong to StarDict.
The word sdcv stands for StarDict under Console Version.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}
# force recreation of the locale files
make %{?_smp_mflags} lang

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%dir %{_mandir}/uk/
%dir %{_mandir}/uk/man1/
%{_mandir}/uk/man1/%{name}.1.gz
%doc README.org NEWS LICENSE AUTHORS

%changelog
