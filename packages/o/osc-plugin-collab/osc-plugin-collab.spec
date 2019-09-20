#
# spec file for package osc-plugin-collab
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 Vincent Untz <vuntz@opensuse.org>
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


Name:           osc-plugin-collab
Version:        0.102
Release:        0
Summary:        Plugin to make collaboration easier with osc
License:        BSD-3-Clause
Group:          Development/Tools/Other
Url:            http://en.opensuse.org/openSUSE:Osc_Collab
Source0:        osc-collab.py
# Needed for directory ownership
BuildRequires:  osc
Requires:       osc >= 0.140.1
%if !(0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?scientificlinux_version})
Recommends:     quilt
Recommends:     rpm-python
Recommends:     xz
%else
Requires:       quilt
Requires:       rpm-python
Requires:       xz
%endif
# osc gnome was part of osc-plugins-gnome
Conflicts:      osc-plugins-gnome <= 0.4.26
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if %(if test -d %{_prefix}/lib/osc-plugins; then echo 1; else echo 0; fi)
%define oscplugindir %{_prefix}/lib/osc-plugins
%else
%define oscplugindir %{_localstatedir}/lib/osc-plugins
%endif

%description
This osc plugin extends osc with commands that makes it easier to use
the collaboration feature in the Build Service, and to keep up with
latest upstream versions.

%prep

%build

%install
install -D -m0644 %{S:0} %{buildroot}%{oscplugindir}/osc-collab.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{oscplugindir}/osc-collab.py
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
%{oscplugindir}/osc-collab.pyc
%{oscplugindir}/osc-collab.pyo
%endif

%changelog
