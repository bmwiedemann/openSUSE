#
# spec file for package polkit
#
# Copyright (c) 2023 SUSE LLC
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


%define _polkit_rulesdir %{_datadir}/polkit-1/rules.d
%define glib_br_version  2.30.0
%define run_tests        1

Name:           polkit
Version:        121
Release:        0
Summary:        PolicyKit Authorization Framework
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.freedesktop.org/wiki/Software/polkit/
Source0:        https://www.freedesktop.org/software/polkit/releases/%{name}-%{version}.tar.gz
Source1:        https://www.freedesktop.org/software/polkit/releases/%{name}-%{version}.tar.gz.sign
Source2:        %{name}.keyring
Source3:        system-user-polkitd.conf
Source99:       baselibs.conf

# Upstream First - Policy:
# Never add any patches to this package without the upstream commit id
# in the patch. Any patches added here without a very good reason to make
# an exception will be silently removed with the next version update.

# PATCH-FIX-OPENSUSE polkit-no-wheel-group.patch vuntz@opensuse.org -- In openSUSE, there's no special meaning for the wheel group, so we shouldn't allow it to be admin
Patch0:         polkit-no-wheel-group.patch
# PATCH-FIX-OPENSUSE polkit-gettext.patch lnussel@suse.de -- allow fallback to gettext for polkit action translations
# polkit-use-gettext-as-fallback.patch
Patch1:         polkit-gettext.patch
# PATCH-FIX-OPENSUSE polkit-keyinit.patch meissner@ -- bsc#1144053 Please add "pam_keyinit.so" to the /etc/pam.d/polkit-1 configuration file
Patch3:         polkit-keyinit.patch
# PATCH-FIX-OPENSUSE polkit-adjust-libexec-path.patch -- Adjust path to polkit-agent-helper-1 (bsc#1180474)
Patch4:         polkit-adjust-libexec-path.patch
# PATCH-FIX-UPSTREAM polkit-fix-pam-prefix.patch luc14n0@opensuse.org -- Make
# intended use of pam_prefix meson option rather than hard-coded path
Patch5:         polkit-fix-pam-prefix.patch
# Read actions also from /etc/polkit-1/actions
Patch6:         polkit-actions-in-etc.patch

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libexpat-devel
BuildRequires:  meson >= 0.50
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(duktape) >= 2.2.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_br_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_br_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib_br_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.2
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%if 0%{?run_tests}
#################################################################
# python3-dbus-python and python3-python-dbusmock are needed for
# test-polkitbackendjsauthority test:
BuildRequires:  python3-dbus-python
BuildRequires:  python3-python-dbusmock
#################################################################
%endif
# gtk-doc drags indirectyly ruby in for one of the helpers. This in turn causes a build cycle.
#!BuildIgnore:  ruby

Requires:       dbus-1
Requires:       libpolkit-agent-1-0 = %{version}-%{release}
Requires:       libpolkit-gobject-1-0 = %{version}-%{release}
Requires(post): permissions
%sysusers_requires
%systemd_ordering

%description
PolicyKit is a toolkit for defining and handling authorizations.
It is used for allowing unprivileged processes to speak to privileged
processes.

%package devel
Summary:        Development files for PolicyKit
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libpolkit-agent-1-0 = %{version}
Requires:       libpolkit-gobject-1-0 = %{version}
Requires:       pkgconfig
Requires:       typelib-1_0-Polkit-1_0 = %{version}

%description devel
Development files for PolicyKit Authorization Framework.

%package -n pkexec
Summary:        Pkexec component of polkit
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}
Requires(post): permissions
Provides:       polkit:/usr/bin/pkexec

%description -n pkexec
This package contains the pkexec setuid root binary part of polkit.

%package doc
Summary:        Development documentation for PolicyKit
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description doc
Development documentation for PolicyKit Authorization Framework.

%package -n libpolkit-agent-1-0
Summary:        PolicyKit Authorization Framework -- Agent Library
Group:          System/Libraries
Requires:       %{name} >= %{version}
Obsoletes:      libpolkit0 < %{version}-%{release}

%description -n libpolkit-agent-1-0
PolicyKit is a toolkit for defining and handling authorizations.
It is used for allowing unprivileged processes to speak to privileged
processes.

This package contains the agent library only.

%package -n libpolkit-gobject-1-0
Summary:        PolicyKit Authorization Framework -- GObject Library
Group:          System/Libraries
Requires:       %{name} >= %{version}
Obsoletes:      libpolkit0 < %{version}-%{release}

%description -n libpolkit-gobject-1-0
PolicyKit is a toolkit for defining and handling authorizations.
It is used for allowing unprivileged processes to speak to privileged
processes.

This package contains the gobject library only.

%package -n typelib-1_0-Polkit-1_0
Summary:        PolicyKit Authorization Framework -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Polkit-1_0
PolicyKit is a toolkit for defining and handling authorizations.
It is used for allowing unprivileged processes to speak to privileged
processes.

This package provides the GObject Introspection bindings for PolicyKit.

%prep
%autosetup -p1 -n polkit-v.%{version}

