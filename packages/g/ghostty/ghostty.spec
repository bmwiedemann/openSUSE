#
# spec file for package ghostty
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


%global shlib_name libghostty-vt0
%global common_build_flags --system %{_builddir}/%{name}-%{version}/vendor/zig/p -Doptimize=ReleaseFast -Dcpu=baseline -Dpie=true -Dstrip=false -Dversion-string=%{version} -fsys=freetype -fsys=harfbuzz -fsys=fontconfig -fsys=libpng -fsys=zlib -fsys=oniguruma -fsys=glslang -fsys=spirv-cross -fsys=simdutf -fsys=gtk4-layer-shell -fsys=highway %{?_smp_mflags}

%bcond_without  standalone_terminfo

Name:           ghostty
Version:        1.3.1
Release:        0
Summary:        Cross-platform terminal emulator
License:        MIT AND OFL-1.1
URL:            https://github.com/ghostty-org/ghostty
# can be verified with:
# minisign -V -P 'RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV' -m ghostty-%%{version}.tar.gz
Source0:        https://release.files.ghostty.org/%{version}/ghostty-%{version}.tar.gz
Source2:        https://release.files.ghostty.org/%{version}/ghostty-%{version}.tar.gz.minisig
Source1:        vendor.tar.zst
Source99:       vendor.sh
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  zig >= 0.15.2
BuildRequires:  cmake(glslang)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(graphene-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libhwy)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(simdutf)
BuildRequires:  pkgconfig(spirv-cross-c-shared)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python-nautilus-common-files
BuildRequires:  python3-gobject
%if %{with standalone_terminfo}
Requires:       terminfo-ghostty = %{version}
%else
BuildRequires:  terminfo
Requires:       terminfo >= %{terminfo_with_ghostty_version}
%endif

%description
Ghostty is a fast, feature-rich, and cross-platform terminal
emulator that uses platform-native UI and GPU acceleration.

%package        bash-completion
Summary:        Bash Support for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash support for %{name}.

%package        fish-completion
Summary:        Fish Support for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish support for %{name}.

%package        zsh-completion
Summary:        Zsh Support for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
Zsh support for %{name}.

%package        nushell-completion
Summary:        Nushell Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       nushell
Supplements:    (%{name} and nushell)
BuildArch:      noarch

%description    nushell-completion
Nushell support for %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides documentation for %{name}

%package neovim
Summary:        Neovim syntax highlighting for %{name} data files
Requires:       %{name} = %{version}
Requires:       neovim
Supplements:    (%{name} and neovim)
BuildArch:      noarch

%description neovim
Optional files for syntax highlighting for %{name} data files in neovim.

%package vim
Summary:        Vim syntax highlighting for %{name} data files
Requires:       %{name} = %{version}
Requires:       vim
Supplements:    (%{name} and vim)
BuildArch:      noarch

%description vim
Optional files for syntax highlighting for %{name} data files in vim.

%package -n nautilus-extension-ghostty
Summary:        Nautilus extension for ghostty
Requires:       %{name} = %{version}
Requires:       nautilus
Requires:       python-nautilus-common-files
Requires:       python3-gobject
Supplements:    (%{name} and nautilus)
BuildArch:      noarch

%description -n nautilus-extension-ghostty
Nautilus extension for ghostty.

%package -n terminfo-ghostty
Summary:        Terminfo files for ghostty
BuildArch:      noarch

%description -n terminfo-ghostty
Ghostty is a fast, feature-rich, and cross-platform terminal
emulator that uses platform-native UI and GPU acceleration.

This holds the terminfo files for ghostty.

%package -n %{shlib_name}
Summary:        C-compatible library for embedding a fast, feature-rich terminal emulator

%description -n %{shlib_name}
A zero-dependency library that provides an API for parsing terminal sequences
and maintaining terminal state, extracted directly from Ghostty's real-world proven core

%ldconfig_scriptlets -n %{shlib_name}

%package devel
Summary:        Development files for for ghostty's VT library
Group:          Development/Libraries/C and C++
Requires:       %{shlib_name} = %{version}

%description devel
This package contains all necessary include files and libraries needed to develop applications
that need to embed a fast, feature-rich terminal emulator

%lang_package

%prep
%autosetup -p1 -a1

%build
# Run `./nix/build-support/fetch-zig-cache.sh` locally to
# prep deps for offline install
zig build %{common_build_flags}

%install
export DESTDIR=%{buildroot}
zig build %{common_build_flags} --prefix %{_prefix} --prefix-lib-dir %{_libdir}
%if %{without standalone_terminfo}
rm -rv %{buildroot}%{_datadir}/terminfo/
%endif

