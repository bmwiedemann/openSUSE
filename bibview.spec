#
# spec file for package bibview
#
# Copyright (c) 2023 SUSE LLC
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


Name:           bibview
BuildRequires:  imake
BuildRequires:  xaw3d-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
Provides:       bibvw15
Version:        2.2
Release:        0
Summary:        X11 Front-End for BibTeX Databases
License:        SUSE-Permissive
Group:          Productivity/Publishing/TeX/Utilities
Source:         bibview-2.2.tar.gz
Patch0:         bibview-2.2.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults

%description
Using bibview, entries in several BiB databases can be moved,
manipulated, created, and searched.

%prep
%autosetup -p0

%build
    xmkmf -a
    make XAWLIB=-lXaw3d %{?_smp_mflags}

%install
    make DESTDIR=%{buildroot} install
    make DESTDIR=%{buildroot} install.man
    mkdir -p %{buildroot}%{_x11data}/de/app-defaults
    install -c -m 0444 BibView.ger.ad   %{buildroot}%{_x11data}/de/app-defaults/BibView
    install -c -m 0444 BibView-color.ad %{buildroot}%{_x11data}/de/app-defaults/BibView-color

%files
%defattr(-,root,root,755)
%{_bindir}/bibview
%dir %{_x11data}/de/
%dir %{_x11data}/de/app-defaults/
%dir %{_appdefdir}
%config %{_appdefdir}/BibView
%config %{_appdefdir}/BibView-color
%config %{_x11data}/de/app-defaults/BibView
%config %{_x11data}/de/app-defaults/BibView-color
%doc %{_mandir}/man1/bibview.1x.gz

%changelog
