#
# spec file for package man-pages-zh_CN
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


Name:           man-pages-zh_CN
Version:        1.5.2.1
Release:        0
Summary:        Simplified Chinese Linux man pages
License:        GFDL-1.3+
Group:          System/I18n/Chinese
Url:            https://github.com/marguerite/man-pages-zh_CN
Source:         https://github.com/marguerite/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  libtool
BuildRequires:  xz
Provides:       locale(man:zh)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Modern Linux man pages localization project for Chinese language.

It's based on manpages-zh project, a successor for CMPP linux man 
pages translation project (discontinued), and Linux CN linux man 
pages translation project, with some new addons from openSUSE
maintainers.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-zhtw

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# remove man pages packaged somewhere else
for man in apropos.1 man.1 whatis.1; do
  rm %{buildroot}%{_mandir}/zh_CN/man1/$man
done

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog AUTHORS
%{_mandir}/zh_CN

%changelog
