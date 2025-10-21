#
# spec file for package borgbackup
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2016-2025 LISA GmbH, Bingen, Germany.
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


# define variables needed to build/install borgbackup >= 1.2.0
%define borg_openssl_prefix BORG_OPENSSL_PREFIX=%{_prefix}/lib:%{_libdir}
# needed when building without the packaged algorithms
%define borg_liblz4_prefix BORG_LIBLZ4_PREFIX=%{_includedir}
%define borg_libzstd_prefix BORG_LIBZSTD_PREFIX=%{_includedir}
# new defintion needed with borgbackup >= 1.4.0
%define borg_libxxhash_prefix BORG_LIBXXHASH_PREFIX=%{_includedir}
%define borg_libacl_prefix BORG_LIBACL_PREFIX=%{_includedir}
%if 0%{?suse_version} >= 1500
# use new compression libs (lz4, zstd)
%bcond_without  borg_newcompr
# run tests (may fail without former conditionals)
%bcond_without  borg_test
# use sphinx guzzle theme
%bcond_without  borg_guzzle
%else
%bcond_with     borg_newcompr
%bcond_with     borg_test
%bcond_with     borg_guzzle
%endif
# libb2 is available since Leap 15.2
%if ( 0%{?sle_version} >= 150200 && 0%{?is_opensuse} ) || ( 0%{?suse_version} > 1500 )
%bcond_without	borg_sysblake2
%else
%bcond_with     borg_sysblake2
%endif
%if 0%{?suse_version} < 1600
%global py3ver 3.11
%global py3pkg python311
%else
%global py3ver 3.13
%global py3pkg python313
%endif

Name:           borgbackup
Version:        1.4.1
Release:        0
Summary:        Deduplicating backup program with compression and authenticated encryption
License:        BSD-3-Clause
Group:          Productivity/Archiving/Backup
URL:            https://github.com/borgbackup/borg
Source0:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz
Source1:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz.asc
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE borgbackup-1.1.4-sphinx-default-theme.patch <hpj@urpla.net>
# python3-guzzle_sphinx_theme isn't available everywhere,
# fall back to Sphinx default theme for older distributions
Patch0:         borgbackup-1.1.4-sphinx-default-theme.patch
# PATCH-FIX-OPENSUSE msgpack-allow-1.1.2.patch -- let's hope, 1.1.2 will work as well
Patch1:         msgpack-allow-1.1.2.patch
# PATCH-FIX-UPSTREAM 0001-set_flags-use-get-set-to-only-influence-specific-fla.patch #9039
Patch2:         0001-set_flags-use-get-set-to-only-influence-specific-fla.patch
# PATCH-FIX-UPSTREAM 0002-set_flags-better-give-up-than-corrupt.patch #9039
Patch3:         0002-set_flags-better-give-up-than-corrupt.patch
# PATCH-FIX-UPSTREAM 0003-set_flags-remove-compression-flag.patch #9039
Patch4:         0003-set_flags-remove-compression-flag.patch
# SECTION build dependencies
BuildRequires:  bash
BuildRequires:  %{py3pkg}-Cython >= 3.0.10
BuildRequires:  %{py3pkg}-devel >= 3.9
BuildRequires:  %{py3pkg}-packaging
BuildRequires:  %{py3pkg}-setuptools
BuildRequires:  %{py3pkg}-setuptools_scm
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel >= 2.2.47
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  pkgconfig
BuildRequires:  zsh
BuildRequires:  pkgconfig(libxxhash)
%if 0%{?suse_version} == 1320 || 0%{?sle_version} == 120200
BuildRequires:  bash-completion
%endif
%if %{with borg_sysblake2}
BuildRequires:  libb2-devel
%endif
%if %{with borg_newcompr}
BuildRequires:  liblz4-devel >= 1.7.0
BuildRequires:  libzstd-devel >= 1.3.0
%endif
# /SECTION
# SECTION runtime and extra requrements
# msgpack is not included with borg version >= 1.2.0 anymore
# The metadata is very specific about the version, the command will fail if msgpack is out of range -- boo#1198267
# See https://github.com/borgbackup/borg/blob/1.2.1/setup.py#L68 and update this for every version bump!
BuildRequires:  (%{py3pkg}-msgpack >= 1.0.3 with %{py3pkg}-msgpack <= 1.1.2)
Requires:       %{py3pkg}-packaging
Requires:       (%{py3pkg}-msgpack >= 1.0.3 with %{py3pkg}-msgpack <= 1.1.2)
%if 0%{?suse_version} > 1500
# upstream recommends a "Requires" if pyfuse3 is available
Requires:       %{py3pkg}-pyfuse3 >= 3.1.1
%else
Recommends:     %{py3pkg}-llfuse >= 1.3.8
%endif
# /SECTION
# SECTION docs requirements
BuildRequires:  %{py3pkg}-Sphinx
BuildRequires:  %{py3pkg}-sphinx_rtd_theme
%if %{with borg_guzzle}
BuildRequires:  %{py3pkg}-guzzle_sphinx_theme
%endif
# /SECTION
# SECTION testing requirements
%if %{with borg_test}
BuildRequires:  %{py3pkg}-dateutil
BuildRequires:  %{py3pkg}-pytest
BuildRequires:  %{py3pkg}-pytest-benchmark
BuildRequires:  %{py3pkg}-pytest-cov
BuildRequires:  %{py3pkg}-pytest-xdist
%endif
# /SECTION

