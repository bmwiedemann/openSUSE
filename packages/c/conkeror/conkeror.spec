#
# spec file for package conkeror
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define commit fe92781

Name:           conkeror
Version:        1.0.4
Release:        0
Summary:        Keyboard-oriented customizable and extensible web browser
License:        MPL-1.1 or GPL-2.0 or LGPL-2.1
Group:          Productivity/Networking/Web/Browsers
Url:            http://conkeror.org
Source0:        http://repo.or.cz/conkeror.git/snapshot/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.svg
# PATCH-FEATURE-OPENSUSE
Patch0:         ctrl-click.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

Requires:       firefox

%description
Conkeror is a keyboard-oriented, highly-customizable,
highly-extensible web browser based on Mozilla XULRunner, written
mainly in JavaScript, and inspired by exceptional software such as
Emacs and vi. Conkeror features a sophisticated keyboard system,
allowing users to run commands and interact with content in powerful
and novel ways. It is self-documenting, featuring a powerful
interactive help system.

%prep
%setup -q -n %{name}-%{version}-%{commit}
%patch0 -p1

%build
make

%install
make install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"

# install icon ...
install -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# ... and fix desktop file accordingly
sed -i 's@Icon=browser@Icon=conkeror@' %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?suse_version}
%suse_update_desktop_file conkeror
%endif

# fix the destdir in run script
sed -i 's@/usr/local@/usr@g' %{buildroot}%{_bindir}/%{name}

# these files are copied manually to different place
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}
%doc CREDITS COPYING contrib/config/common.js

%changelog
