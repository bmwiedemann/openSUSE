#
# spec file for package apache2-icons-oxygen
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           apache2-icons-oxygen
Version:        1.0.1  
Release:        0
Summary:        Oxygen icons for Apache 2 
License:        LGPL-3.0
Group:          Productivity/Networking/Web/Servers
Url:            https://github.com/javierllorente/apache2-icons-oxygen
Source:         %{name}-%{version}.tar.gz  
BuildArch:      noarch 
BuildRequires:  apache2-devel
Requires:       apache2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         apache_sysconfdir %(/usr/sbin/apxs2 -q SYSCONFDIR)

%description  
KDE/Oxygen icons for Apache 2.

%prep  
%setup -q -n %name

%build  

%install  
mkdir -p $RPM_BUILD_ROOT%{_datadir}/apache2/oxygen-icons  
install -m 0644 *.png $RPM_BUILD_ROOT%{_datadir}/apache2/oxygen-icons  
install -m 0644 *.gif $RPM_BUILD_ROOT%{_datadir}/apache2/oxygen-icons  
install -m 0644 *.ico $RPM_BUILD_ROOT%{_datadir}/apache2/oxygen-icons  
mkdir -p $RPM_BUILD_ROOT%{apache_sysconfdir}
cp mod_autoindex-defaults-oxygen.conf $RPM_BUILD_ROOT%{apache_sysconfdir}  

%files  
%defattr(-,root,root)  
%doc README.openSUSE COPYING
%dir %{apache_sysconfdir}
%config(noreplace) %{apache_sysconfdir}/mod_autoindex-defaults-oxygen.conf
%{_datadir}/apache2 
%dir %{_datadir}/apache2/oxygen-icons  

%changelog
