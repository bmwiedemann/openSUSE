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


# Bundled dependencies from NOTICE:
# - Qt (LGPL v2.1)                           => undbundled
# - QtSingleApplication                      => bundled at some version, using BSD-3-Clause
# - Ace (LGPL v2.1)                          => bundled at version 1.4.5 (see ./src/gwt/src/org/rstudio/studio/client/workbench/views/source/editors/text/ace/ace-uncompressed.js), license is BSD-3-Clause
%global bundled_ace_version           1.4.5
# - Stan Ace Mode (LGPL 2.1)                 => does not appear to exist?
# - Boost                                    => unbundled
# - RapidXml                                 => bundled in ./src/cpp/core/include/core/rapidxml/rapidxml.hpp at version 1.13, license is (BSL-1.0 OR MIT)
%global bundled_rapidxml_version      1.13
# - Google Web Toolkit                       => bundled as gwt-rstudio (version 1.3), new upstream https://github.com/rstudio/gwt, license is Apache-2.0
%global bundled_gwt_rstudio_version   1.3
# - Guice                                    => bundled in ./src/gwt/lib/gin/%%{bundled_gin_version}/, version 3.0, license is Apache-2.0
%global bundled_guice_version         3.0
# - GIN                                      => bundled in ./src/gwt/lib/gin/%%{bundled_gin_version}, license is Apache-2.0
%global bundled_gin_version           2.1.2
# - AOP Alliance                             => bundled in ./src/gwt/lib/gin/2.1.2/aopalliance.jar, version 1.0, license is Public Domain
%global bundled_aopalliance_version   1.0
# - RSA-JS                                   => bundled in ./src/gwt/tools/rsa.js, however this is actually part of the jsbn library (ends up as encrypt.min.js in the rpm), version 1.1, license is MIT
%global bundled_jsbn_version          1.1
# - tree.hh                                  => bundled in ./src/cpp/core/include/core/collection/Tree.hpp, version 2.81, license is GPL-3.0-only
%global bundled_treehh_version        2.81
# - Hunspell (MPL)                           => unbundled
# - Chromium Hunspell Dictionaries (MPL)
# - pdf.js                                   => bundled in ./src/cpp/session/resources/pdfjs/build/pdf.js
%global bundled_pdfjs_version         1.3.158
# - SyncTeX                                  => bundled in ./src/cpp/core/tex/synctex, version 1.17, license is MIT
%global bundled_synctex_version       1.17
# - ZLib                                     => only used on windows, license is ZLIB
# - Sundown                                  => bundled in ./src/cpp/core/markdown/sundown, version 1.16.0, license is ISC
%global bundled_sundown_version       1.16.0
# - highlight.js                             => bundled via src/cpp/tools/sync-highlight, license is BSD-3-Clause
%global bundled_highlightjs_version   c589dcc424c034d1cf63a998ee68225e4915dfca
# - MathJax                                  => unbundled at version 2.7
%global bundled_mathjax_short_version 27
# - reveal.js                                => bundled in ./src/cpp/session/resources/presentation/revealjs/js, version 2.4.0, license is MIT and includes fonts under the OFL-1.1
%global bundled_revealjs_version      2.4.0
# - JSCustomBadge                            => used as inspiration for ./src/cpp/desktop/DockTileView.mm
# - DataTables                               => bundled in ./src/cpp/session/resources/grid/datatables/js, license is MIT
%global bundled_datatables_version    1.10.4
# - jQuery                                   => bundled in ./src/cpp/session/resources/grid/datatables/js/jquery.js, version 3.4.0, license is MIT
%global bundled_jquery_version        3.4.0
# - Catch                                    => used for testing only (which we don't run currently)
# - QUnit                                    => bundled in ./src/gwt/test/acesupport/qunit/, version 1.18.0, license is MIT
%global bundled_quinitjs_version      1.18.0
# - xterm.js                                 => bundled in ./src/gwt/src/org/rstudio/studio/client/workbench/views/terminal/xterm/xterm.js, version 3.14.5, license is MIT
%global bundled_xtermjs_version       3.14.5
# - winpty                                   => windows only
# - websocketpp                              => unbundled
# - gwt-websockets                           => bundled in ./src/gwt/src/com/sksamuel/gwt, version 1.0.4, license is Apache-2.0
%global bundled_gwt_websockets_version 1.0.4
# - ansi-regex                               => some ANSI escape sequences from https://github.com/chalk/ansi-regex are used, license is MIT
# - RapidJSON                                => bundled in ./src/cpp/shared_core/include/shared_core/json/rapidjson, unbundled on Leap 15.2 & Tumbleweed, licensed under the MIT
# - msinttypes                               => part of rapidjson on Windows, licensed under BSD-3-Clause
# - fontawesome                              => per https://github.com/rstudio/rstudio/issues/7115, this is actually iconmoon, bundled in ./src/gwt/www/fonts/icomoon.woff, license is GPL-3.0-or-later or CC-BY-4.0, rstudio includes this under CC-BY-4.0
# - gsl-lite                                 => bundled in ./src/cpp/ext/gsl, version is probably 0.34.0, license is MIT
%global bundled_gsl_lite_version      0.34.0
# - inert-polyfill.js                        => bundled in ./src/gwt/www/js/inert-polyfill.min.js, version 0.2.5, license is Apache-2.0
%global bundled_intert_polyfill_js_version 0.2.5
# - focus-visible.js                         => bundled in ./src/gwt/www/js/focus-visible.*, version 5.0.2, license is W3C-20150513
%global bundled_focus_visible_js_version 5.0.2
# - fast-text-encoding                       => bundled in ./src/gwt/www/js/text.min.js, version 1.0.2, license is Apache-2.0
%global bundled_fast_text_encoding_version 1.0.2

