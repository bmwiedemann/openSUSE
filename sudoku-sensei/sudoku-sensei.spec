#
# spec file for package sudoku-sensei
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


%define oversion 02-00
%define oname SudokuSensei
Name:           sudoku-sensei
Version:        02_00
Release:        0
Summary:        Enjoy playing with Sudoku boards designed by yourself
License:        GPL-2.0-or-later
Group:          Amusements/Games/Logic
URL:            http://sudoku-sensei.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-for-linux/Source%20and%20exe%20files%20for%20linux%2C%20ver.%202.00/%{name}-src-%{oversion}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.png
Source3:        %{name}.desktop
# PATCH-FIX-OPENSUSE 0001-Basic-port-to-Qt5.patch
Patch0:         0001-Basic-port-to-Qt5.patch
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif

%description
The engine solves sudokus by applying complex logical rules a few times,
instead of applying simpler rules (like guessing and backtracking)
many many times. These complex logical rules are exactly the same ones
that people use with paper and pen.

%prep
%setup -q -n %{oname}Sources
%patch0 -p1

# Convert to unix line end
find -name "*.txt" -print0 -or -name "*.h" -print0 -or -name "*.cpp" -print0 -or -name "*.html" -print0 | xargs -0 dos2unix

%build
qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true";
make %{?_smp_mflags}

%install
# install wrapper
install -Dm 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# install executable
install -Dm 0755 %{oname} %{buildroot}%{_libexecdir}/%{name}/%{oname}

# install directories
mkdir -p %{buildroot}%{_libexecdir}/%{name}/{board,doc,images,language,saves,system}
for d in board doc images language saves system ; do
    cp -a $d %{buildroot}%{_libexecdir}/%{name}
done

# install files
for f in %{oname}.rc license.txt ; do
    install -Dm 0644 "$f" %{buildroot}%{_libexecdir}/%{name}
done

# install icon
install -Dm 0644 %{SOURCE2} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{SOURCE3} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%license license.txt
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_libexecdir}/%{name}

%changelog
