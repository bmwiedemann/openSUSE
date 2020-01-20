#
# spec file for package rstudio
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


%global bundled_gwt_version 2.8.2
%global bundled_gin_version 2.1.2

# !no longer bundled!
# but upstream expects them in specific locations, so we keep these macros around
%global bundled_mathjax_version 2.6.1
%global bundled_mathjax_short_version 26

%global rstudio_version_major 1
%global rstudio_version_minor 2
%global rstudio_version_patch 5033
# commit of the tag belonging to %%{version}
%global rstudio_git_revision_hash 330255ddec489e7a147ace3e8a9a3e4157d8d5ad

Name:           rstudio
Version:        %{rstudio_version_major}.%{rstudio_version_minor}.%{rstudio_version_patch}
Release:        0
Summary:        R-Studio Desktop
# R-Studio: AGPL 3.0
# GWT: Apache License 2.0
# gin: Apache License 2.0
# dictionaries: see below
License:        AGPL-3.0-only AND Apache-2.0 AND MPL-1.1 AND LGPL-2.1-or-later AND GPL-2.0-only
URL:            https://github.com/%{name}/
Source0:        %{URL}/%{name}/archive/v%{version}.tar.gz

# these appear to have been taken from Chromium's source code, see:
# https://raw.githubusercontent.com/rstudio/rstudio/master/dependencies/tools/sync-hunspell-dictionaries
# upstream source:
# https://src.chromium.org/viewvc/chrome/trunk/deps/third_party/hunspell_dictionaries
# downstream bundle was last touched around 2012
# Upstream claims that the only licenses are:
# GPL 2.0, LGPL 2.1 (or later), MPL 1.1 and Apache 2.0
Source1:        https://s3.amazonaws.com/%{name}-dictionaries/core-dictionaries.zip
Source2:        https://s3.amazonaws.com/%{name}-buildtools/gwt-%{bundled_gwt_version}.zip
Source3:        https://s3.amazonaws.com/%{name}-buildtools/gin-%{bundled_gin_version}.zip
Source99:       %{name}-rpmlintrc

Patch0:         0003-Remove-boost-signals-from-the-required-Boost-librari.patch
Patch1:         0005-Use-find_program-to-find-qmake-if-it-is-not-in-the-p.patch
Patch2:         0002-Bump-bundled-gwt-version.patch
# Tumbleweed and Leap 15.2 only patch
Patch3:         0001-First-pass-at-Boost-1.70-support.patch
# main ubundling patch
Patch4:         0004-Unbundle-mathjax-and-pandoc.patch
# patches for Leap 15.1 & 15.0
Patch5:         0006-Use-std-thread-instead-of-QThread-for-Qt-5.10-suppor.patch
Patch6:         0007-Add-explicit-include-mutex-for-gcc-7-to-DesktopWebpa.patch
Patch7:         0008-Remove-PauseChanged-related-handler-from-DownloadHel.patch
# shorten the installation time a bit by not installing mathjax
Patch8:         0009-Don-t-install-pandoc-and-mathjax.patch

BuildRequires:  Mesa-devel
BuildRequires:  R-core-devel
BuildRequires:  ant
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  glibc-devel
BuildRequires:  java
BuildRequires:  memory-constraints
# for dir ownership of /usr/share/icons/hicolor/*
BuildRequires:  hicolor-icon-theme

BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_random-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)

BuildRequires:  ghc-pandoc-citeproc
BuildRequires:  make
BuildRequires:  mathjax
BuildRequires:  pam-devel
BuildRequires:  pandoc
BuildRequires:  unzip
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(zlib)

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)

Provides:       bundled(gin) = %{bundled_gin_version}
Provides:       bundled(gwt) = %{bundled_gwt_version}

Requires:       R-base
Requires:       R-core-libs
Requires:       ghc-pandoc-citeproc
Requires:       mathjax
Requires:       pandoc

%description
RStudio is a set of integrated tools designed to help you be more productive
with R.

It includes a console, syntax-highlighting editor that supports direct code
execution, and a variety of robust tools for plotting, viewing history,
debugging and managing your workspace.