# missing from NOTICE:
# - Google Closure Compiler                  => bundled in ./src/gwt/tools/compiler/ but AFAIK only used for building, version is "compiler-latest.zip as of July 9, 2019", license is Apache-2.0 with bundled dependencies under (NPL-1.1 AND (MPL-1.1 OR GPL-2.0-or-later)) AND MIT AND CPL-1.0 AND BSD-3-Clause AND Apache-2.0:

# override upstream's choice for the boost version on Leap 15.2,
# but not on Tumbleweed
%if 0%{?sle_version} == 150200
%global rstudio_boost_requested_version 1.66
%endif
%define boost_version %{?rstudio_boost_requested_version}%{?!rstudio_boost_requested_version:1.69}

%global rstudio_version_major 1
%global rstudio_version_minor 3
%global rstudio_version_patch 1073
# commit of the tag belonging to %%{version}
%global rstudio_git_revision_hash 718e6d75b094658d999495534badf55fb2ce0047
Name:           rstudio
Version:        %{rstudio_version_major}.%{rstudio_version_minor}.%{rstudio_version_patch}
Release:        0
Summary:        RStudio base package
# AGPLv3:             RStudio, icomoon glyphs
# Apache-2.0:         gwt, gwt-websockets, gin, guice, pdf.js, fast-text-encoding, inert-polyfill.js
# MIT:                rsa.js/jsbn, synctex, datatables, jquery, reveal.js, jsbn, qunit.js, xterm.js, guidelines-support-library-lite, rapidjson
# BSD-3-Clause        qtsingleapplication, ace, highlight.js, msinttypes
# W3C (2015):         focus-visible.js
# BSL or MIT:         rapidxml
# Public Domain:      AOP Alliance
# GPL-3.0-only:       tree.hh
# ISC:                sundown
# dictionaries: see below
License:        AGPL-3.0-only AND Apache-2.0 AND MPL-1.1 AND LGPL-2.1-or-later AND GPL-2.0-only AND MIT AND W3C-20150513 AND BSD-3-Clause AND (BSL-1.0 OR MIT) AND GPL-3.0-only AND ISC AND OFL-1.1 AND Zlib AND NPL-1.1 AND CC-BY-4.0
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
Source4:        %{name}-server-user.conf
Source99:       %{name}-rpmlintrc
Patch0:         0001-Unbundle-mathjax-and-pandoc.patch
# shorten the installation time a bit by not installing mathjax
Patch1:         0002-Don-t-install-pandoc-and-mathjax.patch
Patch2:         0003-Fix-rstudio-exec-path.patch
# https://github.com/rstudio/rstudio/pull/7011
Patch3:         0004-add-support-for-boost-1.73.patch
Patch4:         0005-Add-additional-includes-for-aarch64.patch
# Make compatible with hunspell 1.4.0 or later, use system hunspell.
Patch5:         0006-Use-system-hunspell.patch
# Make sure we find the right libclang.so and builtin headers, make compatible with newer versions.
Patch6:         0007-Fix-libclang-usage.patch
# Leap 15.2 only patch
Patch7:         0008-Add-support-for-RapidJSON-1.1.0-in-Leap-15.2.patch

