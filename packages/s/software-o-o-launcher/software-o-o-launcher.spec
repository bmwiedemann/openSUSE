#
# spec file for package software-o-o-launcher
#
# Copyright (c) 2023 SUSE LLC
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


Name:           software-o-o-launcher
Version:        1.0
Release:        0
Summary:        A menu item for software.opensuse.org service
# With a respect to the original license of software-o-o itself
License:        GPL-2.0-only
URL:            https://software.opensuse.org
Source:         %{name}-%{version}.tar.xz
BuildRequires:  update-desktop-files
Requires:       xdg-utils
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
Many users struggle to find additional software outside of the openSUSE distributions. Our https://software.opensuse.org does a great job at it, however, not everyone is aware of its
existence. This quick launcher provides a menu launcher for software-o-o webservice with the intention
to bring the service closer to the user.

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
mkdir -p %{buildroot}/%{_datadir}/applications
install -m 0644 %{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 0644 %{name}.desktop %{buildroot}/%{_datadir}/applications/

%suse_update_desktop_file -i %{name} Additional Software

%post
%postun

%files
%dir %{_datadir}/icons
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/applications
%{_datadir}/applications/%{name}.desktop
%license COPYING
%doc README

%changelog
