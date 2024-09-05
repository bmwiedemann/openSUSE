#
# spec file for package system-user-grommunio
#
# Copyright (c) 2024 SUSE LLC
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


Name:           system-user-grommunio
Version:        10
Release:        0
Summary:        General grommunio system user identities
License:        MIT
Group:          System/Fhs
URL:            https://grommunio.com/
Source:         system-user-grommunio.conf
Source2:        dummy_for_debtransform.tgz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Obsoletes:      system-user-groweb < %version-%release
Provides:       system-user-groweb = %version-%release
%if 0%{?suse_version}
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  /usr/sbin/useradd
Requires(pre):  /usr/sbin/groupadd
%endif

%description
This package provides identities related to the Grommunio groupware suite:
* the "grommunio" user identity for running the Administration API
  (usually an uwsgi process instance); AAPI needs to read
  mysql_adaptor.cfg and ldap_adaptor.cfg, so is added to group
  gromoxcf
* the "groweb" user identity for running PHP-FPM workers
* the "groweb" group identity for marking data to be consumed by the
  groweb identity but also created by grommunio-index, e.g. groweb
  search indexes
* the "groindex" user identity for running the indexer service; this
  needs to read mysql_adaptor.cfg so is added to group gromoxcf

%prep

%build
>user.pre
%if 0%{?suse_version}
%sysusers_generate_pre %_sourcedir/system-user-grommunio.conf user system-user-grommunio.conf
%endif

%install
install -Dpm0644 %_sourcedir/system-user-grommunio.conf "%buildroot/%_sysusersdir/system-user-grommunio.conf"

%pre -f user.pre
%if 0%{?rhel} || 0%{?fedora_version}
%sysusers_create_compat %_sourcedir/system-user-grommunio.conf
%endif

%files
%_sysusersdir/*.conf

%changelog
