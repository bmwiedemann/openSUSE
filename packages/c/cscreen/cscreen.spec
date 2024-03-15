#
# spec file for package cscreen
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


%define USERNAME _cscreen
%define HOMEDIR %_localstatedir/lib/cscreen
Name:           cscreen
Version:        1.7
Release:        0
Summary:        Console screen
License:        BSD-4-Clause
Group:          System/Management
URL:            https://github.com/openSUSE/cscreen
Source:         %name-%version.tar.xz
Source1:        %name-rpmlintrc
BuildRequires:  sudo
Recommends:     logrotate
Requires:       screen
Requires:       sudo
Requires(postun): coreutils
BuildRequires:  pkgconfig(systemd)
BuildRequires:  sysuser-tools
Requires(pre):  system-user-%name = %version-%release
%{?systemd_ordering}
BuildArch:      noarch

%description
This package allows to run multiple consoles in one 'screen' and
to start the screen automatically during boot.

%package -n system-user-%name
Summary:        System user %USERNAME
Requires(pre):  group(dialout)
Requires(pre):  group(tty)
%?sysusers_requires

%description -n system-user-%name
System user %USERNAME

%prep
%autosetup -p1
#
%build
#
%install
> %name.files
if ! test -d %_sysconfdir/sudoers.d
then
  echo '%%dir %_sysconfdir/sudoers.d' >> %name.files
fi
mkdir -p %buildroot/%_sbindir

install -Dm644 systemd/cscreen.service %buildroot/%_unitdir/cscreend.service
pushd %buildroot/%_sbindir
ln -sf service %buildroot%_sbindir/rccscreend
popd
mkdir -vp %buildroot%_tmpfilesdir
tee %buildroot%_tmpfilesdir/%name.conf <<'_EOF_'
d %_rundir/%name 0750 %USERNAME %USERNAME -
_EOF_
suc='system-user-%name.conf'
tee "${suc}" <<'_EOC_'
u %USERNAME - "cscreen daemon user" %HOMEDIR /bin/bash
m %USERNAME dialout
m %USERNAME tty
_EOC_
mkdir -p '%buildroot%_sysusersdir'
cp -avLt "$_" "${suc}"
%sysusers_generate_pre "${suc}" system-user-%name

install -Dm640 configs/cscreen.config %buildroot/%_sysconfdir/cscreenrc
install -Dm644 configs/cscreen.logrotate %buildroot/%_sysconfdir/logrotate.d/%name
install -Dm644 configs/cscreen.sudoers %buildroot%_sysconfdir/sudoers.d/%name
install -Dm755 src/cscreen-shell %buildroot/%_datadir/%name/cscreen-shell
install -Dm755 src/cscreen %buildroot/%_bindir/%name
install -Dm755 src/cscreen_update_config.sh %buildroot/%_bindir/cscreen_update_config.sh

mkdir -p %buildroot%_localstatedir/log/screen/old
mkdir -pm700 %buildroot/%HOMEDIR
mkdir -pm700 %buildroot/%HOMEDIR/.ssh

%pre
%service_add_pre cscreend.service

%post
%service_add_post cscreend.service
%tmpfiles_create %_tmpfilesdir/%name.conf

%preun
%service_del_preun cscreend.service

%postun
%if %{defined service_del_postun_without_restart}
%service_del_postun_without_restart cscreend.service
%else
DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun cscreend.service
%endif
if [ -d /run/uscreens/S-cscreen ];then
    if [ "$1" = "0" ];then
	# Only delete on uninstall
	rm -rf /run/uscreens/S-cscreen
    fi
fi

%pre -n system-user-%name -f system-user-%name.pre
%files -n system-user-%name
%_sysusersdir/*.conf

%files -f %name.files
%doc docs/motd_example
%if 0%{?suse_version} > 1320
%license License
%endif
%_bindir/%name
%_bindir/cscreen_update_config.sh
%_datadir/%name
%_tmpfilesdir/%name.conf
%_unitdir/cscreend.service
%_sbindir/rccscreend

%attr(0640,root,root) %config %_sysconfdir/sudoers.d/%name
%attr(755,%{USERNAME}, %{USERNAME}) %dir %_localstatedir/log/screen
%attr(755,%{USERNAME}, %{USERNAME}) %dir %_localstatedir/log/screen/old
%attr(700,%{USERNAME}, %{USERNAME}) %dir %HOMEDIR
%attr(700,%{USERNAME}, %{USERNAME}) %dir %HOMEDIR/.ssh
%attr(644,%{USERNAME}, %{USERNAME}) %config(noreplace) %_sysconfdir/cscreenrc
%config(noreplace) %_sysconfdir/logrotate.d/%name

%changelog
