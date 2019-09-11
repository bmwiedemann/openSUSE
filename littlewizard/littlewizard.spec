#
# spec file for package littlewizard
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           littlewizard
Version:        1.2.2
Release:        0
Summary:        Development Environment for Children
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
Url:            http://littlewizard.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Source1:        littlewizard.1
Patch0:         littlewizard-1.2.2-do-not-override-toolbar-style.patch
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnome-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4
Recommends:     littlewizard-examples
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Little Wizard is created especially for primary school children. It allows to
learn using main elements of present computer languages, including: variables,
expressions, loops, conditions, logical blocks. Every element of language is
represented by an intuitive icon. It allows program Little Wizard without
using keyboard, only mouse.

%package devel
Summary:        Development headers and files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The littlewizard-devel package contains libraries and header files for
littlewizard developing.

%lang_package

%prep
%setup -q
%patch0

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file -r littlewizard Education Teaching

# removing useless files
rm -rf %{buildroot}%{_bindir}/littlewizardtest
rm -rf %{buildroot}%{_prefix}/doc/littlewizard
rm -rf %{buildroot}%{_libdir}/*.*a

# man page
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 %{SOURCE1} %{buildroot}%{_mandir}/man1

%find_lang %{name}

%post
/sbin/ldconfig
%if 0%{?suse_version} > 1130
%desktop_database_post
%endif

%postun
/sbin/ldconfig
%if 0%{?suse_version} > 1130
%desktop_database_postun
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%if 0%{?suse_version} >= 01500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS ChangeLog README TODO
%dir %{_datadir}/icons/gnome/48x48/mimetypes
%{_bindir}/littlewizard
%{_datadir}/littlewizard
%{_datadir}/applications/littlewizard.desktop
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-x-littlewizard.png
%{_datadir}/icons/gnome/scalable/mimetypes/gnome-mime-application-x-littlewizard.svg
%{_datadir}/mime/packages/littlewizard.xml
%{_datadir}/pixmaps/littlewizard
%{_libdir}/liblanguage.so.*
%{_libdir}/liblw.so.*
%{_mandir}/man1/littlewizard.1%{?ext_man}

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/liblanguage.so
%{_libdir}/liblw.so

%changelog
