#
# spec file for package iwidgets
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           iwidgets
BuildRequires:  tcl-devel
Version:        4.1
Release:        0
Source0:        %{name}41.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Summary:        Widget Extension for Tcl/Tk
License:        MIT
Group:          Development/Languages/Tcl
Requires:       itk

%description
[incr Widgets] is an object-oriented mega-widget set that extends
Tcl/Tk and is based on [incr Tcl] and [incr Tk].  This set of
mega-widgets delivers many new, general purpose widgets like option
menus, comboboxes, selection boxes, and various dialogs whose
counterparts are found in Motif and Windows. Since [incr Widgets] is
based on the [incr Tk] extension, the Tk framework of configuration
options, widget commands, and default bindings is maintained.  In other
words, each [incr Widgets] mega-widget seamlessly blends with the
standard Tk widgets. They look, act, and feel like Tk widgets. In
addition, all [incr Widgets] mega-widgets are object oriented and may
themselves be extended, using either inheritance or composition.


%prep
%setup -q -n %name%version

%build

%install
mkdir -p %buildroot%tcl_noarchdir
cp -a library %buildroot%tcl_noarchdir/%name%version

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc license.terms README
%tclscriptdir/%name%version

%changelog
