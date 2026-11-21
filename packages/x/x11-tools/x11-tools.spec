#
# spec file for package x11-tools
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


Name:           x11-tools
Version:        0.1
Release:        0
Summary:        Tools for the X Window System
License:        GPL-2.0-or-later AND MIT
Source2:        xf86debug
Source31:       xim
Source32:       xim.template
Source33:       none
Source34:       sysconfig.language-%{name}
Source35:       nvidia-pre-install
Source36:       nvidia-post-uninstall
Source37:       i18n.template
Requires(post): %fillup_prereq
BuildArch:      noarch

%description
Some useful tools for the X Window System.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 755 %{_sourcedir}/xf86debug      %{buildroot}%{_bindir}
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}%{_prefix}/etc/skel
install -m 644 %{_sourcedir}/xim.template %{buildroot}%{_prefix}/etc/skel/.xim.template
install -m 644 %{SOURCE37} %{buildroot}%{_prefix}/etc/skel/.i18n
mkdir -p %{buildroot}/%{_distconfdir}/X11/xim.d
install -m 644 %{_sourcedir}/xim  %{buildroot}/%{_distconfdir}/X11
install -m 644 %{_sourcedir}/none %{buildroot}/%{_distconfdir}/X11/xim.d
%else
mkdir -p %{buildroot}%{_sysconfdir}/skel
install -m 644 %{_sourcedir}/xim.template %{buildroot}%{_sysconfdir}/skel/.xim.template
install -m 644 %{SOURCE37} %{buildroot}%{_sysconfdir}/skel/.i18n
mkdir -p %{buildroot}%{_sysconfdir}/X11/xim.d
install -m 644 %{_sourcedir}/xim  %{buildroot}%{_sysconfdir}/X11
install -m 644 %{_sourcedir}/none %{buildroot}%{_sysconfdir}/X11/xim.d
%endif
mkdir -p  %{buildroot}/%{_fillupdir}/
install -c -m 644 %{_sourcedir}/sysconfig.language-%{name} %{buildroot}/%{_fillupdir}/
mkdir -p %{buildroot}%{_prefix}/lib/nvidia
install -m 755 %{_sourcedir}/nvidia-pre-install \
  %{buildroot}%{_prefix}/lib/nvidia/pre-install
install -m 755 %{_sourcedir}/nvidia-post-uninstall \
  %{buildroot}%{_prefix}/lib/nvidia/post-uninstall

%post
%{fillup_only -an language}

%files
%dir %{_prefix}/lib/nvidia
%{_bindir}/xf86debug
%{_prefix}/lib/nvidia/pre-install
%{_prefix}/lib/nvidia/post-uninstall
%if 0%{?suse_version} >= 1550
%dir %{_prefix}/etc/skel
%{_prefix}/etc/skel/.i18n
%{_prefix}/etc/skel/.xim.template
%{_distconfdir}/X11
%{_distconfdir}/X11/xim
%dir %{_distconfdir}/X11/xim.d
%{_distconfdir}/X11/xim.d/*
%else
%{_sysconfdir}/skel/.i18n
%{_sysconfdir}/skel/.xim.template
%{_sysconfdir}/X11/xim
%dir %{_sysconfdir}/X11/xim.d
%{_sysconfdir}/X11/xim.d/*
%endif
%{_fillupdir}/sysconfig.language-%{name}

%changelog
