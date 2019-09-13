#
# spec file for package gitolite
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


%define         gitolite_homedir    /srv/gitolite
%define         git_user            git
Name:           gitolite
Version:        3.6.11
Release:        0
Summary:        Server for git directory version tracker
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            http://gitolite.com
Source0:        https://github.com/sitaramc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source11:       README.SUSE
BuildRequires:  git
Requires:       git
Conflicts:      gitosis
BuildArch:      noarch
%if 0%{?suse_version} >= 1330
Requires(pre):  user(wwwrun)
%endif
%if 0%{?suse_version} > 1110
%{perl_requires}
%else
Requires:       perl = %{perl_version}
%endif

%description
Gitolite is an access control layer on top of git, which allows access control
down to the branch level, including specifying who can and cannot rewind a given
branch.

%prep
%setup -q
install -m 644 %{SOURCE11} .

%build

%install
install -d %{buildroot}%{gitolite_homedir}
install -d %{buildroot}%{gitolite_homedir}/.ssh
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{perl_vendorlib}
install -d %{buildroot}%{_datadir}/%{name}

cp -pr src/lib/Gitolite %{buildroot}%{perl_vendorlib}
echo "%{version}" >src/VERSION
cp -a src/* %{buildroot}%{_datadir}/%{name}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

# empty authorized_keys file
touch %{buildroot}%{gitolite_homedir}/.ssh/authorized_keys

%pre
# Create user and group on the system if necessary
# default group: git
getent group %{git_user} >/dev/null || \
	%{_sbindir}/groupadd -r %{git_user}

# default user: git
getent passwd %{git_user} >/dev/null || \
	%{_sbindir}/useradd -c "git repository hosting" \
	-d %{gitolite_homedir} -G %{git_user} -g %{git_user} \
	-r -s /bin/bash %{git_user}

# if apache user is not in git group, add it
getent passwd wwwrun >/dev/null &&
	%{_sbindir}/usermod -a -G git wwwrun

%files
%license COPYING
%doc README.markdown CHANGELOG README.SUSE
%{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/%{name}
%attr(750,%{git_user},%{git_user}) %dir %{gitolite_homedir}
%attr(750,%{git_user},%{git_user}) %dir %{gitolite_homedir}/.ssh
%config(noreplace) %attr(640,%{git_user},%{git_user}) %{gitolite_homedir}/.ssh/authorized_keys

%changelog
