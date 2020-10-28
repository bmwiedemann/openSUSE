#
# spec file for package dnf-plugins-core
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%{?!dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.22}
%global dnf_plugins_extra 2.0.0
%global hawkey_version 0.46.1

%if 0%{?is_opensuse}
# Copr targets are available for openSUSE Leap 15.0 and newer
%bcond_without copr_plugin
%else
# Copr plugin is not supported for this target
%bcond_with copr_plugin
%endif

# YUM v3 has been removed from openSUSE Tumbleweed as of 20191119
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%bcond_with as_yum
%else
%bcond_without as_yum
%endif

%if %{with as_yum}
%global yum_utils_subpackage_name yum-utils
%else
%global yum_utils_subpackage_name dnf-utils
%endif

# Deal with SLE Backports issues
%if 0%{?sle_version} && 0%{?is_backports}
%bcond_without deconflict
%global deconflict_prefix dnfutils-
%else
%bcond_with deconflict
%global deconflict_prefix %{nil}
%endif

%bcond_without tests

#global prerel rc1

Name:           dnf-plugins-core
Version:        4.0.18
Release:        0
Summary:        Core Plugins for DNF
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/rpm-software-management/dnf-plugins-core
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gettext
Requires:       python3-dnf-plugins-core = %{version}-%{release}
Recommends:     %{name}-lang >= %{version}

Provides:       dnf-command(builddep)
Provides:       dnf-command(config-manager)
%if %{with copr_plugin}
Provides:       dnf-command(copr)
%endif
Provides:       dnf-command(builddep)
Provides:       dnf-command(changelog)
Provides:       dnf-command(config-manager)
Provides:       dnf-command(copr)
Provides:       dnf-command(debug-dump)
Provides:       dnf-command(debug-restore)
Provides:       dnf-command(debuginfo-install)
Provides:       dnf-command(download)
Provides:       dnf-command(repoclosure)
Provides:       dnf-command(repodiff)
Provides:       dnf-command(repograph)
Provides:       dnf-command(repomanage)
Provides:       dnf-command(reposync)

# Plugins shift from extras to core
Provides:       dnf-plugins-extras-debug = %{version}-%{release}
Provides:       dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:       dnf-plugins-extras-repograph = %{version}-%{release}
Provides:       dnf-plugins-extras-repomanage = %{version}-%{release}
# Generic package name Provides
Provides:       dnf-plugin-builddep = %{version}-%{release}
Provides:       dnf-plugin-config-manager = %{version}-%{release}
Provides:       dnf-plugin-debuginfo-install = %{version}-%{release}
Provides:       dnf-plugin-download = %{version}-%{release}
Provides:       dnf-plugin-generate_completion_cache = %{version}-%{release}
Provides:       dnf-plugin-needs_restarting = %{version}-%{release}
Provides:       dnf-plugin-repoclosure = %{version}-%{release}
Provides:       dnf-plugin-repograph = %{version}-%{release}
Provides:       dnf-plugin-repomanage = %{version}-%{release}
Provides:       dnf-plugin-reposync = %{version}-%{release}

Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}

%description
Core Plugins for DNF. This package enhances DNF with the builddep, config-manager,
%{?_with_copr_plugin:copr, }debug, debuginfo-install, download, needs-restarting,
repoclosure, repograph, repomanage, and reposync commands. Additionally, it provides
the generate_completion_cache passive plugin.

%package -n python3-dnf-plugins-core
Summary:        Python 3 interface to core plugins for DNF
Group:          System/Packages
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python3-pytest
Requires:       python3-dateutil
Requires:       python3-distro
Requires:       python3-dnf >= %{dnf_lowest_compatible}
Requires:       python3-hawkey >= %{hawkey_version}

Conflicts:      %{name} <= 0.1.5
# let the both python plugin versions be updated simultaneously
Conflicts:      python3-%{name} < %{version}-%{release}
Conflicts:      python2-%{name} < %{version}-%{release}
Provides:       python3-dnf-plugins-extras-debug = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-repograph = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-repomanage = %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-debug < %{dnf_plugins_extra}
Obsoletes:      python3-dnf-plugins-extras-repoclosure < %{dnf_plugins_extra}
Obsoletes:      python3-dnf-plugins-extras-repograph < %{dnf_plugins_extra}
Obsoletes:      python3-dnf-plugins-extras-repomanage < %{dnf_plugins_extra}
# No longer supporting Python 2
Obsoletes:      python2-dnf-plugins-core < 4.0.3

