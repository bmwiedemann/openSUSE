#
# spec file for package pyspacewar
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pyspacewar
Version:        1.1.0
Release:        0
Summary:        Game loosely based on the original Spacewar!
License:        GPL-2.0 and CC-BY-SA-3.0 and SUSE-Public-Domain
Group:          Amusements/Games/Action/Arcade
Url:            http://mg.pov.lt/pyspacewar/
Source0:        https://github.com/mgedmin/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-setuptools
BuildRequires:  update-desktop-files
Requires:       python
Requires:       python-pygame
BuildArch:      noarch

%description
Two ships duel in a gravity field. Gravity doesn't affect
the ships themselves (which have spanking new anti-gravity
devices), but it affects missiles launced by the ships.

You can play against the computer, or two players can play
with one keyboard. There is also a Gravity Wars mode, where
the two ships do not move, and the players repeatedly
specify the direction and velocity of their missiles.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=%{buildroot}

# install icons
for i in 16 22 32 48 ; do
    install -Dm 0644 src/%{name}/icons/%{name}${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
    install -Dm 0644 src/%{name}/icons/%{name}${i}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}${i}.svg
done

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%defattr(-,root,root,-)
%doc GPL.txt *.rst
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.egg-info

%changelog
