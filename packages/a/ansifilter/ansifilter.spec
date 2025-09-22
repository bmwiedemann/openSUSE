#
# spec file for package ansifilter
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 Pascal Bleser.
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           ansifilter
Version:        2.22
Release:        0
Summary:        ANSI Terminal Escape Code Converter
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            http://www.andre-simon.de/
Source:         http://www.andre-simon.de/zip/ansifilter-%{version}.tar.bz2
Source2:        http://www.andre-simon.de/zip/ansifilter-%{version}.tar.bz2.asc
Source99:       ansifilter.keyring
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.30
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
# these were split until 2.21
Obsoletes:      %{name}-bash-completion < %{version}
Provides:       %{name}-bash-completion = %{version}
Obsoletes:      %{name}-fish-completion < %{version}
Provides:       %{name}-fish-completion = %{version}
Obsoletes:      %{name}-zsh-completion < %{version}
Provides:       %{name}-zsh-completion = %{version}

%description
Ansifilter handles text files containing ANSI terminal escape codes.  The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

%package gui
Summary:        ANSI Terminal Escape Code Converter - Qt GUI
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description gui
This package provides a Qt Graphical User Interface to run %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# installed via macro
rm %{buildroot}%{_datadir}/doc/COPYING
# not needed
rm %{buildroot}%{_datadir}/doc/INSTALL
# should be patched up in CMakeLists but I'm lazy right now
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/*.adoc %{buildroot}%{_docdir}/%{name}

%check
%ctest

%files
%license COPYING
%{_bindir}/ansifilter
%{_docdir}/%{name}
%{_mandir}/man1/ansifilter.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%files gui
%license COPYING
%{_bindir}/ansifilter-gui
%{_datadir}/applications/ansifilter.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/ansifilter.xpm

%changelog