%description -n python3-dnf-plugins-core
Core Plugins for DNF, Python 3 interface. This package enhances DNF with
the builddep, config-manager, %{?_with_copr_plugin:copr, }debug, debuginfo-install,
download, needs-restarting, repoclosure, repograph, repomanage, and reposync commands.
Additionally, it provides the generate_completion_cache passive plugin.

%package -n %{yum_utils_subpackage_name}
Summary:        Yum-utils CLI compatibility layer
Group:          System/Packages
%if %{with as_yum}
Obsoletes:      dnf-utils < %{version}-%{release}
Obsoletes:      yum-utils < 4.0.0
Provides:       dnf-utils = %{version}-%{release}
# SUSE-specific yum-utils subpackage obsoletion
Obsoletes:      yum-changelog < 4.0.0
Provides:       yum-changelog = %{version}-%{release}
%else
# dnf-utils offers the same binaries as yum-utils
Conflicts:      yum-changelog
Conflicts:      yum-utils
%endif
%if ! %{with deconflict}
# Cf. https://github.com/openSUSE/zypper/pull/254
Conflicts:      zypper < 1.14.26
Conflicts:      zypper-needs-restarting
%endif
Requires:       %{name} = %{version}-%{release}
Requires:       dnf >= %{dnf_lowest_compatible}
Requires:       python3-dnf >= %{dnf_lowest_compatible}

%description -n %{yum_utils_subpackage_name}
As a Yum-utils CLI compatibility layer, supplies in CLI shims for
debuginfo-install, repograph, package-cleanup, repoclosure, repomanage,
repoquery, reposync, repotrack, builddep, config-manager, debug, and
download that use new implementations using DNF.


%package -n python3-dnf-plugin-leaves
Summary:        Leaves Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugins-extras-leaves = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-leaves = %{version}-%{release}
Provides:       dnf-command(leaves)
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-leaves < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-leaves < %{dnf_plugins_extra}
# Python 2 variants are no longer provided
Obsoletes:      python2-dnf-plugin-leaves < 4.0.3

%description -n python3-dnf-plugin-leaves
Leaves Plugin for DNF, Python 3 version. List all installed packages
not required by any other installed package.

%package -n python3-dnf-plugin-local
Summary:        Local Plugin for DNF
Group:          System/Packages
Requires:       createrepo_c
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-local =  %{version}-%{release}
Provides:       dnf-plugins-extras-local = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-local = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-local < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-local < %{dnf_plugins_extra}
# Python 2 variants are no longer provided
Obsoletes:      python2-dnf-plugin-local < 4.0.3

%description -n python3-dnf-plugin-local
Local Plugin for DNF, Python 3 version. Automatically copy all downloaded
packages to a repository on the local filesystem and generating repo metadata.

%package -n python3-dnf-plugin-post-transaction-actions
Summary:        Post transaction actions Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-post-transaction-actions =  %{version}-%{release}
Conflicts:      python2-dnf-plugin-post-transaction-actions < %{version}-%{release}

%description -n python3-dnf-plugin-post-transaction-actions
Post transaction actions Plugin for DNF, Python 3 version. Plugin runs actions
(shell commands) after transaction is completed. Actions are defined in action
files.

%package -n python3-dnf-plugin-show-leaves
Summary:        Show-leaves Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugin-show-leaves =  %{version}-%{release}
Provides:       dnf-plugins-extras-show-leaves = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-show-leaves = %{version}-%{release}
Provides:       dnf-command(show-leaves)
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-show-leaves < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-show-leaves < %{dnf_plugins_extra}
# Python 2 variants are no longer provided
Obsoletes:      python2-dnf-plugin-show-leaves < 4.0.3

%description -n python3-dnf-plugin-show-leaves
Show-leaves Plugin for DNF, Python 3 version. List all installed
packages that are no longer required by any other installed package
after a transaction.

