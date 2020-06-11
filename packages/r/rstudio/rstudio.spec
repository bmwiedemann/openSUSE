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
%global rstudio_version_patch 5042
# commit of the tag belonging to %%{version}
%global rstudio_git_revision_hash e4a1c219cbf6c10d9aec41461d80171ab3009bef
Name:           rstudio
Version:        %{rstudio_version_major}.%{rstudio_version_minor}.%{rstudio_version_patch}
Release:        0
Summary:        RStudio base package
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
Source4:        %{name}-server-user.conf
Source99:       %{name}-rpmlintrc
Patch0:         0003-Remove-boost-signals-from-the-required-Boost-librari.patch
Patch1:         0002-Bump-bundled-gwt-version.patch
# Tumbleweed and Leap 15.2 only patch
Patch2:         0001-First-pass-at-Boost-1.70-support.patch
# main ubundling patch
Patch3:         0004-Unbundle-mathjax-and-pandoc.patch
# patches for Leap 15.1 & 15.0
Patch4:         0005-Use-std-thread-instead-of-QThread-for-Qt-5.10-suppor.patch
Patch5:         0006-Add-explicit-include-mutex-for-gcc-7-to-DesktopWebpa.patch
Patch6:         0007-Remove-PauseChanged-related-handler-from-DownloadHel.patch
# shorten the installation time a bit by not installing mathjax
Patch7:         0008-Don-t-install-pandoc-and-mathjax.patch
Patch8:         0009-Fix-rstudio-exec-path.patch
Patch9:         0010-fix-STL-access-undefined-behaviour.patch
Patch10:        0011-R_Slave-R_NoEcho-for-non-Windows.patch
BuildRequires:  Mesa-devel
BuildRequires:  R-core-devel
BuildRequires:  ant
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  ghc-pandoc-citeproc
BuildRequires:  glibc-devel
# for dir ownership of /usr/share/icons/hicolor/*
BuildRequires:  hicolor-icon-theme
BuildRequires:  java
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
BuildRequires:  make
BuildRequires:  mathjax
BuildRequires:  memory-constraints
BuildRequires:  pam-devel
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  unzip
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
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
Requires:       R-base
Requires:       R-core-libs
Requires:       ghc-pandoc-citeproc
Requires:       mathjax
Requires:       pandoc
Recommends:     git
Suggests:       rstudio-desktop
Suggests:       rstudio-server
Provides:       bundled(gin) = %{bundled_gin_version}
Provides:       bundled(gwt) = %{bundled_gwt_version}
%{?systemd_requires}

%description
This package provides the common files of RStudio Desktop and RStudio server.

%package        desktop
Summary:        Integrated development environment for the R programming language
Requires:       %{name} = %{version}-%{release}

%description    desktop
RStudio is an integrated development environment (IDE) for the R programming
language. Some of its features include:

- Customizable workbench with all of the tools required to work with R in one
  place (console, source, plots, workspace, help, history, etc.).
- Syntax highlighting editor with code completion.
- Execute code directly from the source editor (line, selection, or file).
- Full support for authoring Sweave and TeX documents.

%package        server
Summary:        Access RStudio via a web browser running on a remote server
Requires:       %{name} = %{version}-%{release}
%sysusers_requires

%description    server
RStudio Server enables you to provide a browser-based interface (the RStudio
IDE) to a version of R running on a remote Linux server. Deploying R and RStudio
on a server has a number of benefits, including:

- The ability to access your R workspace from any computer in any location
- Easy sharing of code, data, and other files with colleagues
- Allowing multiple users to share access to the more powerful compute resources
  (memory, processors, etc.) available on a well-equipped server
- Centralized installation and configuration of R, R packages, TeX, and other
  supporting libraries

%prep
%autosetup -N
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# TW & Leap 15.2 specific patches
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150200
%patch2 -p1
# Leap 15.1 & 15.0 patches:
%else
%patch4 -p1
%patch5 -p1
%patch6 -p1
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

# don't include gwt_build in ALL to avoid recompilation, but then we must build
# it manually
sed -i 's@gwt_build ALL@gwt_build@g' src/gwt/CMakeLists.txt

%build
%sysusers_generate_pre %{SOURCE4} %{name}-server

