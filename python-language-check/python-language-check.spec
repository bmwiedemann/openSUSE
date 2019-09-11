#
# spec file for package python-language-check
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Tests try to access the network on other architectures for some reason
%ifarch x86_64 %{ix86}
%bcond_without  test
%else
%bcond_with     test
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-language-check
Version:        1.1
Release:        0
%define ltver   3.2
Summary:        Python wrapper for checking grammar with LanguageTool
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://github.com/myint/language-check
Source:         https://files.pythonhosted.org/packages/source/l/language-check/language-check-%{version}.tar.gz
Source1:        https://www.languagetool.org/download/LanguageTool-%{ltver}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  java = 1.8.0
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       java = 1.8.0
BuildArch:      noarch

%python_subpackages

%description
Python wrapper for LanguageTool.

This is a fork of language_tool that produces more easily parsable
results from the command-line.

%prep
%setup -q -n language-check-%{version}
%setup -q -T -D -a 1 -n language-check-%{version}
mv LanguageTool-%{ltver} language_check/
chmod a+x language_check/LanguageTool-%{ltver}/org/languagetool/resource/*/*.pl
chmod a+x language_check/LanguageTool-%{ltver}/org/languagetool/resource/*/*.sh
chmod a+x language_check/LanguageTool-%{ltver}/org/languagetool/resource/*/*/*.sh
chmod a+x language_check/LanguageTool-%{ltver}/org/languagetool/resource/sk/bin/filter_lft.py

chmod a-x language_check/LanguageTool-%{ltver}/testrules.bat
chmod a-x language_check/LanguageTool-%{ltver}/org/languagetool/resource/ca/tag_verbs.pl
chmod a-x language_check/LanguageTool-%{ltver}/org/languagetool/resource/ru/dump.sh
chmod a-x language_check/LanguageTool-%{ltver}/org/languagetool/resource/ru/make-dict-ru-cfsa2.sh
chmod a-x language_check/LanguageTool-%{ltver}/org/languagetool/resource/ru/make-dict_synth-ru-cfsa2.sh

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license COPYING COPYING.LESSER
%python3_only %{_bindir}/language-check
%{python_sitelib}/*

%changelog
