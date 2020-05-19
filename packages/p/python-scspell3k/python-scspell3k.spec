#
# spec file for package python-scspell3k
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-scspell3k
Version:        2.2
Release:        0
Summary:        A conservative interactive spell checker for source code
License:        GPL-2.0-only
URL:            https://github.com/myint/scspell
Source0:        https://github.com/myint/scspell/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-cram
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Scspell is a spell checker for source code. This is an unofficial fork (of
https://launchpad.net/scspell) that runs on both Python 2 and 3.

Scspell does not try to be particularly smart--rather, it does the simplest
thing that can possibly work:

    1. All alphanumeric strings (strings of letters, numbers, and
       underscores) are spell-checked tokens.
    2. Each token is split into one or more subtokens. Underscores and digits
       always divide tokens, and capital letters will begin new subtokens. In
       other words, ``some_variable`` and ``someVariable`` will both generate
       the subtoken list {``some``, ``variable``}.
    3. All subtokens longer than three characters are matched against a set of
       dictionaries, and a match failure prompts the user for action. When
       matching against the included English dictionary, *prefix matching* is
       employed; this choice permits the use of truncated words like ``dict``
       as valid subtokens.

When applied to code written in most popular programming languages while using
typical naming conventions, this algorithm will usually catch many errors
without an annoying false positive rate.

In an effort to catch more spelling errors, Scspell is able to check each
file against a set of dictionary words selected *specifically for that file*. Up
to three different sub-dictionaries may be searched for any given file:

    1. A natural language dictionary. (Scspell provides an American
       English dictionary as the default.)
    2. A programming language-specific dictionary, intended to contain
       oddly-spelled keywords and APIs associated with that language.
       (Scspell provides small default dictionaries for a number of popular
       programming languages.)
    3. A file-specific dictionary, intended to contain uncommon strings which
       are not likely to be found in more than a handful of unique files.

%prep
%setup -q -n scspell-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/scspell
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest
sed -i -e 's:python $TESTDIR:python3 $TESTDIR:g' ./test.cram
python3 -m cram --indent=4 ./test.cram

%post
%python_install_alternative scspell

%postun
%python_uninstall_alternative scspell

%files %{python_files}
%doc README.rst
%license COPYING.txt
%python_alternative %{_bindir}/scspell
%{python_sitelib}/*

%changelog
