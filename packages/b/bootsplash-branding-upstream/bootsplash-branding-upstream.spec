#
# spec file for package bootsplash-branding-upstream
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           bootsplash-branding-upstream
Url:            http://www.bootsplash.org/
Version:        3.3
Release:        0
# Scripts and programs
Source0:        upstream.tar.bz2
Source4:        KDE.tar.bz2
Source5:        LICENSE
# sysconfig files
Source23:       sysconfig.bootsplash-branding-upstream
Source24:       sysconfig.bootsplash-branding-KDE
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       bootsplash >= 3.3-11
BuildArch:      noarch
Supplements:    packageand(bootsplash:branding-upstream)
Provides:       bootsplash-branding
Summary:        Unbranded Bootsplash Theme
License:        BSD-3-Clause
Group:          System/Boot
PreReq:         %fillup_prereq perl
Requires:       bootsplash >= 3.3-11

%description
This package contains a theme without trademarked logos.

%package -n     bootsplash-branding-KDE
Supplements:    packageand(bootsplash:branding-KDE)
Provides:       bootsplash-branding
Summary:        KDE Bootsplash Theme
Group:          System/Boot
PreReq:         %fillup_prereq perl
Requires:       bootsplash >= 3.3-11

%description -n bootsplash-branding-KDE
This package contains a KDE branded theme.

%prep
%setup -q -c
%setup -T -D -a 4
cp -p %{SOURCE5} .

%build

%install
mkdir -p %{buildroot}/etc/bootsplash
cp -a themes %{buildroot}/etc/bootsplash
for i in %{buildroot}/etc/bootsplash/themes/* ; do
  cp -a LICENSE $i/.
done
mkdir -p %{buildroot}%{_fillupdir}
cp %{SOURCE23} %{SOURCE24} %{buildroot}%{_fillupdir}/

%post -n bootsplash-branding-upstream
%{fillup_only -ns bootsplash branding-upstream }
perl -pi -e 's/^(THEME=).*/$1"upstream"/' /etc/sysconfig/bootsplash

%post -n bootsplash-branding-KDE
%{fillup_only -ns bootsplash branding-KDE }
perl -pi -e 's/^(THEME=).*/$1"KDE"/' /etc/sysconfig/bootsplash

%files -n bootsplash-branding-upstream
%defattr(-,root,root)
%dir /etc/bootsplash
%dir /etc/bootsplash/themes
/etc/bootsplash/themes/upstream
%config %{_fillupdir}/sysconfig.bootsplash-branding-upstream

%files -n bootsplash-branding-KDE
%defattr(-,root,root)
%dir /etc/bootsplash
%dir /etc/bootsplash/themes
/etc/bootsplash/themes/KDE
%config %{_fillupdir}/sysconfig.bootsplash-branding-KDE

%changelog
