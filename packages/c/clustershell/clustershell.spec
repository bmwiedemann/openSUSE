#
# spec file for package clustershell
#
# Copyright (c) 2023 SUSE LLC
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


%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitelib: %global python2_sitelib %{python_sitelib}}
%{!?__python: %global __python python}
%{!?__python2: %global __python2 %{__python}}

%if 0%{?sle_version} && 0%{?sle_version} < 150400
%define py2 1
%endif

%if 0%{?suse_version} >= 1500
%{!?python2_pkgversion: %global python2_pkgversion 2}
%global python2_pkgprefix python%{python2_pkgversion}
%else
%global python2_pkgprefix python
%endif

%{!?python3_pkgversion: %global python3_pkgversion 3}
%global python3_pkgprefix python%{python3_pkgversion}

%{!?__python3: %global __python3 python3}
%{!?python3_shortver: %global python3_shortver %(%{__python3} -c 'import sys; print(str(sys.version_info.major) + "." + str(sys.version_info.minor))')}

%global srcname ClusterShell

Name:           clustershell
Version:        1.9.2
Release:        1%{?dist}
Summary:        Python framework for efficient cluster administration
License:        LGPL-2.1-or-later
Group:          Productivity/Clustering/Computing

URL:            http://cea-hpc.github.io/clustershell/
Source0:        https://files.pythonhosted.org/packages/source/C/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?py2}
Requires:       python2-%{name} = %{version}-%{release}
%else
Requires:       python3-%{name} = %{version}-%{release}
%endif
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

%if 0%{?py2}
%package -n python2-%{name}
Summary:        ClusterShell module for Python 2
Group:          Productivity/Clustering/Computing
BuildRequires:  %{python2_pkgprefix}-devel
BuildRequires:  %{python2_pkgprefix}-setuptools
Requires:       %{python2_pkgprefix}-setuptools
%if 0%{?suse_version}
Requires:       %{python2_pkgprefix}-PyYAML
%else
Requires:       PyYAML
%endif
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
ClusterShell Python 2 module and related command line tools.
%endif

%package -n %{python3_pkgprefix}-%{name}
Summary:        ClusterShell module for Python 3
Group:          Productivity/Clustering/Computing
BuildRequires:  %{python3_pkgprefix}-devel
BuildRequires:  %{python3_pkgprefix}-setuptools
Requires:       %{python3_pkgprefix}-PyYAML
Requires:       %{python3_pkgprefix}-setuptools
%{!?py2:Obsoletes:      python2-%{name}}
%{?python_provide:%python_provide %{python3_pkgprefix}-%{srcname}}

%description -n %{python3_pkgprefix}-%{name}
ClusterShell Python 3 module and related command line tools.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python3} setup.py build
%{?py2:%{__python2} setup.py build}

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?py2}
pushd %{buildroot}%{_bindir}
for i in clubak cluset clush nodeset; do
  mv $i $i-%{python3_shortver}
done
popd

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%endif

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

%if 0%{?py2}
%files -n python2-%{name}
%{_bindir}/clubak
%{_bindir}/cluset
%{_bindir}/clush
%{_bindir}/nodeset
%{python2_sitelib}/ClusterShell/
%{python2_sitelib}/ClusterShell-*-py?.?.egg-info

%files -n %{python3_pkgprefix}-%{name}
%{_bindir}/clubak-%{python3_shortver}
%{_bindir}/cluset-%{python3_shortver}
%{_bindir}/clush-%{python3_shortver}
%{_bindir}/nodeset-%{python3_shortver}
%{python3_sitelib}/ClusterShell/
%{python3_sitelib}/ClusterShell-*-py?.*.egg-info

%else

%files -n %{python3_pkgprefix}-%{name}
%{_bindir}/clubak
%{_bindir}/cluset
%{_bindir}/clush
%{_bindir}/nodeset
%{python3_sitelib}/ClusterShell/
%{python3_sitelib}/ClusterShell-*-py?.*.egg-info
%endif

%files
%doc ChangeLog README.md
%if 0%{?suse_version} >= 1500
%license COPYING.LGPLv2.1
%else
%doc COPYING.LGPLv2.1
%endif
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
