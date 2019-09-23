#
# spec file for package zathura
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           zathura
Version:        0.4.3
Release:        0
Summary:        A customizable document viewer
License:        Zlib
Group:          Productivity/Office/Other
URL:            http://pwmt.org/projects/zathura/
Source:         http://pwmt.org/projects/zathura/download/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  libseccomp-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  rsvg-view
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(girara-gtk3) >= 0.3.2
BuildRequires:  pkgconfig(sqlite3)
Recommends:     %{name}-lang
Recommends:     zathura-pdf-poppler-plugin
Suggests:       zathura-cb-plugin
Suggests:       zathura-djvu-plugin
Suggests:       zathura-ps-plugin
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(synctex)
%endif

%description
zathura is a customizable document viewer. It provides a minimalistic
and space-saving interface as well as a keyboard-centric interaction.

%package devel
Summary:        Development files for zathura
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
Development and header files for the zathura package.

%package bash-completion
Summary:        Zathura Bash completion
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)

%description bash-completion
Optional dependency offering bash completion for zathura

%package zsh-completion
Summary:        Zathura zsh completion
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    packageand(%{name}:zsh)

%description zsh-completion
Optional dependency offering zsh completion for zathura

%lang_package

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README AUTHORS
%dir %{_datadir}/icons/scalable
%dir %{_datadir}/icons/scalable/apps
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/org.pwmt.%{name}.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}rc.5%{?ext_man}
%{_datadir}/applications/org.pwmt.zathura.desktop
%{_datadir}/icons/hicolor/*/apps/org.pwmt.zathura.png
%{_datadir}/metainfo/org.pwmt.zathura.appdata.xml
%{_datadir}/icons/scalable/apps/org.pwmt.zathura.svg

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%files bash-completion
%{_datadir}/bash-completion/completions/zathura

%files zsh-completion
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_zathura

%files lang -f %{name}.lang

%changelog