%package -n python3-dnf-plugin-versionlock
Summary:        Version Lock Plugin for DNF
Group:          System/Packages
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-versionlock =  %{version}-%{release}
Provides:       dnf-plugins-extras-versionlock = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-versionlock = %{version}-%{release}
Provides:       dnf-command(versionlock)
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-versionlock < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-versionlock < %{dnf_plugins_extra}
# Python 2 variants are no longer provided
Obsoletes:      python2-dnf-plugin-versionlock < 4.0.3
%if %{with as_yum}
# SUSE-specific yum-utils subpackage obsoletion
Obsoletes:      yum-versionlock < 4.0.0
Provides:       yum-versionlock = %{version}-%{release}
%endif

%description -n python3-dnf-plugin-versionlock
Version lock plugin takes a set of name/versions for packages and excludes all other
versions of those packages. This allows you to e.g. protect packages from being
updated by newer versions.

%lang_package

%prep
%autosetup -p1

# openSUSE installs libexec content into /usr/lib...
sed -e "s:libexec:%{_libexecdir}:g" -i libexec/CMakeLists.txt

# Fix sphinx-build run...
sed -e "s/sphinx-build-3/sphinx-build-%{python3_version}/" -i doc/CMakeLists.txt

%build
%cmake -DPYTHON_DESIRED:FILEPATH=%{__python3}
%make_build
make doc-man

%install
pushd ./build
%make_install
popd

%find_lang %{name}

# For directory ownership?
mkdir -p %{buildroot}%{_var}/cache/dnf

mv %{buildroot}%{_libexecdir}/dnf-utils-3 %{buildroot}%{_libexecdir}/dnf-utils
rm -vf %{buildroot}%{_libexecdir}/dnf-utils-*

mkdir -p %{buildroot}%{_bindir}
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/debuginfo-install
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/needs-restarting
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/find-repos-of-install
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repo-graph
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/package-cleanup
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoclosure
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repodiff
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repomanage
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoquery
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/reposync
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repotrack
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-builddep
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-config-manager
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-dump
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-restore
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yumdownloader

%if %{with deconflict}
# Deal with conflicts to unblock backports
mv %{buildroot}%{_bindir}/needs-restarting %{buildroot}%{_bindir}/dnfutils-needs-restarting
mv %{buildroot}%{_mandir}/man1/needs-restarting.1 %{buildroot}%{_mandir}/man1/dnfutils-needs-restarting.1
%endif

%if ! %{with copr_plugin}
# Delete if we're not shipping COPR plugin
rm -rf %{buildroot}%{_sysconfdir}/dnf/plugins/copr.d
rm -rf %{buildroot}%{_sysconfdir}/dnf/plugins/copr.conf
%endif

%if %{with tests}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=./plugins
/usr/bin/pytest-%{python3_version} -v -s tests/
%endif

%files
%license COPYING
%doc AUTHORS README.rst
%{_mandir}/man8/dnf-builddep.*
%{_mandir}/man8/dnf-changelog.*
%{_mandir}/man8/dnf-config-manager.*
%if %{with copr_plugin}
%{_mandir}/man8/dnf-copr.*
%config(noreplace) %{_sysconfdir}/dnf/plugins/copr.conf
%dir %{_sysconfdir}/dnf/plugins/copr.d
%else
%exclude %{_mandir}/man8/dnf-copr.*
%endif
%{_mandir}/man8/dnf-debug.*
%{_mandir}/man8/dnf-debuginfo-install.*
%{_mandir}/man8/dnf-download.*
%{_mandir}/man8/dnf-generate_completion_cache.*
%{_mandir}/man8/dnf-needs-restarting.*
%{_mandir}/man8/dnf-repoclosure.*
%{_mandir}/man8/dnf-repograph.*
%{_mandir}/man8/dnf-repomanage.*
%{_mandir}/man8/dnf-reposync.*
%{_mandir}/man8/dnf-repodiff.*
%dir %{_sysconfdir}/dnf/protected.d
%dir %{_var}/cache/dnf
%ghost %{_var}/cache/dnf/packages.db
%config(noreplace) %{_sysconfdir}/dnf/plugins/debuginfo-install.conf

