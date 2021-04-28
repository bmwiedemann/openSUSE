#
# spec file for package python-IMDbPY
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-IMDbPY
Version:        2021.4.18
Release:        0
Summary:        Python package to access the IMDb's database
License:        GPL-2.0-or-later
URL:            https://imdbpy.sourceforge.io/
Source:         https://files.pythonhosted.org/packages/source/I/IMDbPY/IMDbPY-%{version}.tar.gz
Patch0:         do_not_install_scripts.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy
Requires:       python-lxml
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
IMDbPY is a Python package useful to retrieve and manage the data
of the IMDb movie database about movies, people, characters and companies.

IMDbPY can retrieve data from both the IMDb's web server and a local
copy of the whole database.

%prep
%setup -q -n IMDbPY-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Do not install python scripts under locale/, they are only used at build time
# for the translations
%python_expand rm %{buildroot}/%{$python_sitelib}/imdb/locale/*.py
%python_expand rm -rf %{buildroot}/%{$python_sitelib}/imdb/locale/__pycache__/
%python_expand rm %{buildroot}/%{$python_sitelib}/imdb/locale/*.po
%python_clone -a %{buildroot}%{_bindir}/imdbpy

%post
%python_install_alternative imdbpy

%postun
%python_uninstall_alternative imdbpy

%files %{python_files}
%doc README.rst CHANGELOG.txt
%license LICENSE.txt
%python_alternative %{_bindir}/imdbpy
%{python_sitelib}/IMDbPY-%{version}-py%{python_version}.egg-info
%{python_sitelib}/imdb
%lang(ar) %{python_sitelib}/imdb/locale/ar/LC_MESSAGES/imdbpy.mo
%lang(bg) %{python_sitelib}/imdb/locale/bg/LC_MESSAGES/imdbpy.mo
%lang(de) %{python_sitelib}/imdb/locale/de/LC_MESSAGES/imdbpy.mo
%lang(en) %{python_sitelib}/imdb/locale/en/LC_MESSAGES/imdbpy.mo
%lang(es) %{python_sitelib}/imdb/locale/es/LC_MESSAGES/imdbpy.mo
%lang(fr) %{python_sitelib}/imdb/locale/fr/LC_MESSAGES/imdbpy.mo
%lang(it) %{python_sitelib}/imdb/locale/it/LC_MESSAGES/imdbpy.mo
%lang(pt_BR) %{python_sitelib}/imdb/locale/pt_BR/LC_MESSAGES/imdbpy.mo
%lang(tr) %{python_sitelib}/imdb/locale/tr/LC_MESSAGES/imdbpy.mo

%changelog
