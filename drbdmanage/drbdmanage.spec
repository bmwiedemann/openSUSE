#
# spec file for package drbdmanage
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           drbdmanage
Version:        0.99.18
Release:        0
Summary:        DRBD distributed resource management utility
License:        GPL-3.0
Group:          Productivity/Clustering/HA
Url:            http://www.drbd.org/en/comp/drbdmanage
#Prebuild drbdmanage with man pages packed.
#python setup.py build_man
Source0:        http://www.linbit.com/downloads/drbdmanage/%{name}-%{version}.tar.gz
Patch0:         change_unitdir.patch
Patch1:         Add-no-discard-stderr-to-help2man.patch
BuildRequires:  python-devel

#For buinding man pages
BuildRequires:  dbus-1-python
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  help2man
BuildRequires:  libxslt-tools
BuildRequires:  python-gobject2

Requires:       dbus-1-python
Requires:       drbd-utils >= 8.9.7
Requires:       python-gobject2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Drbdmanage is a daemon and a command line utility that manages DRBD
replicated LVM volumes across a group of machines.
It maintains DRBD configuration an the participating machines. It
creates/deletes the backing LVM volumes. It automatically places
the backing LVM volumes among the participating machines.

%prep
%setup -q
%patch0 -p1
# Fix error: help2man: can't get `--help' info from ./drbdmanage_client.py add-node
# Try `--no-discard-stderr' if option outputs to stderr
%patch1 -p1
#Remove unwanted shebang for rpmlint: non-executable-script
#sed -i '/^#!/d' drbdmanage{*,/drbd/*,/storage/*,/snapshots/*,/plugins/*,/conf/*,/*}.py
#Remove it expliclit expliclitly
sed -i '/^#!/d' drbdmanage/persistence.py \
                drbdmanage/quorum.py \
                drbdmanage/drbd/drbdcore.py \
                drbdmanage/defaultip.py \
                drbdmanage/drbd/persistence.py \
                drbdmanage/storage/lvm_thinlv.py \
                drbdmanage/storage/header.py \
                drbdmanage/utils.py \
                drbdmanage/storage/lvm_common.py \
                drbdmanage/drbd/views.py \
                drbdmanage/exceptions.py \
                drbdmanage/proxy.py \
                drbdmanage/snapshots/views.py \
                drbdmanage/propscontainer.py \
                drbdmanage_server.py \
                drbdmanage/plugins/plugin.py \
                drbdmanage/storage/persistence.py \
                drbdmanage/storage/storagecore.py \
                drbdmanage/server.py \
                drbdmanage/conf/conffile.py \
                drbdmanage_client.py \
                drbdmanage/snapshots/persistence.py \
                drbdmanage/storage/storageplugin_common.py \
                drbdmanage/storage/storagecommon.py \
                drbdmanage/consts.py \
                drbdmanage/storage/zvol.py \
                drbdmanage/dbusserver.py \
                drbdmanage/drbd/drbdcommon.py \
                drbdmanage/snapshots/snapshots.py \
                drbdmanage/deployers.py \
                drbdmanage/storage/lvm.py \
                drbdmanage/storage/lvm_thinpool.py \
                drbdmanage/drbd/metadata.py \
                drbdmanage/drbd/commands.py \
                drbdmanage/dbustracer.py \
                drbdmanage/storage/zvol_thinlv.py \
                drbdmanage/messagelog.py

%build
#make all
python setup.py build_man
python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix} --record=INSTALLED_FILES
cat INSTALLED_FILES

mkdir -p %{buildroot}/%{_sbindir}
ln -fs %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}d

%pre
%service_add_pre drbdmanaged.service

%post
%service_add_post drbdmanaged.service

%preun
%service_del_preun drbdmanaged.service

%postun
%service_del_postun drbdmanaged.service

%files
%defattr(-,root,root)
%{python_sitelib}
%{_bindir}/drbdmanage
%{_bindir}/dbus-drbdmanaged-service
%{_mandir}/man8/drbdmanage-*
%{_mandir}/man8/drbdmanage.*
%{_datadir}/dbus-1/system-services/org.drbd.drbdmanaged.service
%config %{_sysconfdir}/dbus-1/system.d/org.drbd.drbdmanaged.conf
%config %{_sysconfdir}/bash_completion.d/drbdmanage
%config %{_sysconfdir}/drbd.d/drbdctrl.res_template
%config(noreplace) %{_sysconfdir}/drbd.d/drbdmanage-resources.res
%config(noreplace) %{_sysconfdir}/drbdmanaged.cfg
%{_localstatedir}/lib/drbdmanage
%dir %{_sysconfdir}/dbus-1/
%dir %{_sysconfdir}/dbus-1/system.d/
%dir %{_sysconfdir}/drbd.d/
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system-services/
%{_unitdir}/drbdmanaged.service
%{_sbindir}/rc%{name}d

%changelog
