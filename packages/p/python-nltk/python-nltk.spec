#
# spec file for package python-nltk
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.5
Release:        0
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            http://nltk.org/
Source:         https://files.pythonhosted.org/packages/source/n/nltk/%{pyname}-%{version}.zip
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
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
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch
%python_subpackages

%description
NLTK -- the Natural Language Toolkit -- is a suite of
Python modules, data sets and tutorials supporting research and
development in Natural Language Processing.

%prep
%setup -q -n %{pyname}-%{version}

sed -i "1,4{/\/usr\/bin\/env/d}" nltk/corpus/reader/knbc.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/test/runtests.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/test/unit/test_tgrep.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/tgrep.py
sed -i "1,4{/\/usr\/bin\/env/d}" nltk/tokenize/stanford_segmenter.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/nltk

%{python_expand %fdupes %{buildroot}%{$python_sitelib}/
chmod -x %{buildroot}%{$python_sitelib}/nltk/test/dependency.doctest
}

%check
# FOLLOWING http://www.nltk.org/install.html
%python_exec -c "import nltk" || exit 1

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
