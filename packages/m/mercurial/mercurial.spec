#
# spec file for package mercurial
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1600
# Tumbleweed
%define pythons python3
%global pprefix python3
%else
%if 0%{?sle_version} >= 150600
%{?sle15_python_module_pythons}
%global pprefix python311
%else
%define pythons python3
%global pprefix python3
%endif
%endif

%bcond_with tests

%ifarch %{rust_arches}
%bcond_without rust
%endif

Name:           mercurial
Version:        7.1.2
Release:        0
Summary:        Scalable Distributed SCM
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://www.mercurial-scm.org/
Source:         https://www.mercurial-scm.org/release/mercurial-%{version}.tar.gz
Source1:        cacerts.rc
Source99:       mercurial-rpmlintrc
Patch0:         mercurial-hgk-path-fix.diff
# PATCH-FIX-OPENSUSE mercurial-locale-path-fix.patch saschpe@suse.de -- locales are found in /usr/share/locale
Patch2:         mercurial-locale-path-fix.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
Requires:       %{pprefix}-curses
Requires:       %{pprefix}-xml
Provides:       hg = %{version}
BuildRequires:  %{python_module docutils}
%if 0%{?sles_version}
Requires:       openssl-certs
%else
Requires:       ca-certificates
%endif
%if %{with tests}
Source90:       tests.blacklist
BuildRequires:  %{python_module Pygments}
BuildRequires:  breezy
BuildRequires:  git
BuildRequires:  gpg
BuildRequires:  ncurses-devel
BuildRequires:  subversion-python
BuildRequires:  unzip
%endif

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed projects.

%lang_package

%if %{with rust}
%package rust
Summary:        Rust extensions for Mercurial
Requires:       %{name} = %{version}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
Source80:       vendor-rust.tar.zst

%description rust
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed projects.

This package contains Rust-based features for Mercurial:
- hg-core (and hg-pyo3): implementation of some
  functionality of mercurial in Rust, e.g. ancestry computations in
  revision graphs, status or pull discovery.
- rhg: a pure Rust implementation of Mercurial, with a fallback mechanism for
  unsupported invocations. It reuses the logic `hg-core` but
  completely forgoes interaction with Python.

These features are varying degrees of experimental and come with caveats.
See 'hg help rust' (accessible without this package)
or the documentation files in this package for more information.

Installing this package will enable the Rust extensions for hg immediately.
rhg is its own separate program.
%endif

%package tests
Summary:        Mercurial tests
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
BuildArch:      noarch

%description tests
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed projects.

This package contains its tests.

%prep
%setup -q
%patch -P 0
%patch -P 2 -p1

find . -type f -exec sed -i -e '1{/#!/s/env //}' '{}' \;

%if %{with rust}
%setup -q -a 80
%endif

chmod 644 hgweb.cgi

%build
%pyproject_wheel
%make_build -C contrib/chg all

%if %{with rust}
pushd rust
%cargo_build
popd
%endif

%install
%pyproject_install
%make_build -C doc install PREFIX="%{_prefix}" DESTDIR=%{buildroot} PYTHON=%{expand:%%__%{pythons}}
%make_build -C contrib/chg install PREFIX="%{_prefix}" DESTDIR=%{buildroot}
%{expand:%%%{pythons}_fix_shebang}

# Move locales to proper location
mkdir -p %{buildroot}%{_datadir}/locale
mv %{buildroot}%{python_sitearch}/mercurial/locale/* %{buildroot}%{_datadir}/locale
%find_lang hg

# Install stuff in contrib
install -m0755 contrib/hgk %{buildroot}%{_bindir}
install -Dm0644 contrib/bash_completion %{buildroot}%{_datadir}/bash-completion/completions/hg
install -Dm0644 contrib/zsh_completion %{buildroot}%{_datadir}/zsh/site-functions/_mercurial
mkdir -p %{buildroot}%{_datadir}/{x,}emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}%{_datadir}/emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}%{_datadir}/xemacs/site-lisp
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mercurial/hgrc.d/cacerts.rc
%fdupes -s %{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_datadir}/mercurial
cp -a tests/. %{buildroot}%{_datadir}/mercurial/tests

%if %{with rust}
# set modulepolicy that would usually be set by setup.py
echo 'modulepolicy = b"rust+c-allow"' > %{buildroot}%{python_sitearch}/mercurial/__modulepolicy__.py

# workaround cargo-packaging < 1.3.0 not setting CARGO_TARGET_DIR and outputting to ./rust/target
mv rust/target . || true

install -m0755 target/release/rhg %{buildroot}%{_bindir}
install -m0755 target/release/librusthgpyo3.so %{buildroot}%{python_sitearch}/mercurial/pyo3_rustext.so
%endif

%if %{with tests}
%check
# need to temporarily override the locale path to within buildroot to get
# i18n-related tests to succeed in the build env
cp %{buildroot}%{python_sitearch}/mercurial/i18n.py i18n.py.bak
sed -i 's!/usr/share/locale!%{buildroot}/usr/share/locale!' %{buildroot}%{python_sitearch}/mercurial/i18n.py

%make_build tests TESTFLAGS="-v --with-hg=%{buildroot}%{_bindir}/hg --blacklist=%{SOURCE90}" PYTHON=%{expand:%%__%{pythons}} PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}%{buildroot}%{python3_sitearch}

mv i18n.py.bak %{buildroot}%{python_sitearch}/mercurial/i18n.py
%endif

%files lang -f hg.lang

%files tests
%dir %{_datadir}/mercurial
%{_datadir}/mercurial/tests

%if %{with rust}
%files rust
%{_bindir}/rhg
%{python_sitearch}/mercurial/pyo3_rustext.so
%doc rust/rhg/README.md
%endif

%files
%license COPYING
%doc README.rst CONTRIBUTORS hgweb.cgi
%{_bindir}/hg
%{_bindir}/hgk
%{_bindir}/chg
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%config %{_sysconfdir}/mercurial/hgrc.d/*
%{_datadir}/emacs
%{_datadir}/xemacs
%{_mandir}/man1/hg.1%{?ext_man}
%{_mandir}/man1/hg-*.1%{?ext_man}
%{_mandir}/man1/chg.1%{?ext_man}
%{_mandir}/man5/hgignore.5%{?ext_man}
%{_mandir}/man5/hgrc.5%{?ext_man}
%{_mandir}/man8/hg-ssh.8%{?ext_man}
%{python_sitearch}/hgdemandimport
%{python_sitearch}/hgext
%{python_sitearch}/hgext3rd
%{python_sitearch}/mercurial
%{python_sitearch}/mercurial-%{version}*-info

%if %{with rust}
%exclude %{python_sitearch}/mercurial/pyo3_rustext.so
%endif

%changelog
