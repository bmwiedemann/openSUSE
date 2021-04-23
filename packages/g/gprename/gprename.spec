#
# spec file for package gprename
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define upstr_ver 20140325

Name:           gprename
Version:        5.0.%{upstr_ver}
Release:        0
Summary:        A GTK2 batch renamer for files and directories
License:        GPL-3.0+
Group:          Productivity/File utilities
Url:            http://gprename.sourceforge.net/

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
Requires:       perl-Gtk2
Requires:       perl-gettext
Recommends:     %{name}-lang
Recommends:     nautilus-actions
BuildArch:      noarch
# SLE 11 requires it to build:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GPRename is a complete GTK2/perl batch renamer for files and directories.

%lang_package

%prep
%setup -q -n %{name}-%{upstr_ver}
%patch1

%build

%install
make \
     PREFIX=%{_prefix} \
     DESTDIR=%{buildroot}%{_prefix} \
     install
%suse_update_desktop_file -r %{name} 'Utility;System;FileManager;'
%find_lang %{name}

%post
%if 0%{?suse_version} >= 1140
%desktop_database_post
%else
update-desktop-database &> /dev/null || :
%endif

%postun
%if 0%{?suse_version} >= 1140
%desktop_database_postun
%else
update-desktop-database &> /dev/null || :
%endif

%files
%defattr(-,root,root)
# SLE complains: "directories are not even executable by their owner."
%if 0%{?suse_version} >= 1140
%attr(644,root,root) %doc *.TXT
%endif
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*
%doc %{_mandir}/man*/%{name}*
%{_datadir}/pixmaps/%{name}*

%files lang -f %{name}.lang

%changelog
