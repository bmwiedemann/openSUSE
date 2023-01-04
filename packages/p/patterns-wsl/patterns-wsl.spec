#
# spec file for package patterns-wsl
#
# Copyright (c) 2022 SUSE LLC
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


Name:           patterns-wsl
Version:        20221221
Release:        0
Summary:        Recommended packages for Windows Subsystem for Linux, WSL, WSLg
License:        MIT
Group:          Metapackages
URL:            https://github.com/sbradnick/patterns
BuildRequires:  patterns-rpm-macros
BuildRequires:  systemd
BuildRequires:  udev
BuildArch:      noarch

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

# ----

%package base
%pattern_development
Summary:        Base WSL packages
Group:          Metapackages
Provides:       pattern() = wsl_base
Provides:       pattern-icon() = pattern-generic
#Provides:       pattern-order() = ?
Provides:       pattern-visible()
Requires:       bash
Recommends:     fish
Recommends:     zsh

%description base
This package contains the wsl_base pattern: recommended configs,tools,libraries for using WSL.

%pre base
if [[ -f %{_sysconfdir}/wsl.conf && ! -L %{_sysconfdir}/wsl.conf ]];
then
  %{_bindir}/echo "* [wsl_base] Creating backup for %{_sysconfdir}/wsl.conf.wsl_base ..."
  cp -v %{_sysconfdir}/wsl.conf %{_sysconfdir}/wsl.conf.wsl_base
  BOOT_COUNT=$(%{_bindir}/grep -c "\[boot\]" %{_sysconfdir}/wsl.conf.wsl_base)
  if [[ $BOOT_COUNT -gt 0 ]];
  then
    COMMAND_COUNT=$(%{_bindir}/grep -c "^command" %{_sysconfdir}/wsl.conf.wsl_base)
    if [[ $COMMAND_COUNT -gt 0 ]];
    then
      %{_bindir}/echo "* [wsl_base] Entry exists for 'command'; chaining in new item ..."
      EXISTING_COMMAND=$(%{_bindir}/grep "^command" %{_sysconfdir}/wsl.conf.wsl_base | %{_bindir}/cut -d= -f2-)
      %{_bindir}/sed -i /^command/d %{_sysconfdir}/wsl.conf.wsl_base
      %{_bindir}/sed -i 's,\[boot\],\[boot\]\n# adjusted by wsl_base pattern\ncommand=/usr/sbin/sysctl -w net.ipv4.ping_group_range=\\\"0 2147483647\\\" ; '"$EXISTING_COMMAND"'\n# END: wsl_base pattern edit,g' %{_sysconfdir}/wsl.conf.wsl_base
    fi
  else
    %{_bindir}/echo "* [wsl_base] File existed, but no [boot]; adjusting %{_sysconfdir}/wsl.conf.wsl_base ..."
    %{_bindir}/echo -e "# added by wsl_base pattern\n[boot]\ncommand=/usr/sbin/sysctl -w net.ipv4.ping_group_range=\\\"0 2147483647\\\"\n# END: wsl_base pattern edit" >> %{_sysconfdir}/wsl.conf.wsl_base
  fi
elif [[ -f %{_sysconfdir}/wsl.conf && -L %{_sysconfdir}/wsl.conf ]];
then
  %{_bindir}/echo "* [wsl_base] Current %{_sysconfdir}/wsl.conf is a symlink ; ensure contents you want are copied to a non-symlink %{_sysconfdir}/wsl.conf and reinstall the pattern ..."
else
  %{_bindir}/echo "* [wsl_base] No file existed; adding %{_sysconfdir}/wsl.conf.wsl_base ..."
  %{_bindir}/echo -e "# added by wsl_base pattern\n[boot]\ncommand=/usr/sbin/sysctl -w net.ipv4.ping_group_range=\\\"0 2147483647\\\"\n# END: wsl_base pattern edit" > %{_sysconfdir}/wsl.conf.wsl_base
fi

%post base
if [[ -e %{_sysconfdir}/wsl.conf.wsl_base ]];
then
  ln -sf %{_sysconfdir}/wsl.conf.wsl_base %{_sysconfdir}/wsl.conf
fi

%files base
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_base.txt

# ----

