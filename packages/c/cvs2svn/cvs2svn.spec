#
# spec file for package cvs2svn
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?python_sitelib:  %global python_sitelib  %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?py_ver:          %global pyver %(python -c 'import sys; print sys.version[:3]')}
Name:           cvs2svn
Version:        2.4.0
Release:        0
#
Summary:        Converts CVS repositories to Subversion repositories
License:        Apache-2.0
Group:          Development/Tools/Version Control
Url:            http://cvs2svn.tigris.org/
Source0:        http://cvs2svn.tigris.org/files/documents/1462/49237/%{name}-%{version}.tar.gz
Source1:        http://cvs2svn.tigris.org/files/documents/1462/49238/%{name}-%{version}.tar.gz.asc
# http://www-heller.harvard.edu/people/mhagger/pgp.html
Source2:        cvs2svn.keyring
Source99:       cvs2svn-rpmlintrc
Patch0:         cvs2svn.install-prefix.patch
BuildRequires:  python-devel >= 2.4
Requires:       python < %{py_ver}.99
Requires:       python >= %{py_ver}
Requires:       rcs
Requires:       subversion
#
PreReq:         %insserv_prereq %fillup_prereq
Provides:       subversion-cvs2svn = %{version}
Obsoletes:      subversion-cvs2svn < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif
#

%description
Converts CVS repositories to Subversion repositories.

See %{_docdir}/cvs2svn directory for more information.

%prep
%setup -q
#
%patch0
# replace shebang for python with %__python
perl -ni -e 'if (1..1 && m/^#!(.+python)(\s+.+)?$/) {print "#!%__python".$2."\n";} else {print}' cvs2{svn,bzr,git}

%build

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc {BUGS,COMMITTERS,COPYING,README,www/{faq,features,cvs2*}.html}
%doc *-example.options
%attr(755,root,root) %{_bindir}/cvs2svn
%attr(755,root,root) %{_bindir}/cvs2bzr
%attr(755,root,root) %{_bindir}/cvs2git
%dir %{python_sitelib}/cvs2svn_rcsparse
%{python_sitelib}/cvs2svn*

%changelog
