#
# spec file for package wxMaxima
#
# Copyright (c) 2024 SUSE LLC
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


# Tests fail on chroot, but work fine locally
# https://github.com/wxMaxima-developers/wxmaxima/issues/1699
%bcond_with tests
%define X_display ":98"
%define __builder ninja
%define tarname wxmaxima
Name:           wxMaxima
Version:        24.05.0
Release:        0
Summary:        Graphical User Interface for the maxima Computer Algebra System
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://wxmaxima-developers.github.io/wxmaxima/
Source0:        https://github.com/wxmaxima-developers/wxmaxima/archive/Version-%{version}.tar.gz#/%{tarname}-Version-%{version}.tar.gz
BuildRequires:  cmake >= 3.10
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  hicolor-icon-theme
BuildRequires:  maxima >= 5.30.0
BuildRequires:  maxima-exec-sbcl
BuildRequires:  ninja
BuildRequires:  po4a
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel >= 3.1.5
# gnuplot is needed for plotting
Requires:       gnuplot
Requires:       maxima >= 5.30.0
Recommends:     %{name}-lang
# SECTION For tests
%if %{with tests}
BuildRequires:  appstream-glib
BuildRequires:  xvfb-run
%endif
# /SECTION
ExcludeArch:    ppc64 ppc64le

%lang_package

%description
wxMaxima is a GUI for the computer algebra system maxima
based on wxWidgets.

%prep
%autosetup -p1 -n %{tarname}-Version-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

# Manually install mimetype icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes
install -m0644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes data/text-x-wx*.svg

# Remove unnecessary icons out of pixmaps
rm %{buildroot}%{_datadir}/pixmaps/*

# Remove non-standard hicolor icon sizes
for sz in 150 310 44 42 8
do
  rm -fr %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}
done

# Remove license installed by make install, we include them by using %%license
rm %{buildroot}%{_datadir}/doc/%{tarname}/{COPYING,GPL.txt}

%suse_update_desktop_file io.github.wxmaxima_developers.wxMaxima
%fdupes %{buildroot}%{_prefix}
%find_lang %{name} %{?no_lang_C}

%if %{with tests}
%check
# Needed, otherwise maxima tries to write to a dir without permissions
export MAXIMA_USERDIR=./
pushd ./%{__builddir}
xvfb-run ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
popd
%endif

%files
%license COPYING GPL.txt
%doc %{_datadir}/doc/%{tarname}/
%{_bindir}/*
%{_datadir}/wxMaxima/
%{_datadir}/icons/hicolor/*/apps/io.github.wxmaxima_developers.wxMaxima.*
%{_datadir}/icons/hicolor/*/mimetypes/text-x-wx*.svg
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/wxmaxima
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/wxmaxima*%{ext_man}
%{_mandir}/*/man1/wxmaxima*%{ext_man}
%{_datadir}/mime/packages/*.xml

%files lang -f %{name}.lang

%changelog