%package gui
%pattern_development
Summary:        WSL GUI packages
Group:          Metapackages
Provides:       pattern() = wsl_gui
Provides:       pattern-icon() = pattern-generic
#Provides:       pattern-order() = ?
Provides:       pattern-visible()
Requires:       lato-fonts
Recommends:     adwaita-icon-theme
Recommends:     gnome-icon-theme
Recommends:     noto-sans-fonts
Recommends:     powerline-fonts
Recommends:     xeyes

%description gui
This package contains the wsl_gui pattern: recommended configs,tools,libraries for using WSLg.

%pre gui
if [[ -f %{_sysconfdir}/wsl.conf && ! -L %{_sysconfdir}/wsl.conf ]];
then
  %{_bindir}/echo "* [wsl_gui] Creating backup for %{_sysconfdir}/wsl.conf.wsl_gui ..."
  cp -v %{_sysconfdir}/wsl.conf %{_sysconfdir}/wsl.conf.wsl_gui
  BOOT_COUNT=$(%{_bindir}/grep -c "\[boot\]" %{_sysconfdir}/wsl.conf.wsl_gui)
  if [[ $BOOT_COUNT -gt 0 ]];
  then
    COMMAND_COUNT=$(%{_bindir}/grep -c "^command" %{_sysconfdir}/wsl.conf.wsl_gui)
    if [[ $COMMAND_COUNT -gt 0 ]];
    then
      %{_bindir}/echo "* [wsl_gui] Entry exists for 'command'; chaining in new item ..."
      EXISTING_COMMAND=$(%{_bindir}/grep "^command" %{_sysconfdir}/wsl.conf.wsl_gui | %{_bindir}/cut -d= -f2-)
      %{_bindir}/sed -i /^command/d %{_sysconfdir}/wsl.conf.wsl_gui
      %{_bindir}/sed -i 's,\[boot\],\[boot\]\n# adjusted by wsl_gui pattern\ncommand=/usr/sbin/sysctl -w net.ipv4.ping_group_range=\\\"0 2147483647\\\" ; '"$EXISTING_COMMAND"'\n# END: wsl_gui pattern edit,g' %{_sysconfdir}/wsl.conf.wsl_gui
    fi
  else
    %{_bindir}/echo "* [wsl_gui] File existed, but no [boot]; adjusting %{_sysconfdir}/wsl.conf.wsl_gui ..."
    %{_bindir}/echo -e "# added by wsl_gui pattern\n[boot]\ncommand=/usr/sbin/sysctl -w net.ipv4.ping_group_range=\\\"0 2147483647\\\"\n# END: wsl_gui pattern edit" >> %{_sysconfdir}/wsl.conf.wsl_gui
  fi
elif [[ -f %{_sysconfdir}/wsl.conf && -L %{_sysconfdir}/wsl.conf ]];
then
  %{_bindir}/echo "* [wsl_gui] Current %{_sysconfdir}/wsl.conf is a symlink ; ensure contents you want are copied to a non-symlink %{_sysconfdir}/wsl.conf and reinstall the pattern ..."
else
  %{_bindir}/echo "* [wsl_gui] No file existed; adding %{_sysconfdir}/wsl.conf.wsl_gui ..."
  %{_bindir}/echo -e "# added by wsl_gui pattern\n[boot]\ncommand=/usr/sbin/sysctl -w net.ipv4.ping_group_range=\\\"0 2147483647\\\"\n# END: wsl_gui pattern edit" > %{_sysconfdir}/wsl.conf.wsl_gui
fi

%post gui
if [[ -e %{_sysconfdir}/wsl.conf.wsl_gui ]];
then
  ln -sf %{_sysconfdir}/wsl.conf.wsl_gui %{_sysconfdir}/wsl.conf
fi

%files gui
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_gui.txt

# ----

%package systemd
%pattern_development
Summary:        WSL systemd setup
Group:          Metapackages
Provides:       pattern() = wsl_systemd
Provides:       pattern-icon() = pattern-generic
#Provides:       pattern-order() = ?
Provides:       pattern-visible()
Requires:       systemd

%description systemd
This package contains the wsl_systemd pattern: adjusts or provides %{_sysconfdir}/wsl.conf and /sbin/init symlink where required.

