#
# spec file for package cmake
#
# Copyright (c) 2019 SUSE LLC
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
%define psuffix -gui
%bcond_without gui
%else
%define psuffix %{nil}
%bcond_with gui
%endif
%define shortversion 3.15
Name:           cmake%{psuffix}
Version:        3.15.5
Release:        0
URL:            https://www.cmake.org/
Source0:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}.tar.gz
Source1:        cmake.macros
# bnc#947585 - Let CMake produces automatic RPM provides
Source3:        cmake.attr
Source4:        cmake.prov
Source5:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}-SHA-256.txt
Source6:        https://www.cmake.org/files/v%{shortversion}/cmake-%{version}-SHA-256.txt.asc
Source7:        cmake.keyring
Patch1:         cmake-fix-ruby-test.patch
# PATCH-FIX-UPSTREAM form.patch -- set the correct include path for the ncurses includes
Patch2:         form.patch
# Search for python interpreters from newest to oldest rather then picking up /usr/bin/python as first choice
Patch3:         feature-suse-python-interp-search-order.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcurl-mini-devel
# this is commented as it would create dependancy cycle between jsoncpp and cmake
#if 0 % { ? suse_version} > 1320
#BuildRequires:  pkgconfig(jsoncpp)
#endif
BuildRequires:  pkgconfig
BuildRequires:  rhash-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libarchive) >= 3.0.2
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libuv) >= 1.10
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)
Requires:       make
%if %{with gui}
Summary:        CMake graphical user interface
License:        BSD-3-Clause
%else
Summary:        Cross-platform make system
License:        BSD-3-Clause
%endif
%if %{with gui}
BuildRequires:  python-sphinx
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       cmake
Recommends:     cmake-man
%else
# bnc#953842 - A python file is shipped so require python base so it can be run.
Requires:       python3-base
%endif

%package -n cmake-man
Summary:        Manual pages for cmake, a cross-platform make system

%description -n cmake-man
Manual pages for cmake, a cross-platform make system.

%if %{with gui}
%description
This is a Graphical User Interface for CMake, a cross-platform
build system.
%else
%description
CMake is a cross-platform build system.
%endif

%prep
# The publisher doesn't sign the source tarball, but a signatures file containing multiple hashes.
# Verify hashes in that file against source tarball.
echo "`grep cmake-%{version}.tar.gz %{SOURCE5} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%setup -q -n cmake-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# This is not autotools configure
./configure \
    --prefix=%{_prefix} \
    --datadir=/share/cmake \
    --docdir=/share/doc/packages/cmake \
    --mandir=/share/man \
    --system-libs \
    --no-system-jsoncpp \
    --no-system-libarchive \
    --no-system-zstd \
    --parallel=0%{jobs} \
    --verbose \
%if %{with gui}
    --qt-gui \
    --sphinx-man \
%else
    --no-qt-gui \
%endif
    %{nil}
make VERBOSE=1 %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/cmake
%if %{with gui}
%suse_update_desktop_file  -r cmake-gui CMake Development IDE Tools Qt

# delete files that belong to the 'cmake' package
rm -rf %{buildroot}%{_bindir}/{cpack,cmake,ctest,ccmake}
rm -rf %{buildroot}%{_datadir}/cmake
rm -rf %{buildroot}%{_datadir}/aclocal/cmake.m4
rm -rf %{buildroot}%{_docdir}/cmake
%else

find %{buildroot}%{_datadir}/cmake -type f -print0 | xargs -0 chmod 644
# rpm macros
install -m644 %{SOURCE1} -D %{buildroot}%{_rpmconfigdir}/macros.d/macros.cmake

# RPM auto provides
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_libexecdir}/rpm/fileattrs/cmake.attr
install -p -m0755 -D %{SOURCE4} %{buildroot}%{_libexecdir}/rpm/cmake.prov

# Install bash completion symlinks
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
for f in %{buildroot}%{_datadir}/%{name}/completions/*
do
  ln -s ../../%{name}/completions/$(basename $f) %{buildroot}%{_datadir}/bash-completion/completions
done

# cmake-mode.el
%define cmake_mode_el %{_datadir}/emacs/site-lisp/%{name}-mode.el
install -D -p -m 0644 Auxiliary/cmake-mode.el %{buildroot}%cmake_mode_el
rm %{buildroot}%{_datadir}/%{name}/editors/emacs/cmake-mode.el
# fix: W: files-duplicate  (%license covers already)
rm %{buildroot}%{_docdir}/%{name}/Copyright.txt

%fdupes %{buildroot}%{_datadir}/cmake

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
%{_datadir}/applications/%{name}.desktop
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
%license Copyright.txt
%doc README.rst
%config %{_rpmconfigdir}/macros.d/macros.cmake
%{_libexecdir}/rpm
%{_bindir}/cpack
%{_bindir}/cmake
%{_bindir}/ctest
%{_bindir}/ccmake
%{_datadir}/cmake
%{_libdir}/cmake
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/cmake.m4
%doc %{_docdir}/%{name}
%{_datadir}/bash-completion
%cmake_mode_el
%dir %{dirname:%cmake_mode_el}
%endif

%changelog
