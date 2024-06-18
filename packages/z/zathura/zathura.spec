#
# spec file for package zathura
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.5.6
Release:        0
Summary:        A customizable document viewer
License:        Zlib
URL:            https://pwmt.org/projects/zathura/
Source:         %{url}/download/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE no-parallel-xvfb.patch smolsheep@opensuse.org -- Fix tests that rely on xvfb
Patch0:         no-parallel-xvfb.patch
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  fish
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  rsvg-convert
BuildRequires:  xvfb-run
BuildRequires:  zsh
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(girara-gtk3) >= 0.4.3
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(sqlite3)
Recommends:     %{name}-lang
Recommends:     zathura-pdf-poppler-plugin
Suggests:       zathura-cb-plugin
Suggests:       zathura-djvu-plugin
Suggests:       zathura-ps-plugin
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(synctex) >= 1.19
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

%description bash-completion
Optional dependency offering bash completion for zathura

%package zsh-completion
Summary:        Zathura zsh completion
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Optional dependency offering zsh completion for zathura

%package fish-completion
Summary:        Zathura fish completion
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)

%description fish-completion
Optional dependency offering fish completion for zathura

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%if 0%{?suse_version} < 1550
%meson -Dsynctex=disabled
%else
%meson
%endif
%meson_build

%check
%if 0%{?qemu_user_space_build}
# qemu does not implement seccomp
echo 'int main() { return 77; }' > tests/test_session.c
%endif
%meson_test

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/org.pwmt.%{name}.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}rc.5%{?ext_man}
%{_datadir}/applications/org.pwmt.zathura.desktop
%{_datadir}/icons/hicolor/*/apps/org.pwmt.zathura.*
%{_datadir}/metainfo/org.pwmt.zathura.appdata.xml

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%files bash-completion
%{_datadir}/bash-completion/completions/zathura

%files zsh-completion
%{_datadir}/zsh/site-functions/_zathura

%files fish-completion
%{_datadir}/fish/vendor_completions.d/zathura.fish

%files lang -f %{name}.lang

%changelog