%pre systemd -p /bin/bash
if [[ ! -L /sbin/init ]];
then
  %{_bindir}/echo "* [wsl_systemd] Adding /sbin/init -> /usr/lib/systemd/systemd symlink."
  %{_bindir}/ln -s %{_systemd_util_dir}/systemd /sbin/init
fi
if [[ -f %{_sysconfdir}/wsl.conf && ! -L %{_sysconfdir}/wsl.conf ]];
then
  %{_bindir}/echo "* [wsl_systemd] Creating backup for %{_sysconfdir}/wsl.conf.wsl_systemd ..."
  cp -v %{_sysconfdir}/wsl.conf %{_sysconfdir}/wsl.conf.wsl_systemd
  BOOT_COUNT=$(%{_bindir}/grep -c "\[boot\]" %{_sysconfdir}/wsl.conf.wsl_systemd)
  if [[ $BOOT_COUNT -gt 0 ]];
  then
    COMMAND_COUNT=$(%{_bindir}/grep -c "^command" %{_sysconfdir}/wsl.conf.wsl_systemd)
    if [[ $COMMAND_COUNT -gt 0 ]];
    then
      %{_bindir}/echo "* [wsl_systemd] Entry exists for 'command'; looking for and removing ping_group_range (if found) ..."
      CMDS_TO_KEEP=""
      PREEXISTING_COMMANDS=$(%{_bindir}/grep ^command %{_sysconfdir}/wsl.conf.wsl_systemd | %{_bindir}/cut -d= -f2- | %{_bindir}/awk -F';' '{for (i=1; i<=NF; ++i) {print $i}}')
      while read -r line
      do
        LINE_CHECK=$(%{_bindir}/echo $line | grep -v ping_group_range)
        if [[ ! -z $LINE_CHECK ]];
        then
          if [[ -z $CMDS_TO_KEEP ]];
          then
            CMDS_TO_KEEP=$(%{_bindir}/echo "$LINE_CHECK")
          else
            CMDS_TO_KEEP=$(%{_bindir}/echo "$CMDS_TO_KEEP ; $LINE_CHECK")
          fi
        fi
      done <<< "$PREEXISTING_COMMANDS"
      %{_bindir}/sed -i 's,^command.*$,command='"$CMDS_TO_KEEP"',g' %{_sysconfdir}/wsl.conf.wsl_systemd
    fi
    %{_bindir}/echo "* [wsl_systemd] Adjusting %{_sysconfdir}/wsl.conf.wsl_systemd ..."
    %{_bindir}/sed -i 's,\[boot\],\[boot\]\n# adjusted by wsl_systemd pattern\nsystemd=true\n# END: wsl_systemd pattern edit,g' %{_sysconfdir}/wsl.conf.wsl_systemd
  else
    %{_bindir}/echo "* [wsl_systemd] File existed, but no [boot]; adjusting %{_sysconfdir}/wsl.conf.wsl_systemd ..."
    %{_bindir}/echo -e "# added by wsl_systemd pattern\n[boot]\nsystemd=true\n# END: wsl_systemd pattern edit" >> %{_sysconfdir}/wsl.conf.wsl_systemd
  fi
elif [[ -f %{_sysconfdir}/wsl.conf && -L %{_sysconfdir}/wsl.conf ]];
then
  %{_bindir}/echo "* [wsl_systemd] Current %{_sysconfdir}/wsl.conf is a symlink ; ensure contents you want are copied to a non-symlink %{_sysconfdir}/wsl.conf and reinstall the pattern ..."
else
  %{_bindir}/echo "* [wsl_systemd] No file existed; adding %{_sysconfdir}/wsl.conf.wsl_systemd ..."
  %{_bindir}/echo -e "# added by wsl_systemd pattern\n[boot]\nsystemd=true\n# END: wsl_systemd pattern edit" > %{_sysconfdir}/wsl.conf.wsl_systemd
fi

%post systemd
if [[ -e %{_sysconfdir}/wsl.conf.wsl_systemd ]];
then
  ln -sf %{_sysconfdir}/wsl.conf.wsl_systemd %{_sysconfdir}/wsl.conf
fi

%files systemd
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_systemd.txt

# ----

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_base to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_base.txt
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_gui to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_gui.txt
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_systemd to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_systemd.txt

%changelog

