#
# spec file for package bumblebee-status
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


Name:           bumblebee-status
Version:        1.6.1
Release:        0
Summary:        Modular, theme-able status line generator for the i3 window manager
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/tobi-wan-kenobi/bumblebee-status/wiki
Source0:        https://github.com/tobi-wan-kenobi/bumblebee-status/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         use-python-3.patch
# In earlier i3 versions, blocks won't have background colors
Requires:       i3 >= 4.12
# Supported Python versions: 2.7, 3.3, 3.4, 3.5, 3.6
#  3.2 is unsupported (missing unicode literals)
Requires:       python >= 3.3
Requires:       python3-netifaces
Requires:       python3-psutil
Requires:       python3-requests
Recommends:     fontaweseome-fonts
Recommends:     powerline-fonts
BuildArch:      noarch

%description
bumblebee-status is a modular, themeable status line generator for the i3 window manager.
It supports theming and does not require any configuration files.

You can use the mouse wheel up/down to switch workspaces forward and back everywhere throughout the bar.

%package module-cmus
Summary:        Widget to show information about the current song in cmus
Group:          System/Monitoring
Requires:       cmus
Supplements:    packageand(%{name}:cmus)
BuildArch:      noarch

%description module-cmus
Displays information about the current song in cmus via cmus-remote.

It takes a parameter (cmus.format) which customizes how the song
is displayed. Tag values can be put in curly brackets, (i.e., {artist}).

%package module-dnf
Summary:        Widget to display DNF package update information
Group:          System/Monitoring
Requires:       dnf
Supplements:    packageand(%{name}:dnf)
BuildArch:      noarch

%description module-dnf
Displays DNF package update information (<security>/<bugfixes>/<enhancements>/<other>)
via dnf.

It takes a parameter (dnf.interval) which controls the time in seconds
between two consecutive update checks (default = 30 minutes)

%package module-mpd
Summary:        Widget to display information about the current song in mpd
Group:          System/Monitoring
Requires:       mpclient
Supplements:    packageand(%{name}:mpd)
BuildArch:      noarch

%description module-mpd
Displays information about the current song in mpd (via mpc)

Takes two parameters:
  * mpd.format: Format string for the song information. Tag values can
    be put in curly brackets (i.e. {artist})
  * mpd.host: MPD host to connect to. (mpc behaviour by default)

%package module-redshift
Summary:        Widget to display the current color temperature of redshift
Group:          System/Monitoring
Requires:       redshift
Supplements:    packageand(%{name}:redshift)
BuildArch:      noarch

%description module-redshift
Displays the current color temperature of redshift. Takes no parameters.

%package module-mocp
Summary:        Widget to display information about the current song in moc
Group:          System/Monitoring
Requires:       moc
Supplements:    packageand(%{name}:moc)
BuildArch:      noarch

%description module-mocp
Displays information about the current song in moc, via mocp.

Takes one parameter (mocp.format) that formats song information. Tag values can
be put in curly brackets (i.e. {artist})

%prep
%setup -q
%patch1 -p1

%build

%install
mkdir -p "%{buildroot}%{_bindir}"
mkdir -p "%{buildroot}%{_datadir}/licenses/%{name}"
mkdir -p "%{buildroot}%{_datadir}/%{name}/themes/icons"
mkdir -p "%{buildroot}%{_datadir}/%{name}/bumblebee/modules"

# Install main files, themes, modules and icons

# 1. prepare filesystem
install -d %{buildroot}%{_bindir} \
%{buildroot}%{_datadir}/%{buildroot}/{bumblebee/modules,themes/icons}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

# 2. remove modules:
#    * pacman (only usable on arch linux)
#    * stock (relies on deprecated Yahoo API)
rm -f bumblebee/modules/{pacman,stock}.py

