#
# spec file for package zathura
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define  appid  org.pwmt.zathura
%if 0%{?suse_version} == 1600
%bcond_without gcc15
%endif
Name:           zathura
Version:        2026.07.08
Release:        0
Summary:        A customizable document viewer
License:        Zlib
URL:            https://pwmt.org/projects/zathura/
Source0:        %{url}/download/%{name}-%{version}.tar.xz
Source1:        %{url}/download/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  AppStream
BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  fish
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 1.5
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  rsvg-convert
BuildRequires:  weston
BuildRequires:  xvfb-run
BuildRequires:  zsh
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(girara) >= 2026.07.07
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gmodule-no-export-2.0) >= 2.72
BuildRequires:  pkgconfig(gthread-2.0) >= 2.72
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(sqlite3) >= 3.35.0
BuildRequires:  pkgconfig(synctex) >= 2
Recommends:     %{name}-lang
Recommends:     %{name}-pdf-poppler-plugin
Suggests:       %{name}-cb-plugin
Suggests:       %{name}-djvu-plugin
Suggests:       %{name}-ps-plugin
%if %{with gcc15}
BuildRequires:  gcc15
%endif

%description
zathura is a customizable document viewer. It provides a minimalistic
and space-saving interface as well as a keyboard-centric interaction.

%package devel
Summary:        Development files for zathura
Requires:       %{name} = %{version}

%description devel
Development and header files for the zathura package.

%package bash-completion
Summary:        Zathura Bash completion
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Optional dependency offering bash completion for zathura

%package zsh-completion
Summary:        Zathura zsh completion
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Optional dependency offering zsh completion for zathura

%package fish-completion
Summary:        Zathura fish completion
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Optional dependency offering fish completion for zathura

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="%{?build_ldflags} -pie"
%{?with_gcc15:export CC=gcc-15}
%meson
%meson_build

%install
%meson_install

%find_lang %{appid} %{name}.lang

%check
xvfb-run %{_bindir}/meson test -C %{_vpath_builddir} %{?_smp_mflags} --print-errorlogs

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-sandbox
%{_datadir}/dbus-1/interfaces/%{appid}.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-sandbox.1%{?ext_man}
%{_mandir}/man5/%{name}rc.5%{?ext_man}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}.??g
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files lang -f %{name}.lang

%changelog
