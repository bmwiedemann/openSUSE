#
# spec file for package weechat
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


Name:           weechat
Version:        4.3.1
Release:        0
Summary:        Multi-protocol extensible Chat Client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/IRC
URL:            https://weechat.org
Source:         https://weechat.org/files/src/%{name}-%{version}.tar.xz
Source1:        weechat.desktop
Source2:        https://weechat.org/files/src/%{name}-%{version}.tar.xz.asc
Source3:        %{name}.keyring
Source4:        %{name}.changes
BuildRequires:  ca-certificates
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  grep
BuildRequires:  hicolor-icon-theme
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  ruby-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tcl)
Requires:       ca-certificates
Requires:       hicolor-icon-theme
Recommends:     %{name}-lang = %{version}
# without scripts it is a bit annoying
Recommends:     %{name}-perl = %{version}
Recommends:     %{name}-python = %{version}
Obsoletes:      %{name}-guile < 2.6

%description
WeeChat (Wee Enhanced Environment for Chat) is a free chat client, fast and light, designed for many operating systems. It is highly customizable and extensible with scripts.

Homepage: https://weechat.org/

%lang_package

%package devel
Summary:        Development Environment for %{name} Plugins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development environment for authoring %{name} plugins.

%package lua
Summary:        Lua Scripting Support for %{name}
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}

%description lua
Support for %{name} scripts written in the Lua language.

%package perl
Summary:        Perl Scripting Support for %{name}
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}
%{?libperl_requires}

%description perl
Support for %{name} scripts written in the Perl language.

%package python
Summary:        Python Scripting Support for %{name}
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}

%description python
Support for %{name} scripts written in the Python language.

%package tcl
Summary:        Tcl Scripting Support for %{name}
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}

%description tcl
Support for %{name} scripts written in the Tcl language.

%package ruby
Summary:        Ruby Scripting Support for %{name}
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}

%description ruby
Support for %{name} scripts written in the Ruby language.

%package spell
Summary:        Aspell and Enchant Spell-Checking Support for %{name}
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}
Supplements:    (%{name} and enchant-2-backend-hunspell)
Obsoletes:      %{name}-aspell < %{version}
Provides:       %{name}-aspell = %{version}

%description spell
Spell-checking support for %{name}, using the aspell and enchant libraries.

%prep
%autosetup -p1
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE4}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -name '*.[ch]' -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" "{}" "+"

%build
export CFLAGS="%{optflags}"
# Tests require cpputest package
# no-undefined for perl seem not to work as desired
%cmake \
    -DLIBDIR="%{_libdir}" \
    -DENABLE_PYTHON=ON \
    -DPYTHON_LIBRARY="%{_libdir}/libpython%{py3_ver}m.so" \
    -DENABLE_ENCHANT=ON \
    -DENABLE_GUILE=OFF \
    -DENABLE_JAVASCRIPT=OFF \
    -DENABLE_PHP=OFF \
    -DCA_FILE=%{_sysconfdir}/ssl/ca-bundle.pem
%cmake_build

%install
%cmake_install

install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" Network IRCClient

%find_lang "%{name}" --with-man

%files
%doc AUTHORS.adoc ChangeLog.adoc Contributing.adoc
%doc README.adoc ReleaseNotes.adoc
%license COPYING
%{_bindir}/weechat-curses
%{_bindir}/weechat-headless
%{_bindir}/weechat
%dir %{_libdir}/weechat
%dir %{_libdir}/weechat/plugins
%{_libdir}/weechat/plugins/alias.so
%{_libdir}/weechat/plugins/buflist.so
%{_libdir}/weechat/plugins/charset.so
%{_libdir}/weechat/plugins/exec.so
%{_libdir}/weechat/plugins/fifo.so
%{_libdir}/weechat/plugins/irc.so
%{_libdir}/weechat/plugins/logger.so
%{_libdir}/weechat/plugins/relay.so
%{_libdir}/weechat/plugins/script.so
%{_libdir}/weechat/plugins/trigger.so
%{_libdir}/weechat/plugins/xfer.so
%{_libdir}/weechat/plugins/fset.so
%{_libdir}/weechat/plugins/typing.so
%{_datadir}/applications/weechat.desktop
%{_datadir}/icons/hicolor/*/apps/weechat.png

%files -f "%{name}.lang" lang
%license COPYING

%files devel
%license COPYING
%{_includedir}/weechat
%{_libdir}/pkgconfig/weechat.pc

%files lua
%license COPYING
%{_libdir}/weechat/plugins/lua.so

%files perl
%license COPYING
%{_libdir}/weechat/plugins/perl.so

%files python
%license COPYING
%{_libdir}/weechat/plugins/python.so

%files tcl
%license COPYING
%{_libdir}/weechat/plugins/tcl.so

%files ruby
%license COPYING
%{_libdir}/weechat/plugins/ruby.so

%files spell
%license COPYING
%{_libdir}/weechat/plugins/spell.so

%changelog
