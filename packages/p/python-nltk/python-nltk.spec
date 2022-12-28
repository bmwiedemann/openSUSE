#
# spec file for package python-nltk
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


%{!?python_module:%define python_module() python-%{**} python3-%{**}}
%define pyname nltk
%define skip_python2 1
Name:           python-nltk
Version:        3.7
Release:        0
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            http://nltk.org/
Source0:        https://files.pythonhosted.org/packages/source/n/nltk/%{pyname}-%{version}.zip
# Downloaded NLTK data via python3 -m nltk.downloader,
# then unzip downloaded zip archive.
# see https://www.nltk.org/data.html for more details
Source1:        nltk_data.tar.xz
Source99:       python-nltk.rpmlintrc
# PATCH-FIX-UPSTREAM skip-networked-test.patch gh#nltk/nltk#2969 mcepl@suse.com
# skip tests requiring network connection
Patch0:         skip-networked-test.patch
# PATCH-FIX-UPSTREAM port-2to3.patch bsc#[0-9]+ mcepl@suse.com
# port scripts in nltk_data to Python 3
Patch1:         port-2to3.patch
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# For testing
BuildRequires:  %{python_module tk}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# BuildRequires:  %%{python_module gensim}
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module python-crfsuite}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module text-unidecode}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module twython}
#
Requires:       python-regex
Requires:       python-six
Recommends:     python-gensim
Recommends:     python-matplotlib
Recommends:     python-numpy
Recommends:     python-pyparsing
Recommends:     python-python-crfsuite
Recommends:     python-requests
Recommends:     python-scikit-learn
Recommends:     python-scipy
Recommends:     python-twython
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

# changedir = nltk/test

%description
NLTK -- the Natural Language Toolkit -- is a suite of
Python modules, data sets and tutorials supporting research and
development in Natural Language Processing.

%prep
%autosetup -p1 -a1 -n %{pyname}-%{version}

# Remove obsolete scripts
rm tools/nltk_term_index.py tools/run_doctests.py nltk_data/corpora/semcor/semcor.py

# Fix EOL
sed -i 's/\r/\n/g; s/\n$//' \
    README.md \
    nltk/corpus/reader/knbc.py \
    nltk/test/unit/test_tgrep.py \
    nltk/tgrep.py \
    nltk/tokenize/stanford_segmenter.py \
    nltk/corpus/reader/knbc.py \
    nltk/test/unit/test_tgrep.py \
    nltk/tgrep.py \
    nltk/tokenize/stanford_segmenter.py \
    nltk/corpus/reader/knbc.py \
    nltk/test/unit/test_tgrep.py \
    nltk/tgrep.py \
    nltk/tokenize/stanford_segmenter.py

# Remove unrequired shebangs
sed -E -i "/#![[:space:]]*\/usr\/bin\/env python/d" \
    nltk/tgrep.py \
    nltk/tokenize/stanford_segmenter.py \
    nltk/test/unit/test_tgrep.py \
    nltk/corpus/reader/knbc.py

# Switch shebangs to the standard Python interpreter
sed -E -i "s|#![[:space:]]*%{_bindir}/env python|#!%{_bindir}/python3|" \
    setup.py \
    tools/global_replace.py \
    nltk_data/corpora/pl196x/splitter.py \
    tools/find_deprecated.py \
    tools/svnmime.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/nltk

%{python_expand %fdupes %{buildroot}%{$python_sitelib}/
chmod -x %{buildroot}%{$python_sitelib}/nltk/test/dependency.doctest
}

%check
export NLTK_DATA=$(readlink -f ./nltk_data/)
# export PYTEST_ADDOPTS="--doctest-modules"
%pytest -k 'not network'

%post
%python_install_alternative nltk

%postun
%python_uninstall_alternative nltk

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/%{pyname}/
%{python_sitelib}/%{pyname}-%{version}-py%{python_version}.egg-info/
%python_alternative %{_bindir}/nltk

%changelog
