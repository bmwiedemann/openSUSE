#
# spec file for package linkchecker
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           linkchecker
Version:        9.4.0
Release:        0
Summary:        Tool to check websites and HTML documents for broken links
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://linkchecker.github.io/linkchecker/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-cssutils
BuildRequires:  python-devel
BuildRequires:  python-optcomplete
BuildRequires:  python-setuptools
BuildRequires:  python-xml
BuildRequires:  update-desktop-files
Requires:       python-cssutils
Requires:       python-dnspython
Requires:       python-optcomplete
Requires:       python-pyxdg
Requires:       python-requests
Requires:       tidy
%py_requires

%description
LinkChecker checks websites and HTML documents for broken links.

Features are:
* recursive checking
* multithreaded
* output in colored or normal text, HTML, SQL, CSV, XML or a sitemap graph in different formats
* HTTP/1.1, HTTPS, FTP, mailto:, news:, nntp:, Gopher, Telnet and local file links support
* restriction of link checking with regular expression filters for URLs
* proxy support
* username/password authorization for HTTP and FTP
* robots.txt exclusion protocol support
* i18n support
* a command line interface
* a (Fast)CGI web interface (requires HTTP server)

%prep
%setup -q -n %{name}
cp -a doc/examples .

%build
make -C doc
python setup.py build
chmod -x examples/*.sh

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix} --record-rpm=INSTALLED_FILES.in
# 'brp-compress' compresses the manpages without distutils knowing.
# So append ".gz" suffixes to the affected manpage filenames.
sed -i -e 's@/usr/share/man/man\([[:digit:]]\)/\(.\+\.[[:digit:]]\)$@%doc /usr/share/man/man\1/\2.gz@g' INSTALLED_FILES.in
sed -i -e 's@/usr/share/man/de/man\([[:digit:]]\)/\(.\+\.[[:digit:]]\)$@%doc /usr/share/man/de/man\1/\2.gz@g' INSTALLED_FILES.in
sed -i -e 's@/usr/share/man/fr/man\([[:digit:]]\)/\(.\+\.[[:digit:]]\)$@%doc /usr/share/man/fr/man\1/\2.gz@g' INSTALLED_FILES.in
rm -rf examples
mv %{buildroot}%{_datadir}/%{name}/examples ./
grep -E -v '/usr/share/linkchecker/examples|/usr/share/locale' INSTALLED_FILES.in > INSTALLED_FILES
echo "%{py_sitedir}/_LinkChecker_configdata.pyc" >> INSTALLED_FILES
find %{buildroot}/%{_mandir} -name \*.1 -o -name \*.5 -exec gzip -9 {} +
pushd doc
install -d -m 0755 %{buildroot}%{_datadir}/pixmaps
install -D -m 644 web/media/images/logo128x128.png web/media/images/logo16x16.png web/media/images/logo32x32.png web/media/images/logo48x48.png web/media/images/logo64x64.png %{buildroot}%{_datadir}/pixmaps
popd

%find_lang %name

%files -f INSTALLED_FILES -f %name.lang
%defattr(-,root,root)
%doc examples doc/upgrading.txt doc/changelog.txt
%{_datadir}/pixmaps/logo*.png

%changelog
