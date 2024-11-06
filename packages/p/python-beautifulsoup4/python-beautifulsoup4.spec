#
# spec file for package python-beautifulsoup4
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-beautifulsoup4
Version:        4.12.3
Release:        0
Summary:        HTML/XML Parser for Quick-Turnaround Applications Like Screen-Scraping
License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/
Source:         https://files.pythonhosted.org/packages/source/b/beautifulsoup4/beautifulsoup4-%{version}.tar.gz
# PATCH-FIX-UPSTREAM soupsieve26-compat.patch lp#2086199 mcepl@suse.com
# compatibility patch for various versions of soupsieve
Patch0:         soupsieve26-compat.patch
BuildRequires:  %{python_module cchardet}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module soupsieve >= 1.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-cchardet
Requires:       python-soupsieve >= 1.2
Suggests:       python-html5lib
Suggests:       python-lxml >= 3.4.4
Provides:       python-bs4 = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Beautiful Soup is a Python HTML/XML parser designed for quick turnaround
projects like screen-scraping. Three features make it powerful:

* Beautiful Soup won't choke if you give it bad markup. It yields a parse tree
  that makes approximately as much sense as your original document. This is
  usually good enough to collect the data you need and run away

* Beautiful Soup provides a few simple methods and Pythonic idioms for
  navigating, searching, and modifying a parse tree: a toolkit for dissecting a
  document and extracting what you need. You don't have to create a custom
  parser for each application

* Beautiful Soup automatically converts incoming documents to Unicode and
  outgoing documents to UTF-8. You don't have to think about encodings, unless
  the document doesn't specify an encoding and Beautiful Soup can't autodetect
  one. Then you just have to specify the original encoding

Beautiful Soup parses anything you give it, and does the tree traversal stuff
for you. You can tell it "Find all the links", or "Find all the links of class
externalLink", or "Find all the links whose urls match "foo.com", or "Find the
table heading that's got bold text, then give me that text."

Valuable data that was once locked up in poorly-designed websites is now within
your reach. Projects that would have taken hours take only minutes with
Beautiful Soup.

%if 0%{?suse_version} > 1500
%package -n python-beautifulsoup4-doc
Summary:        Documentation for %{name}
Recommends:     %{name} = %{version}
Obsoletes:      python2-beautifulsoup4-doc
Obsoletes:      python3-beautifulsoup4-doc

%description -n python-beautifulsoup4-doc
Documentation and help files for %{name}
%endif

%prep
%autosetup -p1 -n beautifulsoup4-%{version}

%build
%pyproject_wheel
pushd doc && make html && rm build/html/.buildinfo build/html/objects.inv &&  popd

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/bs4/
%{python_sitelib}/beautifulsoup4-%{version}*-info

%if 0%{?suse_version} > 1500
%files -n python-beautifulsoup4-doc
%endif
%doc CHANGELOG README.md doc/build/html

%changelog
