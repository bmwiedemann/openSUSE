#
# spec file for package cmake
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "gui"
%define psuffix -ui
%bcond_without gui
%else
%bcond_with gui
%endif
%if "%{flavor}" == "mini"
%define psuffix -mini
%bcond_without mini
%else
%bcond_with mini
%endif
%if "%{flavor}" == "full"
%define psuffix -full
%bcond_without full
%else
%bcond_with full
%endif
%define shortversion 3.18
Name:           cmake%{?psuffix}
Version:        3.18.3
Release:        0
Summary:        Cross-platform make system
License:        BSD-3-Clause
URL:            https://www.cmake.org/
Source0:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}.tar.gz
Source1:        cmake.macros
# bnc#947585 - Let CMake produces automatic RPM provides
Source3:        cmake.attr
Source4:        cmake.prov
Source5:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}-SHA-256.txt
Source6:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}-SHA-256.txt.asc
Source7:        cmake.keyring
Source99:       README.SUSE
Patch0:         cmake-fix-ruby-test.patch
# Search for python interpreters from newest to oldest rather then picking up /usr/bin/python as first choice
Patch1:         feature-suse-python-interp-search-order.patch
Patch2:         cmake-fix-png-include-dir.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  rhash-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libuv) >= 1.10
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)
%if "%{flavor}" == ""
Requires:       cmake-implementation = %{version}
%endif
%if %{with full} || %{with mini}
Requires:       make
# bnc#953842 - A python file is shipped so require python base so it can be run.
Requires:       python3-base
Conflicts:      cmake-implementation
Provides:       cmake-implementation = %{version}
%endif
%if %{with mini}
Requires:       this-is-only-for-build-envs
%endif
%if %{with full} || %{with gui}
BuildRequires:  pkgconfig(jsoncpp) >= 1.4.1
BuildRequires:  pkgconfig(libarchive) >= 3.3.3
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libzstd)
%endif
%if %{with gui}
BuildRequires:  python3-Sphinx
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Widgets)
%endif

%description
CMake is a cross-platform build system.

%package -n cmake-man
Summary:        Manual pages for cmake, a cross-platform make system
Supplements:    cmake

%description -n cmake-man
Manual pages for cmake, a cross-platform make system.

%package -n cmake-gui
Summary:        CMake graphical user interface
Requires:       cmake

%description -n cmake-gui
This is a Graphical User Interface for CMake, a cross-platform
build system.

%prep
# The publisher doesn't sign the source tarball, but a signatures file containing multiple hashes.
# Verify hashes in that file against source tarball.
echo "`grep cmake-%{version}.tar.gz %{SOURCE5} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup -p1 -n cmake-%{version}

%build
cp %{SOURCE99} .
%if "%{flavor}" != ""
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# This is not autotools configure
./configure \
    --prefix=%{_prefix} \
    --datadir=/share/cmake \
    --docdir=/share/doc/packages/cmake \
    --mandir=/share/man \
    --system-libs \
%if %{with mini}
    --no-system-curl \
    --no-system-nghttp2 \
    --no-system-jsoncpp \
    --no-system-libarchive \
    --no-system-zstd \
%endif
    --parallel=0%{jobs} \
    --verbose \
%if %{with gui}
    --qt-gui \
    --sphinx-man \
%else
    --no-qt-gui \
%endif
    %{nil}
%make_build
%endif

%install
%if "%{flavor}" != ""
%make_install
mkdir -p %{buildroot}%{_libdir}/cmake
%if %{with gui}
%suse_update_desktop_file  -r cmake-gui CMake Development IDE Tools Qt

# delete files that belong to the 'cmake' package
rm -rf %{buildroot}%{_bindir}/{cpack,cmake,ctest,ccmake}
rm -rf %{buildroot}%{_datadir}/cmake
rm -rf %{buildroot}%{_datadir}/aclocal/cmake.m4
rm -rf %{buildroot}%{_docdir}/cmake
rm -rf %{buildroot}%{_datadir}/bash-completion/completions/{cmake,cpack,ctest}
rm -rf %{buildroot}%{_datadir}/emacs/site-lisp/cmake-mode.el
rm -rf %{buildroot}%{_datadir}/vim/
%else

find %{buildroot}%{_datadir}/cmake -type f -print0 | xargs -0 chmod 644
# rpm macros
install -m644 %{SOURCE1} -D %{buildroot}%{_rpmconfigdir}/macros.d/macros.cmake

# RPM auto provides
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_fileattrsdir}/cmake.attr
install -p -m0755 -D %{SOURCE4} %{buildroot}%{_rpmconfigdir}/cmake.prov

# fix: W: files-duplicate  (%%license covers already)
rm %{buildroot}%{_docdir}/cmake/Copyright.txt

%fdupes %{buildroot}%{_datadir}/cmake
%endif
%endif

%if "%{flavor}" == "full"
%check
# Excluded tests:
#    TestUpload: uses internet connection
#    SimpleInstall: seems to fail due to RPATH strictness
#                   if any other app installs then this test is bogus
#    suse specific brp-25-symlink cramps the symlinks, hence the CPackComponentsForAll-RPM-(default|OnePackPerGroup|IgnoreGroup|AllInOne) fail
./bin/ctest --force-new-ctest-process --output-on-failure %{?_smp_mflags} \
    -E "(TestUpload|SimpleInstall|SimpleInstall-Stage2|CPackComponentsForAll-RPM-(default|OnePackPerGroup|IgnoreGroup|AllInOne)|CPack_RPM)"
%endif

%if %{with gui}
%files -n cmake-gui
%license Copyright.txt
%{_bindir}/cmake-gui
%{_datadir}/applications/cmake-gui.desktop
%{_datadir}/mime/packages/cmakecache.xml
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/*
%{_datadir}/icons/hicolor/128x128/apps/CMakeSetup.png
%{_datadir}/icons/hicolor/32x32/apps/CMakeSetup.png

%files -n cmake-man
%license Copyright.txt
%{_mandir}/man7/*
%{_mandir}/man1/*
%else
%files
%if "%{flavor}" == ""
%doc README.SUSE
%else
%license Copyright.txt
%doc README.rst
%{_rpmconfigdir}/macros.d/macros.cmake
%{_fileattrsdir}/cmake.attr
%{_rpmconfigdir}/cmake.prov
%{_bindir}/cpack
%{_bindir}/cmake
%{_bindir}/ctest
%{_bindir}/ccmake
%{_datadir}/cmake
%{_libdir}/cmake
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/cmake.m4
%doc %{_docdir}/cmake
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/{cmake,cpack,ctest}
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/cmake-mode.el
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/indent
%{_datadir}/vim/vimfiles/indent/cmake.vim
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/syntax/cmake.vim
%endif
%endif

%changelog
