#
# spec file for package 
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:       ibus-chewing
Version:    1.3.9.2
Release:    1
Summary:    The Chewing engine for IBus input platform
License:    GPLv2+
Group:      System/I18n/Chinese
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  ibus-devel >= 1.2
BuildRequires:  cmake
BuildRequires:  gob2
BuildRequires:  libchewing-devel >= 0.3.2
BuildRequires:  pkg-config
BuildRequires:  gconf2-devel
BuildRequires:  gcc-c++
BuildRequires:  xorg-x11-devel
Requires:   ibus >= 1.2
Requires:  libchewing >= 0.3.2
Requires:  gconf2

%gconf_schemas_prereq 

%description
The Chewing engine for IBus platform. It provides Chinese input method from
libchewing.
新酷音輸入法

%prep
%setup -q -n %{name}-%{version}-Source

%build
cmake -DCMAKE_INSTALL_PREFIX='/usr' \
      -DLIBEXEC_DIR='%{_libdir}/ibus' \
      -DSYSCONF_INSTALL_DIR='/etc'
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/gconf/schemas
make install \
DESTDIR=$RPM_BUILD_ROOT
rm -r $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
%find_lang %{name}

%find_gconf_schemas   
cat %{name}.schemas_list %{name}.lang >%{name}.lst 

%pre -f %{name}.schemas_pre

%post

%preun -f %{name}.schemas_preun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lst
%defattr(-,root,root,-)
%doc AUTHORS README ChangeLog COPYING
%{_libdir}/ibus
%{_datadir}/%{name}
%{_datadir}/ibus

%changelog
* Sat Oct 10 2009 Jing <jingfu.lai at gmail.com> 
- Version 1.2.0.20091002 for opensuse

* Tue Mar 10 2009 swyear <swyear at gmail com> 
- First Release for opensuse

* Mon Mar 02 2009 Ding-Yi Chen <dchen at redhat.com> -1.0.2.20090302
- Required gconf2 -> GConf2.
- Fix RPM install issues.

* Fri Feb 27 2009 Ding-Yi Chen <dchen at redhat.com> - 1.0.1.20090227-1
- Setting shows/hides KBType, selKeys, and various settings.
- Add gconf schema.
- Fix some memory leaking checked.
- Move some function to cmake_modules.
- Fix Google code issue 281

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1.20081023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ding-Yi Chen <dchen at redhat.com> - 1.0.0.20090220-1
- First working version for IBus C

* Wed Jan 28 2009 Ding-Yi Chen <dchen at redhat.com> - 1.0.0.20090128-1
- Fix the binding with libchewing 0.3.2.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20081023-2
- Rebuild for Python 2.6

* Thu Oct 23 2008 Huang Peng <shawn.p.huang@gmail.com> - 0.1.1.20080923-1
- Update to 0.1.1.20080923.

* Wed Sep 17 2008 Huang Peng <shawn.p.huang@gmail.com> - 0.1.1.20080917-1
- Update to 0.1.1.20080917.

* Tue Sep 16 2008 Huang Peng <shawn.p.huang@gmail.com> - 0.1.1.20080916-1
- Update to 0.1.1.20080916.

* Mon Sep 09 2008 Huang Peng <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update to 0.1.1.20080901.

* Fri Aug 15 2008 Huang Peng <shawn.p.huang@gmail.com> - 0.1.1.20081023-1
- The first version.
