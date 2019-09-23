#
# spec file for package scite
#
# Copyright (c) 2016-2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2017 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           scite
Version:        3.7.5
Release:        0
%define tar_ver 375
Summary:        Source Code Editor based on Scintilla
License:        MIT
Group:          Productivity/Text/Editors
Url:            http://www.scintilla.org/SciTE.html
Source0:        http://download.sourceforge.net/scintilla/%{name}%{tar_ver}.tgz
Source1:        %{name}.changes
BuildRequires:  gcc-c++
%if 0%{?favor_gtk2}
BuildRequires:  gtk2-devel
%else
BuildRequires:  gtk3-devel
%endif
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SciTE is a SCIntilla based Text Editor. Originally built to demonstrate
Scintilla, it has grown to be a generally useful editor with facilities for
building and running programs.

%prep
%setup -q -c

# Fix "Your file uses  __DATE and __TIME__ this causes the package to rebuild when not needed warning"
# http://sourceforge.net/tracker/?func=detail&atid=102439&aid=3314371&group_id=2439 is WONTFIX.
# We use the date from the changes file
set_date_time=`date --date "@\`stat --format %Y %{S:1}\`" +"%B %Y %H:%M"`
sed -i 's/wsci, \"    \" \_\_DATE\_\_ \" \" \_\_TIME\_\_ \"\\n"/wsci, \"'"$set_date_time"'\\n\"/g' scite/src/Credits.cxx

%build
export CXXFLAGS='%{optflags}'
export CFLAGS='%{optflags}'

%if 0%{?favor_gtk2}
make %{?_smp_mflags} -C scintilla/gtk
make %{?_smp_mflags} -C scite/gtk
%else
make GTK3=1 %{?_smp_mflags} -C scintilla/gtk
make GTK3=1 %{?_smp_mflags} -C scite/gtk
%endif

%install
%if 0%{?favor_gtk2}
make DESTDIR=%{buildroot} -C scite/gtk install
%else
make GTK3=1 DESTDIR=%{buildroot} -C scite/gtk install
%endif
# Add the man page
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 scite/doc/scite.1 %{buildroot}%{_mandir}/man1/SciTE.1
%suse_update_desktop_file -r SciTE GTK Development Utility Building TextEditor

%if !0%{?sles_version}
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc scite/README scite/License.txt
%{_bindir}/SciTE
%{_datadir}/scite/
%{_datadir}/pixmaps/Sci48M.png
%{_datadir}/applications/SciTE.desktop
%{_mandir}/man1/SciTE.1%{?ext_man}

%changelog
