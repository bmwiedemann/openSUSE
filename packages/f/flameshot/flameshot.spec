#
# spec file for package flameshot
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


Name:           flameshot
Version:        0.8.3
Release:        0
Summary:        Screenshot software
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
URL:            https://github.com/lupoDharkael/flameshot#flameshot
#Git-Clone:     https://github.com/flameshot-org/flameshot.git
Source0:        https://github.com/lupoDharkael/flameshot/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5
BuildRequires:  pkgconfig(Qt5DBus) >= 5
BuildRequires:  pkgconfig(Qt5Gui) >= 5
BuildRequires:  pkgconfig(Qt5Network) >= 5
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5

%description
A program to capture screenshots.
It includes CLI options as well as a UI for capturing and annotating screenshots.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (flameshot and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for flameshot's CLI.

%package zsh-completion
Summary:        ZSH completion for %{name}
Group:          Productivity/Networking/Security
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for %{name}.

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install
install -d %{buildroot}/%{_sysconfdir}/zsh_completion.d
mv %{buildroot}%{_datadir}/zsh/site-functions/_flameshot %{buildroot}%{_sysconfdir}/zsh_completion.d/%{name}
%suse_update_desktop_file -r %{name} Utility X-SuSE-DesktopUtility

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/interfaces/org.flameshot.Flameshot.xml
%{_datadir}/dbus-1/services/org.flameshot.Flameshot.service
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_sysconfdir}/zsh_completion.d
%config %{_sysconfdir}/zsh_completion.d/%{name}

%changelog
