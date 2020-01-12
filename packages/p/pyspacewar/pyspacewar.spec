#
# spec file for package pyspacewar
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pyspacewar
Version:        1.1.1
Release:        0
Summary:        Game loosely based on the original Spacewar!
License:        GPL-2.0-only AND CC-BY-SA-3.0 AND SUSE-Public-Domain
URL:            https://github.com/mgedmin/pyspacewar
Source0:        https://github.com/mgedmin/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pygame
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       python3-pygame
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
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

# install icons
for i in 16 22 32 48 ; do
    install -Dm 0644 src/%{name}/icons/%{name}${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
    install -Dm 0644 src/%{name}/icons/%{name}${i}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}${i}.svg
done

# install Desktop file
install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest -v

%files
%license LICENSE
%doc *.rst
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.egg-info

%changelog
