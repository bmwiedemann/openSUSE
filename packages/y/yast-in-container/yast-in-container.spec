#
# spec file for package yast-in-container
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yast-in-container
Version:        4.5.10
Release:        0
Summary:        Experimental package for running YaST in a container
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-in-container
# the container images are only built for x86_64
ExclusiveArch:  x86_64
Source0:        %{name}-%{version}.tar.bz2

# recommend Podman for running the containers, optionally Docker might be used
Recommends:     podman

%description
This package contains scripts which can run YaST in a container for managing
the host system.

* WARNING: This an experimental package, do not use in a production system!
* There is a high risk of breaking the system or data loss!

%prep

%setup -q

%build

%install

# install main scripts
mkdir -p %{buildroot}/%{_sbindir}
install -m 755 src/scripts/yast2_container %{buildroot}/%{_sbindir}
ln -s yast2_container %{buildroot}/%{_sbindir}/yast_container
ln -s yast2_container %{buildroot}/%{_sbindir}/yast2_web_container

# install desktop file
mkdir -p %{buildroot}/%{_datadir}/applications
install -m 644 desktop/org.opensuse.YaST-in-container.desktop %{buildroot}/%{_datadir}/applications

# install icons
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
install -m 644 src/icons/hicolor/scalable/apps/* %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps

# install license and documentation
mkdir -p %{buildroot}/%{_docdir}/%{name}
install -m 644 COPYING %{buildroot}/%{_docdir}/%{name}
install -m 644 README.md %{buildroot}/%{_docdir}/%{name}

# /sbin compatibility symlinks
%if !0%{?usrmerged}
mkdir -p %{buildroot}/sbin
ln -s ../%{_sbindir}/yast_container  %{buildroot}/sbin
ln -s ../%{_sbindir}/yast2_container %{buildroot}/sbin
ln -s ../%{_sbindir}/yast2_web_container %{buildroot}/sbin
%endif

%files

# the main scripts
%{_sbindir}/yast*_container

# /sbin compatibility symlinks
%if !0%{?usrmerged}
/sbin/yast*_container
%endif

# desktop file
%{_datadir}/applications/*.desktop

# icons
%{_datadir}/icons/hicolor

# license and documentation
%doc %dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/README.md

%changelog