%prep
%autosetup -N
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch8 -p1

# TW & Leap 15.2 specific patches
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150200
%patch3 -p1
# Leap 15.1 & 15.0 patches:
%else
%patch5 -p1
%patch6 -p1
%patch7 -p1
%endif

# unpack common-dictionaries
mkdir -p dependencies/common/dictionaries
unzip -d dependencies/common/dictionaries %{SOURCE1}
# unpack gwt
mkdir -p src/gwt/lib/gwt
unzip -d src/gwt/lib/gwt/ %{SOURCE2}
mv src/gwt/lib/gwt/gwt-%{bundled_gwt_version} src/gwt/lib/gwt/%{bundled_gwt_version}
# unpack gin
mkdir -p src/gwt/lib/gin/%{bundled_gin_version}
unzip -d src/gwt/lib/gin/%{bundled_gin_version} %{SOURCE3}

%build
%limit_build -m 1500
export RSTUDIO_VERSION_MAJOR=%{rstudio_version_major}
export RSTUDIO_VERSION_MINOR=%{rstudio_version_minor}
export RSTUDIO_VERSION_PATCH=%{rstudio_version_patch}
export RSTUDIO_GIT_REVISION_HASH=%{rstudio_git_revision_hash}
export GIT_COMMIT=%{rstudio_git_revision_hash}
%cmake -DRSTUDIO_TARGET=Desktop -DCMAKE_BUILD_TYPE=Release -DRSTUDIO_BOOST_SIGNALS_VERSION=2 -DCMAKE_INSTALL_PREFIX=%{_libexecdir}/rstudio

# dirty hack:
# gwtc compilation runs via make -> ant -> java and something in that chain
# starts a lot of threads that can OOM the worker. Unfortunately, the
# parallelism cannot be turned off...
#
# So we just build everything that doesn't require gwt first and then start a
# single make task (in %%install) and cross our fingers hoping that gwt itself
# is not enough to OOM the machine. We don't add an addional make call here,
# because the gwt compilation is *always* re-run on make (i.e. it will run again
# in %%cmake_install), so adding that would be a waste of resources.
%make_build rstudio rsession rpostback rstudio-core rstudio-monitor rstudio-r rstudio-session-workers diagnostics

%install
# fun fact: this recompiles gwt…
%cmake_install

install -d -m 0755 %{buildroot}%{_bindir}
ln -s %{_libexecdir}/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}

# symlink the location where the bundled mathjax should be to
# /usr/share/javascript/mathjax as mathjax-%%{bundled_mathjax_short_version}
ln -sf %{_datadir}/javascript/mathjax \
    %{buildroot}%{_libexecdir}/%{name}/resources/mathjax-%{bundled_mathjax_short_version}

# redo the same for pandoc & pandoc-citeproc
for pd in pandoc pandoc-citeproc; do
    ln -sf %{_bindir}/${pd} %{buildroot}%{_libexecdir}/%{name}/bin/${pd}
done

# cleanup
find %{buildroot}%{_libexecdir}/%{name} -name .gitignore -delete
find %{buildroot}%{_libexecdir}/%{name} -name .Rbuildignore -delete
rm %{buildroot}%{_libexecdir}/%{name}/{INSTALL,COPYING,NOTICE,README.md,SOURCE}

%fdupes -s %{buildroot}%{_libexecdir}/%{name}
%fdupes -s %{buildroot}%{_datadir}

# fix shebangs from /usr/bin/env bash to
BASH_PATH=$(which bash)
for f in postback/askpass-passthrough postback/rpostback-askpass postback/rpostback-editfile postback/rpostback-gitssh postback/rpostback-pdfviewer r-ldpath rstudio-backtrace.sh; do
    full_path=%{buildroot}%{_libexecdir}/%{name}/bin/$f
    sed -i.orig 's:^#\!/usr/bin/env\s\+bash\s\?$:#\!'"${BASH_PATH}"':' $full_path
    touch -r $full_path.orig $full_path
    rm $full_path.orig
done

%files
%license COPYING
%doc NOTICE README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
