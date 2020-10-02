#
# spec file for package ansifilter
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013 Pascal Bleser.
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


%bcond_without gui
Name:           ansifilter
Version:        2.17
Release:        0
Summary:        ANSI Terminal Escape Code Converter
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            http://www.andre-simon.de/
Source:         http://www.andre-simon.de/zip/ansifilter-%{version}.tar.bz2
Source2:        http://www.andre-simon.de/zip/ansifilter-%{version}.tar.bz2.asc
Source99:       ansifilter.keyring
BuildRequires:  gcc-c++

%description
Ansifilter handles text files containing ANSI terminal escape codes.
The command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

%if %{with gui}
%package gui
Summary:        ANSI Terminal Escape Code Converter - Qt GUI
Group:          Development/Tools/Other
BuildRequires:  libqt5-qtbase-devel
Requires:       %{name} = %{version}

%description gui
This package provides a Qt Graphical User Interface to run %{name}.
%endif

%prep
%setup -q
%if %{with gui}
# Remove generated files which may cause errors when building with
# a version of Qt different from the one used to generate the files.
rm -v src/qt-gui/moc_*.cpp
rm -v src/qt-gui/ui_ansifilter.h
%endif

%build
make \
  CFLAGS="%{optflags} -fPIC" \
  CXXFLAGS="%{optflags} -std=c++11 -fPIC" \
  QMAKE="qmake-qt5" \
  all \
%if %{with gui}
  all-gui \
%endif
  %{?_smp_mflags}

%install
make \
  DESTDIR=%{buildroot} \
  doc_dir="%{_docdir}/%{name}" \
  install \
%if %{with gui}
  install-gui
%endif

rm %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/ChangeLog.adoc
%{_docdir}/%{name}/README.adoc
%{_bindir}/ansifilter
%{_mandir}/man1/ansifilter.1%{ext_man}

%if %{with gui}
%files gui
%{_bindir}/ansifilter-gui
%{_datadir}/applications/ansifilter.desktop
%{_datadir}/pixmaps/ansifilter.xpm
%endif

%changelog
