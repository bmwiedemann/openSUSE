#
# spec file for package x11-tools
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           x11-tools
Requires(post): %fillup_prereq
Provides:       3ddiag
Provides:       xf86tools
Obsoletes:      3ddiag
Obsoletes:      xf86tools
Version:        0.1
Release:        0
Summary:        Tools for the X Window System
License:        GPL-2.0-or-later AND MIT
Group:          System/X11/Utilities
Source2:        xf86debug
Source31:       xim
Source32:       xim.template
Source33:       none
Source34:       sysconfig.language-%{name}
Source35:       nvidia-pre-install
Source36:       nvidia-post-uninstall
Source37:       i18n.template
BuildArch:      noarch

%description
Some useful tools for the X Window System.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 %{_sourcedir}/xf86debug      %{buildroot}/usr/bin
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}/usr/etc/skel
install -m 644 %{_sourcedir}/xim.template %{buildroot}/usr/etc/skel/.xim.template
install -m 644 %{S:37} %{buildroot}/usr/etc/skel/.i18n
mkdir -p %{buildroot}/%{_distconfdir}/X11/xim.d
install -m 644 %{_sourcedir}/xim  %{buildroot}/%{_distconfdir}/X11
install -m 644 %{_sourcedir}/none %{buildroot}/%{_distconfdir}/X11/xim.d
%else
mkdir -p %{buildroot}/etc/skel
install -m 644 %{_sourcedir}/xim.template %{buildroot}/etc/skel/.xim.template
install -m 644 %{S:37} %{buildroot}/etc/skel/.i18n
mkdir -p %{buildroot}/etc/X11/xim.d
install -m 644 %{_sourcedir}/xim  %{buildroot}/etc/X11
install -m 644 %{_sourcedir}/none %{buildroot}/etc/X11/xim.d
%endif
mkdir -p  %{buildroot}/%{_fillupdir}/
install -c -m 644 %{_sourcedir}/sysconfig.language-%{name} %{buildroot}/%{_fillupdir}/
mkdir -p %{buildroot}/usr/lib/nvidia
install -m 755 %{_sourcedir}/nvidia-pre-install \
  %{buildroot}/usr/lib/nvidia/pre-install
install -m 755 %{_sourcedir}/nvidia-post-uninstall \
  %{buildroot}/usr/lib/nvidia/post-uninstall

%post
%{fillup_only -an language}

%files
%dir /usr/lib/nvidia
/usr/bin/xf86debug
/usr/lib/nvidia/pre-install
/usr/lib/nvidia/post-uninstall
%if 0%{?suse_version} >= 1550
%dir /usr/etc/skel
/usr/etc/skel/.i18n
/usr/etc/skel/.xim.template
%{_distconfdir}/X11
%{_distconfdir}/X11/xim
%dir %{_distconfdir}/X11/xim.d
%{_distconfdir}/X11/xim.d/*
%else
/etc/skel/.i18n
/etc/skel/.xim.template
/etc/X11/xim
%dir /etc/X11/xim.d
/etc/X11/xim.d/*
%endif
%{_fillupdir}/sysconfig.language-%{name}

%changelog
