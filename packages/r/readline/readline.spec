#
# spec file for package readline
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


%define rl_major 8
%define rextend  %{nil}
%define rversion 8.3
%define rpatchlvl %(bash %{_sourcedir}/get_version_number.sh %{_sourcedir})

Name:           readline
Version:        %{rversion}.%{rpatchlvl}
Release:        0
Summary:        The readline library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/readline/
# Git:          http://git.savannah.gnu.org/cgit/bash.git
Source0:        https://ftp.gnu.org/gnu/readline/readline-%{rversion}%{rextend}.tar.gz
Source1:        https://ftp.gnu.org/gnu/readline/readline-%{rversion}%{rextend}.tar.gz.sig
Source2:        baselibs.conf
Source3:        get_version_number.sh
Source4:        https://tiswww.case.edu/php/chet/gpgkey.asc#/%{name}.keyring
# official patches
Patch101:       readline83-001
Patch102:       readline83-002
Patch103:       readline83-003
# signatures for official patches
Source101:      readline83-001.sig
Source102:      readline83-002.sig
Source103:      readline83-003.sig
# local patches
Patch200:       readline-%{rversion}.dif
Patch201:       readline-6.3-input.dif
Patch202:       readline-5.2-conf.patch
Patch203:       readline-6.2-metamode.patch
Patch205:       readline-6.2-xmalloc.dif
Patch206:       readline-6.3-destdir.patch
Patch207:       readline-6.3-rltrace.patch
Patch208:       readline-7.0-screen.patch
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
#
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif

%description
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package -n libreadline%{rl_major}
Summary:        The Readline Library
Group:          System/Libraries
Suggests:       readline-doc = %{version}
Provides:       bash:/%{_lib}/libreadline.so.%{rl_major}
Provides:       libreadline%{rl_major} = %{rversion}
Provides:       readline = %{rversion}
Obsoletes:      readline <= 6.3

%description -n libreadline%{rl_major}
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package devel
Summary:        Development files for readline
Group:          Development/Libraries/C and C++
Provides:       pkgconfig(readline) = %{rversion}
Requires:       libreadline%{rl_major} >= %{rversion}
Requires:       ncurses-devel
Recommends:     readline-doc = %{version}

%description devel
This package contains the header files for the readline library.

%package devel-static
Summary:        Static library for development with readline
Group:          Development/Libraries/C and C++
Requires:       ncurses-devel
Requires:       readline-devel = %{version}
Recommends:     readline-doc = %{version}

%description devel-static
This package contains the static library for the readline library.

%package doc
Summary:        Documentation how to Use and Program with the Readline Library
Group:          Documentation/Other
Supplements:    (libreadline%{rl_major} and patterns-base-documentation)
Provides:       readline:%{_infodir}/readline.info.gz
BuildArch:      noarch

%description doc
This package contains the documentation for using the readline library
as well as programming with the interface of the readline library.

