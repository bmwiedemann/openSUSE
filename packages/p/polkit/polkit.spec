#
# spec file for package polkit
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


Name:           polkit
Version:        0.120
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
# PATCH-FIX-OPENSUSE polkit-no-wheel-group.patch vuntz@opensuse.org -- In openSUSE, there's no special meaning for the wheel group, so we shouldn't allow it to be admin
Patch0:         polkit-no-wheel-group.patch
# PATCH-FIX-OPENSUSE polkit-gettext.patch lnussel@suse.de -- allow fallback to gettext for polkit action translations
Patch1:         polkit-gettext.patch
# PATCH-FIX-UPSTREAM pkexec.patch schwab@suse.de -- pkexec: allow --version and --help even if not setuid
Patch2:         pkexec.patch
# PATCH-FIX-OPENSUSE polkit-keyinit.patch meissner@ -- bsc#1144053 Please add "pam_keyinit.so" to the /etc/pam.d/polkit-1 configuration file
Patch3:         polkit-keyinit.patch
# adjust path to polkit-agent-helper-1 (bsc#1180474)
Patch4:         polkit-adjust-libexec-path.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libexpat-devel
# needed for patch1 and 2
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.2
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mozjs-78)
BuildRequires:  pkgconfig(systemd)
# gtk-doc drags indirectyly ruby in for one of the helpers. This in turn causes a build cycle.
#!BuildIgnore:  ruby
Requires:       dbus-1
Requires:       libpolkit-agent-1-0 = %{version}-%{release}
Requires:       libpolkit-gobject-1-0 = %{version}-%{release}
Requires(post): permissions
%sysusers_requires
%systemd_ordering
# Upstream First - Policy:
# Never add any patches to this package without the upstream commit id
# in the patch. Any patches added here without a very good reason to make
# an exception will be silently removed with the next version update.

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

%package doc
Summary:        Development documentation for PolicyKit
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

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
%autosetup -p1

%build
# Needed for patch1 and patch2
autoreconf -fi
export SUID_CFLAGS="-fPIE"
export SUID_LDFLAGS="-z now -pie"
%configure \
	--with-os-type=suse \
	--enable-gtk-doc \
	--disable-static \
	--enable-introspection \
	--enable-examples \
	--enable-libsystemd-login \
	%{nil}
%make_build libprivdir=%{_libexecdir}/polkit-1
%sysusers_generate_pre %{SOURCE3} polkit system-user-polkitd.conf

%install
# install explicitly into libexec. upstream has some unflexible logic for
# this executable at the moment, but there is a PR# open to fix this:
#     https://gitlab.freedesktop.org/polkit/polkit/-/merge_requests/63
# once this has been resolved upstream and we update to a new release we can
# remove this and also patch4 above.
%make_install libprivdir=%{_libexecdir}/polkit-1
find %{buildroot} -type f -name "*.la" -delete -print
# create $HOME for polkit user
install -d %{buildroot}%{_localstatedir}/lib/polkit
%find_lang polkit-1
mkdir -p %{buildroot}%{_distconfdir}/pam.d
mv %{buildroot}%{_sysconfdir}/pam.d/* %{buildroot}%{_distconfdir}/pam.d/
mv %{buildroot}%{_sysconfdir}/polkit-1/rules.d/50-default.rules %{buildroot}%{_datadir}/polkit-1/rules.d/50-default.rules
mkdir -p %{buildroot}%{_sysusersdir}
install -m0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/

%pre -f polkit.pre
%service_add_pre polkit.service

%preun
%service_del_preun polkit.service

%postun
%service_del_postun polkit.service

%post
%set_permissions %{_bindir}/pkexec
%set_permissions %{_libexecdir}/polkit-1/polkit-agent-helper-1
%service_add_post polkit.service

%verifyscript
%verify_permissions -e %{_bindir}/pkexec
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
%license COPYING

%{_mandir}/man1/pkexec.1%{?ext_man}
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
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.policy
%attr(0700,polkitd,root) %dir %{_datadir}/polkit-1/rules.d
%attr(0700,polkitd,root) %{_datadir}/polkit-1/rules.d/50-default.rules
%{_distconfdir}/pam.d/polkit-1
%dir %{_sysconfdir}/polkit-1
%attr(0700,polkitd,root) %dir %{_sysconfdir}/polkit-1/rules.d
%{_bindir}/pkaction
%{_bindir}/pkcheck
%verify(not mode) %attr(4755,root,root) %{_bindir}/pkexec
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

%files doc
%doc NEWS
%doc %{_datadir}/gtk-doc/html/polkit-1/

%changelog
