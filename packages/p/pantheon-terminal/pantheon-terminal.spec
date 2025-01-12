#
# spec file for package pantheon-terminal
#
# Copyright (c) 2025 SUSE LLC
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


%define         appid io.elementary.terminal
Name:           pantheon-terminal
Version:        6.3.1
Release:        0
Summary:        Lightweight and modern Terminal for the Pantheon Desktop
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/terminal
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(vte-2.91)
Provides:       elementary-terminal = %{version}
Obsoletes:      elementary-terminal < %{version}

%description
A super lightweight, beautiful, and simple terminal. It is designed to be
setup with sane defaults and little to no configuration. It is just a
terminal, nothing more, nothing less.

%package        fish-completion
Summary:        The fish shell support for %{name}
Supplements:    (fish and %{name})
BuildArch:      noarch

%description    fish-completion
Lightweight and modern Terminal for the Pantheon Desktop.

This package contains the configuration files when using the fish shell.

%lang_package

%prep
%autosetup -n terminal-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/applications/open-pantheon-terminal-here.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_mandir}/man?/%{appid}.?%{?ext_man}
%{_datadir}/%{appid}
%{_datadir}/metainfo/%{appid}.appdata.xml

%files fish-completion
%{_datadir}/fish/vendor_conf.d/pantheon_terminal_process_completion_notifications.fish

%files lang -f %{appid}.lang

%changelog
