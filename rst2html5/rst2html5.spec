#
# spec file for package rst2html5
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


# tox for python3 seems to be broken due to too recent pluggy
%bcond_with tests

Name:           rst2html5
Version:        1.9.3
Release:        0
Summary:        RestructuredText to (X)HTML5
License:        MIT
Group:          Development/Languages/Python
Url:            https://marianoguerra.github.io/rst2html5/
Source:         https://files.pythonhosted.org/packages/source/r/rst2html5/rst2html5-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Genshi >= 0.7
BuildRequires:  python3-Pygments >= 2.0.2
BuildRequires:  python3-beautifulsoup4 >= 4.4
BuildRequires:  python3-docutils >= 0.12
%if %{with tests}
BuildRequires:  python3-tox >= 2.3.1
BuildRequires:  python3-nose >= 1.3.7
%endif
Requires:       python3-Genshi >= 0.7
Requires:       python3-Pygments >= 2.0.2
Requires:       python3-docutils >= 0.12
Requires(post):   update-alternatives
Requires(preun):  update-alternatives
BuildArch:      noarch

%description
rst2html tool generates basic HTML and CSS from Restructured Text. It
provides ways to modify the output with extensions like Nice CSS
(thanks to Twitter's Bootstrap CSS) or online presentations with
deck.js.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}%{python3_sitelib}

rm %{buildroot}%{_bindir}/rst2html5.py

# To avoid conflicts with the python3-docutils package
mv %{buildroot}%{_bindir}/rst2html5 %{buildroot}%{_bindir}/rst2html5-rst2html5
ln -s -f %{_sysconfdir}/alternatives/rst2html5 %{buildroot}%{_bindir}/rst2html5

%post
update-alternatives --install %{_bindir}/rst2html5 rst2html5 %{_bindir}/rst2html5-rst2html5 30

%preun
if [ ! -f %{_bindir}/rst2html5-rst2html5 ] ; then
   update-alternatives --remove rst2html5 %{_bindir}/rst2html5-rst2html5
fi

%if %{with tests}
%check
tox
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS.rst CHANGELOG.rst LICENSE
%{_bindir}/rst2html5
%{_bindir}/rst2html5-rst2html5
%ghost %{_sysconfdir}/alternatives/rst2html5
%{python3_sitelib}/rst2html5_.py
%{python3_sitelib}/__pycache__/rst2html5_.*.pyc
%{python3_sitelib}/modules/
%{python3_sitelib}/rst2html5-%{version}-py*.egg-info

%changelog
