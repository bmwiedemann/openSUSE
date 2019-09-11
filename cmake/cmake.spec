#
# spec file for package cmake
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define shortversion 3.14
# exclude for SLE 12 and Leap 42.x
%if 0%{?suse_version} == 1315
%define system_libuv OFF
%else
%define system_libuv ON
BuildRequires:  libuv-devel >= 1.10
%endif
Name:           cmake
Version:        3.14.5
Release:        0
Summary:        Cross-platform, open-source make system
License:        BSD-3-Clause
Group:          Development/Tools/Building
URL:            https://www.cmake.org/
Source0:        https://www.cmake.org/files/v%{shortversion}/%{name}-%{version}.tar.gz
Source1:        cmake.macros
# bnc#947585 - Let CMake produces automatic RPM provides
Source3:        cmake.attr
Source4:        cmake.prov
Source5:        https://www.cmake.org/files/v%{shortversion}/%{name}-%{version}-SHA-256.txt
Source6:        https://www.cmake.org/files/v%{shortversion}/%{name}-%{version}-SHA-256.txt.asc
Source7:        cmake.keyring
Patch2:         cmake-fix-ruby-test.patch
# PATCH-FIX-UPSTREAM form.patch -- set the correct include path for the ncurses includes
Patch4:         form.patch
# PATCH-FIX-UPSTREAM system-libs.patch -- allow choosing between bundled and system jsoncpp & form libs
Patch5:         system-libs.patch
# Search for python interpreters from newest to oldest rather then picking up /usr/bin/python as first choice
Patch7:         feature-suse-python-interp-search-order.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libarchive-devel >= 3.0.2
BuildRequires:  libbz2-devel
BuildRequires:  libexpat-devel
BuildRequires:  ncurses-devel
# this is commented as it would create dependancy cycle between jsoncpp and cmake
#if 0 % { ? suse_version} > 1320
#BuildRequires:  pkgconfig(jsoncpp)
#endif
BuildRequires:  pkgconfig
BuildRequires:  rhash-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(liblzma)
Requires:       make
# bnc#953842 - A python file is shipped so require python base so it can be run.
Requires:       python3-base
Recommends:     cmake-man
%if 0%{?suse_version} >= 1330
BuildRequires:  libcurl-mini-devel
%else
BuildRequires:  libcurl-devel
%endif

%description
CMake is a cross-platform, open-source build system

%prep
# The publisher doesn't sign the source tarball, but a signatures file containing multiple hashes.
# Verify hashes in that file against source tarball.
echo "`grep %{name}-%{version}.tar.gz %{SOURCE5} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
# This is not autotools configure
./configure \
    --prefix=%{_prefix} \
    --datadir=/share/%{name} \
    --docdir=/share/doc/packages/%{name} \
    --mandir=/share/man \
    --system-libs \
    --no-system-jsoncpp \
    --parallel=0%{jobs} \
    --verbose \
    --no-qt-gui \
    -- \
    -DCMAKE_USE_SYSTEM_LIBRARY_LIBUV=%{system_libuv}
make VERBOSE=1 %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/cmake
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
install -D -p -m 0644 Auxiliary/cmake-mode.el %{buildroot}%{cmake_mode_el}
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
%{cmake_mode_el}
%dir %{dirname:%{cmake_mode_el}}

%changelog
