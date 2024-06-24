#
# spec file for package mercurial
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%if 0%{?suse_version} > 1600
# Tumbleweed
%define pythons                        python3
%define mercurial_python               python3
%define mercurial_python_executable    python3
%define mercurial_python_fix_shebang() %python3_fix_shebang
%else
%if 0%{?sle_version} >= 150600
%{?sle15_python_module_pythons}
# Leap 15.6
%if %pythons == "python311"
%define mercurial_python               python311
%define mercurial_python_executable    python3.11
%define mercurial_python_fix_shebang() %python311_fix_shebang
%endif
%else
%define pythons                        python3
%define mercurial_python               python3
%define mercurial_python_executable    python3
%define mercurial_python_fix_shebang() %python3_fix_shebang
%endif
%endif

Name:           mercurial
Version:        6.7.4
Release:        0
Summary:        Scalable Distributed SCM
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://www.mercurial-scm.org/
Source:         https://www.mercurial-scm.org/release/mercurial-%{version}.tar.gz
Source1:        cacerts.rc
Source99:       mercurial-rpmlintrc
Patch0:         mercurial-hgk-path-fix.diff
# PATCH-FIX-OPENSUSE mercurial-docutils-compat.diff -- Fix for new docutils options not available on 11.1 and older
Patch1:         mercurial-docutils-compat.diff
# PATCH-FIX-OPENSUSE mercurial-locale-path-fix.patch saschpe@suse.de -- locales are found in /usr/share/locale
Patch2:         mercurial-locale-path-fix.patch
BuildRequires:  %{mercurial_python}
BuildRequires:  %{mercurial_python}-devel
BuildRequires:  %{mercurial_python}-xml
BuildRequires:  fdupes
Requires:       %{mercurial_python}-curses
Requires:       %{mercurial_python}-xml
Provides:       hg = %{version}
%if 0%{?suse_version} < 1210
BuildRequires:  docutils
%else
BuildRequires:  %{mercurial_python}-docutils
%endif
%if 0%{?sles_version}
Requires:       openssl-certs
%else
Requires:       ca-certificates
%endif
%if 0%{?with_tests}
Source90:       tests.blacklist
BuildRequires:  %{mercurial_python}-Pygments
BuildRequires:  bzr
BuildRequires:  git
BuildRequires:  gpg
BuildRequires:  ncurses-devel
BuildRequires:  subversion-python
BuildRequires:  unzip
#BuildRequires:  python-pyflakes
%endif

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed projects.

%lang_package

%package tests
Summary:        Mercurial tests
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}

%description tests
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed projects.

This package contains its tests.

%prep
%setup -q
%patch -P 0
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%patch -P 1
%endif
%patch -P 2 -p1

sed -i -e '1s@env @@' contrib/hgk

chmod 644 hgweb.cgi

%build
%make_build all PYTHON=%{mercurial_python_executable}
%make_build -C contrib/chg all

%install
make install PREFIX="%{_prefix}" DESTDIR=%{buildroot} PYTHON=%{mercurial_python_executable}
make -C contrib/chg install PREFIX="%{_prefix}" DESTDIR=%{buildroot}
%mercurial_python_fix_shebang

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

%if 0%{?with_tests}
%check
%make_build tests TESTFLAGS="-v --blacklist=%{SOURCE90}" PYTHON=%{mercurial_python_executable}
%endif

%files lang -f hg.lang

%files tests
%dir %{_datadir}/mercurial
%{_datadir}/mercurial/tests

%files
%license COPYING
%doc README.rst CONTRIBUTORS hgweb.cgi
%{_bindir}/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%config %{_sysconfdir}/mercurial/hgrc.d/*
%{_datadir}/emacs
%{_datadir}/xemacs
%{_mandir}/man1/hg.1%{?ext_man}
%{_mandir}/man1/chg.1%{?ext_man}
%{_mandir}/man5/hgignore.5%{?ext_man}
%{_mandir}/man5/hgrc.5%{?ext_man}
%{_mandir}/man8/hg-ssh.8%{?ext_man}
%{python_sitearch}/*

%changelog
