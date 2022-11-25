#
# spec file for package wxMaxima
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


# Tests fail on chroot, but work fine locally
# https://github.com/wxMaxima-developers/wxmaxima/issues/1699
%bcond_with tests
%define X_display ":98"
%define __builder ninja
%define tarname wxmaxima
Name:           wxMaxima
Version:        22.09.0
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
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel >= 3.2
# gnuplot is needed for plotting
Requires:       gnuplot
Requires:       maxima >= 5.30.0
Recommends:     %{name}-lang
# SECTION For tests
%if %{with tests}
BuildRequires:  appstream-glib
%if 0%{?suse_version} >= 1550
BuildRequires:  xorg-x11-server-Xvfb
%else
BuildRequires:  xorg-x11-server
%endif
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
# INSTALL HI-RES ICONS GENERATED OUT OF UPSTREAM SVG ICON
for i in 24 32 48 64 128 256 512
do
  rsvg-convert -w ${i} data/io.github.wxmaxima_developers.wxMaxima.svg -o wxmaxima-${i}.png
  install -D -m 0644 wxmaxima-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/io.github.wxmaxima_developers.wxMaxima.png
  rsvg-convert -w ${i} data/text-x-wxmathml.svg -o text-x-wxmathml-${i}.png
  install -D -m 0644 text-x-wxmathml-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/text-x-wxmathml.png
  rsvg-convert -w ${i} data/text-x-wxmaxima-batch.svg -o text-x-wxmaxima-batch-${i}.png
  install -D -m 0644 text-x-wxmaxima-batch-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/text-x-wxmaxima-batch.png
done
install -D -m 0644 data/io.github.wxmaxima_developers.wxMaxima.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/io.github.wxmaxima_developers.wxMaxima.svg
install -D -m 0644 data/text-x-wxmathml.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-wxmathml.svg
install -D -m 0644 data/text-x-wxmaxima-batch.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-wxmaxima-batch.svg

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes

# REMOVE UNNECESSARY ICONS OUT OF PIXMAPS
rm %{buildroot}%{_datadir}/pixmaps/*

# Remove license installed by make install, we include them by using %%license
rm %{buildroot}%{_datadir}/doc/%{tarname}/{COPYING,GPL.txt}

%suse_update_desktop_file io.github.wxmaxima_developers.wxMaxima
%fdupes %{buildroot}%{_prefix}
%find_lang %{name} %{?no_lang_C}

%if %{with tests}
%check
export DISPLAY="%{X_display}"
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 5

# Needed, otherwise maxima tries to write to a dir without permissions
export MAXIMA_USERDIR=./
%ctest

%endif

%post
%install_info --info-dir=%{_infodir} %{_infodir}/wxmaxima.info%{ext_info}

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/wxmaxima.info%{ext_info}

%files
%license COPYING GPL.txt
%doc %{_datadir}/doc/%{tarname}/
%{_bindir}/*
%{_datadir}/wxMaxima/
%{_datadir}/icons/hicolor/*/apps/io.github.wxmaxima_developers.wxMaxima.*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/wxmaxima
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/wxmaxima*%{ext_man}
%{_mandir}/*/man1/wxmaxima*%{ext_man}
%{_datadir}/mime/packages/*.xml

%files lang -f %{name}.lang

%changelog
