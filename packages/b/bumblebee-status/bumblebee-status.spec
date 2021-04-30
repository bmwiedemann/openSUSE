#
# spec file for package bumblebee-status
#
# Copyright (c) 2021 SUSE LLC
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


%define pythons python3
Name:           bumblebee-status
Version:        2.1.4
Release:        0
Summary:        Modular, theme-able status line generator for the i3 window manager
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/tobi-wan-kenobi/bumblebee-status
Source0:        https://github.com/tobi-wan-kenobi/bumblebee-status/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         use-python-3.patch
Patch2:         import_fix.patch
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Pillow-tk}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module i3ipc}
BuildRequires:  %{python_module libvirt-python}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module netifaces}
BuildRequires:  %{python_module power}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pygit2}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-yubico}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module pyusb}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module suntime}
BuildRequires:  %{python_module taskw}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  %{python_module xkbgroup}
BuildRequires:  NetworkManager
BuildRequires:  alsa-utils
BuildRequires:  iputils
BuildRequires:  libnotify-tools
BuildRequires:  password-store
BuildRequires:  pavucontrol
BuildRequires:  playerctl
BuildRequires:  progress
BuildRequires:  psmisc
BuildRequires:  pulseaudio-utils
BuildRequires:  python-rpm-macros
BuildRequires:  sensors
BuildRequires:  setxkbmap
BuildRequires:  smartmontools
BuildRequires:  speedtest-cli
BuildRequires:  sudo
BuildRequires:  systemd
BuildRequires:  wireless-tools
BuildRequires:  xdg-utils
BuildRequires:  xdotool
BuildRequires:  xprop
BuildRequires:  xrandr
BuildRequires:  xset
# bluetooth, bluetooth2, deezer, spotify, etc use dbus-send
Requires:       dbus-1
# In earlier i3 versions, blocks won't have background colors
Requires:       i3 >= 4.12
# psmisc provides killall, etc used by many modules
Requires:       psmisc
Requires:       python3 >= 3.4
Requires:       python3-dbus-python
Requires:       python3-netifaces
Requires:       python3-power
Requires:       python3-psutil
Requires:       python3-pytz
Requires:       python3-requests
Requires:       python3-tzlocal
Requires:       sudo
# xdg-utils provides xdg-open, used by several modules,
# and provides xdg-screensaver used by caffeine
Requires:       xdg-utils
# gnome-system-monitor is a click action for core cpu, load and memory modules
Recommends:     gnome-system-monitor
# iputils required by module ping
Recommends:     iputils
# wireless-tools provides iwgetid, used by core module nic
Recommends:     wireless-tools
Recommends:     bumblebee-status-module-caffeine = %{version}
Recommends:     bumblebee-status-module-indicator = %{version}
Recommends:     bumblebee-status-module-layout = %{version}
Recommends:     bumblebee-status-module-layout-xkb = %{version}
Recommends:     bumblebee-status-module-playerctl = %{version}
Recommends:     bumblebee-status-module-pulseaudio = %{version}
Recommends:     bumblebee-status-module-rss = %{version}
Recommends:     bumblebee-status-module-sensors = %{version}
Recommends:     bumblebee-status-module-sun = %{version}
Recommends:     bumblebee-status-module-title = %{version}
Recommends:     bumblebee-status-module-xrandr = %{version}
Recommends:     bumblebee-status-theme-powerline = %{version}
Suggests:       bumblebee-status-module-alsa = %{version}
Suggests:       bumblebee-status-module-arandr = %{version}
Suggests:       bumblebee-status-module-brightness = %{version}
Suggests:       bumblebee-status-module-cmus = %{version}
Suggests:       bumblebee-status-module-deadbeef = %{version}
Suggests:       bumblebee-status-module-deezer = %{version}
Suggests:       bumblebee-status-module-docker-ps = %{version}
Suggests:       bumblebee-status-module-duns = %{version}
Suggests:       bumblebee-status-module-git = %{version}
Suggests:       bumblebee-status-module-layout-xkbswitch = %{version}
Suggests:       bumblebee-status-module-libvirt = %{version}
Suggests:       bumblebee-status-module-mocp = %{version}
Suggests:       bumblebee-status-module-mpd = %{version}
Suggests:       bumblebee-status-module-notmuch = %{version}
Suggests:       bumblebee-status-module-nvidia-prime = %{version}
Suggests:       bumblebee-status-module-octoprint = %{version}
Suggests:       bumblebee-status-module-progress = %{version}
Suggests:       bumblebee-status-module-redshift = %{version}
Suggests:       bumblebee-status-module-smartstatus = %{version}
Suggests:       bumblebee-status-module-speedtest = %{version}
Suggests:       bumblebee-status-module-spotify = %{version}
Suggests:       bumblebee-status-module-taskwarrior = %{version}
Suggests:       bumblebee-status-module-vault = %{version}
Suggests:       bumblebee-status-module-vpn = %{version}
Suggests:       bumblebee-status-module-watson = %{version}
Suggests:       bumblebee-status-module-yubikey = %{version}
BuildArch:      noarch
# SECTION missing dependencies
#Suggests:       bumblebee-status-module-nvidia = %{version}
#Suggests:       bumblebee-status-module-pihole = %{version}
#Suggests:       bumblebee-status-module-twmn = %{version}
#Suggests:       bumblebee-status-module-zfs = %{version}
# /SECTION

