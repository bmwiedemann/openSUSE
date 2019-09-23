#
# spec file for package submin
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Andreas Stieger <andreas.stieger@gmx.de>
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


%define tarversion 2.2.1-1
Name:           submin
Version:        2.2.1.1
Release:        0
Summary:        Web Adminstration Interface to Subversion and git
License:        MIT and GPL-2.0 and Apache-2.0 and BSD-3-Clause and Beerware
Group:          Development/Tools/Version Control
Url:            https://supermind.nl/submin/
Source:         https://supermind.nl/submin/current/%{name}-%{tarversion}.tar.gz
# upstream source is at https://ssl.supermind.nl/collab/svn/submin/submin/trunk
BuildRequires:  python-devel
Requires:       %{name}-backend
Requires:       %{name}-webui
Requires:       http_daemon
Requires:       smtp_daemon
Recommends:     %{name}-apache
Recommends:     %{name}-svn
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{?suse_version} >= 1310
BuildArch:      noarch
%endif

%description
Submin provides a Web-based admin interface to Subversion and git
repositories.

Features:
 * Create SVN/Git repositories
 * Add users/groups
 * Control read/write access to repositories
 * Easily upload SSH-key(s) for Git access
 * Config file generation for Apache/Nginx
 * Web-based configuration diagnostics
 * Enable repository commit/push notifications
 * Enable trac commit/push ticket sync
 * Enable/disable commit/push email notifications
 * Change password/email address
 * Forgot password? Reset via e-mail
 * Automatic database upgrades
 * See repository URL

Run the configuration assistant with the first username:
submin2-admin /var/lib/submin initenv user@example.com

%package apache
Summary:        Dependencies when using Submin with Apache httpd
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
Requires:       apache2-mod_wsgi
Requires:       libapr-util1-dbd-sqlite3
Provides:       %{name}-webui

%description apache
This package collects some dependencies for using Submin with Apache httpd and does not contain any files.

%package nginx
Summary:        Dependencies when using Submin with nginx
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
Requires:       nginx
Provides:       %{name}-webui

%description nginx
This package collects some dependencies for using Submin with nginx and does not contain any files.

%package svn
Summary:        Dependencies when using Submin with Apache Subversion
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
Requires:       %{name}-apache = %{version}
Requires:       subversion-python
Requires:       subversion-server
Provides:       %{name}-backend

%description svn
This package collects some dependencies for using Submin with Apache Subversion and does not contain any files.

%package git
Summary:        Dependencies when using Submin with git
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
Requires:       %{name}-webui
Requires:       git
Provides:       %{name}-backend

%description git
This package collects some dependencies for using Submin with git and does not contain any files.

%prep
%setup -q -n %{name}-%{tarversion}

%build
python setup.py build --verbose

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
%if %{?suse_version} >= 1310
python setup.py check
%endif

%files
%defattr(-,root,root)
%doc LICENSE CHANGES CONFIGURATION IMPORTING REMOVING UPGRADING
%doc copying/*
%{python_sitelib}/*
%{_bindir}/submin2-admin
%{_bindir}/submin2-quickstart
%{_mandir}/man1/submin2-admin.1*

%files apache
%defattr(-,root,root)
%dir %{_docdir}/%{name}

%files svn
%defattr(-,root,root)
%dir %{_docdir}/%{name}

%changelog
