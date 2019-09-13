#
# spec file for package gtk-key-theme-ctrluftw
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# icecream 0


Name:           gtk-key-theme-ctrluftw
Summary:        GTK key theme that sets ctrl-u in text entries
Version:        1
Release:        0
License:        GPL-2.0+
Group:          System/Libraries
Source:         gtk-key-theme-ctrluftw.tar.bz2
BuildArch:      noarch

%description
A GTK key theme that makes ctrl-u, ctrl-w and ctrl-h work in text
entries and text views. In contrast to the Emacs key theme which
redefines many other common key bindings (like ctrl-p) this is
one is reduced to the bare minimum to make text entries usable.

%prep

%build

%install
mkdir -p %{buildroot}
tar -C %{buildroot} -xjf %SOURCE0

%files
%defattr(-, root, root)
/usr/share/themes/ctrluftw
/usr/bin/*

%changelog
