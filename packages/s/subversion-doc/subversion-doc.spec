#
# spec file for package subversion-doc
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


#
%define apache_sysconfdir %{_sysconfdir}/apache2
Name:           subversion-doc
Version:        1.8.r5043
Release:        0
#
Summary:        Documentation files for Subversion
License:        CC-BY-2.0
Group:          Development/Tools/Version Control
Url:            http://svnbook.red-bean.com/
Source0:        %{name}-%{version}.tar.bz2
Source1:        subversion.doc.conf
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
# from http://svnbook.red-bean.com/en/1.7/svn.copyright.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version} > 1210
BuildRequires:  libxml2-tools
%endif

%description
This package contains the subversion book (see
http://svnbook.red-bean.com/) and a configuration file to make this
book accessible via apache2.

%prep
%setup -q
ln -sv %{_datadir}/xml/docbook/stylesheet/nwalsh/current/ tools/xsl

%build
cd en
SVNVERSION=`echo "%{version}" | sed -r "s/[0-9]+\.[0-9]+\.(r[0-9]+)/\1/"`
sed -i "s/&svn\.version;/${SVNVERSION}/g" book/book.xml
make %{?_smp_mflags} html SVNVERSION=/bin/false

%install
cd en
make install-html SVNVERSION=/bin/false INSTALL_DIR=%{buildroot}%{_defaultdocdir}/subversion/html
install -m 644 -D %{SOURCE1} %{buildroot}/%{apache_sysconfdir}/conf.d/subversion.doc.conf
find %{buildroot} -type d -print0 | xargs -0 chmod 755
find %{buildroot} -type f -print0 | xargs -0 chmod 644

%files
%defattr(-,root,root)
#
%dir %{apache_sysconfdir}
%dir %{apache_sysconfdir}/conf.d
%config (noreplace) %{apache_sysconfdir}/conf.d/subversion.doc.conf
%dir %{_defaultdocdir}/subversion
%{_defaultdocdir}/subversion/html

%changelog
