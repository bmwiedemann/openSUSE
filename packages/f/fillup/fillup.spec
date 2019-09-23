#
# spec file for package fillup
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           fillup
Version:        1.42
Release:        0
Summary:        Tool for Merging Config Files
License:        GPL-2.0+
Group:          System/Base
Url:            http://github.com/openSUSE/fillup
Source:         fillup-%{version}.tar.bz2
Patch0:         fillup-optflags.patch
Patch1:         fillup-warnings.dif
Patch2:         fillup-%{version}.dif
Patch3:         fillup-retval.dif
Patch4:         fillup-nodate.patch
Patch5:         fillup-1.42-cloexec.patch
Provides:       aaa_base:/bin/fillup
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fillup merges files that hold variables.  A variable is defined by an
entity composed of a preceding comment, a variable name, an assignment
delimiter, and a related variable value.  A variable is determined by
its variable name.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2
%patch3
%patch4
%patch5

%build
make %{?_smp_mflags} compile COMPILE_OPTION=OPTIMIZE OPTISPLUS="%{optflags}"

%install
mkdir -p %{buildroot}%{_fillupdir}
install -d -m 755 %{buildroot}/%{_bindir}
install -m 755 BIN/fillup %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man8
install -m 644 SGML/fillup.8.gz %{buildroot}/%{_mandir}/man8

#UsrMerge - There are literally hundreds of rpm scritps referencing /bin/fillup (suse macro)
# So let's at least keep the symlink there for now (DimStar - 2014-10-31)
install -d -m 755 $RPM_BUILD_ROOT/bin
ln -sf %{_bindir}/fillup $RPM_BUILD_ROOT/bin
#EndUserMerge

%check
make %{?_smp_mflags} test    OPTISPLUS="%{optflags}"

%files
%defattr(-,root,root)
# rpm scriptlets still use this, based on %*fillup* macros
/bin/fillup
%{_bindir}/fillup
%{_mandir}/man8/fillup*

%changelog
