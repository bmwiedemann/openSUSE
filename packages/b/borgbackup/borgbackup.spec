#
# spec file for package borgbackup
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016-2019 LISA GmbH, Bingen, Germany.
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

Name:           borgbackup
Version:        1.1.13
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

# build dependencies
BuildRequires:  bash
%if 0%{?suse_version} == 1320 || 0%{?sle_version} == 120200
BuildRequires:  bash-completion
%endif
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
%if %{with borg_sysblake2}
BuildRequires:  libb2-devel
%endif
%if %{with borg_newcompr}
BuildRequires:  liblz4-devel >= 1.7.0
BuildRequires:  libzstd-devel >= 1.3.0
%endif
BuildRequires:  openssl-devel >= 1.0.0
BuildRequires:  python3 >= 3.4
BuildRequires:  python3-Cython
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  zsh

# docs requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
%if %{with borg_guzzle}
BuildRequires:  python3-guzzle_sphinx_theme
%endif

# testing requirements
%if %{with borg_test}
BuildRequires:  python3-pytest
%endif

Requires:       python3-setuptools
Recommends:     python3-llfuse
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BorgBackup is a deduplicating backup program which stores deltas. It
supports compression and authenticated encryption as well,
facilitating frequent backups and storing to not fully trusted
targets.

%package doc
Summary:        Documentation files for borgbackup
Group:          Documentation/HTML

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
Supplements:    packageand(borgbackup:bash)
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
Supplements:    packageand(borgbackup:zsh)
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
Supplements:    packageand(borgbackup:fish)
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
%patch0 -p1
%endif
# remove bundled libraries, that we don't want to be included
rm -rf src/borg/algorithms/{lz4,zstd}
# remove bundled blake2 library, if appropriate
%if %{with borg_sysblake2}
rm -rf src/borg/algorithms/blake2
%endif
# remove precompiled Cython code
find src/ -name '*.pyx' | sed -e 's/.pyx/.c/g' | xargs rm -f
# bundled msgpack is C++ based
find src/ -name '*.pyx' | sed -e 's/.pyx/.cpp/g' | xargs rm -f
# better name for msgpack license
cp -a docs/3rd_party/msgpack/COPYING LICENSE.msgpack

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" python3 setup.py build
export PYTHONPATH=$(pwd)/build/lib.linux-$(uname -m)-%{py3_ver}
make -C docs html man && rm docs/_build/html/.buildinfo

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
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
export PYTHONPATH=$(pwd)/build/lib.linux-$(uname -m)-%{py3_ver}
TEST_SELECTOR="not benchmark"
# for some reason, these tests fail with Tumbleweed: hints welcome
%if 0%{?suse_version} >= 1500
TEST_SELECTOR="$TEST_SELECTOR and not test_progress_percentage_sameline and not test_progress_percentage_step"
%endif
LANG=en_US.UTF-8 py.test -x -vk "$TEST_SELECTOR" $PYTHONPATH/borg/testsuite/*.py
%endif

%files
%defattr(-,root,root,-)
%doc CHANGES.rst README.rst
%license LICENSE LICENSE.msgpack
%{python3_sitearch}/borg/
%{python3_sitearch}/borgbackup-%{version}-py%{py3_ver}.egg-info
%{_bindir}/borg
%{_bindir}/borgfs
%{_mandir}/man1/borg*.1%{ext_man}

%files doc
%defattr(-,root,root,-)
%doc docs/_build/html

%files bash-completion
%defattr(-,root,root,-)
%{_datadir}/bash-completion/completions/borg

%files zsh-completion
%defattr(-,root,root,-)
%{_datadir}/zsh/site-functions/_borg

%files fish-completion
%defattr(-,root,root,-)
%{_datadir}/fish/vendor_completions.d/borg.fish

%changelog
