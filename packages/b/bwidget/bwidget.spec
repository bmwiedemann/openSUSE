#
# spec file for package bwidget
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           bwidget
BuildRequires:  dos2unix
BuildRequires:  tcl
Version:        1.9.9
Release:        0
Summary:        A Set of Megawidgets for Tcl/Tk
Url:            http://sourceforge.net/projects/tcllib/
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       tk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://downloads.sourceforge.net/project/tcllib/BWidget/%{version}/%{name}-%{version}.tar.gz

%description
Add useful and nice-looking widgets to your interfaces with the BWidget
Toolkit, a set of native Tk 8.x Widgets using Tcl8.x namespaces. The
BWidgets have a professional look and feel as in other well-known
toolkits (Tix or Incr Widget). However, the concept is radically
different because everything is native. There is no platform
compilation and no compiled extension libraries are needed. The code is
in pure Tcl/Tk.

%prep
%setup -q -n %{name}-%version

find . -name \*.txt -print0 | xargs -0 dos2unix

%build

%install
dir=%buildroot%tcl_noarchdir/%name%version
mkdir -m755 -p $dir
cp -a *.tcl images lang $dir
chmod a+x demo/demo.tcl

%files
%defattr(-,root,root)
%doc demo BWman/* ChangeLog CHANGES.txt LICENSE.txt README.txt
%tcl_noarchdir

%changelog
