#
# spec file for package gimp-plugin-resynthesizer
#
# Copyright (c) 2020 SUSE LLC
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

Name:           gimp-plugin-resynthesizer
Version:        2.0.3.20190428
Release:        0
License:        GPL-3.0+
Summary:        Suite of gimp plugins for texture synthesis
Url:            https://github.com/bootchk/resynthesizer
Group:          Productivity/Graphics/Bitmap Editors
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gimp
BuildRequires:  gimp-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0)
Requires:       gimp-plugins-python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package is a set of plugins for use with the Gimp program.
The package includes:

- resynthesizer plugin engine (without a GUI)
- resynthesizer-gui plugin control panel for the engine
- various plugins (in Python language) that call the resynthesizer engine

%prep
%autosetup

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang resynthesizer

%clean
rm -rf %{buildroot}

%files -f resynthesizer.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/gimp/2.0/plug-ins/*
%{_datadir}/resynthesizer/

%changelog