%description
bumblebee-status is a modular, themeable status line generator for the i3 window manager.
It supports theming and does not require any configuration files.

You can use the mouse wheel up/down to switch workspaces forward and back everywhere throughout the bar.

%package theme-powerline
Summary:        Bumblebee themes using awesome and powerline fonts
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       fontawesome-fonts
Requires:       powerline-fonts
Supplements:    (%{name} and powerline)
BuildArch:      noarch

%description theme-powerline
Bumbebee themes using awesome-fonts and powerline-fonts.

%package module-alsa
Summary:        Control the alsa volume
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       alsa-utils
Supplements:    (%{name} and alsa-utils)
BuildArch:      noarch

%description module-alsa
Get volume level or control it.

%package module-arandr
Summary:        Enables handy interaction with arandr for display management
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       arandr
Supplements:    (%{name} and arandr)
BuildArch:      noarch

%description module-arandr
Enables handy interaction with arandr for display management.

%package module-brightness
Summary:        Displays the brightness of a display
Group:          System/Monitoring
Requires:       %{name} = %{version}
Recommends:     brightnessctl
Recommends:     light
Recommends:     xbacklight
Supplements:    (%{name} and xprop)
BuildArch:      noarch

%description module-brightness
Displays the brightness of a display.

%package module-caffeine
Summary:        Widget for automatic screen locking
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       libnotify-tools
Requires:       xdotool
Requires:       xprop
Supplements:    (%{name} and xdg-utils and xprop)
BuildArch:      noarch

%description module-caffeine
Enable/disable automatic screen locking.

%package module-cmus
Summary:        Widget to show information about the current song in cmus
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       cmus
Supplements:    (%{name} and cmus)
BuildArch:      noarch

%description module-cmus
Displays information about the current song in cmus via cmus-remote.

It takes a parameter (cmus.format) which customizes how the song
is displayed. Tag values can be put in curly brackets, (i.e., {artist}).

%package module-deadbeef
Summary:        Widget for deadbeef
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       deadbeef
Supplements:    (%{name} and deadbeef)
BuildArch:      noarch

%description module-deadbeef
Displays the current song being played in DeaDBeeF and provides
some media control bindings.

%package module-deezer
Summary:        Widget for deezer
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-dbus-python
BuildArch:      noarch

%description module-deezer
Displays the current song being played in deezer and provides
some media control bindings.

%package module-dnf
Summary:        Widget to display DNF package update information
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       dnf
Supplements:    (%{name} and dnf)
BuildArch:      noarch

%description module-dnf
Displays DNF package update information (<security>/<bugfixes>/<enhancements>/<other>)
via dnf.

It takes a parameter (dnf.interval) which controls the time in seconds
between two consecutive update checks (default = 30 minutes)

%package module-docker-ps
Summary:        Widget for docker containers running
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-docker
Supplements:    (%{name} and docker)
BuildArch:      noarch

%description module-docker-ps
Displays the number of docker containers running.

