#
# spec file for package python-nltk
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


%define modname nltk
Name:           python-nltk
Version:        3.8.1
Release:        0
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            http://nltk.org/
# SourceRepository: https://github.com/nltk/nltk
Source0:        https://github.com/nltk/%{modname}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# Download/Update NLTK data:
#     quilt setup python-nltk.spec
#     pushd nltk-?.?.?
#     python3 -m nltk.downloader -d nltk_data tests \
#          averaged_perceptron_tagger_ru \
#          brown \
#          cess_cat \
#          cess_esp \
#          conll2007 \
#          floresta \
#          gutenberg \
#          inaugural \
#          indian \
#          large_grammars \
#          nombank.1.0 \
#          omw-1.4 \
#          pl196x \
#          ptb \
#          punkt \
#          rte \
#          sinica_treebank \
#          stopwords \
#          treebank \
#          udhr \
#          universal_tagset \
#          wordnet \
#          wordnet_ic \
#          words
#     tar -cJf ../nltk_data.tar.xz nltk_data
#     popd
# see https://www.nltk.org/data.html for more details
Source1:        nltk_data.tar.xz
Source99:       python-nltk.rpmlintrc
# PATCH-FIX-UPSTREAM skip-networked-test.patch gh#nltk/nltk#2969 mcepl@suse.com
# skip tests requiring network connection
Patch0:         skip-networked-test.patch
# PATCH-FIX-UPSTREAM nltk-pr3207-py312.patch gh#nltk/nltk#3207
Patch1:         nltk-pr3207-py312.patch
# PATCH-FIX-UPSTREAM CVE-2024-39705-disable-download.patch bsc#1227174 mcepl@suse.com
# this patch makes things totally awesome
Patch2:         CVE-2024-39705-disable-download.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION runtime
BuildRequires:  %{python_module regex >= 2021.8.3}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module tqdm}
# /SECTION
# SECTION test
BuildRequires:  %{python_module tk}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-crfsuite}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module text-unidecode}
BuildRequires:  %{python_module twython}
# /SECTION
Requires:       python-regex >= 2021.8.3
Requires:       python-click
Requires:       python-joblib
Requires:       python-tqdm
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
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

# changedir = nltk/test

%description
NLTK -- the Natural Language Toolkit -- is a suite of
Python modules, data sets and tutorials supporting research and
development in Natural Language Processing.

%prep
%setup -q -a1 -n %{modname}-%{version}

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
    tools/find_deprecated.py

%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/nltk

%{python_expand %fdupes %{buildroot}%{$python_sitelib}/
chmod -x %{buildroot}%{$python_sitelib}/nltk/test/dependency.doctest
}

%check
export NLTK_DATA=$(readlink -f ./nltk_data/)
# export PYTEST_ADDOPTS="--doctest-modules"
# Skip tests requiring pickle.load gh#nltk/nltk#3266 (CVE-2024-39705)
skip_tests=" or test_basic or test_increment or test_pad_asterisk or test_pad_dotdot"
skip_tests+=" or test_pos_tag_eng or test_pos_tag_eng_universal or test_pos_tag_rus"
skip_tests+=" or test_pos_tag_rus_universal or test_pos_tag_unknown_lang"
skip_tests+=" or test_sent_tokenize or test_unspecified_lang or test_word_tokenize"
%pytest -k "not (network ${skip_tests})"

%post
%python_install_alternative nltk

%postun
%python_uninstall_alternative nltk

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/nltk/
%{python_sitelib}/nltk-%{version}.dist-info/
%python_alternative %{_bindir}/nltk

%changelog
