#
# spec file for package mercurial
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


%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif
Name:           mercurial
Version:        5.1.1
Release:        0
Summary:        Scalable Distributed SCM
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
Url:            https://www.mercurial-scm.org/
Source:         https://www.mercurial-scm.org/release/mercurial-%{version}.tar.gz
Source1:        cacerts.rc
Source2:        https://www.mercurial-scm.org/release/mercurial-%{version}.tar.gz.asc
Source3:        mercurial.keyring
Source99:       mercurial-rpmlintrc
Patch0:         mercurial-hgk-path-fix.diff
# PATCH-FIX-OPENSUSE mercurial-docutils-compat.diff -- Fix for new docutils options not available on 11.1 and older
Patch1:         mercurial-docutils-compat.diff
# PATCH-FIX-OPENSUSE mercurial-locale-path-fix.patch saschpe@suse.de -- locales are found in /usr/share/locale
Patch2:         mercurial-locale-path-fix.patch
# PATCH-FIX-OPENSUSE mercurial-4.8-python2-shebang.patch develop7@develop7.info sets shebang to python2
Patch3:         mercurial-4.8-python2-shebang.patch
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-xml
Requires:       python-curses
Requires:       python-openssl
Requires:       python-xml
Requires:       python(abi) < 3.0
Requires:       python(abi) >= 2.7
Recommends:     %{name}-lang
Provides:       hg = %{version}
%if 0%{?suse_version} < 1210
BuildRequires:  docutils
%else
BuildRequires:  python-docutils
%endif
%if 0%{?sles_version}
Requires:       openssl-certs
%else
Requires:       ca-certificates
%endif
%if 0%{?with_tests}
Source90:       tests.blacklist
BuildRequires:  bzr
BuildRequires:  git
BuildRequires:  gpg
BuildRequires:  ncurses-devel
BuildRequires:  python-Pygments
BuildRequires:  python-openssl
BuildRequires:  subversion-python
BuildRequires:  unzip
#BuildRequires:  python-pyflakes
%endif

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed projects.

%lang_package

%prep
%setup -q
%patch0
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%patch1
%endif
%patch2 -p1
%patch3 -p0

chmod 644 hgweb.cgi

%build
make %{?_smp_mflags} all

%install
make install PREFIX="%{_prefix}" DESTDIR=%{buildroot}

# Move locales to proper location
mkdir -p %{buildroot}%{_datadir}/locale
mv %{buildroot}%{python_sitearch}/mercurial/locale/* %{buildroot}%{_datadir}/locale
%find_lang hg

# Install stuff in contrib
install -m0755 contrib/hgk %{buildroot}%{_bindir}
install -Dm0644 contrib/bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/mercurial.sh
install -Dm0644 contrib/zsh_completion %{buildroot}%{_datadir}/zsh/site-functions/_mercurial
mkdir -p %{buildroot}%{_datadir}/{x,}emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}%{_datadir}/emacs/site-lisp
install -m0644 contrib/*.el %{buildroot}%{_datadir}/xemacs/site-lisp
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mercurial/hgrc.d/cacerts.rc
%fdupes -s %{buildroot}%{_prefix}

%if 0%{?with_tests}
%check
make %{?_smp_mflags} tests TESTFLAGS="-v --blacklist=%{SOURCE90}"
%endif

%files lang -f hg.lang

%files
%license COPYING
%doc README.rst CONTRIBUTORS hgweb.cgi
%{_bindir}/*
%{_sysconfdir}/bash_completion.d/*
%{_datadir}/zsh/
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%config %{_sysconfdir}/mercurial/hgrc.d/*
%{_datadir}/emacs
%{_datadir}/xemacs
%{_mandir}/man1/hg.1%{?ext_man}
%{_mandir}/man5/hgignore.5%{?ext_man}
%{_mandir}/man5/hgrc.5%{?ext_man}
%{_mandir}/man8/hg-ssh.8%{?ext_man}
%{python_sitearch}/*

%changelog