%package module-dunst
Summary:        Widget to toggle dunst notifications
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       dunst >= 1.5.0
Supplements:    (%{name} and dunst)
BuildArch:      noarch

%description module-dunst
Toggle dunst notifications.

%package module-git
Summary:        Widget to show git information
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-pygit2
Requires:       xcwd
Supplements:    (%{name} and git-core)
BuildArch:      noarch

%description module-git
Displays information about the git repository.

%package module-indicator
Summary:        Widget to show indicator status, for numlock, scrolllock and capslock
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       xset
Supplements:    (%{name} and xset)
BuildArch:      noarch

%description module-indicator
Displays the indicator status, for numlock, scrolllock and capslock.

%package module-layout
Summary:        Displays and changes the current keyboard layout
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       setxkbmap
BuildArch:      noarch

%description module-layout
Displays and changes the current keyboard layout.

%package module-layout-xkb
Summary:        Widget to show xkb layout
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-xkbgroup
BuildArch:      noarch

%description module-layout-xkb
Widget for displaying information about the xkb layout.

%package module-layout-xkbswitch
Summary:        Widget to show and switch keyboard layout
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       xkb-switch
BuildArch:      noarch

%description module-layout-xkbswitch
Widget to show and switch keyboard layout.

%package module-libvirt
Summary:        Displays count of running libvirt VMs
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-libvirt-python
Requires:       virt-manager
Supplements:    (%{name} and virt-manager)
BuildArch:      noarch

%description module-libvirt
Displays count of running libvirt VMs.

%package module-mocp
Summary:        Widget to display information about the current song in moc
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       moc
Supplements:    (%{name} and moc)
BuildArch:      noarch

%description module-mocp
Displays information about the current song in moc, via mocp.

Takes one parameter (mocp.format) that formats song information. Tag values can
be put in curly brackets (i.e. {artist})

%package module-mpd
Summary:        Widget to display information about the current song in mpd
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       mpclient
Supplements:    (%{name} and mpd)
BuildArch:      noarch

%description module-mpd
Displays information about the current song in mpd (via mpc)

Takes two parameters:
  * mpd.format: Format string for the song information. Tag values can
    be put in curly brackets (i.e. {artist})
  * mpd.host: MPD host to connect to. (mpc behaviour by default)

%package module-notmuch
Summary:        Displays the result of a notmuch count query
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       notmuch
Supplements:    (%{name} and notmuch)
BuildArch:      noarch

%description module-notmuch
Displays the result of a notmuch count query.

%package module-nvidia
Summary:        Displays GPU name, temperature and memory usage
Group:          System/Monitoring
Requires:       %{name} = %{version}
# Requires:       nvidia-smi
# Supplements:    (%%{name} and nvidia-smi)
BuildArch:      noarch

%description module-nvidia
Displays GPU name, temperature and memory usage.

%package module-nvidia-prime
Summary:        GPU selection for NVIDIA optimus
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       suse-prime-bbswitch
Supplements:    (%{name} and suse-prime-bbswitch)
BuildArch:      noarch

%description module-nvidia-prime
GPU (nvidia/intel) selection for NVIDIA optimus laptops with bbswitch support.

%package module-octoprint
Summary:        Displays Octoprint status
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-Pillow-tk
Requires:       python3-simplejson
BuildArch:      noarch

%description module-octoprint
Displays the Octoprint status and the printer's bed/tools temperature in the status bar.

%package module-pihole
Summary:        Displays the pi-hole status
Group:          System/Monitoring
Requires:       %{name} = %{version}
# Requires:       pi-hole
# Supplements:    (%%{name} and pi-hole)
BuildArch:      noarch

%description module-pihole
Displays the pi-hole status (up/down)
together with the number of ads that were blocked today.

%package module-playerctl
Summary:        Displays information about the current song using playerctl
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       playerctl
Supplements:    (%{name} and playerctl)
BuildArch:      noarch

%description module-playerctl
Displays information about the current song in
vlc, audacious, bmp, xmms2, spotify and others.

%package module-progress
Summary:        Show progress for cp, mv, dd, etc
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       progress
Supplements:    (%{name} and progress)
BuildArch:      noarch

%description module-progress
Show progress for cp, mv, dd, etc.

