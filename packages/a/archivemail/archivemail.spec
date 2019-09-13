#
# spec file for package archivemail
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           archivemail
Version:        0.9.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://archivemail.sf.net/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Summary:        Tool for Archiving and Compressing Old Email in Mailboxes
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Utilities
BuildRequires:  ed
BuildRequires:  python-devel
%{py_requires}
%if %{?suse_version: %{suse_version} > 1110} %{!?suse_version:1}
BuildArch:      noarch
%endif

%description
archivemail is a tool for archiving and compressing old email in mailboxes. It
moves messages older than the specified number of days to a separate mbox
format mailbox that is compressed with gzip. It can also just delete old email
rather than archive it.

%prep
%setup -q
ed -s examples/archivemail_all 2>/dev/null <<'EOF'
,s/\/usr\/local\/bin\/archivemail/\/usr\/bin\/archivemail/
w
EOF

%build
%{__python} setup.py build

%install
# python => 2.5 expects this to exist (it will exist if the package
# installs something there, but we don't)
mkdir -p $RPM_BUILD_ROOT/%{python_sitelib}
%{__python} setup.py install --prefix=%{_prefix} --root %{buildroot}
# we don't need the egg file which python => 2.5 installs
rm -f $RPM_BUILD_ROOT/%{python_sitelib}/*

%files
%defattr(-,root,root)
%{_bindir}/archivemail
%doc %{_mandir}/man1/archivemail.1*
%doc CHANGELOG examples/* FAQ README TODO

%changelog