%description
BorgBackup is a deduplicating backup program which stores deltas. It
supports compression and authenticated encryption as well,
facilitating frequent backups and storing to not fully trusted
targets.

%package doc
Summary:        Documentation files for borgbackup
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
BorgBackup is a deduplicating backup program which stores deltas. It
supports compression and authenticated encryption as well,
facilitating frequent backups and storing to not fully trusted
targets.

Run borg for a commands overview and check out the docs at
%{_docdir}/%{name}/html/index.html.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Archiving/Backup
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (borgbackup and bash)
BuildArch:      noarch

%description bash-completion
BorgBackup is a deduplicating backup program which stores deltas. It
supports compression and authenticated encryption as well,
facilitating frequent backups and storing to not fully trusted
targets.

This package contains the bash completion script for borgbackup.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          Productivity/Archiving/Backup
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (borgbackup and zsh)
BuildArch:      noarch

%description zsh-completion
BorgBackup is a deduplicating backup program which stores deltas. It
supports compression and authenticated encryption as well,
facilitating frequent backups and storing to not fully trusted
targets.

This package contains the zsh completion script for borgbackup.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          Productivity/Archiving/Backup
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (borgbackup and fish)
BuildArch:      noarch

%description fish-completion
BorgBackup is a deduplicating backup program which stores deltas. It
supports compression and authenticated encryption as well,
facilitating frequent backups and storing to not fully trusted
targets.

This package contains the fish completion script for borgbackup.

%prep
%setup -q
%if ! %{with borg_guzzle}
%patch -P 0 -p1
%endif
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

%ifnarch %ix86 %arm
  # https://github.com/borgbackup/borg/issues/6996
  sed -i 's/SUPPORT_32BIT_PLATFORMS = True/SUPPORT_32BIT_PLATFORMS = False/' src/borg/helpers/time.py
%endif
# remove bundled libraries, that we don't want to be included
rm -rf src/borg/algorithms/{lz4,zstd}
# remove bundled blake2 library, if appropriate
%if %{with borg_sysblake2}
rm -rf src/borg/algorithms/blake2
%endif
# remove precompiled Cython code
find src/ -name '*.pyx' | sed -e 's/.pyx/.c/g' | xargs rm -f
# better name for msgpack license
cp -a %{_datadir}/licenses/%{python_flavor}-msgpack/COPYING LICENSE.msgpack

%build
%{borg_openssl_prefix} %{borg_libzstd_prefix} %{borg_liblz4_prefix} %{borg_libxxhash_prefix} %{borg_libacl_prefix} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" python3 setup.py build
export PYTHONPATH=$(pwd)/build/lib.linux-$(uname -m)-%{py3_ver}
%make_build -C docs html man && rm docs/_build/html/.buildinfo

%install
%{borg_libacl_prefix} %{borg_libxxhash_prefix} %{borg_openssl_prefix} %{borg_liblz4_prefix} %{borg_libzstd_prefix} python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
# install all man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 docs/man/borg*.1 %{buildroot}%{_mandir}/man1
# install shell completions
install -D -m 0644 scripts/shell_completions/bash/borg %{buildroot}/%{_datadir}/bash-completion/completions/borg
install -D -m 0644 scripts/shell_completions/zsh/_borg %{buildroot}/%{_datadir}/zsh/site-functions/_borg
install -D -m 0644 scripts/shell_completions/fish/borg.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/borg.fish
# link duplicate files
%fdupes %{buildroot}/%{python3_sitearch}/borgbackup-%{version}-py%{py3_ver}.egg-info/
# fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' docs/_build/html/_static/fonts/open-sans/stylesheet.css
sed -i 's/\r$//' docs/_build/html/_static/fonts/source-serif-pro/LICENSE.txt

%if %{with borg_test}
%check
# tests need to run in the build env for some reason
export py3_ver_nodot=$(echo %{py3_ver} | tr -d '.')
export PYTHONPATH=$(pwd)/build/lib.linux-$(uname -m)-cpython-$py3_ver_nodot
TEST_SELECTOR="not benchmark"
LANG=en_US.UTF-8 py.test -x -vk "$TEST_SELECTOR" $PYTHONPATH/borg/testsuite/*.py
%endif

%files
%doc CHANGES.rst README.rst
%license LICENSE LICENSE.msgpack
%{python3_sitearch}/borg/
%{python3_sitearch}/borgbackup-%{version}-py%{py3_ver}.egg-info
%{_bindir}/borg
%{_bindir}/borgfs
%{_mandir}/man1/borg*.1%{?ext_man}

%files doc
%doc docs/_build/html

%files bash-completion
%{_datadir}/bash-completion/completions/borg

%files zsh-completion
%{_datadir}/zsh/site-functions/_borg

%files fish-completion
%{_datadir}/fish/vendor_completions.d/borg.fish

%changelog
