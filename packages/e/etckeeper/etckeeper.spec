# vim: set sw=4 ts=4 et nu:
#
# spec file for package etckeeper
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Mitsutoshi NAKANO <bkbin005@rinku.zaq.ne.jp>
# Copyright (c) 2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


# this would pull python2
%bcond_with bzr
%bcond_without systemd

%if %{with bzr}
%define python_versioned python
%define python_args PYTHON_INSTALL_OPTS="--prefix=%{_prefix} --install-purelib=%{python_sitearch}"
%else
%define python_versioned python3
%define python_args %{nil}
%endif

%define make_args systemddir=%{_unitdir} PYTHON=%{python_versioned} %{python_args}

Name:           etckeeper
Version:        1.18.18
Release:        0
Summary:        Store /etc under Version Control
License:        GPL-2.0-or-later
Group:          System/Management
Source:         https://git.joeyh.name/index.cgi/etckeeper.git/snapshot/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM etckeeper-avoid-packagelist.patch gh#joeyh/etckeeper#17 bkbin005@rinku.zaq.ne.jp -- add AVOID_PACKAGELIST
Patch0:         etckeeper-avoid-packagelist.patch
Patch1:         etckeeper-set-package-manager.patch
URL:            http://etckeeper.branchable.com/
%if ! %{with bzr}
BuildArch:      noarch
%endif
BuildRequires:  %{python_versioned}-devel
%if 0%{suse_version} >= 1500
BuildRequires:  bash-completion-devel
%else
BuildRequires:  bash-completion
%endif
BuildRequires:  make
# for the path ownership
BuildRequires:  %{python_versioned}-zypp-plugin
BuildRequires:  libzypp
BuildRequires:  systemd-rpm-macros
%if %{with bzr}
BuildRequires:  bzr
%endif

Recommends:     %{name}-zypp-plugin = %{version}-%{release}
Recommends:     git-core
%if %{with bzr}
Recommends:     %{name}-bzr = %{version}-%{release}
%endif
%if %{with systemd}
%{?systemd_requires}
Obsoletes:      %{name}-cron = %{version}-%{release}
%else
Recommends:     %{name}-cron = %{version}-%{release}
%endif

%description
The etckeeper program is a tool to let /etc be stored in a git,
mercurial, bzr or darcs repository. It hooks into yum to automatically
commit changes made to /etc during package upgrades. It tracks file
metadata that version control systems do not normally support, but that
is important for /etc, such as the permissions of /etc/shadow. It is
quite modular and configurable, while also being simple to use if you
understand the basics of working with version control.

%package cron
Summary:        The etckeeper cron function
Group:          System/Management
%if ! %{with bzr}
BuildArch:      noarch
%endif
Requires:       etckeeper = %{version}-%{release}
Provides:       etckeeper:%{_sysconfdir}/cron.daily/etckeeper
Requires:       cron

%description cron
The etckeeper-cron calls etckeeper from cron.

%package zypp-plugin
Summary:        The etckeeper integration function with ZYpp
Group:          System/Management
%if ! %{with bzr}
BuildArch:      noarch
%endif
Requires:       %{python_versioned}-zypp-plugin
Requires:       etckeeper = %{version}-%{release}
Obsoletes:      etckeeper-pkgmanager-collabo < %{version}-%{release}
Provides:       etckeeper-pkgmanager-collabo = %{version}-%{release}
Provides:       etckeeper:%{_prefix}/lib/zypp/plugins/commit/zypper-etckeeper.py

%description zypp-plugin
The etckeeper-zypp-plugin calls etckeeper from ZYpp.

%package bzr
Summary:        The etckeeper integration function with bzr
Group:          System/Management
Requires:       %{python_versioned}-base
Requires:       etckeeper = %{version}-%{release}

%description bzr
The etckeeper integration function with bzr

%package bash-completion
Summary:        The bash completion for etckeeper
Group:          System/Shells
Requires:       bash-completion
Requires:       etckeeper = %{version}-%{release}
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        The zsh completion for etckeeper
Group:          System/Shells
Requires:       etckeeper = %{version}-%{release}

%description zsh-completion
zsh command line completion support for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
find -type f -name ".gitignore" -delete
rm -f ./doc/todo/.mdwn
rm README.md
cp -a doc/README.mdwn README.md
perl -p -i -e 's|%{_bindir}/python|%{_bindir}/%{python_versioned}|g' zypper-etckeeper.py
make %{?_smp_mflags} %{make_args}

%install
%make_install %{make_args}
%if ! %{with systemd}
install -D debian/cron.daily "%{buildroot}/etc/cron.daily/%{name}"
%endif

mkdir %{buildroot}%{_sbindir}
ln -s ../bin/%{name} %{buildroot}%{_sbindir}/%{name}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre etckeeper.timer etckeeper.service

%preun
%service_del_preun etckeeper.timer etckeeper.service

%post
%service_add_post etckeeper.timer etckeeper.service

%postun
%service_del_postun etckeeper.timer etckeeper.service

%files
%doc README.md
%license GPL
%{_unitdir}/etckeeper.timer
%{_unitdir}/etckeeper.service
%{_bindir}/etckeeper
%{_sbindir}/etckeeper
%{_sbindir}/rcetckeeper
%dir %{_sysconfdir}/etckeeper
%dir %{_sysconfdir}/etckeeper/*.d
%{_sysconfdir}/etckeeper/daily
%config(noreplace) %{_sysconfdir}/etckeeper/etckeeper.conf
%config %{_sysconfdir}/etckeeper/*.d/*
%{_mandir}/man8/etckeeper.8*

%if ! %{with systemd}
%files cron
%config(noreplace) %{_sysconfdir}/cron.daily/etckeeper
%endif

%files bash-completion
%{_datadir}/bash-completion/completions/etckeeper

%files zsh-completion
%{_datadir}/zsh
%{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_etckeeper

%files zypp-plugin
%{_prefix}/lib/zypp/plugins/commit/zypper-etckeeper.py

%if %{with bzr}
%files bzr
%{python_sitearch}/bzrlib/plugins/%{name}/
%{python_sitearch}/bzr_%{name}-*.egg-info
%endif

%changelog