BuildRequires:  Mesa-devel
BuildRequires:  R-core-devel
BuildRequires:  ant
BuildRequires:  clang-devel
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
BuildRequires:  libboost_atomic-devel          >= %{boost_version}
BuildRequires:  libboost_chrono-devel          >= %{boost_version}
BuildRequires:  libboost_date_time-devel       >= %{boost_version}
BuildRequires:  libboost_filesystem-devel      >= %{boost_version}
BuildRequires:  libboost_headers-devel         >= %{boost_version}
BuildRequires:  libboost_iostreams-devel       >= %{boost_version}
BuildRequires:  libboost_program_options-devel >= %{boost_version}
BuildRequires:  libboost_random-devel          >= %{boost_version}
BuildRequires:  libboost_regex-devel           >= %{boost_version}
BuildRequires:  libboost_system-devel          >= %{boost_version}
BuildRequires:  libboost_thread-devel          >= %{boost_version}
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  make
BuildRequires:  mathjax
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
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(websocketpp)
BuildRequires:  pkgconfig(zlib)
Requires:       R-base
Requires:       R-core-libs
Recommends:     ghc-pandoc-citeproc
Recommends:     libclang%{_llvm_sonum}
Recommends:     mathjax
Recommends:     pandoc
Recommends:     git
Recommends:     gcc
Recommends:     gcc-c++
Suggests:       rstudio-desktop
Suggests:       rstudio-server
Provides:       bundled(ace.js) = %{bundled_ace_version}
Provides:       bundled(aopalliance) = %{bundled_aopalliance_version}
Provides:       bundled(datatables) = %{bundled_datatables_version}
Provides:       bundled(fast-text-encoding) = %{bundled_fast_text_encoding_version}
Provides:       bundled(focus-visible.js) = %{bundled_focus_visible_js_version}
Provides:       bundled(fontawesome)
Provides:       bundled(gin) = %{bundled_gin_version}
Provides:       bundled(gsl-lite) = %{bundled_gsl_lite_version}
Provides:       bundled(guice) = %{bundled_guice_version}
Provides:       bundled(gwt-rstudio) = %{bundled_gwt_rstudio_version}
Provides:       bundled(gwt-websockets) = %{bundled_gwt_websockets_version}
Provides:       bundled(highlight.js) = %{bundled_highlightjs_version}
Provides:       bundled(inert-polyfill.js) = %{bundled_intert_polyfill_js_version}
Provides:       bundled(jquery.js) = %{bundled_jquery_version}
Provides:       bundled(jsbn) = %{bundled_jsbn_version}
Provides:       bundled(pdf.js) = %{bundled_pdfjs_version}
Provides:       bundled(qtsingleapplication)
Provides:       bundled(quinit.js) = %{bundled_quinitjs_version}
Provides:       bundled(rapidxml) = %{bundled_rapidxml_version}
Provides:       bundled(reveal.js) = %{bundled_revealjs_version}
Provides:       bundled(sundown) = %{bundled_sundown_version}
Provides:       bundled(tree.hh) = %{bundled_treehh_version}
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
%if 0%{?sle_version} == 150200
%autosetup -p1
%else
%autosetup -N
%autopatch -p1 -M 6
%endif

# use system libraries when available
rm -r \
    src/cpp/core/include/core/libclang/clang-c/ \
    src/cpp/core/spelling/hunspell/ \
    src/cpp/ext/websocketpp \
    src/cpp/shared_core/include/shared_core/json/rapidjson/
find src/cpp/core/zlib -type f -not -name '*.cpp' -delete

ln -sf %{_includedir}/websocketpp src/cpp/ext/websocketpp
ln -sf %{_includedir}/rapidjson src/cpp/shared_core/include/shared_core/json/rapidjson

# unpack common-dictionaries
mkdir -p dependencies/common/dictionaries
unzip -d dependencies/common/dictionaries %{SOURCE1}

# don't include gwt_build in ALL to avoid recompilation, but then we must build
# it manually
sed -i 's@gwt_build ALL@gwt_build@g' src/gwt/CMakeLists.txt

# The unversioned libclang.so is only part of clang-devel, so we use the versioned so instead.
sed -i 's#LIBCLANG_PLACEHOLDER#%{_libdir}/libclang.so.%{_llvm_sonum}#' src/cpp/core/libclang/LibClang.cpp

%build
%sysusers_generate_pre %{SOURCE4} %{name}-server

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
    %{?rstudio_boost_requested_version:-DRSTUDIO_BOOST_REQUESTED_VERSION=%{rstudio_boost_requested_version}} \
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
%license COPYING NOTICE
%doc README.md
%{_libexecdir}/rstudio
%exclude %{_libexecdir}/rstudio/bin/rserver
%exclude %{_libexecdir}/rstudio/bin/rserver-pam
%exclude %{_libexecdir}/rstudio/bin/%{name}

%files desktop
%{_bindir}/%{name}
%{_libexecdir}/rstudio/bin/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%files server
%{_bindir}/rserver
%{_bindir}/rserver-pam
%{_libexecdir}/rstudio/bin/rserver
%{_libexecdir}/rstudio/bin/rserver-pam
%dir %{_localstatedir}/log/%{name}-server
%dir %{_localstatedir}/lib/%{name}-server
%{_unitdir}/%{rserver_service}
%{_sbindir}/rc%{name}-server
%config %{_sysconfdir}/pam.d/%{name}
%{_sysusersdir}/%{name}-server-user.conf

%changelog