%build
%meson                                     \
    -D session_tracking=libsystemd-login   \
    -D systemdsystemunitdir="%{_unitdir}"  \
    -D os_type=suse                        \
    -D pam_module_dir="%{_pam_moduledir}"  \
    -D pam_prefix="%{_pam_vendordir}"      \
    -D examples=true                       \
    -D tests=true                          \
    -D gtk_doc=true                        \
    -D man=true                            \
    -D js_engine=duktape                   \
    %{nil}
%meson_build
%sysusers_generate_pre %{SOURCE3} polkit system-user-polkitd.conf

%if 0%{?run_tests}
%check
%meson_test
%endif

%install
# install explicitly into libexec. upstream has some unflexible logic for
# this executable at the moment, but there is a PR# open to fix this:
#     https://gitlab.freedesktop.org/polkit/polkit/-/merge_requests/63
# once this has been resolved upstream and we update to a new release we can
# remove this and also patch4 above.
#
# Additional note: Upstream turned down the MR above, preferring to stick to
# using ${prefix}/lib/polkit-1 and non-distro-configurable.
%meson_install
%find_lang polkit-1

# create $HOME for polkit user
install -d %{buildroot}%{_localstatedir}/lib/polkit

# We use /usr/share as prefix for the rules.d directory
mv %{buildroot}%{_sysconfdir}/polkit-1/rules.d/50-default.rules \
   %{buildroot}%{_polkit_rulesdir}/50-default.rules

# Install the polkitd user creation file:
mkdir -p %{buildroot}%{_sysusersdir}
install -m0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/

# create actions dir in /etc
mkdir %{buildroot}/%{_sysconfdir}/polkit-1/actions

%pre -f polkit.pre
%service_add_pre polkit.service

%preun
%service_del_preun polkit.service

%postun
%service_del_postun polkit.service

%post -n pkexec
%set_permissions %{_bindir}/pkexec

%post
%set_permissions %{_libexecdir}/polkit-1/polkit-agent-helper-1
%service_add_post polkit.service

%verifyscript -n pkexec
%verify_permissions -e %{_bindir}/pkexec

%verifyscript
%verify_permissions -e %{_libexecdir}/polkit-1/polkit-agent-helper-1

%post -n libpolkit-agent-1-0 -p /sbin/ldconfig
%postun -n libpolkit-agent-1-0 -p /sbin/ldconfig
%post -n libpolkit-gobject-1-0 -p /sbin/ldconfig
%postun -n libpolkit-gobject-1-0 -p /sbin/ldconfig

%files -n libpolkit-agent-1-0
%{_libdir}/libpolkit-agent-1.so.*

%files -n libpolkit-gobject-1-0
%{_libdir}/libpolkit-gobject-1.so.*

%files -n typelib-1_0-Polkit-1_0
%{_libdir}/girepository-1.0/Polkit-1.0.typelib
%{_libdir}/girepository-1.0/PolkitAgent-1.0.typelib

%files -f polkit-1.lang
%doc NEWS.md README.md
%license COPYING

%{_mandir}/man1/pkaction.1%{?ext_man}
%{_mandir}/man1/pkcheck.1%{?ext_man}
%{_mandir}/man1/pkttyagent.1%{?ext_man}
%{_mandir}/man8/polkitd.8%{?ext_man}
%{_mandir}/man8/polkit.8%{?ext_man}
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.freedesktop.PolicyKit1.service
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
%dir %{_datadir}/polkit-1
%{_datadir}/polkit-1/policyconfig-1.dtd
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.policy
%attr(0750,root,polkitd) %dir %{_polkit_rulesdir}
%attr(0640,root,polkitd) %{_polkit_rulesdir}/50-default.rules
%{_pam_vendordir}/polkit-1
%dir %{_sysconfdir}/polkit-1
%attr(0750,root,polkitd) %dir %{_sysconfdir}/polkit-1/rules.d
%dir %{_sysconfdir}/polkit-1/actions
%{_bindir}/pkaction
%{_bindir}/pkcheck
%{_bindir}/pkttyagent
%dir %{_libexecdir}/polkit-1
%{_libexecdir}/polkit-1/polkitd
%verify(not mode) %attr(4755,root,root) %{_libexecdir}/polkit-1/polkit-agent-helper-1
# $HOME for polkit user
%dir %{_localstatedir}/lib/polkit
%{_sysusersdir}/system-user-polkitd.conf
%{_unitdir}/polkit.service

%files devel
%{_libdir}/libpolkit-agent-1.so
%{_libdir}/libpolkit-gobject-1.so
%{_libdir}/pkgconfig/polkit-agent-1.pc
%{_libdir}/pkgconfig/polkit-gobject-1.pc
%{_includedir}/polkit-1/
%{_bindir}/pk-example-frobnicate
%{_datadir}/gir-1.0/*.gir
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.examples.pkexec.policy
%{_datadir}/gettext/its/polkit.its
%{_datadir}/gettext/its/polkit.loc

%files -n pkexec
%{_mandir}/man1/pkexec.1%{?ext_man}
%verify(not mode) %attr(4755,root,root) %{_bindir}/pkexec

%files doc
%doc %{_datadir}/gtk-doc/html/polkit-1/

%changelog
