#
# spec file for package watchman
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


%define docdir %{_defaultdocdir}/watchman
%define rundir /run/watchman
Name:           watchman
Version:        4.9.0
Release:        0
Summary:        A file watching service
# the thirdparty code is partially MIT-licensed or at least some such
License:        Apache-2.0 AND MIT
Group:          System/Monitoring
URL:            https://facebook.github.io/watchman/
Source0:        https://github.com/facebook/watchman/archive/v%{version}.tar.gz
# tmpfiles.d configuration for statedir
Source1:        watchman.conf
Source2:        watchman@.service
Source3:        watchman@.socket
# prevent the build system overwriting the autotools docdir in a hard-coded way
Patch0:         %{name}_4.7.0_makefile-am.diff
Patch1:         0001-Replaced-memset-calls-with-appopriate-C-11-init-or-a.patch
Patch2:         0002-Re-worked-replacement-of-memset-with-proper-init-to-.patch
Patch3:         libart-gcc10.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpcre16)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libpcreposix)
Requires:       pcre
# TODO: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
%{?systemd_requires}

%description
Watchman exists to watch files and record when they change. It can also trigger
actions (such as rebuilding assets) when matching files change.

* Watchman can recursively watch one or more directory trees (we call them
roots).
* Watchman does not follow symlinks. It knows they exist, but they show up the
same as any other file in its reporting.
* Watchman waits for a root to settle down before it will start to trigger
notifications or command execution.
* Watchman is conservative, preferring to err on the side of caution; it
considers files to be freshly changed when you start to watch them or when it
is unsure.
* You can query a root for file changes since you last checked, or the current
state of the tree
* You can subscribe to file changes that occur in a root

%package -n python3-watchman
Version:        1.4.0
Release:        0
Summary:        A python package for talking to the watchman service
# from python/setup.py
License:        BSD-3-Clause
Group:          System/Monitoring
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-base
Conflicts:      watchman-python < %{version}

# NOTE: the additional scripts like watchman-make are written in python. I
# guess those scripts don't justify another subpackage, so I add them as a
# bargain to the python bindings.
%description -n python3-watchman
Provides Python bindings for directly talking to the watchman service from
within Python.

Additionally, some Python tools that are part of watchman will be installed.

# %%package ruby
# There's also a ruby interface included in watchman.
# The integration into autotools is done via ruby's bundler.
# We can use gem2rpm to create a spec file for it, but it's probably better
# not to make it a subpackage but an independent package rubygem-watchman

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1

# There is some basic support for watchman to run under systemd:
#
# 	https://github.com/facebook/watchman/commit/2985377eaf8c8538b28fae9add061b67991a87c2
#
# It uses inetd style activation of watchman via systemd based on the socket
# it normally creates per user in /run/watchman/<user>-state.
#
# The unit files aren't currently shipped by upstream. Instead I've added
# them as extra source files. The two files for service and socket are
# template systemd unit files. This way multiple instances of watchman can be
# setup for each user in the system.
#
# It's a bit unclear what the best group ownership and mode bits for the
# socket should be (see watchman@.socket). I'm currently going for more secure
# mode bits.
#
# Does it make sense to run watchman globally as a daemon as root?
#
# -> The developer emphasises that it's supposed to be per user:
#
# https://github.com/facebook/watchman/issues/8
#
# But using the systemd template unit file we can also setup a watchman
# instance for the root user, if desired.
#
# watchman wants to install a statedir in <prefix>/var/run. This statedir is
# supposed to have the sticky bit set, so any user can create sub-directories
# in it for their private state.
#
# Due to systemd handling of /run & /var/run we need to change this to a
# tmpfiles.d approach. We still need to configure with --enable-statedir,
# however, because otherwise the code wouldn't operate with the statedir any
# more but resort to statedirs in /tmp:
#
# https://facebook.github.io/watchman/docs/cli-options.html#quick-note-on-default-locations
#
# We could patch this, but for now I pass the correct enable-statedir which
# gives the code to the right behaviour and location. The statedir that's
# installed via 'make install' is then removed again and replaced by the
# correct tmpfiles.d handling. Otherwise rpmlint barks about evil permissions
# of the statedir (world-writable).
#
# There's no man page for this package as the developer prefers his readme in
# markdown format and also doesn't believe in man pages in the 21st century:
#
# https://github.com/facebook/watchman/issues/30

%build
./autogen.sh
# There is a single gcc strict aliasing problem in "bser.c" which is used to
# build a shared-object "bser.so" that is used in the python package. It can't
# be easily fixed, however, because the aliasing problem arises in
# python-devel headers. It's the same situation as described here:
#
# https://lists.fedoraproject.org/pipermail/scm-commits/2010-September/496900.html
#
# So let's build everything with no strict aliasing then
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -Wno-format-truncation"
%configure \
	--without-ruby \
	--enable-statedir=%{rundir} \
	--docdir=%docdir # see Patch0, docs should be placed in the packages subdir
make %{?_smp_mflags}

%install
%make_install

%define build_tmpfiles %{buildroot}%{_tmpfilesdir}
%define build_tmpfile_conf %{build_tmpfiles}/%{name}.conf
# don't package this installed state directory, we just need to configure with
# --enable-statedir for the code to be compiled with support for it, otherwise
# watchman falls back to using statedirs in /tmp.
rm -rf %{buildroot}/%{rundir}
# install the tmpfiles.d file instead for creating the statedir during runtime
# with sticky bit as expected by watchman
install -d -m 0755 %{build_tmpfiles}
install -m 0644 %{SOURCE1} %{build_tmpfile_conf}

%define build_unitdir %{buildroot}%{_unitdir}
install -D -m 444 %{SOURCE2} %{build_unitdir}/%{name}@.service
install -D -m 444 %{SOURCE3} %{build_unitdir}/%{name}@.socket

%define tmpfile_conf %{_tmpfilesdir}/%{name}.conf

%files
%doc %docdir
%{_bindir}/watchman
# explicitly own this dir, otherwise SLE12-SP2 build breaks? should actually
# be owned by the filesystem package.
%if 0%{?sle_version} <= 120200
%dir %{_tmpfilesdir}
%endif

%{tmpfile_conf}
# avoid rpmlint warning tmpfile-not-in-filelist
%ghost %{rundir}

%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}@.socket

%files -n python3-watchman
%{python3_sitearch}
# additional python tools for working with watchman, not strictly part of the
# python bindings, actually
%{_bindir}/watchman-*

%pre
%service_add_pre %{name}@.socket %{name}@.service

%post
# NOTE: when updating a warning is printed:
#
# Failed to try-restart watchman@s*: Unit name watchman@s* is not valid
#
# A similar warning is emitted during uninstall
#
# This seems to be an error in the generic systemd macros, they're not dealing
# correctly with template unit files.
%service_add_post %{name}@.socket %{name}@.service
# to initially create the statedir without reboot
# NOTE: This macro is not available in older versions of systemd-rpm-macros,
# causing builds on openSUSE_Leap < 42_2 to fail currently.
%tmpfiles_create %{tmpfile_conf}

%preun
%service_del_preun %{name}@.socket %{name}@.service

%postun
%service_del_postun %{name}@.socket %{name}@.service

%changelog
