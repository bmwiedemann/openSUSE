#
# spec file for package gprename
#
# Copyright (c) 2022 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define upstr_ver 20220807

Name:           gprename
Version:        5.0.%{upstr_ver}
Release:        0
Summary:        A GTK3 batch renamer for files and directories
License:        GPL-3.0+
Group:          Productivity/File utilities
Url:            https://gprename.sourceforge.net

Source0:        http://kent.dl.sourceforge.net/project/gprename/gprename/%{upstr_ver}/gprename-%{upstr_ver}.tar.bz2
# PATCH-FIX-OPENSUSE to prevent
# 1) "The databases in [/usr/share/applications]
# could not be updated";
# 2) "install: cannot create regular file
# '/usr/share/icons/gprename.png': Permission denied";
# 3) "ERROR: Icon file not installed: /home/abuild/
# /rpmbuild/BUILDROOT/gprename-5.0.20140325-0.x86_64/usr/
# /share/applications//gprename..desktop (gprename)";
# 4) "Failed to open file '/usr/share/icons/gprename.png':
# No such file or directory at /usr/bin/gprename line 131."
Patch1:         desktop_icon.patch

BuildRequires:  desktop-file-utils
BuildRequires:  update-desktop-files
Requires:       perl-Gtk3
Requires:       perl-gettext
Requires:       perl-libintl-perl
Requires:       perl-Pango
Recommends:     %{name}-lang
BuildArch:      noarch

%description
GPRename is a complete GTK3/perl batch renamer for files and directories.

%lang_package

%prep
%setup -q -n %{name}-%{upstr_ver}
%patch1
chmod -x *.TXT

%build

%install
make \
     PREFIX=%{_prefix} \
     DESTDIR=%{buildroot}%{_prefix} \
     install
%suse_update_desktop_file -r %{name} 'Utility;System;FileManager;'
%find_lang %{name}

%files
%license COPYING.TXT
%doc README.TXT
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*
%doc %{_mandir}/man*/%{name}*
%{_datadir}/pixmaps/%{name}*

%files lang -f %{name}.lang

%changelog
