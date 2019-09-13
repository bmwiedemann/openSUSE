#
# spec file for package yum-utils
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           yum-utils
BuildRequires:  python-devel
Version:        1.1.13
Release:        48
License:        GPL-2.0+
Group:          System/Packages
Summary:        Utilities based around the yum package manager
Source:         %{name}-%{version}.tar.bz2
Patch:          %{name}-1.1.6.patch
Patch1:         yum-utils-1.1.6-changelog.patch
Patch2:         yum-utils-1.1.10.patch
Url:            http://linux.duke.edu/yum/download/yum-utils/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       yum >= 3.1.1
%if 0%{?suse_version} > 1030
%py_requires
%endif

%description
yum-utils is a collection of utilities and examples for the yum package
manager. It includes utilities by different authors that make yum
easier and more powerful to use.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-changelog
License:        GPL-2.0+
Summary:        Yum plugin for viewing package changelogs before/after updating
Group:          System/Packages
Requires:       yum >= 3.0
Requires:       python-dateutil

%description -n yum-changelog
This plugin adds a command line option to allow viewing package
changelog deltas before or after updating packages.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-fastestmirror
License:        GPL-2.0+
Summary:        Yum plugin which chooses fastest repository from a mirrorlist
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-fastestmirror
This plugin sorts each repository's mirrorlist by connection speed
prior to downloading packages.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-protectbase
License:        GPL-2.0+
Summary:        Yum plugin to protect packages from certain repositories
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-protectbase
This plugin allows certain repositories to be protected. Packages in
the protected repositories can't be overridden by packages in
non-protected repositories even if the non-protected repo has a later
version.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-versionlock
License:        GPL-2.0+
Summary:        Yum plugin to lock specified packages from being updated
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-versionlock
This plugin allows certain packages specified in a file to be protected
from being updated by newer versions.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-tsflags
License:        GPL-2.0+
Summary:        Yum plugin to add tsflags by a commandline option
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-tsflags
This plugin allows you to specify optional transaction flags on the yum
command line



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-downloadonly
License:        GPL-2.0+
Summary:        Yum plugin to add downloadonly command option
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-downloadonly
This plugin adds a --downloadonly flag to yum so that yum will only
download the packages and not install/update them.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-allowdowngrade
License:        GPL-2.0+
Summary:        Yum plugin to enable manual downgrading of packages
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-allowdowngrade
This plugin adds a --allow-downgrade flag to yum to make it possible to
manually downgrade packages to specific versions.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-priorities
License:        GPL-2.0+
Summary:        Plugin to give priorities to packages from different repos
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-priorities
This plugin allows repositories to have different priorities. Packages
in a repository with a lower priority can't be overridden by packages
from a repository with a higher priority even if repo has a later
version.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-merge-conf
License:        GPL-2.0+
Summary:        Yum plugin to merge configuration changes when installing packages
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-merge-conf
This yum plugin adds the "--merge-conf" command line option. With this
option, Yum will ask you what to do with config files which have
changed on updating a package.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-protect-packages
License:        GPL-2.0+
Summary:        Yum plugin to prevents Yum from removing itself and other protected packages
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-protect-packages
This plugin prevents Yum from removing itself and other protected
packages. By default, yum is the only package protected, but by
extension this automatically protects everything on which yum depends
(rpm, python, glibc, and so on).Therefore, the plugin functions well
even without compiling careful lists of all important packages.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-basearchonly
License:        GPL-2.0+
Summary:        Yum plugin to let Yum install only basearch packages
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-basearchonly
This plugin makes Yum only install basearch packages on multiarch
systems. If you type 'yum install foo' on a x68_64 system, only
'foo-x.y.x86_46.rpm' is If you want to install the foo-x.y.i386.rpm,
you have to type 'yum install foo. The plugin only works with 'yum
install'.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-aliases
License:        GPL-2.0+
Summary:        Yum plugin to enable aliases filters
Group:          System/Packages
Requires:       yum >= 3.0.5

%description -n yum-aliases
This plugin adds the command alias, and parses the aliases config. file
to enable aliases.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-list-data
License:        GPL-2.0+
Summary:        Yum plugin to list aggregate package data
Group:          System/Packages
Requires:       yum >= 3.0.5

%description -n yum-list-data
This plugin adds the commands list- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-filter-data
License:        GPL-2.0+
Summary:        Yum plugin to list filter based on package data
Group:          System/Packages
Requires:       yum >= 3.0.5

%description -n yum-filter-data
This plugin adds the options --filter- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes. Note that each package must match at
least one pattern/range in each category, if any were specified.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-refresh-updatesd
License:        GPL-2.0+
Summary:        Tell yum-updatesd to check for updates when yum exits
Group:          System/Packages
Requires:       yum >= 3.0
Requires:       yum-updatesd

%description -n yum-refresh-updatesd
yum-refresh-updatesd tells yum-updatesd to check for updates when yum
exits. This way, if you run 'yum update' and install all available
updates, puplet will almost instantly update itself to reflect this.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-tmprepo
License:        GPL-2.0+
Summary:        Yum plugin to add temporary repositories
Group:          System/Packages
Requires:       yum >= 3.2.11

%description -n yum-tmprepo
This plugin adds the option --tmprepo which takes a url to a .repo file
downloads it and enables it for a single run. This plugin tries to
ensure that temporary repositories are safe to use, by default, by not
allowing gpg checking to be disabled.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-upgrade-helper
License:        GPL-2.0+
Summary:        Yum plugin to help upgrades to the next distribution version
Group:          System/Packages
Requires:       yum >= 3.0

