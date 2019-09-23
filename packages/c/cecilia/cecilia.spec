#
# spec file for package cecilia
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



Name:           cecilia
Summary:        Tcl/Tk Front-End for Csound
Version:        2.0.5
Release:        260
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Editors and Convertors
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://cecilia.sf.net
Source:         %{name}-%{version}.tar.bz2
Patch:          cecilia-path-fix.dif
Patch1:         cecilia-CVE-2008-1832.patch
Requires:       tk sox
Requires:       csound > 3.47
BuildRequires:  fdupes
BuildArch:      noarch

%description
Cecilia is a Tcl/Tk front-end for the Csound sound synthesis program.

%prep
%setup -q
%patch1
# applay the following to install the files under /usr/share
# %patch

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/cecilia
install -c -m 0755 cecilia $RPM_BUILD_ROOT%{_bindir}
install -c -m 0755 cecilia-tcl $RPM_BUILD_ROOT%{_bindir}
cp -r files $RPM_BUILD_ROOT%{_prefix}/lib/cecilia
cp -r lib $RPM_BUILD_ROOT%{_prefix}/lib/cecilia
(cd $RPM_BUILD_ROOT%{_prefix}/lib/cecilia;
 find . -name CVS | xargs rm -rf)
%fdupes -s $RPM_BUILD_ROOT/%_mandir
%fdupes $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING README TODO
%{_bindir}/*
%{_prefix}/lib/*

%changelog
