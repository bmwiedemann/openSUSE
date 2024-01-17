#
# spec file for package lua-readline
#
# Copyright (c) 2021 SUSE LLC
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

%define flavor @BUILD_FLAVOR@%{nil}
%define mod_name readline
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        3.0
Release:        0
License:        MIT
Group:          Development/Languages/Other
Summary:        a simple interface to the readline and history libraries
Url:            https://pjb.com.au/comp/lua/readline.html
Source0:        https://pjb.com.au/comp/lua/%{mod_name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  readline-devel
Requires:       %{flavor}-luaposix >= 30
%lua_provides

%description
This Lua module offers a simple calling interface to the GNU Readline/History Library.
The function readline() is a wrapper, which invokes the GNU readline, adds the line to the end of the History List, and then returns the line. Usually you call save_history() before the program exits, so that the History List is saved to the histfile.
Various options can be changed using the set_options{} function.
The user can configure the GNU Readline (e.g. vi or emacs keystrokes ?) with their individual ~/.inputrc file, see the INITIALIZATION FILE section of man readline.
By default, the GNU readline library dialogues with the user by reading from stdin and writing to stdout; this fits very badly with applications that want to use stdin and stdout to input and output data. Therefore, this Lua module dialogues with the user on the controlling-terminal of the process (typically /dev/tty) as returned by ctermid().
Most of readline's Alternate Interface is now included, namely   handler_install,   read_char   and handler_remove.
Some applications need to interleave keyboard I/O with file, device, or window system I/O, typically by using a main loop to select() on various file descriptors.   To accommodate this need, readline can also be invoked as a 'callback' function from an event loop, and the Alternate Interface offers functions to do this.
The Alternate Interface does offer tab-completion; but it does not add to the history file, so you will probably want to call RL.add_history(s) explicitly. See handler_install()
Access to readline's Custom Completion is now provided.
This module does not work lua -i because that runs its own readline, and the two conflict with each other.

%prep
%autosetup -n %{mod_name}-%{version}

%build
CFLAGS="%{optflags}"
CFLAGS="$CFLAGS -I%{lua_incdir}"
cc $CFLAGS -shared -o C-readline.so -fPIC C-readline.c -llua -lreadline

%install
install -Dm644 C-readline.so %{buildroot}%{lua_archdir}/C-readline.so
install -Dm644 readline.lua %{buildroot}%{lua_noarchdir}/readline.lua

%files
%doc doc/readline.html
%{lua_archdir}/*
%{lua_noarchdir}/*

%changelog
