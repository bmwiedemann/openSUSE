#
# spec file for package python-feedparser
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-feedparser
Version:        5.2.1
Release:        0
Summary:        Universal Feed Parser Module for Python
License:        BSD-2-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/kurtmckee/feedparser
Source:         https://files.pythonhosted.org/packages/source/f/feedparser/feedparser-%{version}.tar.bz2
Patch0:         py37.patch
Patch1:         non-ascii-entity-hiding.patch
# Similar to https://github.com/kurtmckee/feedparser/commit/b3d9463.patch
# However the "gets overwritten as xml.sax.SAXException later" is not
# happening in version 5.2.1.
Patch2:         catch-gzip-error.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-sgmllib3k
# Tests fail in Python 2 and 3 when chardet is installed
#BuildRequires:  python3-chardet
Requires:       python-xml
# chardet is an optional dependency, but some tests fail when it is present
Recommends:     python-chardet
%ifpython3
# If sgmllib is not available, the parser can fail with undefined local variable
Requires:       python3-sgmllib3k
%endif
BuildArch:      noarch
%python_subpackages

%description
A universal feed parser module for Python that handles RSS 0.9x, RSS 1.0, RSS
2.0, CDF, Atom 0.3, Atom 1.0 feeds.

%prep
%setup -q -n feedparser-%{version}
%autopatch -p1

find . -type f -exec chmod 0644 {} \;  # 5.2.1 had executable bit set on almost all files

# In version 5.2.1, it contains only test data, so move it out of install
mv feedparser/tests .

# Move the test module out of the runtime install, into top level directory
# so it can find the test data, and manually run 2to3.
python3 -m lib2to3 -w -n -o . --add-suffix=-%{python3_bin_suffix} --no-diffs feedparser/feedparsertest.py
mv feedparser/feedparsertest.py feedparsertest.py-%{python2_bin_suffix}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}:${PWD}
cp feedparsertest.py-%{$python_bin_suffix} feedparsertest.py
$python -c 'import feedparser; assert feedparser._XML_AVAILABLE == 1; assert feedparser._SGML_AVAILABLE == 1'
$python -c 'import feedparsertest; assert feedparsertest._UTF32_AVAILABLE == 1'
$python feedparsertest.py
}

%files %{python_files}
%license LICENSE
%doc NEWS README.rst
%{python_sitelib}/feedparser.py*
%pycache_only %{python_sitelib}/__pycache__/feedparser.*.py*
%{python_sitelib}/feedparser-%{version}-py*.egg-info

%changelog