%description -n yum-upgrade-helper
this plugin allows yum to erase specific packages on install/update
based on an additional metadata file in repositories. It is used to
simplify distribution upgrade hangups.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%package -n yum-verify
License:        GPL-2.0+
Summary:        Yum plugin to add verify command, and options
Group:          System/Packages
Requires:       yum >= 3.2.12

%description -n yum-verify
This plugin adds the commands verify, verify-all and verify-rpm. There
are also a couple of options. This command works like rpm -V, to verify
your installation.



Authors:
--------
    Gijs Hollestelle <gijs@gewis.nl>
    Seth Vidal <skvidal@phy.duke.edu>
    Panu Matilainen <pmatilai@laiskiainen.org>
    Sean Dilda <sean@duke.edu>

%prep
%setup -q
%patch
%patch1
%patch2

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install
plugins="changelog fastestmirror protectbase versionlock tsflags downloadonly allowdowngrade priorities merge-conf protect-packages basearchonly aliases list-data filter-data refresh-updatesd tmprepo upgrade-helper verify"
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/ $RPM_BUILD_ROOT/usr/lib/yum-plugins/
cd plugins
for plug in $plugins; do
    install -m 644 $plug/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/
    install -m 644 $plug/*.py $RPM_BUILD_ROOT/usr/lib/yum-plugins/
done
install -m 644 aliases/aliases $RPM_BUILD_ROOT/%{_sysconfdir}/yum/aliases.conf
install -m 644 versionlock/versionlock.list $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/
# not packaged plugin
rm $RPM_BUILD_ROOT/%{_mandir}/man8/yum-security.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README 
%dir %{_sysconfdir}/yum
%dir %{_sysconfdir}/yum/pluginconf.d
%dir /usr/lib/yum-plugins
%{_bindir}/debuginfo-install
%{_bindir}/package-cleanup
%{_bindir}/repoclosure
%{_bindir}/repodiff
%{_bindir}/repomanage
%{_bindir}/repoquery
%{_bindir}/repotrack
%{_bindir}/reposync
%{_bindir}/repo-graph
%{_bindir}/repo-rss
%{_bindir}/yumdownloader
%{_bindir}/yum-builddep
%{_sbindir}/yum-complete-transaction
%{_mandir}/man1/yum-utils.1.*
%{_mandir}/man1/package-cleanup.1.*
%{_mandir}/man1/repo-rss.1.*
%{_mandir}/man1/repoquery.1.*
%{_mandir}/man1/reposync.1.*
%{_mandir}/man1/yum-builddep.1.*
%{_mandir}/man8/yum-complete-transaction.8.*
%{_mandir}/man1/yumdownloader.1.*

%files -n yum-changelog
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/changelog.conf
/usr/lib/yum-plugins/changelog.*
%{_mandir}/man1/yum-changelog.1.*
%{_mandir}/man5/yum-changelog.conf.5.*

%files -n yum-fastestmirror
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/fastestmirror.conf
/usr/lib/yum-plugins/fastestmirror.*

%files -n yum-protectbase
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/protectbase.conf
/usr/lib/yum-plugins/protectbase.*

%files -n yum-versionlock
%defattr(-, root, root)
%doc plugins/versionlock/README
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/versionlock.conf
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/versionlock.list
/usr/lib/yum-plugins/versionlock.*

%files -n yum-tsflags
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/tsflags.conf
/usr/lib/yum-plugins/tsflags.*

%files -n yum-downloadonly
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/downloadonly.conf
/usr/lib/yum-plugins/downloadonly.*

%files -n yum-allowdowngrade
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/allowdowngrade.conf
/usr/lib/yum-plugins/allowdowngrade.*

%files -n yum-priorities
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/priorities.conf
/usr/lib/yum-plugins/priorities.*

%files -n yum-merge-conf
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/merge-conf.conf
/usr/lib/yum-plugins/merge-conf.*

%files -n yum-protect-packages
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/protect-packages.conf
/usr/lib/yum-plugins/protect-packages.*

%files -n yum-basearchonly
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/basearchonly.conf
/usr/lib/yum-plugins/basearchonly.*

%files -n yum-refresh-updatesd
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/refresh-updatesd.conf
/usr/lib/yum-plugins/refresh-updatesd.*

%files -n yum-upgrade-helper  
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/upgrade-helper.conf  
/usr/lib/yum-plugins/upgrade-helper.*  

%files -n yum-aliases   
%defattr(-, root, root)   
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/aliases.conf   
%config(noreplace) %{_sysconfdir}/yum/aliases.conf
/usr/lib/yum-plugins/aliases.*

%files -n yum-list-data
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/list-data.conf
/usr/lib/yum-plugins/list-data.*
%{_mandir}/man1/yum-list-data.1.*

%files -n yum-filter-data
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/filter-data.conf
/usr/lib/yum-plugins/filter-data.*
%{_mandir}/man1/yum-filter-data.1.*

%files -n yum-tmprepo
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/tmprepo.conf
/usr/lib/yum-plugins/tmprepo.*

%files -n yum-verify
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/verify.conf
/usr/lib/yum-plugins/verify.*
%{_mandir}/man1/yum-verify.1.*

%changelog