%package module-pulseaudio
Summary:        Widget for pulseaudio
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       pavucontrol
Requires:       pulseaudio-utils
Supplements:    (%{name} and pulseaudio)
BuildArch:      noarch

%description module-pulseaudio
Displays volume and mute status and controls for PulseAudio devices.
Use wheel up and down to change volume, left click mutes, right click opens pavucontrol.

%package module-redshift
Summary:        Widget to display the current color temperature of redshift
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       redshift
Supplements:    (%{name} and redshift)
BuildArch:      noarch

%description module-redshift
Displays the current color temperature of redshift. Takes no parameters.

%package module-rss
Summary:        Widget to display RSS feed
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-feedparser
BuildArch:      noarch

%description module-rss
Displays a RSS feed.

%package module-sensors
Summary:        Widget for sensors
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       sensors
Supplements:    (%{name} and sensors)
BuildArch:      noarch

%description module-sensors
Displays sensors information.

%package module-smartstatus
Summary:        Displays HDD smart status
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       smartmontools
Supplements:    (%{name} and smartmontools)
BuildArch:      noarch

%description module-smartstatus
Displays HDD smart status of different drives or all drives.

%package module-speedtest
Summary:        Performs a speedtest
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       speedtest-cli
BuildArch:      noarch

%description module-speedtest
Performs a speedtest.

%package module-spotify
Summary:        Widget to display spotify
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-dbus-python
Requires:       spotify-easyrpm
Supplements:    (%{name} and spotify-easyrpm)
BuildArch:      noarch

%description module-spotify
Displays a spotify widget.

%package module-sun
Summary:        Widget to display sunrise and sunset times
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-python-dateutil
Requires:       python3-suntime
BuildArch:      noarch

%description module-sun
Displays sunrise and sunset times.

%package module-taskwarrior
Summary:        Widget to display number of pending tasks in TaskWarrior
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-taskw
Supplements:    (%{name} and taskwarrior)
BuildArch:      noarch

%description module-taskwarrior
Displays the number of pending tasks in TaskWarrior.

%package module-title
Summary:        Widget to display focused i3 window title
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-i3ipc
BuildArch:      noarch

%description module-title
Displays focused i3 window title.

%package module-twmn
Summary:        Widget to toggle twmn notifications
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       systemd
# Requires:       twmn
# Supplements:    (%%{name} and twmn)
BuildArch:      noarch

%description module-twmn
Toggle twmn notifications.

%package module-vault
Summary:        Copy passwords from a password store
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       password-store
Supplements:    (%{name} and password-store)
BuildArch:      noarch

%description module-vault
Copy passwords from a password store to the clipboard.

%package module-vpn
Summary:        Displays the VPN profile
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-tk
Supplements:    (%{name} and NetworkManager)
BuildArch:      noarch

%description module-vpn
Displays the VPN profile that is currently in use.

%package module-watson
Summary:        Displays the status of watson
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       watson
Supplements:    (%{name} and watson)
BuildArch:      noarch

%description module-watson
Displays the status of watson (time-tracking tool).

%package module-xrandr
Summary:        Widget for each connected screen and allows the user to enable/disable screens
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       xrandr
Supplements:    (%{name} and xrandr)
BuildArch:      noarch

%description module-xrandr
Shows a widget for each connected screen and allows the user to enable/disable screens.

%package module-yubikey
Summary:        Shows yubikey information
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-python-yubico
Supplements:    (%{name} and python3-python-yubico)
BuildArch:      noarch

%description module-yubikey
The output indicates that a YubiKey is not connected or it displays
the corresponding serial number.

%package module-zfs
Summary:        Shows zpool information
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       python3-setuptools
# Requires:       zfs
# Supplements:    (%%{name} and zfs)
BuildArch:      noarch

%description module-zfs
Displays info about zpools present on the system.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
# Remove hashbang from modules
sed -i '1{/^#!/d}' bumblebee_status/modules/contrib/{network_traffic,playerctl,spaceapi}.py
chmod a-x bumblebee_status/modules/contrib/playerctl.py

%build

