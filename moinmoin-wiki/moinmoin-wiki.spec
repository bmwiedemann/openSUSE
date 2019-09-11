#
# spec file for package moinmoin-wiki
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


%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif
Name:           moinmoin-wiki
# NB: When bumping the version, also adjust /moin_staticXXX in apache configs
Version:        1.9.10
Release:        0
Summary:        Wiki engine written in Python
License:        GPL-2.0-or-later AND Apache-2.0
Group:          Productivity/Networking/Web/Frontends
Url:            http://moinmo.in/MoinMoinWiki
Source0:        http://static.moinmo.in/files/moin-%{version}.tar.gz
Source1:        moin.wsgi
Source2:        moin-apache22.conf
Source3:        moin-apache24.conf
Source4:        mkwiki.moin
Source5:        http://static.moinmo.in/files/moin-%{version}.tar.gz.asc
Source6:        %{name}.keyring
# NB: the AnyWikiDraw applet is no longer included in openSUSE package
Source80:       Re:_Proprietary_code_in_AnyWikiDraw.mbox
Source90:       README.SUSE
Source91:       moin.1
Source92:       mkwiki.moin.8
Source99:       moinmoin-wiki.rpmlintrc
BuildRequires:  apache2
BuildRequires:  dos2unix
BuildRequires:  fdupes
%if 0%{?sle_version} < 120300
BuildRequires:  python-devel >= 2.5
%else
BuildRequires:  python2-devel >= 2.5
%endif
Requires:       apache2-mod_wsgi
Requires:       python2-xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Obsoletes:      python-moin < 1.9.8-50.0
Provides:       python-moin = %{version}

%description
MoinMoin is an extensible wiki engine. It focuss on collaboration on
editable web pages. All wiki data is stored in plain files - no
database is required. MoinMoin is implemented in Python.

This package configures MoinMoin to serve wiki pages via the Apache web server.

%prep
%setup -q -n moin-%{version}

# Always use python2
grep -rl "#!/usr/bin/env python" . | xargs -L 1 --verbose sed -i -e "s|#!/usr/bin/env python|#!/usr/bin/python2|g"
sed -i -e "s|#!/usr/bin/python|#!/usr/bin/python2|g" wiki/server/moin.fcgi

# remove pre-built applet JARs
find . -type f -name "*.jar" -print -delete

%build
cp %{SOURCE90} .

dos2unix docs/licenses/pygments/LICENSE
dos2unix docs/licenses/werkzeug/LICENSE
find MoinMoin/web/static/htdocs/applets/FCKeditor/editor/filemanager/connectors/py -name "*.py" | xargs dos2unix
dos2unix MoinMoin/web/static/htdocs/applets/FCKeditor/editor/filemanager/connectors/perl/connector.cgi
dos2unix MoinMoin/web/static/htdocs/applets/FCKeditor/editor/filemanager/connectors/perl/upload.cgi

python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}

mkdir -p %{buildroot}%{_sbindir}

install -m 744 %{SOURCE4} %{buildroot}%{_sbindir}

mkdir -p %{buildroot}/srv/moin
cp %{SOURCE1} %{buildroot}/srv/moin

mkdir -p %{buildroot}%{_sysconfdir}/apache2/conf.d
if [ 0%{?suse_version} -le 1310 ]; then
	cp %{SOURCE2} %{buildroot}%{_sysconfdir}/apache2/conf.d/moin.conf
else
	cp %{SOURCE3} %{buildroot}%{_sysconfdir}/apache2/conf.d/moin.conf
fi

%fdupes %{buildroot}/%{python_sitelib}/MoinMoin

mkdir -p %{buildroot}%{_mandir}/man1
gzip -c %{SOURCE91} > %{buildroot}%{_mandir}/man1/moin.1.gz
mkdir -p %{buildroot}%{_mandir}/man8
gzip -c %{SOURCE92} > %{buildroot}%{_mandir}/man8/mkwiki.moin.8.gz

%post
if [ "$1" = 1 ]; then
	echo "Please refer to %{_docdir}/%{name}/README.SUSE for"
	echo "instructions on how to complete the installation of MoinMoin."
fi

%files
%defattr(-, root, root)
%doc README.rst docs/* README.SUSE
%config(noreplace) %{_sysconfdir}/apache2/conf.d/moin.conf
%{_bindir}/moin
%{_sbindir}/mkwiki.moin
%{_datadir}/moin
%{python_sitelib}
%dir /srv/moin
%config(noreplace) /srv/moin/moin.wsgi
%{_mandir}/man1/moin.1.gz
%{_mandir}/man8/mkwiki.moin.8.gz

%changelog
