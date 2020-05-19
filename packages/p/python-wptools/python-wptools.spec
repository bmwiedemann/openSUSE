#
# spec file for package python-wptools
#
# Copyright (c) 2020 SUSE LLC
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


%define pyname wptools
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-wptools
Version:        0.4.17
Release:        0
Summary:        Wikipedia tools (for Humans)
License:        MIT
URL:            https://github.com/siznax/wptools/
Source:         https://files.pythonhosted.org/packages/source/w/wptools/%{pyname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-wptools-avoid-reading-readme.patch badshah400@gmail.com -- README.rst contains numerous spurious characters that are not readable in ascii. Skip reading this file in setup.py and manually insert a long description text instead
Patch0:         python-wptools-avoid-reading-readme.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi >= 2017.7.27.1
Requires:       python-html2text >= 2016.9.19
Requires:       python-lxml >= 3.8.0
Requires:       python-pycurl >= 7.43.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python and command-line MediaWiki access for Humans.

Features:
* get an HTML or plain text "extract" (lead or summary)
* get a representative image (pageimage, thumb, etc.)
* get an Infobox as a python dictionary
* get any/all Wikidata by title
* get info in any language
* get random info

%prep
%setup -q -n wptools-%{version}
%patch0 -p1
sed -E -i "1{/^#!\/usr\/bin.*python/d}" scripts/wptool.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/wptool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative wptool

%postun
%python_uninstall_alternative wptool

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%python_alternative %{_bindir}/wptool
%{python_sitelib}/*

%changelog