mv %{buildroot}%{_datadir}/pkgconfig/ %{buildroot}%{_libdir}

%find_lang com.mitchellh.ghostty

%fdupes %{buildroot}/%{_datadir}/icons/hicolor
%fdupes %{buildroot}/%{_datadir}/%{pkg_name}/themes

%files
%license LICENSE src/font/res/OFL.txt
%{_bindir}/ghostty
%{_datadir}/applications/com.mitchellh.ghostty.desktop
%{_mandir}/man1/ghostty.1%{?ext_man}
%{_mandir}/man5/ghostty.5%{?ext_man}
%{_datadir}/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png
%{_datadir}/icons/hicolor/1024x1024/apps/com.mitchellh.ghostty.png
%dir %{_datadir}/icons/hicolor/128x128@2
%dir %{_datadir}/icons/hicolor/128x128@2/apps
%dir %{_datadir}/icons/hicolor/16x16@2
%dir %{_datadir}/icons/hicolor/16x16@2/apps
%dir %{_datadir}/icons/hicolor/256x256@2
%dir %{_datadir}/icons/hicolor/256x256@2/apps
%dir %{_datadir}/icons/hicolor/32x32@2
%dir %{_datadir}/icons/hicolor/32x32@2/apps

%dir %{_datadir}/ghostty
%dir %{_datadir}/ghostty/shell-integration
%{_datadir}/ghostty/shell-integration/elvish/
%{_datadir}/ghostty/themes/

%dir %{_datadir}/bat
%dir %{_datadir}/bat/syntaxes
%{_datadir}/bat/syntaxes/ghostty.sublime-syntax

%{_userunitdir}/app-com.mitchellh.ghostty.service
%{_datadir}/dbus-1/services/com.mitchellh.ghostty.service
%{_datadir}/metainfo/com.mitchellh.ghostty.metainfo.xml

%dir %{_datadir}/kio
%dir %{_datadir}/kio/servicemenus
%{_datadir}/kio/servicemenus/com.mitchellh.ghostty.desktop

%files -n nautilus-extension-ghostty
%license LICENSE
%{_datadir}/nautilus-python/extensions/ghostty.py

%files neovim
%license LICENSE
%{_datadir}/nvim/site/ftdetect/ghostty.vim
%{_datadir}/nvim/site/ftplugin/ghostty.vim
%{_datadir}/nvim/site/syntax/ghostty.vim
%{_datadir}/nvim/site/compiler/ghostty.vim
%dir %{_datadir}/nvim
%dir %{_datadir}/nvim/site
%dir %{_datadir}/nvim/site/ftdetect
%dir %{_datadir}/nvim/site/ftplugin
%dir %{_datadir}/nvim/site/syntax
%dir %{_datadir}/nvim/site/compiler/

%files doc
%license LICENSE
%dir %{_datadir}/ghostty/doc
%{_datadir}/ghostty/doc/ghostty.1.html
%{_datadir}/ghostty/doc/ghostty.1.md
%{_datadir}/ghostty/doc/ghostty.5.html
%{_datadir}/ghostty/doc/ghostty.5.md

%files bash-completion
%license LICENSE
%{_datadir}/bash-completion/completions/ghostty.bash
%{_datadir}/ghostty/shell-integration/bash/

%files fish-completion
%license LICENSE
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/ghostty.fish
%{_datadir}/ghostty/shell-integration/fish/

%files zsh-completion
%license LICENSE
%{_datadir}/zsh/site-functions/_ghostty
%{_datadir}/ghostty/shell-integration/zsh/

%files nushell-completion
%license LICENSE
%{_datadir}/ghostty/shell-integration/nushell/

%files vim
%license LICENSE
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/ftplugin
%dir %{_datadir}/vim/vimfiles/syntax
%dir %{_datadir}/vim/vimfiles/compiler
%{_datadir}/vim/vimfiles/ftdetect/ghostty.vim
%{_datadir}/vim/vimfiles/ftplugin/ghostty.vim
%{_datadir}/vim/vimfiles/syntax/ghostty.vim
%{_datadir}/vim/vimfiles/compiler/ghostty.vim

%if %{with standalone_terminfo}
%files -n terminfo-ghostty
%license LICENSE
%{_datadir}/terminfo/g/ghostty
%{_datadir}/terminfo/x/xterm-ghostty
%endif

%files -f com.mitchellh.ghostty.lang lang

%files -n %{shlib_name}
%license LICENSE
%{_libdir}/libghostty-vt.so.*

%files devel
%license LICENSE
%{_includedir}/ghostty
%{_libdir}/libghostty-vt.so
%{_libdir}/pkgconfig/libghostty-vt.pc

%changelog
