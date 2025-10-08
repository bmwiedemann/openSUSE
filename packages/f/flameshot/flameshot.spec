#
# spec file for package flameshot
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        13.1.0
Release:        0
Summary:        Screenshot software
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
URL:            https://github.com/flameshot-org/flameshot#flameshot
Source0:        https://github.com/flameshot-org/flameshot/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://gitlab.com/mattbas/Qt-Color-Widgets/-/archive/3.0.0/Qt-Color-Widgets-3.0.0.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  cmake >= 3.13.0
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 7
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core) >= 6.0.0
BuildRequires:  cmake(Qt6DBus) >= 6.0.0
BuildRequires:  cmake(Qt6Gui) >= 6.0.0
BuildRequires:  cmake(Qt6LinguistTools) >= 6.0.0
BuildRequires:  cmake(Qt6Network) >= 6.0.0
BuildRequires:  cmake(Qt6Svg) >= 6.0.0
BuildRequires:  cmake(Qt6Widgets) >= 6.0.0
Requires:       hicolor-icon-theme
Requires:       libQt6Core6
Requires:       libQt6Svg6
Suggests:       %{name}-bash-completion
Suggests:       %{name}-fish-completion
Suggests:       %{name}-zsh-completion
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
BuildRequires:  kf6-kguiaddons-devel
%endif

%description
A program to capture screenshots.

Features:

 * Customizable appearance
 * Annotation and drawing tools
 * DBus interface
 * Export to file, web

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (flameshot and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for flameshot's CLI.

%package zsh-completion
Summary:        ZSH completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p0 -a1

# Move dependency to external folder
mkdir external
mv Qt-Color-Widgets-3.0.0 external/Qt-Color-Widgets

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:BOOL=OFF \
-DUSE_KDSINGLEAPPLICATION=OFF \
-DDISABLE_UPDATE_CHECKER:BOOL=ON \
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
-DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
%endif

%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r org.flameshot.Flameshot Utility X-SuSE-DesktopUtility
%fdupes %{buildroot}%{_datadir}/icons/hicolor

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/org.flameshot.Flameshot.desktop
%{_datadir}/dbus-1/interfaces/org.flameshot.Flameshot.xml
%{_datadir}/dbus-1/services/org.flameshot.Flameshot.service
%{_datadir}/icons/hicolor*
%{_datadir}/metainfo/org.flameshot.Flameshot.metainfo.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_flameshot

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/flameshot.fish

%changelog