# 3. copy files from source
cp -a --parents %{name} bumblebee/{,modules/}*.py themes/{,icons/}*.json \
%{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bumblebee
%dir %{_datadir}/%{name}/bumblebee/modules
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/icons
%dir %{_datadir}/licenses/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/bumblebee/__init__.py
%{_datadir}/%{name}/bumblebee/config.py
%{_datadir}/%{name}/bumblebee/engine.py
%{_datadir}/%{name}/bumblebee/error.py
%{_datadir}/%{name}/bumblebee/input.py
%{_datadir}/%{name}/bumblebee/modules/__init__.py
%{_datadir}/%{name}/bumblebee/modules/amixer.py
%{_datadir}/%{name}/bumblebee/modules/battery.py
%{_datadir}/%{name}/bumblebee/modules/bluetooth.py
%{_datadir}/%{name}/bumblebee/modules/brightness.py
%{_datadir}/%{name}/bumblebee/modules/caffeine.py
%{_datadir}/%{name}/bumblebee/modules/cpu.py
%{_datadir}/%{name}/bumblebee/modules/currency.py
%{_datadir}/%{name}/bumblebee/modules/datetime.py
%{_datadir}/%{name}/bumblebee/modules/disk.py
%{_datadir}/%{name}/bumblebee/modules/error.py
%{_datadir}/%{name}/bumblebee/modules/getcrypto.py
%{_datadir}/%{name}/bumblebee/modules/github.py
%{_datadir}/%{name}/bumblebee/modules/gpmdp.py
%{_datadir}/%{name}/bumblebee/modules/kernel.py
%{_datadir}/%{name}/bumblebee/modules/layout-xkb.py
%{_datadir}/%{name}/bumblebee/modules/layout.py
%{_datadir}/%{name}/bumblebee/modules/load.py
%{_datadir}/%{name}/bumblebee/modules/memory.py
%{_datadir}/%{name}/bumblebee/modules/nic.py
%{_datadir}/%{name}/bumblebee/modules/nvidiagpu.py
%{_datadir}/%{name}/bumblebee/modules/ping.py
%{_datadir}/%{name}/bumblebee/modules/publicip.py
%{_datadir}/%{name}/bumblebee/modules/pulseaudio.py
%{_datadir}/%{name}/bumblebee/modules/sensors.py
%{_datadir}/%{name}/bumblebee/modules/spacer.py
%{_datadir}/%{name}/bumblebee/modules/spotify.py
%{_datadir}/%{name}/bumblebee/modules/taskwarrior.py
%{_datadir}/%{name}/bumblebee/modules/test.py
%{_datadir}/%{name}/bumblebee/modules/title.py
%{_datadir}/%{name}/bumblebee/modules/todo.py
%{_datadir}/%{name}/bumblebee/modules/traffic.py
%{_datadir}/%{name}/bumblebee/modules/weather.py
%{_datadir}/%{name}/bumblebee/modules/xrandr.py
%{_datadir}/%{name}/bumblebee/modules/hipchat.py
%{_datadir}/%{name}/bumblebee/modules/rotation.py
%{_datadir}/%{name}/bumblebee/modules/shortcut.py
%{_datadir}/%{name}/bumblebee/modules/uptime.py
%{_datadir}/%{name}/bumblebee/modules/zpool.py
%{_datadir}/%{name}/bumblebee/output.py
%{_datadir}/%{name}/bumblebee/popup.py
%{_datadir}/%{name}/bumblebee/store.py
%{_datadir}/%{name}/bumblebee/theme.py
%{_datadir}/%{name}/bumblebee/util.py
%{_datadir}/%{name}/themes/sac_red.json
%{_datadir}/%{name}/themes/wal-powerline.json
%{_datadir}/%{name}/themes/default.json
%{_datadir}/%{name}/themes/gruvbox-powerline.json
%{_datadir}/%{name}/themes/gruvbox.json
%{_datadir}/%{name}/themes/icons/ascii.json
%{_datadir}/%{name}/themes/icons/awesome-fonts.json
%{_datadir}/%{name}/themes/icons/paxy97.json
%{_datadir}/%{name}/themes/icons/test.json
%{_datadir}/%{name}/themes/greyish-powerline.json
%{_datadir}/%{name}/themes/powerline.json
%{_datadir}/%{name}/themes/solarized-dark-awesome.json
%{_datadir}/%{name}/themes/solarized-powerline.json
%{_datadir}/%{name}/themes/solarized.json
%{_datadir}/%{name}/themes/test.json
%{_datadir}/%{name}/themes/test_cycle.json
%{_datadir}/%{name}/themes/test_invalid.json

%files module-cmus
%{_datadir}/%{name}/bumblebee/modules/cmus.py

%files module-dnf
%{_datadir}/%{name}/bumblebee/modules/dnf.py

%files module-mpd
%{_datadir}/%{name}/bumblebee/modules/mpd.py

%files module-redshift
%{_datadir}/%{name}/bumblebee/modules/redshift.py

%files module-mocp
%{_datadir}/%{name}/bumblebee/modules/mocp.py

%changelog
