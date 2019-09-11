#
# spec file for package clone-master-clean-up
#
# Copyright (c) 2017 SUSE LLC
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

Name:           clone-master-clean-up
Version:        1.4
Release:        0
License:        GPL-2.0+
Summary:        Clean up a system for cloning preparation
Url:            https://www.suse.com
Group:          System/Management
Source0:        clone-master-clean-up.sh
Source1:        clone-master-clean-up.1
Source2:        sysconfig.clone-master-clean-up
Source3:        custom_remove.template
Source10:       LICENSE
Source11:       README.md
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       systemd sed curl coreutils
Requires(post): %fillup_prereq
BuildArch:      noarch

%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif


%description
Clean up a system for cloning preparation by cleaning up usage history and log files, etc.

%prep

%build
cp %{S:10} %{S:11} .

%install
mkdir -p %{buildroot}%{_sbindir}
install -m700 %{S:0} %{buildroot}/%{_sbindir}/clone-master-clean-up
# manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 %{S:1} %{buildroot}/%{_mandir}/man1/clone-master-clean-up.1
# sysconfig file
mkdir -p %{buildroot}%{_fillupdir}
install -m644 %{S:2} %{buildroot}/%{_fillupdir}/sysconfig.clone-master-clean-up
# template
mkdir -p %{buildroot}/%{_datadir}/%{name}/
install -m644 %{S:3} %{buildroot}/%{_datadir}/%{name}/custom_remove.template
# custom_remove file location
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/

%post
%fillup_only -n clone-master-clean-up

%files
%doc %{basename:%{S:11}}
%license %{basename:%{S:10}}
%{_sbindir}/*
%{_mandir}/man1/*
%{_fillupdir}/*
%dir %{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_datadir}/%{name}/custom_remove.template
%ghost %config %{_sysconfdir}/%{name}/custom_remove
