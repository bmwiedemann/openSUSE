#
# spec file for package cvs2svn
#
# Copyright (c) 2019 SUSE LLC
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


Name:           cvs2svn
Version:        2.4.0
Release:        0
Summary:        Converts CVS repositories to Subversion repositories
License:        Apache-2.0
Group:          Development/Tools/Version Control
URL:            http://cvs2svn.tigris.org/
Source0:        http://cvs2svn.tigris.org/files/documents/1462/49237/%{name}-%{version}.tar.gz
Source1:        http://cvs2svn.tigris.org/files/documents/1462/49238/%{name}-%{version}.tar.gz.asc
# http://www-heller.harvard.edu/people/mhagger/pgp.html
Source2:        cvs2svn.keyring
Source99:       cvs2svn-rpmlintrc
Patch0:         cvs2svn.install-prefix.patch
BuildRequires:  fdupes
BuildRequires:  python-devel >= 2.4
Requires:       rcs
Requires:       subversion
BuildArch:      noarch

%description
Converts CVS repositories to Subversion repositories.

See %{_docdir}/cvs2svn directory for more information.

%prep
%autosetup

%build
%python2_build

%install
%python2_install
%fdupes %{buildroot}%{python_sitelib}

%files
%license COPYING
%doc {BUGS,COMMITTERS,README,www/{faq,features,cvs2*}.html}
%doc *-example.options
%{_bindir}/cvs2svn
%{_bindir}/cvs2bzr
%{_bindir}/cvs2git
%dir %{python_sitelib}/cvs2svn_rcsparse
%{python_sitelib}/cvs2svn*

%changelog
