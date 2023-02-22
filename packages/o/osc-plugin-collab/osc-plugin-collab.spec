#
# spec file for package osc-plugin-collab
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2009 Vincent Untz <vuntz@opensuse.org>
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


%if %(if test -d %{_prefix}/lib/osc-plugins; then echo 1; else echo 0; fi)
%define oscplugindir %{_prefix}/lib/osc-plugins
%else
%define oscplugindir %{_localstatedir}/lib/osc-plugins
%endif
Name:           osc-plugin-collab
Version:        0.104+26
Release:        0
Summary:        Plugin to make collaboration easier with osc
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://en.opensuse.org/openSUSE:Osc_Collab
Source0:        %{name}-%{version}.tar.xz
Source1:        sysuser-osc-collab.conf
# Needed for directory ownership
BuildRequires:  osc
BuildRequires:  sysuser-tools
Requires:       osc >= 0.165.0
# osc gnome was part of osc-plugins-gnome
Conflicts:      osc-plugins-gnome <= 0.4.26
BuildArch:      noarch
%if !(0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?scientificlinux_version})
Recommends:     quilt
Recommends:     rpm-python3
Recommends:     xz
%else
Requires:       quilt
Requires:       rpm-python3
Requires:       xz
%endif

%description
This osc plugin extends osc with commands that makes it easier to use
the collaboration feature in the Build Service, and to keep up with
latest upstream versions.

%package -n osc-collab-server
Summary:        Server component for osc collab
Group:          Development/Tools/Other
Requires:       osc
Requires:       python3
Requires:       python3-feedparser
Requires:       python3-rpm
Requires:       python3-sgmllib3k
Requires:       python3-xml
Requires:       withlock
Requires:       user(osc-collab)

%description -n osc-collab-server
The server part of osc-plugin-collab, handles package reservations
and tracks in a database the various versions in devel projects, Factory
and upstream.

%package -n system-user-osc-collab
Summary:        System user for the osc-collab server component
Group:          System/Base
%sysusers_requires

%description -n system-user-osc-collab
System user for the osc-collab server component.

%prep
%autosetup

%build
%sysusers_generate_pre %{SOURCE1} sysuser-osc-collab

%install
install -D -m0644 osc-collab.py %{buildroot}%{oscplugindir}/osc-collab.py

mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/system-user-osc-collab.conf
install -d %{buildroot}%{_localstatedir}/lib/osc-collab
install -d %{buildroot}%{_datadir}/osc-collab-server
cp -r server %{buildroot}%{_datadir}/osc-collab-server

# Install default config file to /etc
mkdir -p %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/osc-collab-server/server/openSUSE-setup/collab-data/osc-collab.conf %{buildroot}%{_sysconfdir}

# Install run-scripts to /usr/lib/osc-collab-server
mkdir -p %{buildroot}%{_libexecdir}/osc-collab-server
mv %{buildroot}%{_datadir}/osc-collab-server/server/openSUSE-setup/cron-scripts/* %{buildroot}%{_libexecdir}/osc-collab-server

# And osc-collab-runner to /usr/bin
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/osc-collab-server/server/openSUSE-setup/osc-collab-runner %{buildroot}%{_bindir}

%pre -n system-user-osc-collab -f sysuser-osc-collab.pre

%files
%{oscplugindir}/osc-collab.py*

%files -n osc-collab-server
%attr(0700,osc-collab,root) %{_localstatedir}/lib/osc-collab
%{_datadir}/osc-collab-server
%{_bindir}/osc-collab-runner
%{_libexecdir}/osc-collab-server
%config %{_sysconfdir}/osc-collab.conf

%files -n system-user-osc-collab
%{_sysusersdir}/system-user-osc-collab.conf

%changelog
