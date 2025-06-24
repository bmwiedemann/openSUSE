#
# spec file for package clustershell
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2023 Stephane Thiell <sthiell@stanford.edu>
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


%global srcname ClusterShell
%define pythons python3
Name:           clustershell
Version:        1.9.3
Release:        1%{?dist}
Summary:        Python framework for efficient cluster administration
License:        LGPL-2.1-or-later
Group:          Productivity/Clustering/Computing

URL:            http://cea-hpc.github.io/clustershell/
Source0:        https://files.pythonhosted.org/packages/source/C/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-%{name} = %{version}-%{release}
Requires:       vim
BuildRequires:  fdupes
BuildRequires:  vim
Provides:       vim-clustershell = %{version}-%{release}
Obsoletes:      vim-clustershell < 1.7.81-4

%description
ClusterShell is a set of tools and a Python library to execute commands
on cluster nodes in parallel depending on selected engine and worker
mechanisms. Advanced node sets and node groups handling methods are provided
to ease and improve the daily administration of large compute clusters or
server farms. Command line utilities like clush, clubak and nodeset (or
cluset) allow traditional shell scripts to take benefit of the features
offered by the library.

%package -n python3-%{name}
Summary:        ClusterShell module for Python 3
Group:          Productivity/Clustering/Computing
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
Requires:       python3-PyYAML
%{!?py2:Obsoletes:      python2-%{name}}
%{?python_provide:%python_provide %{python3_pkgprefix}-%{srcname}}

%description -n python3-%{name}
ClusterShell Python 3 module and related command line tools.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# move config dir away from default setuptools /usr prefix (if rpm-building as user)
[ -d %{buildroot}/usr/etc ] && mv %{buildroot}/usr/etc %{buildroot}/%{_sysconfdir}

# man pages
install -d %{buildroot}/%{_mandir}/{man1,man5}
install -p -m 0644 doc/man/man1/clubak.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/cluset.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/clush.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/nodeset.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man5/clush.conf.5 %{buildroot}/%{_mandir}/man5/
install -p -m 0644 doc/man/man5/groups.conf.5 %{buildroot}/%{_mandir}/man5/

# vim addons
%define vimdatadir %{_datadir}/vim/site

install -d %{buildroot}/%{vimdatadir}/{ftdetect,syntax}
install -p -m 0644 doc/extras/vim/ftdetect/clustershell.vim %{buildroot}/%{vimdatadir}/ftdetect/
install -p -m 0644 doc/extras/vim/syntax/clushconf.vim %{buildroot}/%{vimdatadir}/syntax/
install -p -m 0644 doc/extras/vim/syntax/groupsconf.vim %{buildroot}/%{vimdatadir}/syntax/
%fdupes %{buildroot}

%files -n python3-%{name}
%{_bindir}/clubak
%{_bindir}/cluset
%{_bindir}/clush
%{_bindir}/nodeset
%{python3_sitelib}/[Cc]luster[Ss]hell/
%{python3_sitelib}/[Cc]luster[Ss]hell-%{version}.dist-info

%files
%doc ChangeLog README.md
%license COPYING.LGPLv2.1
%doc doc/examples
%doc doc/sphinx
%{_mandir}/man1/clubak.1*
%{_mandir}/man1/cluset.1*
%{_mandir}/man1/clush.1*
%{_mandir}/man1/nodeset.1*
%{_mandir}/man5/clush.conf.5*
%{_mandir}/man5/groups.conf.5*
%dir %{_sysconfdir}/clustershell
%dir %{_sysconfdir}/clustershell/clush.conf.d
%dir %{_sysconfdir}/clustershell/groups.d
%dir %{_sysconfdir}/clustershell/groups.conf.d
%config(noreplace) %{_sysconfdir}/clustershell/clush.conf
%config(noreplace) %{_sysconfdir}/clustershell/groups.conf
%ghost %{_sysconfdir}/clustershell/groups
%config(noreplace) %{_sysconfdir}/clustershell/groups.d/local.cfg
%doc %{_sysconfdir}/clustershell/clush.conf.d/README
%doc %{_sysconfdir}/clustershell/clush.conf.d/*.conf.example
%doc %{_sysconfdir}/clustershell/groups.conf.d/README
%doc %{_sysconfdir}/clustershell/groups.conf.d/*.conf.example
%doc %{_sysconfdir}/clustershell/groups.d/README
%doc %{_sysconfdir}/clustershell/groups.d/*.yaml.example
%doc %{_sysconfdir}/clustershell/topology.conf.example
%{vimdatadir}/ftdetect/clustershell.vim
%{vimdatadir}/syntax/clushconf.vim
%{vimdatadir}/syntax/groupsconf.vim

%changelog