%files lang -f %{name}.lang

%files -n python3-dnf-plugins-core
%license COPYING
%doc AUTHORS README.rst
%{python3_sitelib}/dnf-plugins/builddep.py
%{python3_sitelib}/dnf-plugins/changelog.py
%{python3_sitelib}/dnf-plugins/config_manager.py
%if %{with copr_plugin}
%{python3_sitelib}/dnf-plugins/copr.py
%else
%exclude %{python3_sitelib}/dnf-plugins/copr.*
%endif
%{python3_sitelib}/dnf-plugins/debug.py
%{python3_sitelib}/dnf-plugins/debuginfo-install.py
%{python3_sitelib}/dnf-plugins/download.py
%{python3_sitelib}/dnf-plugins/generate_completion_cache.py
%{python3_sitelib}/dnf-plugins/needs_restarting.py
%{python3_sitelib}/dnf-plugins/repoclosure.py
%{python3_sitelib}/dnf-plugins/repograph.py
%{python3_sitelib}/dnf-plugins/repomanage.py
%{python3_sitelib}/dnf-plugins/reposync.py
%{python3_sitelib}/dnf-plugins/repodiff.py
%{python3_sitelib}/dnfpluginscore/

%files -n %{yum_utils_subpackage_name}
%{_libexecdir}/dnf-utils
%{_mandir}/man1/dnf-utils.1*
%{_bindir}/debuginfo-install
%{_mandir}/man1/debuginfo-install.1*
%{_bindir}/%{?deconflict_prefix}needs-restarting
%{_mandir}/man1/%{?deconflict_prefix}needs-restarting.1*
%{_bindir}/find-repos-of-install
%{_bindir}/package-cleanup
%{_mandir}/man1/package-cleanup.1*
%{_bindir}/repo-graph
%{_mandir}/man1/repo-graph.1*
%{_bindir}/repoclosure
%{_mandir}/man1/repoclosure.1*
%{_bindir}/repodiff
%{_mandir}/man1/repodiff.1*
%{_bindir}/repomanage
%{_mandir}/man1/repomanage.1*
%{_bindir}/repoquery
%{_bindir}/reposync
%{_mandir}/man1/reposync.1*
%{_bindir}/repotrack
%{_bindir}/yum-builddep
%{_mandir}/man1/yum-builddep.1*
%{_bindir}/yum-config-manager
%{_mandir}/man1/yum-config-manager.1*
%{_bindir}/yum-debug-dump
%{_mandir}/man1/yum-debug-dump.1*
%{_bindir}/yum-debug-restore
%{_mandir}/man1/yum-debug-restore.1*
%{_bindir}/yumdownloader
%{_mandir}/man1/yumdownloader.1*
%{_mandir}/man1/yum-changelog.1*
%{_mandir}/man1/yum-utils.1*
%{_mandir}/man5/yum-versionlock.conf.5*
%{_mandir}/man8/yum-copr.8*
%{_mandir}/man8/yum-versionlock.8*

%files -n python3-dnf-plugin-leaves
%{python3_sitelib}/dnf-plugins/leaves.*
%{_mandir}/man8/dnf-leaves.*

%files -n python3-dnf-plugin-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python3_sitelib}/dnf-plugins/local.*
%{_mandir}/man8/dnf-local.*

%files -n python3-dnf-plugin-post-transaction-actions
%config(noreplace) %{_sysconfdir}/dnf/plugins/post-transaction-actions.conf
%dir %{_sysconfdir}/dnf/plugins/post-transaction-actions.d
%{python3_sitelib}/dnf-plugins/post-transaction-actions.*
%{_mandir}/man8/dnf-post-transaction-actions.*

%files -n python3-dnf-plugin-show-leaves
%{python3_sitelib}/dnf-plugins/show_leaves.*
%{_mandir}/man8/dnf-show-leaves.*

%files -n python3-dnf-plugin-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python3_sitelib}/dnf-plugins/versionlock.*
%{_mandir}/man8/dnf-versionlock.*

%changelog
