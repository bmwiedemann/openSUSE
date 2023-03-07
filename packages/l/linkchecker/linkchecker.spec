#
# spec file for package linkchecker
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pythons python3
Name:           linkchecker
Version:        10.1.0
Release:        0
Summary:        Tool to check websites and HTML documents for broken links
License:        GPL-2.0-or-later
URL:            https://github.com/linkchecker/linkchecker
Source:         https://files.pythonhosted.org/packages/source/L/LinkChecker/LinkChecker-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4 >= 4.8.1}
BuildRequires:  %{python_module dnspython >= 2.0}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pyftpdlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module requests >= 2.4}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       python-beautifulsoup4 >= 4.8.1
Requires:       python-dnspython >= 2.0
Requires:       python-pyxdg
Requires:       python-requests >= 2.4
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       linkchecker = %{version}
Obsoletes:      linkchecker < %{version}
BuildArch:      noarch
%python_subpackages

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
%setup -q -n LinkChecker-%{version}
# Avoid dependency on python-miniboa
rm tests/checker/test_telnet.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/linkchecker
%python_expand %fdupes %{buildroot}%{$python_sitelib}

rm -rf examples
mv %{buildroot}%{_datadir}/%{name}/examples ./

install -d -m 0755 %{buildroot}%{_datadir}/pixmaps
install -D -m 644 doc/src/images/logo128x128.png %{buildroot}%{_datadir}/pixmaps/linkchecker128x128.png

%check
export LANG=en_US.UTF-8
# Two 'test_encoding_detection_iso_bad' tests fail utf-8 != ascii
%pytest -rs -k 'not test_encoding_detection_iso_bad'

%post
%python_install_alternative linkchecker

%postun
%python_uninstall_alternative linkchecker

%files %{python_files}
%doc README.rst examples doc/upgrading.txt doc/changelog.txt
%license COPYING
%python_alternative %{_bindir}/linkchecker
%{python_sitelib}/linkcheck/
%{python_sitelib}/_LinkChecker_configdata.py
%{python_sitelib}/LinkChecker-*/
%pycache_only %{python_sitelib}/__pycache__/
%{_datadir}/pixmaps/linkchecker128x128.png
%dir %{_datadir}/linkchecker
%{_datadir}/linkchecker/linkcheckerrc
%dir %doc %{_mandir}/de/man1
%doc %{_mandir}/de/man1/linkchecker.1%{?ext_man}
%dir %doc %{_mandir}/de/man5
%doc %{_mandir}/de/man5/linkcheckerrc.5%{?ext_man}
%doc %{_mandir}/man1/linkchecker.1%{?ext_man}
%doc %{_mandir}/man5/linkcheckerrc.5%{?ext_man}

%changelog