%prep
%setup -q -n readline-%{rversion}%{rextend}
# official patches
%patch -P101 -p0
%patch -P102 -p0
%patch -P103 -p0
# local patches
%patch -P201 -p2 -b .zerotty
%patch -P202 -p2 -b .conf
%patch -P203 -p2 -b .metamode
%patch -P205  -b .xm
%patch -P206  -b .destdir
%patch -P207 -p2 -b .tmp
%patch -P208 -p2 -b .screen
%patch -P200  -b .0

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
LANG=POSIX
LC_ALL=$LANG
unset LC_CTYPE
autoconf
cflags ()
{
    local flag=$1; shift
    local var=$1; shift
    test -n "${flag}" -a -n "${var}" || return
    case "${!var}" in
    *${flag}*) return
    esac
    set -o noclobber
    case "$flag" in
    -Wl,*)
	  if echo 'int main () { return 0; }' | \
 	     ${CC:-gcc} -Werror $flag -o /dev/null -xc - > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
	  ;;
    *)
	  if ${CC:-gcc} -Werror ${flag/#-Wno-/-W} -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
	  if ${CXX:-g++} -Werror ${flag/#-Wno-/-W} -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
    esac
    set +o noclobber
}
LARGEFILE="$(getconf LFS_CFLAGS)"
(cat > dyn.map)<<-'EOF'
	{
	    *;
	    !rl_*stream;
	};
	EOF
(cat > rl.map)<<-'EOF'
	READLINE_6.3 {
	    rl_change_environment;
	    rl_clear_history;
	    rl_executing_key;
	    rl_executing_keyseq;
	    rl_filename_stat_hook;
	    rl_history_substr_search_backward;
	    rl_history_substr_search_forward;
	    rl_input_available_hook;
	    rl_print_last_kbd_macro;
	    rl_signal_event_hook;
	};

	READLINE_7.0 {
	    rl_bracketed_paste_begin;
	    rl_callback_sigcleanup;
	    rl_clear_visible_line;
	    rl_pending_signal;
	    rl_redraw_prompt_last_line;
	    rl_tty_set_echoing;
	    rl_vi_unix_word_rubout;
	    rl_vi_yank_pop;
	    history_file_version;
	    history_lines_read_from_file;
	    history_lines_written_to_file;
	    history_multiline_entries;
	    rl_persistent_signal_handlers;
	    history_file_version;
	    history_lines_read_from_file;
	    history_lines_written_to_file;
	    history_multiline_entries;
	    rl_persistent_signal_handlers;
	} READLINE_6.3;

	READLINE_8.0 {
	    remove_history_range;
	    rl_check_signals;
	    rl_empty_keymap;
	    rl_function_of_keyseq_len;
	    rl_next_screen_line;
	    rl_previous_screen_line;
	    rl_set_keymap_name;
	    history_quoting_state;
	} READLINE_7.0;

	READLINE_8.1 {
	    rl_activate_mark;
	    rl_clear_display;
	    rl_deactivate_mark;
	    rl_keep_mark_active;
	    rl_mark_active_p;
	    rl_operate_and_get_next;
	} READLINE_8.0;

	READLINE_8.2 {
	    rl_fetch_history;
	    rl_set_timeout;
	    rl_timeout_remaining;
	    rl_trim_arg_from_keyseq;
	    rl_eof_found;
	    rl_timeout_event_hook;
	} READLINE_8.1;
	EOF
found=0
for rl in %{_libdir}/libreadline.so.*.*
do
    test READLINE_${rl##/*.so.} = READLINE_%{rversion} && found=1
done
if test $found = 0
then
   %{warn:Warning, ABI change likely}
   sleep 5
fi

CFLAGS="%{optflags} $LARGEFILE -D_GNU_SOURCE -D_RPM_OPT_FLAGS -g"
LDFLAGS=""
cflags -Wuninitialized         CFLAGS
cflags -Wextra                 CFLAGS
cflags -Wno-unprototyped-calls CFLAGS
cflags -Wno-switch-enum        CFLAGS
cflags -Wno-unused-variable    CFLAGS
cflags -Wno-unused-parameter   CFLAGS
cflags -Wno-parentheses        CFLAGS
cflags -ftree-loop-linear      CFLAGS
cflags -pipe                   CFLAGS
cflags -Wl,--as-needed         LDFLAGS
cflags -Wl,-O2                 LDFLAGS
cflags -Wl,--version-script=${PWD}/rl.map   LDFLAGS
cflags -Wl,--dynamic-list=${PWD}/dyn.map    LDFLAGS
CC=gcc
CC_FOR_BUILD="$CC"
CFLAGS_FOR_BUILD="$CFLAGS"
LDFLAGS_FOR_BUILD="$LDFLAGS"
export CC_FOR_BUILD CFLAGS_FOR_BUILD LDFLAGS_FOR_BUILD CFLAGS LDFLAGS CC
# FIXME: you should use the %%configure macro
./configure --build=%{_target_cpu}-suse-linux	\
	--enable-static			\
	--enable-shared			\
	--enable-multibyte		\
	--disable-bracketed-paste-default \
	--prefix=%{_prefix}		\
	--with-curses			\
	--mandir=%{_mandir}		\
	--infodir=%{_infodir}		\
	--docdir=%{_docdir}/%{name}	\
	--libdir=%{_libdir}
%make_build
%make_build documentation

%install
%make_install everything htmldir=%{_docdir}/%{name} installdir=%{_docdir}/%{name}/examples

%post -n libreadline%{rl_major} -p /sbin/ldconfig
%postun -n libreadline%{rl_major} -p /sbin/ldconfig

%files -n libreadline%{rl_major}
%license COPYING
%{_libdir}/libhistory.so.%{rl_major}
%{_libdir}/libhistory.so.%{rversion}
%{_libdir}/libreadline.so.%{rl_major}
%{_libdir}/libreadline.so.%{rversion}

%files devel
%{_includedir}/readline/
%{_libdir}/libhistory.so
%{_libdir}/libreadline.so
%{_libdir}/pkgconfig/history.pc
%{_libdir}/pkgconfig/readline.pc

%files devel-static
%{_libdir}/libhistory.a
%{_libdir}/libreadline.a

%files doc
%{_infodir}/history.info%{?ext_info}
%{_infodir}/readline.info%{?ext_info}
%{_infodir}/rluserman.info%{?ext_info}
%{_mandir}/man3/history.3%{?ext_man}
%{_mandir}/man3/readline.3%{?ext_man}
%doc %{_docdir}/%{name}/

%changelog
