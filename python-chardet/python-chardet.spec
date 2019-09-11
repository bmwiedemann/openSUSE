#
# spec file for package python-chardet
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-chardet%{psuffix}
Version:        3.0.4
Release:        0
Summary:        Universal encoding detector
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/chardet/chardet
Source0:        https://files.pythonhosted.org/packages/source/c/chardet/chardet-%{version}.tar.gz
Source1:        python-chardet-rpmlintrc
Patch0:         pytest4.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-runner}
%endif
%python_subpackages

%description
Universal character encoding detector
-------------------------------------

Detects
 - ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
 - Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
 - EUC-JP, SHIFT_JIS, ISO-2022-JP (Japanese)
 - EUC-KR, ISO-2022-KR (Korean)
 - KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
 - ISO-8859-2, windows-1250 (Hungarian)
 - ISO-8859-5, windows-1251 (Bulgarian)
 - windows-1252 (English)
 - ISO-8859-7, windows-1253 (Greek)
 - ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
 - TIS-620 (Thai)

Requires Python 2.1 or later

Command-line Tool
-----------------

chardet comes with a command-line script which reports on the encodings of one
or more files::

    % chardetect.py somefile someotherfile
    somefile: windows-1252 with confidence 0.5
    someotherfile: ascii with confidence 1.0

%prep
%setup -q -n chardet-%{version}
%patch0 -p1

%build
%python_build

%install
%if !%{with test}
%{python_expand %$python_install
mv %{buildroot}%{_bindir}/chardetect %{buildroot}%{_bindir}/chardetect-%{$python_bin_suffix}
%fdupes -s %{buildroot}%{$python_sitelib}
}
%prepare_alternative chardetect
%endif

%check
%if %{with test}
%pytest test.py
%endif

%if !%{with test}
%post
%python_install_alternative chardetect

%postun
%python_uninstall_alternative chardetect

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/chardetect
%{python_sitelib}/chardet
%{python_sitelib}/chardet-%{version}-py%{python_version}.egg-info
%endif

%changelog
