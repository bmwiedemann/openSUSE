#
# spec file for package econnman
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


Name:           econnman
Version:        1.1
Release:        0
Summary:        EFL user interface for connman
License:        GPL-3.0-only
Group:          Productivity/Networking/System
Url:            http://enlightenment.org/
Source:         https://download.enlightenment.org/rel/apps/econnman/%{name}-%{version}.tar.xz
Patch0:         desktop.patch
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(edje) >= 1.8.0
# SECTION Check list of dependencies
BuildRequires:  adwaita-icon-theme
BuildRequires:  connman
BuildRequires:  python3-efl
Requires:       connman
Requires:       python3
Requires:       python3-efl
BuildArch:      noarch
# /SECTION
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
EFL user interface for connman (Connection Manager).

%prep
%setup -q
%patch0 -p1

# Default python executable
for _file in $(grep -rl '^\#\!'); do
  find -name ${_file##*/} -type f -exec sed -i '/^\#\!/s/python/python3/' {} +
done

%build
[ ! -e configure ] && NOCONFIGURE=1 ./autogen.sh
export PYTHON=%{_bindir}/python3
%{!?mageia:%configure}
%{?mageia:%configure2_5x}
make %{?_smp_mflags}

%install
%make_install

# Fix: Icon file not found
for _file in $(find %{buildroot} -name \*.desktop); do
    _icon=$(sed -ne '/^Icon/s/[^=]*=//p' -ne '/^Icon/s/\..*//p' $_file)
    if ! find %{buildroot} -name "${_icon##*/}.??g" | grep -q .; then
        for _icon in $(find %{_datadir}/icons -name network-wired.png | sort -r | head -n1); do
          install -Dm0644 "$_icon" "%{buildroot}%{_datadir}/pixmaps/${_icon##*/}"
          sed -i '/^Icon/s/[^=]*$/network-wired/' $_file
        done
    else
        "$_icon file exists" 2> /dev/null
    fi
done

%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} Enlightenment Network Settings
%suse_update_desktop_file -u -r %{name} Enlightenment Network Settings
%endif

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/%{name}-bin
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/network-wired.??g

%changelog
