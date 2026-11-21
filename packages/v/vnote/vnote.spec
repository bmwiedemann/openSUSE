#
# spec file for package vnote
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           vnote
Version:        4.14.4
Release:        0
Summary:        A Vim-inspired note-taking application, especially for Markdown
License:        LGPL-3.0-only AND MIT AND BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND ISC AND MPL-1.1 AND MPL-2.0 AND LGPL-2.1-or-later AND GPL-2.0-only WITH linking-exception AND LicenseRef-SUSE-Public-Domain AND OFL-1.1 AND Unicode-3.0 AND CC0-1.0 AND Zlib AND Unlicense AND 0BSD AND MIT-0 AND BSL-1.0
URL:            https://github.com/vnotex/vnote
Source0:        https://github.com/vnotex/vnote/archive/v%{version}.tar.gz#/vnote-%{version}.tar.gz
# Bundled build dependencies, pinned to the commits referenced by vnote
# (git submodules) and to the revisions used by vxcore's FetchContent calls.
Source1:        vtextedit.tar.xz
Source2:        QHotkey.tar.xz
Source3:        vxcore.tar.xz
Source4:        qwindowkit.tar.xz
Source5:        m3.tar.xz
Source6:        cpp-httplib.tar.xz
# Crates vendored from libs/vtextedit/tools/typst-backend/Cargo.lock
Source7:        vtextedit-typst-vendor.tar.xz
# PATCH-FIX-OPENSUSE 0001-QtKeychain-include-dir.patch -- Qt6Keychain installs keychain.h in an include subdirectory
Patch0:         0001-QtKeychain-include-dir.patch
# PATCH-FIX-OPENSUSE 0002-use-system-curl.patch -- Build against the system libcurl
Patch1:         0002-use-system-curl.patch
# PATCH-FIX-OPENSUSE 0003-use-system-pugixml.patch -- Build against the system pugixml
Patch2:         0003-use-system-pugixml.patch
# PATCH-FIX-OPENSUSE 0004-use-system-libsodium.patch -- Build against the system libsodium
Patch3:         0004-use-system-libsodium.patch
BuildRequires:  cargo >= 1.99
BuildRequires:  cmake >= 3.21
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.99
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.9
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Pdf)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(pugixml) >= 1.16
BuildRequires:  pkgconfig(libcurl) >= 7.64
BuildRequires:  pkgconfig(libsodium) >= 1.0.18
BuildRequires:  pkgconfig(openssl)
Provides:       bundled(cmark)
Provides:       bundled(cpp-httplib)
Provides:       bundled(hunspell)
Provides:       bundled(libgit2)
Provides:       bundled(m3)
Provides:       bundled(qmsetup)
Provides:       bundled(qwindowkit)
Provides:       bundled(sonnet)
Provides:       bundled(sqlite)
Provides:       bundled(syntax-highlighting)
Provides:       bundled(typst)
Provides:       bundled(vtextedit)
Provides:       bundled(vxcore)

%description
VNote is a note-taking application, designed especially for Markdown.
VNote provides both note management and Markdown edit experience.

%prep
# The submodule directories are filled in below, so the patches that touch them
# are applied by hand instead of by %%autosetup.
%autosetup -N -p1
%patch -P 0 -p1

cd libs
rmdir QHotkey m3 qwindowkit vtextedit vxcore
for tarball in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
    tar -xJf "${tarball}" -C .
done
cd ..

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

# Build-time dependencies that upstream fetches from the network
mkdir -p %{_builddir}/vnote-deps
tar -xJf %{SOURCE6} -C %{_builddir}/vnote-deps

# Offline crates for the Typst backend
mkdir -p libs/vtextedit/tools/typst-backend/vendor
tar -xJf %{SOURCE7} -C libs/vtextedit/tools/typst-backend/vendor --strip-components=1
mkdir -p libs/vtextedit/tools/typst-backend/.cargo
cat > libs/vtextedit/tools/typst-backend/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "%{_builddir}/vnote-%{version}/libs/vtextedit/tools/typst-backend/vendor"
EOF

# Note: the bundled pdf.js web application ships prebuilt wasm decoders
# (jbig2, openjpeg, qcms, quickjs) that upstream does not provide sources
# for. They are part of the upstream web asset distribution and required
# for PDF preview.

# CPack and the Windows/macOS deployment helpers are not used for RPMs
sed -i '/Packaging.cmake/d' src/CMakeLists.txt

# Use a less generic location for translations
sed -i 's#app:translations#app:vnote/translations#' src/main.cpp

%build
%cmake_qt6 \
  -DCMAKE_SKIP_RPATH:BOOL=TRUE \
  -DVXCORE_USE_SYSTEM_CURL:BOOL=ON \
  -DVXCORE_USE_SYSTEM_PUGIXML:BOOL=ON \
  -DVXCORE_USE_SYSTEM_SODIUM:BOOL=ON \
  -DFETCHCONTENT_SOURCE_DIR_VNOTE_CPP_HTTPLIB=%{_builddir}/vnote-deps/cpp-httplib

%qt6_build
# The application catalogs are only generated by this target
cmake --build build --target lrelease

%install
%qt6_install

# Move translations to a less generic location
mkdir -p %{buildroot}%{_datadir}/vnote
mv %{buildroot}%{_datadir}/translations %{buildroot}%{_datadir}/vnote/translations

# The bundled libraries are not meant to be used by other packages
rm -rf %{buildroot}%{_includedir}/vtextedit
rm -f %{buildroot}%{_libdir}/libVTextEdit.so %{buildroot}%{_libdir}/libvtextedit_typst.so
chmod 0755 %{buildroot}%{_libdir}/libvtextedit_typst.so.1
# cmark is built as a static dependency of vtextedit only
rm -rf %{buildroot}%{_bindir}/cmark \
    %{buildroot}%{_includedir}/cmark.h \
    %{buildroot}%{_includedir}/cmark_export.h \
    %{buildroot}%{_includedir}/cmark_version.h \
    %{buildroot}%{_libdir}/cmake/cmark \
    %{buildroot}%{_libdir}/libcmark.a \
    %{buildroot}%{_libdir}/pkgconfig/libcmark.pc \
    %{buildroot}%{_mandir}/man1/cmark.1* \
    %{buildroot}%{_mandir}/man3/cmark.3*

%ldconfig_scriptlets

%files
%license COPYING.LESSER
%doc README.md changes.md THIRD-PARTY-NOTICES.md
%{_bindir}/vnote
%{_datadir}/applications/vnote.desktop
%{_datadir}/icons/hicolor
%{_datadir}/licenses/vnote/LICENSE.*
%{_datadir}/vnote_extra.rcc
%{_datadir}/vnote/
# The bundled editor library is private to vnote, so it stays in this package
%{_libdir}/libVTextEdit.so.12*
%{_libdir}/libvtextedit_typst.so*

%changelog
