#
# spec file for package nuoveXT2-icon-theme
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


Name:           nuoveXT2-icon-theme
Version:        0.5.1
Release:        0
Summary:        This package provides the default LXDE icon theme
License:        GPL-3.0
Group:          System/GUI/Other
Url:            http://www.lxde.org
Source0:        lxde-icon-theme-%{version}.tar.xz
Source1:        tango-volume.tar.bz2
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides the default LXDE icon theme.
nuoveXT2-icon-theme is no more maintained from his author so
LXDE project decided to maintain it and keep working on it

%prep
%setup -q -n lxde-icon-theme-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
tar -xjvf %{SOURCE1} -C %{buildroot}/%{_datadir}/icons/nuoveXT2/
%fdupes -s %{buildroot}

%files
%defattr(-,root,root,755)
%{_datadir}/icons/nuoveXT2

%changelog