%install
mkdir -p "%{buildroot}%{_bindir}"
mkdir -p "%{buildroot}%{_datadir}/%{name}/themes/icons"
mkdir -p "%{buildroot}%{_datadir}/%{name}/bumblebee/modules"

# Install main files, themes, modules and icons

# 1. prepare filesystem
install -d %{buildroot}%{_bindir} \
%{buildroot}%{_datadir}/%{buildroot}/{bumblebee/modules,themes/icons}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

# 2. remove modules:
#    * apt (debian)
#    * arch-update and pacman (only usable on arch linux)
#    * gpmdp (needs Google Play music player)
#    * hddtemp (no longer maintained)
rm bumblebee_status/modules/contrib/{apt,arch_update,arch-update,gpmdp,hddtemp,pacman,portage_status}.py
rm tests/modules/contrib/test_{apt,arch-update,gpmdp,hddtemp,pacman,portage_status}.py

# 3. copy files from source
cp -a --parents %{name} themes/{,icons/}*.json %{buildroot}%{_datadir}/%{name}
cd bumblebee_status
cp -r . %{buildroot}%{_datadir}/%{name}/bumblebee/

%check
export LANG=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{_datadir}/%{name}/:%{buildroot}%{_datadir}/%{name}/bumblebee/
# Speedtest is not available for python3.6
%pytest -rs --ignore tests/modules/core/test_speedtest.py

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/icons
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}
%dir %{_datadir}/%{name}/bumblebee/
%{_datadir}/%{name}/bumblebee/*.py
%{_datadir}/%{name}/bumblebee/core/
%{_datadir}/%{name}/bumblebee/util/
%dir %{_datadir}/%{name}/bumblebee/modules/
%{_datadir}/%{name}/bumblebee/modules/__init__.py
%dir %{_datadir}/%{name}/bumblebee/modules/contrib/
%{_datadir}/%{name}/bumblebee/modules/contrib/__init__.py
%dir %{_datadir}/%{name}/bumblebee/modules/core/
%{_datadir}/%{name}/bumblebee/modules/core/__init__.py
%{_datadir}/%{name}/bumblebee/modules/core/cpu.py
%{_datadir}/%{name}/bumblebee/modules/core/date.py
%{_datadir}/%{name}/bumblebee/modules/core/datetime.py
%{_datadir}/%{name}/bumblebee/modules/core/debug.py
%{_datadir}/%{name}/bumblebee/modules/core/disk.py
%{_datadir}/%{name}/bumblebee/modules/core/error.py
%{_datadir}/%{name}/bumblebee/modules/core/keys.py
%{_datadir}/%{name}/bumblebee/modules/core/load.py
%{_datadir}/%{name}/bumblebee/modules/core/memory.py
%{_datadir}/%{name}/bumblebee/modules/core/nic.py
%{_datadir}/%{name}/bumblebee/modules/core/ping.py
%{_datadir}/%{name}/bumblebee/modules/core/spacer.py
%{_datadir}/%{name}/bumblebee/modules/core/test.py
%{_datadir}/%{name}/bumblebee/modules/core/time.py
%{_datadir}/%{name}/bumblebee/modules/contrib/battery.py
%{_datadir}/%{name}/bumblebee/modules/contrib/battery_upower.py
%{_datadir}/%{name}/bumblebee/modules/contrib/battery-upower.py
%{_datadir}/%{name}/bumblebee/modules/contrib/bluetooth2.py
%{_datadir}/%{name}/bumblebee/modules/contrib/bluetooth.py
%{_datadir}/%{name}/bumblebee/modules/contrib/currency.py
%{_datadir}/%{name}/bumblebee/modules/contrib/datetimetz.py
%{_datadir}/%{name}/bumblebee/modules/contrib/datetz.py
%{_datadir}/%{name}/bumblebee/modules/contrib/getcrypto.py
%{_datadir}/%{name}/bumblebee/modules/contrib/github.py
%{_datadir}/%{name}/bumblebee/modules/contrib/hostname.py
%{_datadir}/%{name}/bumblebee/modules/contrib/http_status.py
%{_datadir}/%{name}/bumblebee/modules/contrib/kernel.py
%{_datadir}/%{name}/bumblebee/modules/contrib/messagereceiver.py
%{_datadir}/%{name}/bumblebee/modules/contrib/network_traffic.py
%{_datadir}/%{name}/bumblebee/modules/contrib/pomodoro.py
%{_datadir}/%{name}/bumblebee/modules/contrib/publicip.py
%{_datadir}/%{name}/bumblebee/modules/contrib/rofication.py
%{_datadir}/%{name}/bumblebee/modules/contrib/shell.py
%{_datadir}/%{name}/bumblebee/modules/contrib/shortcut.py
%{_datadir}/%{name}/bumblebee/modules/contrib/spaceapi.py
%{_datadir}/%{name}/bumblebee/modules/contrib/stock.py
%{_datadir}/%{name}/bumblebee/modules/contrib/system.py
%{_datadir}/%{name}/bumblebee/modules/contrib/thunderbird.py
%{_datadir}/%{name}/bumblebee/modules/contrib/timetz.py
%{_datadir}/%{name}/bumblebee/modules/contrib/todo.py
%{_datadir}/%{name}/bumblebee/modules/contrib/todo_org.py
%{_datadir}/%{name}/bumblebee/modules/contrib/traffic.py
%{_datadir}/%{name}/bumblebee/modules/contrib/uptime.py
%{_datadir}/%{name}/bumblebee/modules/contrib/weather.py
%{_datadir}/%{name}/bumblebee/modules/contrib/xkcd.py
%{_datadir}/%{name}/themes/default.json
%{_datadir}/%{name}/themes/gruvbox-light.json
%{_datadir}/%{name}/themes/gruvbox.json
%{_datadir}/%{name}/themes/solarized.json
%{_datadir}/%{name}/themes/test.json
%{_datadir}/%{name}/themes/test_cycle.json
%{_datadir}/%{name}/themes/test_invalid.json
%{_datadir}/%{name}/themes/icons/ascii.json
%{_datadir}/%{name}/themes/icons/ionicons.json
%{_datadir}/%{name}/themes/icons/paxy97.json
%{_datadir}/%{name}/themes/icons/test.json

%files theme-powerline
%{_datadir}/%{name}/themes/icons/awesome-fonts.json
%{_datadir}/%{name}/themes/dracula-powerline.json
%{_datadir}/%{name}/themes/firefox-dark-powerline.json
%{_datadir}/%{name}/themes/greyish-powerline.json
%{_datadir}/%{name}/themes/gruvbox-powerline.json
%{_datadir}/%{name}/themes/gruvbox-powerline-light.json
%{_datadir}/%{name}/themes/iceberg-contrast.json
%{_datadir}/%{name}/themes/iceberg-dark-powerline.json
%{_datadir}/%{name}/themes/iceberg-powerline.json
%{_datadir}/%{name}/themes/iceberg-rainbow.json
%{_datadir}/%{name}/themes/iceberg.json
%{_datadir}/%{name}/themes/night-powerline.json
%{_datadir}/%{name}/themes/nord-powerline.json
%{_datadir}/%{name}/themes/onedark-powerline.json
%{_datadir}/%{name}/themes/powerline.json
%{_datadir}/%{name}/themes/powerline-pango.json
%{_datadir}/%{name}/themes/sac_red.json
%{_datadir}/%{name}/themes/solarized-dark-awesome.json
%{_datadir}/%{name}/themes/solarized-powerline.json
%{_datadir}/%{name}/themes/wal-powerline.json

%files module-alsa
%{_datadir}/%{name}/bumblebee/modules/contrib/amixer.py

%files module-arandr
%{_datadir}/%{name}/bumblebee/modules/contrib/arandr.py

%files module-brightness
%{_datadir}/%{name}/bumblebee/modules/contrib/brightness.py

%files module-caffeine
%{_datadir}/%{name}/bumblebee/modules/contrib/caffeine.py

%files module-cmus
%{_datadir}/%{name}/bumblebee/modules/contrib/cmus.py

%files module-deezer
%{_datadir}/%{name}/bumblebee/modules/contrib/deezer.py

%files module-deadbeef
%{_datadir}/%{name}/bumblebee/modules/contrib/deadbeef.py

%files module-dnf
%{_datadir}/%{name}/bumblebee/modules/contrib/dnf.py

%files module-docker-ps
%{_datadir}/%{name}/bumblebee/modules/contrib/docker_ps.py

%files module-dunst
%{_datadir}/%{name}/bumblebee/modules/contrib/dunst.py
%{_datadir}/%{name}/bumblebee/modules/contrib/dunstctl.py

%files module-git
%{_datadir}/%{name}/bumblebee/modules/core/git.py

%files module-indicator
%{_datadir}/%{name}/bumblebee/modules/contrib/indicator.py

%files module-layout
%{_datadir}/%{name}/bumblebee/modules/contrib/layout.py

%files module-layout-xkb
%{_datadir}/%{name}/bumblebee/modules/core/layout_xkb.py
%{_datadir}/%{name}/bumblebee/modules/core/layout-xkb.py

%files module-layout-xkbswitch
%{_datadir}/%{name}/bumblebee/modules/contrib/layout_xkbswitch.py
%{_datadir}/%{name}/bumblebee/modules/contrib/layout-xkbswitch.py

%files module-libvirt
%{_datadir}/%{name}/bumblebee/modules/contrib/libvirtvms.py

%files module-mocp
%{_datadir}/%{name}/bumblebee/modules/contrib/mocp.py

%files module-mpd
%{_datadir}/%{name}/bumblebee/modules/contrib/mpd.py

%files module-nvidia
%{_datadir}/%{name}/bumblebee/modules/contrib/nvidiagpu.py

%files module-nvidia-prime
%{_datadir}/%{name}/bumblebee/modules/contrib/prime.py

%files module-notmuch
%{_datadir}/%{name}/bumblebee/modules/contrib/notmuch_count.py

%files module-octoprint
%{_datadir}/%{name}/bumblebee/modules/contrib/octoprint.py

%files module-pihole
%{_datadir}/%{name}/bumblebee/modules/contrib/pihole.py

%files module-playerctl
%{_datadir}/%{name}/bumblebee/modules/contrib/playerctl.py

%files module-progress
%{_datadir}/%{name}/bumblebee/modules/contrib/progress.py

%files module-pulseaudio
%{_datadir}/%{name}/bumblebee/modules/core/pasink.py
%{_datadir}/%{name}/bumblebee/modules/core/pasource.py
%{_datadir}/%{name}/bumblebee/modules/core/pulseaudio.py

%files module-redshift
%{_datadir}/%{name}/bumblebee/modules/core/redshift.py

%files module-rss
%{_datadir}/%{name}/bumblebee/modules/contrib/rss.py

%files module-sensors
%{_datadir}/%{name}/bumblebee/modules/contrib/cpu2.py
%{_datadir}/%{name}/bumblebee/modules/contrib/sensors.py
%{_datadir}/%{name}/bumblebee/modules/core/sensors2.py

%files module-smartstatus
%{_datadir}/%{name}/bumblebee/modules/contrib/smartstatus.py

%files module-speedtest
%{_datadir}/%{name}/bumblebee/modules/core/speedtest.py

%files module-spotify
%{_datadir}/%{name}/bumblebee/modules/contrib/spotify.py

%files module-sun
%{_datadir}/%{name}/bumblebee/modules/contrib/sun.py

%files module-taskwarrior
%{_datadir}/%{name}/bumblebee/modules/contrib/taskwarrior.py

%files module-title
%{_datadir}/%{name}/bumblebee/modules/contrib/title.py

%files module-twmn
%{_datadir}/%{name}/bumblebee/modules/contrib/twmn.py

%files module-vault
%{_datadir}/%{name}/bumblebee/modules/core/vault.py

%files module-vpn
%{_datadir}/%{name}/bumblebee/modules/contrib/vpn.py

%files module-watson
%{_datadir}/%{name}/bumblebee/modules/contrib/watson.py

%files module-xrandr
%{_datadir}/%{name}/bumblebee/modules/core/xrandr.py
%{_datadir}/%{name}/bumblebee/modules/contrib/rotation.py

%files module-yubikey
%{_datadir}/%{name}/bumblebee/modules/contrib/yubikey.py

%files module-zfs
%{_datadir}/%{name}/bumblebee/modules/contrib/zpool.py

%changelog