%limit_build -m 1500
export RSTUDIO_VERSION_MAJOR=%{rstudio_version_major}
export RSTUDIO_VERSION_MINOR=%{rstudio_version_minor}
export RSTUDIO_VERSION_PATCH=%{rstudio_version_patch}
export RSTUDIO_GIT_REVISION_HASH=%{rstudio_git_revision_hash}
export GIT_COMMIT=%{rstudio_git_revision_hash}
%cmake -DRSTUDIO_TARGET=Desktop -DRSTUDIO_SERVER=TRUE -DCMAKE_BUILD_TYPE=Release    \
    -DCMAKE_INSTALL_PREFIX=%{_libexecdir}/%{name}                                   \
    -DRSTUDIO_USE_SYSTEM_BOOST=TRUE                                                 \
    -DRSTUDIO_BOOST_SIGNALS_VERSION=2                                               \
    -DBOOST_ROOT=%{_prefix} -DBOOST_LIBRARYDIR=%{_lib}                              \
    -DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt5

%make_build
%make_build gwt_build

%install
%cmake_install

# sysuser for rstudio-server
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/

# create /usr/bin/rstudio-desktop, /usr/bin/rserver, /usr/bin/rserver-pam
install -d -m 0755 %{buildroot}%{_bindir}
for binary in %{name} rserver rserver-pam; do
    ln -s %{_libexecdir}/%{name}/bin/${binary} %{buildroot}%{_bindir}/${binary}
done

# create required directories for rstudio-server (according to INSTALL):
# * do not create /var/lock/rstudio-server as that is only for legacy init
#   scripts
# * do not create /var/run, that one is owned by the filesystem package and
#   doesn't need to be Require'd.
#   Also, the INSTALL appears to be wrong, it's only creating a
#   rstudio-server.pid file there.
# FIXME: await confirm from https://github.com/rstudio/rstudio/issues/6112
for dir in log lib; do
    mkdir -p %{buildroot}%{_localstatedir}/${dir}/%{name}-server
done

# install the systemd service file
%define rserver_service %{name}-server.service
install -D -m 0644 %{buildroot}%{_libexecdir}/%{name}/extras/systemd/%{name}-server.redhat.service \
    %{buildroot}%{_unitdir}/%{rserver_service}
# create link /usr/sbin/rcrstudio-server -> /usr/sbin/service
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-server

# install the PAM module
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m 0644 %{buildroot}%{_libexecdir}/%{name}/extras/pam/%{name} \
    %{buildroot}%{_sysconfdir}/pam.d/%{name}

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
# don't need the extras dir, as we took everything from that already
rm -rf %{buildroot}%{_libexecdir}/%{name}/extras

%fdupes -s %{buildroot}%{_libexecdir}/%{name}
%fdupes -s %{buildroot}%{_datadir}

# fix shebangs from /usr/bin/env bash to
BASH_PATH=$(which bash)
for f in postback/askpass-passthrough postback/rpostback-askpass postback/rpostback-editfile postback/rpostback-gitssh postback/rpostback-pdfviewer r-ldpath rstudio-backtrace.sh; do
    full_path=%{buildroot}%{_libexecdir}/%{name}/bin/$f
    sed -i.orig 's:^#\!%{_bindir}/env\s\+bash\s\?$:#\!'"${BASH_PATH}"':' $full_path
    touch -r $full_path.orig $full_path
    rm $full_path.orig
done

%pre server -f rstudio-server.pre
%service_add_pre %{rserver_service}

%post server
%service_add_post %{rserver_service}

%preun server
%service_del_preun %{rserver_service}

%postun server
%service_del_postun %{rserver_service}

%files
%license COPYING
%doc NOTICE README.md
%{_libexecdir}/rstudio

%files desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%files server
%{_bindir}/rserver
%{_bindir}/rserver-pam
%dir %{_localstatedir}/log/%{name}-server
%dir %{_localstatedir}/lib/%{name}-server
%{_unitdir}/%{rserver_service}
%{_sbindir}/rc%{name}-server
%config %{_sysconfdir}/pam.d/%{name}
%{_sysusersdir}/%{name}-server-user.conf

%changelog
