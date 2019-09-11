#
# spec file for package boo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 2_0_9_3
%define _version_short 0.9.3
# gtksourceview is required so that we can put the sourceview lang definitions
# in the right location
# On older versions of suse, this was defined as /opt/gnome... make it cross distro
%define gtksourceview_prefix %(pkg-config --variable=prefix gtksourceview-2.0)
%define mime_info_prefix %(pkg-config --variable=prefix shared-mime-info)
Name:           boo
Version:        0.9.3.3457
Release:        0
Summary:        A CLI Scripting Language
License:        MIT
Group:          Development/Languages/Other
Url:            http://boo-lang.org/
Source0:        boo-%{version}.tar.bz2
Patch1:         boo-pkgconfig_path_fix.patch
BuildRequires:  mono-devel
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(gtksourceview-2.0)
Requires:       %{name}-%{_version} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Boo is a new object oriented statically typed programming language for
the Common Language Infrastructure with a python inspired syntax and a
special focus on language and compiler extensibility.

%package devel
Summary:        A CLI Scripting Language
Group:          Development/Languages/Other
Requires:       boo = %{version}

%description devel
Boo is a new object-oriented statically-typed programming language for
the common language infrastructure with a Python-inspired syntax and a
special focus on language and compiler extensibility.

%package 2_0_9_3
Summary:        A CLI Scripting Language
Group:          Development/Languages/Other

%description %{_version}
Boo is a new object-oriented statically-typed programming language for
the common language infrastructure with a Python-inspired syntax and a
special focus on language and compiler extensibility.

%prep
%setup -q
%patch1

# Fix gtksourceview version
sed -i "s#gtksourceview-1.0#gtksourceview-2.0#g" configure

%build
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_datadir}/
# boo.lang is provided by gtksourceview
rm -rf %{buildroot}%{_datadir}/gtksourceview-1.0

%files
%defattr(-, root, root)
%{_prefix}/lib/mono/boo

%files %{_version}
%defattr(-, root, root)
%dir %{_prefix}/lib/mono/gac/Boo.Lang*
%{_prefix}/lib/mono/gac/Boo.Lang*/2.%{_version_short}*

%files devel
%defattr(-, root, root)
%{_bindir}/boo*
%{_datadir}/pkgconfig/boo*.pc
%{_prefix}/lib/boo
%{_datadir}/mime/packages/boo-mime-info.xml

%post
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%postun
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%changelog
